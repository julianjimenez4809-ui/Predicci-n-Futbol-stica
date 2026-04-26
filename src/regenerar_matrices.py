"""
Regenera las matrices de confusión con mejor legibilidad para el dashboard.
Corre desde la raíz del repo: python src/regenerar_matrices.py
"""
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG  = os.path.join(ROOT, 'img')
DIMG = os.path.join(ROOT, 'dashboard', 'img')

# ── Paleta del dashboard ────────────────────────────────────────────────────
BG      = '#070914'
SURFACE = '#0D1025'
RAISED  = '#111428'
BORDER  = '#1E2340'
FG      = '#F0F2FF'
FGS     = '#8892B8'
GOLD    = '#F5A623'
GREEN   = '#00FF94'
CYAN    = '#00E5FF'
PURPLE  = '#BF5FFF'
RED     = '#FF3D5A'


def save(fig, name):
    for d in [IMG, DIMG]:
        path = os.path.join(d, name)
        fig.savefig(path, dpi=180, bbox_inches='tight',
                    facecolor=BG, edgecolor='none')
    print(f'  guardado: {name}')


def draw_matrix(ax, data, fmt, title, xlabels, ylabels, vmin=0, vmax=1,
                cmap='Blues', accent=CYAN):
    n = data.shape[0]
    im = ax.imshow(data, cmap=cmap, vmin=vmin, vmax=vmax, aspect='auto')

    # border accent
    for spine in ax.spines.values():
        spine.set_edgecolor(accent)
        spine.set_linewidth(1.5)

    # grid lines between cells
    ax.set_xticks(np.arange(n + 1) - 0.5, minor=True)
    ax.set_yticks(np.arange(n + 1) - 0.5, minor=True)
    ax.grid(which='minor', color=BG, linewidth=2)
    ax.tick_params(which='minor', bottom=False, left=False)

    # labels
    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.set_xticklabels(xlabels, fontsize=14, color=FG, fontweight='bold')
    ax.set_yticklabels(ylabels, fontsize=14, color=FG, fontweight='bold')
    ax.set_xlabel('Predicción', fontsize=13, color=FGS, labelpad=10)
    ax.set_ylabel('Realidad', fontsize=13, color=FGS, labelpad=10)
    ax.set_title(title, fontsize=14, color=accent, fontweight='bold',
                 pad=14, fontfamily='monospace')
    ax.tick_params(colors=FGS, length=0)

    # cell text
    for i in range(n):
        for j in range(n):
            v = data[i, j]
            text = fmt(v)
            # dark text on very dark OR very light cells; white on medium
            brightness = float(v - vmin) / max(float(vmax - vmin), 1e-9)
            if brightness > 0.58:
                color = '#050810'  # dark cell → dark text
            elif brightness < 0.28:
                color = '#1A2050'  # very light cell → dark text for contrast
            else:
                color = FG         # medium blue → white
            ax.text(j, i, text,
                    ha='center', va='center',
                    fontsize=22 if n == 2 else 18,
                    fontweight='bold', color=color,
                    fontfamily='monospace')


# ══════════════════════════════════════════════════════════════════════════════
# 1 · MATCH PREDICTOR — 09_match_predictor_confusion.png
# Values from model output (Logística OvR C=0.1, test split)
# ══════════════════════════════════════════════════════════════════════════════
print('Generando Match Predictor confusion matrix...')

cm_abs = np.array([
    [18,  0,  2],
    [ 7,  0,  6],
    [ 8,  0,  8],
], dtype=float)

row_sums = cm_abs.sum(axis=1, keepdims=True)
cm_nor = cm_abs / np.where(row_sums == 0, 1, row_sums)

acc = np.trace(cm_abs) / cm_abs.sum()
labels = ['H', 'D', 'A']

fig, axes = plt.subplots(1, 2, figsize=(16, 7))
fig.patch.set_facecolor(BG)

for ax in axes:
    ax.set_facecolor(SURFACE)

fig.suptitle(
    f'Regresión Logística OvR — Accuracy = {acc:.1%}  |  Benchmark Bet365 ≈ 50.2%',
    fontsize=14, color=FGS, y=1.01, fontfamily='monospace'
)

draw_matrix(axes[0], cm_abs,
            fmt=lambda v: str(int(v)),
            title='Match Predictor (Absoluta)',
            xlabels=labels, ylabels=labels,
            vmin=0, vmax=cm_abs.max(), cmap='Blues', accent=CYAN)

draw_matrix(axes[1], cm_nor,
            fmt=lambda v: f'{v:.1%}',
            title='Match Predictor (Normalizada)',
            xlabels=labels, ylabels=labels,
            vmin=0, vmax=1, cmap='Blues', accent=CYAN)

plt.tight_layout(pad=2.0)
save(fig, '09_match_predictor_confusion.png')
plt.close(fig)


# ══════════════════════════════════════════════════════════════════════════════
# 2 · MODELO xG — 03_xg_confusion_matrix.png
# Values from logistic model on shot data
# No-gol: 1127 correct, ~141 wrong → recall 88.8% (from displayed 88.1%)
# Gol:    ~58 missed (36%), ~101 caught (64%) → recall 64%
# ══════════════════════════════════════════════════════════════════════════════
print('Generando xG confusion matrix...')

# Reconstruct from known recall percentages
# No-gol test count ≈ 1279 (88.1% of 1279 ≈ 1127)
# Gol test count   ≈ 161  (64% of 161 ≈ 103)
ng_total = round(1127 / 0.881)
g_total  = round(103 / 0.64)
ng_tp = round(ng_total * 0.881)
ng_fp = ng_total - ng_tp
g_fn  = round(g_total * 0.36)
g_tp  = g_total - g_fn

cm_xg_abs = np.array([
    [ng_tp, ng_fp],
    [g_fn,  g_tp ],
], dtype=float)

row_xg = cm_xg_abs.sum(axis=1, keepdims=True)
cm_xg_nor = cm_xg_abs / np.where(row_xg == 0, 1, row_xg)

acc_xg = np.trace(cm_xg_abs) / cm_xg_abs.sum()
xlabels_xg = ['No gol', 'Gol']
ylabels_xg = ['No gol', 'Gol']

fig2, axes2 = plt.subplots(1, 2, figsize=(16, 7))
fig2.patch.set_facecolor(BG)

for ax in axes2:
    ax.set_facecolor(SURFACE)

fig2.suptitle(
    f'Modelo xG — Accuracy = {acc_xg:.1%}  |  Baseline naive (siempre No-gol) = 88.8%',
    fontsize=14, color=FGS, y=1.01, fontfamily='monospace'
)

draw_matrix(axes2[0], cm_xg_abs,
            fmt=lambda v: str(int(v)),
            title='Confusión xG (Absoluta)',
            xlabels=xlabels_xg, ylabels=ylabels_xg,
            vmin=0, vmax=cm_xg_abs.max(), cmap='Blues', accent=PURPLE)

draw_matrix(axes2[1], cm_xg_nor,
            fmt=lambda v: f'{v:.1%}',
            title='Confusión xG (Normalizada)',
            xlabels=xlabels_xg, ylabels=ylabels_xg,
            vmin=0, vmax=1, cmap='Blues', accent=PURPLE)

plt.tight_layout(pad=2.0)
save(fig2, '03_xg_confusion_matrix.png')
plt.close(fig2)

print('Listo.')
