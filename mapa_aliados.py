#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Para cada municipio que queda lejos de Bogota, calcula desde que ciudad-base
saldria mas facil mandar un mariachi aliado. Mide tiempo real de manejo (OSRM).

    python3 mapa_aliados.py
"""
import json, subprocess, sys, time, urllib.parse

UA = "mbt-aliados/1.0 (apolo489@gmail.com)"

# ciudades con escena de mariachi propia, candidatas a ser base de un aliado
BASES = [
    "Bogotá, Colombia", "Tunja, Boyacá, Colombia", "Duitama, Boyacá, Colombia",
    "Sogamoso, Boyacá, Colombia", "Girardot, Cundinamarca, Colombia",
    "Villavicencio, Meta, Colombia", "Ibagué, Tolima, Colombia",
    "Zipaquirá, Cundinamarca, Colombia", "Facatativá, Cundinamarca, Colombia",
    "Fusagasugá, Cundinamarca, Colombia", "Chiquinquirá, Boyacá, Colombia",
]

# destinos que hoy no se pueden atender bien desde Bogota
DESTINOS = [
    "Machetá, Cundinamarca, Colombia", "Villapinzón, Cundinamarca, Colombia",
    "Chocontá, Cundinamarca, Colombia", "Guatavita, Cundinamarca, Colombia",
    "Suesca, Cundinamarca, Colombia", "Sesquilé, Cundinamarca, Colombia",
    "Ubaté, Cundinamarca, Colombia", "Guaduas, Cundinamarca, Colombia",
    "Girardot, Cundinamarca, Colombia", "Melgar, Tolima, Colombia",
    "Villeta, Cundinamarca, Colombia", "Pacho, Cundinamarca, Colombia",
    "Gachetá, Cundinamarca, Colombia", "Medina, Cundinamarca, Colombia",
]

_cache = {}


def _curl(url, ua=False):
    cmd = ["curl", "-s", "-m", "25"] + (["-A", UA] if ua else []) + [url]
    return subprocess.run(cmd, capture_output=True, text=True).stdout


def geo(nombre):
    if nombre in _cache:
        return _cache[nombre]
    q = urllib.parse.quote(nombre)
    try:
        d = json.loads(_curl("https://nominatim.openstreetmap.org/search"
                             f"?format=json&limit=1&countrycodes=co&q={q}", ua=True))
        pt = (float(d[0]["lat"]), float(d[0]["lon"])) if d else None
    except Exception:
        pt = None
    _cache[nombre] = pt
    time.sleep(1.1)          # cortesia con Nominatim
    return pt


def ruta(a, b):
    u = ("https://router.project-osrm.org/route/v1/driving/"
         f"{a[1]},{a[0]};{b[1]},{b[0]}?overview=false")
    try:
        d = json.loads(_curl(u))
        if d.get("code") != "Ok":
            return None, None
        r = d["routes"][0]
        return r["duration"] / 60, r["distance"] / 1000
    except Exception:
        return None, None


def main():
    bases = [(b, geo(b)) for b in BASES]
    bases = [(b.split(",")[0], p) for b, p in bases if p]
    print("Bases geocodificadas:", ", ".join(b for b, _ in bases), "\n")

    print("%-14s %s" % ("DESTINO", "las 3 bases mas cercanas (minutos de manejo)"))
    print("-" * 78)
    for d in DESTINOS:
        pd = geo(d)
        if not pd:
            print("%-14s  no geocodifica" % d.split(",")[0]); continue
        filas = []
        for nb, pb in bases:
            t, km = ruta(pb, pd)
            if t is not None:
                filas.append((t, km, nb))
        filas.sort()
        txt = "   ".join("%s %.0f min/%.0f km" % (nb, t, km) for t, km, nb in filas[:3])
        bog = next((t for t, km, nb in filas if nb == "Bogotá"), None)
        ahorro = ""
        if bog and filas and filas[0][2] != "Bogotá":
            ahorro = "   ← %.0f min menos que desde Bogotá" % (bog - filas[0][0])
        print("%-14s %s%s" % (d.split(",")[0], txt, ahorro))


if __name__ == "__main__":
    main()
