# Oral ESP - Luis Buñuel (opción 1)

Deck as code para el oral de **Español Intermedio LES 51201**.

- **Opción**: filmografía de un realizador hispano (≥2 películas)
- **Corpus**: *Un perro andaluz* (1929) · *Los olvidados* (1950) · *Viridiana* (1961)
- **Plantilla**: `assets/Template_X.pptx` (École polytechnique)
- **Extractos**: 3 clips incrustados (18 s / 40 s / 40 s), carteles = plan B
- **Interacción**: planche 12 « Preguntas para ustedes »

## Build

```bash
uv sync
uv run python scripts/render.py check
uv run python scripts/render.py all
```

Livrable: `build/Presentation_ESP_Bunuel_Filmografia_Ivann_KAMDEM.pptx`
