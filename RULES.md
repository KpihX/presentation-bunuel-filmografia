# Reglas del oral ESP (LES 51201) y cómo este soporte las cumple

Fuente: notas de clase sesión 2 (`2_Luis_Bunuel_Cine_Surrealista_Y_Evaluacion.md`,
Gdrive_X) + Moodle LES_51201.

## Opción elegida

**Opción 1 : Filmografía de un realizador hispano**

Análisis temático de la obra de un director español o latinoamericano a partir
de **al menos dos películas**. Identificar obsesiones, temas recurrentes y
estilo visual, con extractos breves comentados en directo.

## Fechas P1

Orales del primer periodo: **18 de noviembre** y **2 de diciembre** de 2026.
(11 nov = festivo, sin clase.)

## Duración

**Ninguna regla del curso escribe una duración.** El deck no impone límite:
las notas son ligeras (español de principiante, frases cortas) y el orador
toma su tiempo. `deck.py` solo informa, nunca juzga.

## Contrato de este deck

| Regla del curso | Dónde se cumple |
|---|---|
| Al menos dos películas | *Un perro andaluz* (1929), *Los olvidados* (1950), *Viridiana* (1961) (+ ancla *El ángel exterminador*) |
| Obsesiones / temas / estilo | Parte III + figura `obsesiones` |
| Extractos comentados en directo | Clips incrustados 06 / 07 / 08 (18 s / 40 s / 40 s), clic en sala |
| Incorporar fragmentos para apoyar | Ídem: video real, no imagen |
| Dinamizar: preguntas / debate / Kahoot | Planche 11 « Para el público » + debate 2 min |
| Individual o grupo 2-3 | Preparado en individual (ajustable) |
| Sin diapositiva « Gracias / Preguntas » | Última planche = conclusión abierta |
| 12 planches, sin annexes | 12 planches, 0 annexes |
| Orden fluido | Mapa cronológico planche 4, luego 1929 → 1950 → 1961 |
| Orientación en cada planche | `part:` breadcrumb chronologique (année / étape) |

## Citas proyectadas (fuentes)

- *Un perro andaluz* : André Breton, película « totalmente surrealista » (1929).
- *Los olvidados* : UNESCO, Memoria del Mundo (2003) · Cannes 1951 mejor dirección.
- *Viridiana* : *L'Osservatore Romano*, « insulto sacrílego » (1961).

## Plan B técnico

Si la sala niega la vidéo : el cartel (poster) queda en el panel y el
orador comenta la imagen. Los carteles viven en `assets/clips/poster_*.jpg`.

## Densité (k-presentation / perfil académico)

- ≤ 6 palabras por línea proyectada
- ≤ 5 líneas por bloque de columna
- Markdown posee cada frase; Python solo coloca
- Template X oficial (`assets/Template_X.pptx`)
- Panel derecho: video 16:9 (planches 06-08) o foto cover-crop
