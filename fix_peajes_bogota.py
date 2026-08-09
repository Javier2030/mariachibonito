#!/usr/bin/env python3
"""Quita 'peajes incluidos' de las paginas de Bogota y deja 'Transporte y Sonido Incluido'
en los items de los paquetes. Las paginas de municipios NO se tocan: alli el peaje es real.
Uso: fix_peajes_bogota.py [--apply]"""
import re, sys, glob, os, collections

MUNICIPIOS = {
    "anapoima", "cajica", "chia", "cota", "facatativa", "funza", "fusagasuga",
    "granada-cundinamarca", "la-calera", "la-mesa", "madrid-cundinamarca",
    "mesitas-del-colegio", "mosquera", "sibate", "silvania", "soacha", "sopo",
    "tabio", "tenjo", "tocancipa", "zipaquira",
}

REEMPLAZOS = [
    # items de las tarjetas de paquetes
    (r"<li>Transporte incluido</li>", "<li>Transporte y Sonido Incluido</li>"),
    (r"<li>Traslado y peajes incluidos</li>", "<li>Transporte y Sonido Incluido</li>"),
    (r"<li>Traslado y peajes a [^<]+ incluidos</li>", "<li>Transporte y Sonido Incluido</li>"),
    # frase informativa sobre los municipios de la sabana
    (r"su precio publicado con traslado y peajes incluidos",
     "su precio publicado con el traslado incluido"),
    (r"traslado y los peajes van incluidos", "el traslado va incluido"),
    (r"con el traslado y los peajes ya incluidos", "con el traslado ya incluido"),
    (r"con traslado y peajes incluidos", "con el traslado incluido"),
    (r"traslado y peajes incluidos", "traslado incluido"),
]


def es_municipio(path):
    n = os.path.basename(path).replace("mariachis-", "").replace(".html", "")
    return n in MUNICIPIOS


def main():
    aplicar = "--apply" in sys.argv
    total = collections.Counter()
    tocados = 0
    for f in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs", "*.html"))):
        if es_municipio(f):
            continue
        s = open(f, encoding="utf-8").read()
        orig = s
        for pat, rep in REEMPLAZOS:
            s, n = re.subn(pat, rep, s)
            if n:
                total[pat] += n
        rest = len(re.findall(r"peajes?", s, re.I))
        if s != orig:
            tocados += 1
            if aplicar:
                open(f, "w", encoding="utf-8").write(s)
        if rest:
            print("  QUEDA peaje en", os.path.basename(f), "x", rest)
    print("\nArchivos %s: %d" % ("modificados" if aplicar else "que cambiarian", tocados))
    for pat, n in total.most_common():
        print("  %4d  %s" % (n, pat[:70]))


if __name__ == "__main__":
    main()
