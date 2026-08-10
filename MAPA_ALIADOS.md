# 🤝 MAPA DE ALIADOS — mandar mariachi desde fuera de Bogotá

Idea del dueño (10-ago-2026): *"por el precio que pongo desde Bogotá casi ningún cliente
contrata, pero si hubiera un mariachi cerca puedo dar un precio más barato y ganar comisión"*.

**Es correcto y es el único modelo que abre los municipios lejanos.** El costo que mata la
venta no es la música: es la gasolina, los peajes y las 5 horas de carretera de cinco músicos.
Si el que toca ya vive a 40 minutos, ese costo desaparece y el precio baja solo.

Medido con `mapa_aliados.py` (tiempos reales de manejo, no en línea recta).

---

## Los cuatro nodos

| Base | Qué cubre | Minutos hasta cada destino |
|---|---|---|
| **ZIPAQUIRÁ** ⭐ | Suesca · Sesquilé · Pacho · Ubaté · Chocontá · Guatavita · Villapinzón · Machetá | 37 · 37 · 50 · 53 · 59 · 69 · 75 · 112 |
| **TUNJA** | Villapinzón · Chocontá · Machetá | 53 · 60 · 121 |
| **FACATATIVÁ** | Villeta · Guaduas | 45 · 67 |
| **GIRARDOT** | Girardot · Melgar (y Anapoima, Tocaima) | 0 · 28 |
| **VILLAVICENCIO** | Medina | 91 |

**Zipaquirá es el nodo #1**: con un solo aliado ahí se abren ocho municipios que hoy no se
pueden vender. Ninguno de esos ocho tiene página todavía.

### Cuánto se gana en tiempo frente a salir de Bogotá

| Destino | Desde Bogotá | Desde la base | Ahorro |
|---|---:|---:|---:|
| Melgar | 133 min | Girardot 28 | **−105 min** |
| Villapinzón | 140 min | Tunja 53 | **−65 min** |
| Ubaté | 114 min | Chiquinquirá 39 | **−61 min** |
| Pacho | 151 min | Zipaquirá 50 | **−51 min** |
| Villeta | 143 min | Facatativá 45 | **−49 min** |
| Suesca | 83 min | Zipaquirá 37 | **−46 min** |
| Chocontá | 119 min | Zipaquirá 59 | **−43 min** |
| Machetá | 172 min | Zipaquirá 112 | **−43 min** |

---

## Contactos reales por base (verificados en directorios públicos, sin llamar todavía)

**ZIPAQUIRÁ**
- Mariachis Zipaquirá — 320 353 4365
- Mariachi Tapatío Zipaquirá — 310 809 6117 (24 h, cubre fuera de la ciudad)
- Mariachi Serenatas (Cra. 22) — 302 230 5738 (24/7)
- Zacatecas Mariachi (Cra. 6 #17a-02) — 314 460 6204 (24/7)
- Mariachi Son de México (Transv. 5b #12-86)

**TUNJA**
- Mariachi Nuevo Son — 318 744 8838 · 311 282 5060 (cubre todo Boyacá)
- Mariachi Imperial Tunja — 311 856 1500 (24/7, +10 años)
- Mariachi Clásico Imperial — 313 811 5913 · 315 327 3857 (10 canciones, 8 integrantes, sonido)
- Mariachi Juvenil de Oro — 310 216 2076

**FACATATIVÁ**
- Mariachi Legado Mexicano — 321 919 1801
- Mariachi Juvenil de Miguel Runza — 310 311 2053 (24/7)
- Mariachi Tradición Evolución (Cra. 14 #13b-53) — cubre la región del Tequendama

**GIRARDOT**
- Mariachi Girardot (Cra. 10 #18-64 of. 102) — cubre Anapoima y Tocaima
- Mariachi Patria · Mariachi Tequila (Cr 18 #17-29) · Banda Show Chingones

---

## Lo que hay que preguntarle a cada aliado (y lo que NO)

Preguntar: **tarifa de canal para un intermediario** (no la tarifa al público), número de
músicos, si llevan sonido propio, hasta qué municipios se desplazan sin recargo, disponibilidad
en fines de semana y 24 h, y si aceptan que el cliente pague al intermediario y ellos cobren
después.

⛔ **No decirles nunca de dónde salen los clientes, ni que hay páginas web posicionadas por
municipio, ni cuánto se le cobra al cliente final.** El día que lo sepan, montan su propia
página y el intermediario sobra. Misma lógica que la regla de los proveedores de Almadía.

---

## El riesgo real y cómo se tapa

El activo es la página posicionada, no el músico. El peligro es que el aliado se quede con el
cliente en el segundo pedido:

1. Que el cliente **pague siempre a Mariachi Bonito**, nunca al aliado en efectivo.
2. Entregar al aliado **solo dirección y hora**, no el teléfono del cliente.
3. Que la marca visible en el evento sea la tuya (el aliado va como refuerzo).
4. Tener **dos aliados por zona**: el que se salta el acuerdo pierde el flujo.

---

## Estado de Machetá

**No es viable ni con aliado**: 172 min desde Bogotá, 112 desde Zipaquirá, 121 desde Tunja,
63 desde Guateque o Chocontá — y en esos dos pueblos no hay mariachi con presencia comercial.
Machetá está detrás de la montaña; se atiende solo por pedido puntual y cotizado a mano.

**Los que sí valen la pena abrir primero:** Suesca, Sesquilé, Chocontá y Guatavita desde
Zipaquirá, y Melgar desde Girardot — el de mayor demanda de todos, por ser destino de fin de
semana.
