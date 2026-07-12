# 🚀 Cómo poner tus 10 páginas en circulación (paso a paso)

Tienes **30 páginas listas** (todas al 99% de calidad), `style.css`, `sitemap.xml`
y `robots.txt` en la carpeta `output/`. Esto es lo que sigue.

---

## 1) ⚠️ Importante: NO compres 10 dominios — compra UNO
Las 10 páginas viven en **un solo dominio**, como rutas distintas:
```
tudominio.com/                                  (Mariachis en Bogotá)
tudominio.com/serenata-cumpleanos-bogota.html
tudominio.com/serenata-de-amor-bogota.html
tudominio.com/mariachis-dia-de-la-madre-bogota.html
... (y las demás)
```
Comprar un dominio por página **divide tu autoridad y parece spam** → peor SEO.
Un dominio + muchas páginas = toda la fuerza concentrada. Eso es lo que domina.

## 2) Elige y compra tu dominio
El exact-match `mariachisbogota.com` ya está tomado. Usa una **marca + keyword**
(rankea igual de bien a nivel nacional y se ve más profesional). Candidatos a revisar:

- `mariachisya.com` · `tumariachis.com` · `mimariachis.com` · `gomariachis.com`
- `mariachisbogota.com.co` · `mariachis-bogota.co`
- O tu marca: `mariachirealdebogota.com`, `mariachibonito.co`

**Verifica disponibilidad real con el motor (desde tu PC):**
```bash
python cli.py -k "mariachis bogota" --domains --city bogota
python cli.py -k "mariachis colombia" --domains
```
Compra el que salga **libre** en un registrador barato (un `.com` ronda USD 10–12/año):
- **Porkbun** → https://porkbun.com (de los más baratos, ~$11/año)
- **Namecheap** → https://www.namecheap.com (fácil, promos primer año)
- **Cloudflare Registrar** → https://www.cloudflare.com/products/registrar/ (al costo, sin sobreprecio)
- `.co` (Colombia) disponible en los tres.

## 3) Tus datos ✅ (ya quedaron listos)
Ya está todo personalizado: marca **Mariachi Bonito Tecalitlán**, teléfono y
WhatsApp **301 4232500** en el formulario y los botones, y sin reseñas inventadas.
Solo falta que TÚ, cuando puedas, añadas **fotos y un video reales** de tu grupo
(en la galería) y **reseñas reales** cuando las tengas. Nada de esto frena la publicación.

## 4) Publica el sitio GRATIS — lo más fácil primero
Todo el sitio es estático → hosting gratis, rápido y sin tarjeta.

**La forma más rápida (3 clics, sin crear cuenta para probar):**
1. Entra a `app.netlify.com/drop` desde el navegador.
2. **Arrastra la carpeta `output/` completa** a esa página.
3. En segundos te da una URL en vivo tipo `algo-aleatorio.netlify.app`. ¡Ya está online!
   (Crea una cuenta gratis ahí mismo para conservarla y ponerle un nombre bonito.)

**Opción permanente con nombre elegido — Cloudflare Pages (gratis):**
1. `dash.cloudflare.com` → Workers & Pages → Create → Pages → "Upload assets".
2. Nombra el proyecto **`mariachibonito`** (así la URL será `mariachibonito.pages.dev`,
   que es la que ya dejé configurada). Sube TODO el contenido de `output/`.
3. Más adelante, conecta tu dominio propio en "Custom domains".

> **Importante:** dejé el sitio configurado para `mariachibonito.pages.dev`. Si tu URL
> final es otra (Netlify te da una distinta), cambia la línea `domain` en `generate.py`
> por tu URL real y corre `python generate.py` otra vez — o pásame la URL y te lo dejo
> ajustado al instante. (Los enlaces entre páginas funcionan igual desde ya.)

## 5) Dile a Google que existes (indexación rápida — clave)
1. Entra a **Google Search Console** (`search.google.com/search-console`), agrega
   tu dominio y verifícalo (Cloudflare lo hace en 1 clic).
2. En **Sitemaps**, envía: `tudominio.com/sitemap.xml`.
3. Usa **Inspección de URL** → "Solicitar indexación" para cada una de las 10 páginas.

## 6) La otra mitad del #1 (no la saltes)
Las páginas son tu mitad on-page (al 99%). Para pelear arriba de verdad, en paralelo:
- **Perfil de Google Business** (lo #1 para el mapa local) + **reseñas reales**.
- Unos pocos **enlaces gratis reales** (directorios CO, redes, colaboraciones).
- Enlazar tus redes sociales a la web.

Detalle completo en `CAMINO_AL_NUMERO_1.md` y `PLAN_MARIACHIS_COLOMBIA.md`.

---

## 7) Escala a 30+ páginas (cuando quieras)
En `generate.py`, agrega entradas a la lista `PAGES` (localidades como
`/mariachis-suba-bogota`, más ocasiones, otras ciudades) y vuelve a correr
`python generate.py`. La fábrica genera todo con el mismo nivel de calidad.

**Orden recomendado:** localidades top (Suba, Kennedy, Usaquén, Chapinero) →
otras ciudades (Medellín, Cali) → artículos ("cuánto cuesta un mariachi").
