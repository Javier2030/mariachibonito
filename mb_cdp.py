#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""mb_cdp.py — cliente CDP minimo y parametrizable por puerto para MARIACHI.

Motivo (7-sep-2026): el puerto historico 9445 lo ocupa el Chrome del bufete
(C:\\wa_bufete, WhatsApp Web) y matarlo romperia otro proyecto del usuario.
Este cliente permite apuntar a cualquier puerto y adjuntarse a una pestana ya
abierta o crear una nueva desechable.
"""
import json, time, urllib.request, urllib.parse
import websocket


class CDP:
    def __init__(self, port=9446, host="localhost"):
        self.base = f"http://{host}:{port}"

    def http(self, method, path):
        req = urllib.request.Request(self.base + path, method=method)
        with urllib.request.urlopen(req, timeout=20) as r:
            body = r.read().decode("utf-8", "replace")
        try:
            return json.loads(body)
        except Exception:
            return body

    def tabs(self):
        return [t for t in self.http("GET", "/json/list") if t.get("type") == "page"]

    def find(self, substr):
        for t in self.tabs():
            if substr.lower() in (t.get("url", "") + " " + t.get("title", "")).lower():
                return t
        return None

    def new(self, url):
        return self.http("PUT", "/json/new?" + urllib.parse.quote(url, safe=""))

    def close(self, tid):
        try:
            self.http("GET", "/json/close/" + tid)
        except Exception:
            pass


class Tab:
    def __init__(self, cdp, info=None, url=None, own=False):
        self.cdp = cdp
        self.own = own
        if info is None:
            info = cdp.new(url)
            self.own = True
        self.info = info
        self.id = info["id"]
        self.ws = websocket.create_connection(
            info["webSocketDebuggerUrl"], timeout=90, suppress_origin=True)
        self.n = 0

    def send(self, method, params=None, timeout=None):
        self.n += 1
        self.ws.send(json.dumps({"id": self.n, "method": method, "params": params or {}}))
        while True:
            msg = json.loads(self.ws.recv())
            if msg.get("id") == self.n:
                return msg

    def js(self, expr, wait=True):
        r = self.send("Runtime.evaluate", {
            "expression": expr, "returnByValue": True,
            "awaitPromise": wait, "timeout": 60000})
        res = r.get("result", {})
        if "exceptionDetails" in res:
            return {"__error__": str(res["exceptionDetails"])[:600]}
        return res.get("result", {}).get("value")

    def goto(self, url, settle=6):
        self.send("Page.navigate", {"url": url})
        time.sleep(settle)

    def front(self):
        self.send("Page.bringToFront")

    def text(self, limit=6000):
        return (self.js("document.body?document.body.innerText:''") or "")[:limit]

    def click_xy(self, x, y):
        for t in ("mousePressed", "mouseReleased"):
            self.send("Input.dispatchMouseEvent", {
                "type": t, "x": x, "y": y, "button": "left", "clickCount": 1,
                "buttons": 1 if t == "mousePressed" else 0})
            time.sleep(0.05)

    def click_sel(self, sel, idx=0):
        """Clic NATIVO en el centro del elemento (evita listeners que ignoran .click())."""
        box = self.js("""(()=>{const e=document.querySelectorAll(%s)[%d];
            if(!e) return null; e.scrollIntoView({block:'center'});
            const r=e.getBoundingClientRect();
            return {x:r.left+r.width/2,y:r.top+r.height/2,w:r.width,h:r.height};})()"""
            % (json.dumps(sel), idx))
        if not isinstance(box, dict) or not box.get("w"):
            return False
        time.sleep(0.3)
        self.click_xy(box["x"], box["y"])
        return True

    def type_text(self, txt):
        self.send("Input.insertText", {"text": txt})

    def key(self, code, key, vk, mods=0):
        for t in ("rawKeyDown", "keyUp"):
            self.send("Input.dispatchKeyEvent", {
                "type": t, "code": code, "key": key, "modifiers": mods,
                "windowsVirtualKeyCode": vk, "nativeVirtualKeyCode": vk})

    def set_files(self, sel, files, idx=0):
        """DOM.setFileInputFiles sobre el input[type=file] que casa con sel."""
        self.send("DOM.enable")
        doc = self.send("DOM.getDocument", {"depth": -1})
        root = doc["result"]["root"]["nodeId"]
        q = self.send("DOM.querySelectorAll", {"nodeId": root, "selector": sel})
        ids = q.get("result", {}).get("nodeIds", [])
        if len(ids) <= idx:
            return f"FAIL: {len(ids)} inputs, pedido idx {idx}"
        r = self.send("DOM.setFileInputFiles", {"files": files, "nodeId": ids[idx]})
        return "OK" if "error" not in r else json.dumps(r)[:300]

    def close(self):
        try:
            self.ws.close()
        except Exception:
            pass
        if self.own:
            self.cdp.close(self.id)
