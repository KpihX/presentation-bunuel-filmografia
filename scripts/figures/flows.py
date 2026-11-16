"""Figuras analiticas del oral Buñuel."""

from __future__ import annotations

import theme
from style import C, band, box, canvas, disc, save, tag, arrow, note


def fig_obsesiones():
    key = "obsesiones"
    W, H = theme.FIGURE_WITH_CAPTION.width, theme.FIGURE_WITH_CAPTION.height
    fig, ax = canvas(W, H)
    items = (
        ("1", "Burguesía", "Rituales vacíos\nhipocresía de clase", "navy"),
        ("2", "Religión", "Dogma jesuita\nsubvertido en imagen", "gold"),
        ("3", "Deseo", "Posesión machista\nfrustración erótica", "teal"),
        ("4", "Sueño", "Grietas oníricas\nen cualquier género", "sage"),
    )
    bw, gap = 2.55, 0.35
    y, bh = 1.55, 2.55
    for i, (n, title, sub, color) in enumerate(items):
        x = 0.15 + i * (bw + gap)
        box(ax, x, y, bw, bh, [title, *sub.split("\n")], fill=C["white"],
            edge=C[color], sizes=(17, 12))
        disc(ax, x + 0.38, y + bh - 0.38, 0.26, n, C[color])
    band(ax, 0.15, 0.35, W - 0.30, 0.85,
         "Constantes de autor: cambia el marco, no la herida.",
         size=15, bold=True)
    tag(ax, 0.20, 4.35, "cuatro hilos", size=11)
    return save(fig, key)


def fig_etapas_firma():
    key = "etapas_firma"
    W, H = theme.FIGURE_WITH_CAPTION.width, theme.FIGURE_WITH_CAPTION.height
    fig, ax = canvas(W, H)
    stages = (
        ("París 1929", "Un perro andaluz", "Choque surrealista", "navy"),
        ("México 1950", "Los olvidados", "Realismo + sueño", "teal"),
        ("España 1961", "Viridiana", "Sátira bajo censura", "gold"),
    )
    bw, gap = 3.3, 0.55
    y, bh = 2.20, 1.85
    xs = []
    for i, (place, film, idea, color) in enumerate(stages):
        x = 0.35 + i * (bw + gap)
        xs.append(x)
        box(ax, x, y, bw, bh, [place, film, idea],
            fill=C["pale"] if i != 1 else C["white"],
            edge=C[color], sizes=(14, 13))
    for i in range(2):
        arrow(ax, (xs[i] + bw - 0.05, y + bh / 2),
              (xs[i + 1] + 0.05, y + bh / 2), lw=2.0)
    band(ax, 0.35, 0.40, W - 0.70, 0.95,
         "Misma firma: herir el confort para revelar el poder.",
         size=16, bold=True)
    tag(ax, 0.40, 4.45, "tres etapas", size=11)
    note(ax, W / 2, 1.55,
         "El marco muda (vanguardia / industria mexicana / franquismo).",
         size=12, ha="center")
    return save(fig, key)


ALL = (fig_obsesiones, fig_etapas_firma)
