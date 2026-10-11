#!/usr/bin/env python3
"""SRHF v3.1 science figures, corrections to the historically mapped figures.

The eleven figures retain their established identities, but their underlying
arrays come solely from the frozen A0 canonical model. These are descriptive
orbital-spacing plots, not statistical significance or dynamical stability
proofs. Harmonia is explicitly unobserved.

Historical originals: v3.0/scripts/srhf_*.py (unaltered).
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'audit' / 'srhf_a0'))
import canonical_srhf as canonical  # noqa: E402

INDIGO = '#2B2F8A'
TEAL = '#1F7A8C'
CRIMSON = '#B22222'
ORANGE = '#E07A1A'
GOLD = '#D4AF37'
ROBIN_EGG = '#1FCECB'
BG = '#f8f8f8'
GRID = '#e0e0e0'
GRAY = '#52565e'
PLANET_COLORS = ['#4169E1', '#C38A08', '#008C91', '#4682B4', '#B54356']

NAMES = canonical.BODY_ORDER
OBS_NAMES = canonical.PRIMARY_NINE
OUTER = canonical.OUTER_FIVE
PRED = canonical.fixed_srhf_au()
OBS = canonical.OBSERVED_AU
H_SILVER = canonical.silver_node_au()
H_OPT = canonical.fitted_outer_node_au()
H_PI = canonical.pi_node_au()
H_NEPTUNE = canonical.neptune_zero_node_au()
COEFF = canonical.outer_coefficients()
OUTER_OBS = np.array([OBS[n] for n in OUTER], dtype=float)


def base(figsize=(9, 6)):
    fig, ax = plt.subplots(figsize=figsize)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    ax.set_axisbelow(True)
    ax.grid(color=GRID, linewidth=.9, alpha=.9)
    return fig, ax


def node_markers(ax, neptune=False):
    for h, label, color, line in [
        (H_SILVER, rf'$a_H^{{\mathrm{{Silver}}}}={H_SILVER:.6f}$ AU', ORANGE, '-.'),
        (H_OPT, rf'$a_H^{{\mathrm{{opt}}}}={H_OPT:.6f}$ AU (fitted)', CRIMSON, '--'),
        (H_PI, rf'$a_H^{{\pi}}={H_PI:.6f}$ AU', TEAL, ':'),
    ]:
        ax.axvline(h, color=color, linestyle=line, lw=1.6, label=label)
    if neptune:
        ax.axvline(H_NEPTUNE, color=GRAY, linestyle=(0, (2, 3)), lw=1.4,
                   label=f'Neptune residual zero = {H_NEPTUNE:.6f} AU')


def outer_pred(h):
    return np.asarray(h)[..., None] * COEFF


def outer_resid(h):
    return 100 * (outer_pred(h) - OUTER_OBS) / OUTER_OBS


def rmse_outer(h):
    return np.sqrt(np.mean((outer_pred(h) - OUTER_OBS) ** 2, axis=-1))


def hsi_outer(h):
    return np.std(outer_resid(h), axis=-1, ddof=0)


def save(fig, name, folder):
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f'{name}.png'
    fig.savefig(path, dpi=230, bbox_inches='tight', facecolor=BG, metadata={'Software': 'SRHF v3.1 matplotlib'})
    plt.close(fig)
    return path


def figure_harmonia_orbit(folder):
    fig, ax = base((7.5, 7))
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    for radius, label, color, ls in [
        (1.524, 'Mars (adopted 1.524 AU)', GRAY, '-'),
        (H_SILVER, 'Unobserved SRHF node (2.1421 AU)', INDIGO, '--'),
        (2.2, 'Approx. belt inner edge', '#916E4C', ':'),
        (3.2, 'Approx. belt outer edge', '#916E4C', ':'),
        (5.204, 'Jupiter (adopted 5.204 AU)', GOLD, '-'),
    ]:
        ax.add_patch(Circle((0, 0), radius, fill=False, edgecolor=color,
                            linestyle=ls, lw=2, label=label))
    rng = np.random.default_rng(42)
    r = rng.uniform(2.2, 3.2, 175)
    theta = rng.uniform(0, 2 * np.pi, 175)
    ax.scatter(r*np.cos(theta), r*np.sin(theta), s=2, color='#916E4C', alpha=.5)
    ax.plot(0, 0, '*', markersize=18, color='#D9A400', label='Sun')
    ax.set_xlabel('Projected distance (AU)')
    ax.set_ylabel('Projected distance (AU)')
    ax.set_title('Illustrative circular orbits and unobserved Harmonia node')
    ax.legend(loc='upper left', fontsize=8, framealpha=.95)
    fig.text(.5, .015, 'Schematic only; no detected planet or established stable orbit implied.',
             ha='center', fontsize=9, color=GRAY)
    return save(fig, 'srhf_harmonia_orbit', folder)


def figure_harmonia_optimisation(folder):
    h = np.linspace(2.12, 2.18, 1400)
    fig, ax = base((9.5, 6.3))
    ax.plot(h, rmse_outer(h), color=INDIGO, lw=2.2, label='Outer-five RMSE (AU)')
    node_markers(ax)
    ax.set_xlim(h[0], h[-1])
    ax.set_xlabel(r'Harmonia semi-major axis $a_H$ (AU)')
    ax.set_ylabel('Root mean square error (AU)')
    ax.set_title('Five-outer-body fit: fixed SRHF reference nodes and fitted optimum')
    ax.legend(fontsize=8.5, loc='upper center', framealpha=.95)
    return save(fig, 'srhf_harmonia_optimisation', folder)


def figure_rmse_hsi_basin(folder):
    h = np.linspace(2.12, 2.16, 1400)
    fig, ax = base((9.5, 6.4))
    second = ax.twinx()
    ax.plot(h, rmse_outer(h), color=INDIGO, lw=2.1, label='RMSE (AU)')
    second.plot(h, hsi_outer(h), color=GOLD, lw=2.1, label='HSI (residual spread)')
    ax.set_xlabel(r'Harmonia semi-major axis $a_H$ (AU)')
    ax.set_ylabel('Outer-five RMSE (AU)', color=INDIGO)
    second.set_ylabel('Harmonic Spread Index (percentage points)', color=GOLD)
    ax.tick_params(axis='y', labelcolor=INDIGO)
    second.tick_params(axis='y', labelcolor='#876c04')
    ax.set_xlim(h[0], h[-1])
    node_markers(ax, neptune=True)
    a, al = ax.get_legend_handles_labels()
    b, bl = second.get_legend_handles_labels()
    ax.legend(b + a, bl + al, fontsize=8.0, loc='upper center', framealpha=.94)
    ax.set_title('Descriptive RMSE and residual-spread curves (not a stability basin)')
    fig.text(.5, .014, 'HSI is linear for positive $a_H$; no dynamical stability inference.',
             ha='center', fontsize=9, color=GRAY)
    return save(fig, 'srhf_rmse_hsi_basin', folder)


def candidate_residuals():
    return [
        ('Silver (fixed)', H_SILVER, ORANGE),
        ('Empirical optimum (fitted)', H_OPT, CRIMSON),
        (r'$\pi$ reference (fixed)', H_PI, TEAL),
    ]


def figure_residuals_comparison(folder):
    fig, ax = base((9.5, 6.3))
    x = np.arange(len(OUTER))
    width = .25
    for j, (label, h, color) in enumerate(candidate_residuals()):
        ax.bar(x + (j - 1) * width, outer_resid(h), width,
               color=color, label=label)
    ax.axhline(0, color=GRAY, lw=1)
    ax.set_xticks(x, OUTER)
    ax.set_ylabel('Signed model-minus-observed residual (%)')
    ax.set_title('Outer-five percentage residuals at three Harmonia references')
    ax.legend(fontsize=9, loc='upper left')
    return save(fig, 'srhf_residuals_comparison', folder)


def figure_hsi_values(folder):
    fig, ax = base((9.5, 6.3))
    x = np.arange(len(OUTER))
    width = .25
    for j, (label, h, color) in enumerate(candidate_residuals()):
        spread = float(hsi_outer(h))
        ax.bar(x+(j-1)*width, outer_resid(h), width, color=color,
               label=f'{label}; HSI={spread:.4f} pp')
    ax.axhline(0, color=GRAY, lw=1)
    ax.set_xticks(x, OUTER)
    ax.set_ylabel('Signed residual (%)')
    ax.set_title('Candidate residual bars and Harmonic Spread Index (not HSI minimum)')
    ax.legend(fontsize=8.5, loc='upper left')
    return save(fig, 'srhf_hsi_values', folder)


def figure_residuals_log(folder, symlog=False):
    h = np.linspace(2.12, 2.18, 1600)
    fig, (ax, low) = plt.subplots(2, 1, figsize=(9.5, 9), gridspec_kw={'height_ratios': [1.65, 1]})
    fig.patch.set_facecolor(BG)
    for a in (ax, low):
        a.set_facecolor(BG)
        a.set_axisbelow(True)
        a.grid(color=GRID, alpha=.85)
    second = ax.twinx()
    ax.plot(h, rmse_outer(h), color=INDIGO, lw=2, label='RMSE (AU)')
    second.plot(h, hsi_outer(h), color=GOLD, lw=2, label='HSI (residual spread)')
    ax.set_ylabel('RMSE (AU)', color=INDIGO)
    second.set_ylabel('HSI (percentage points)', color=GOLD)
    node_markers(ax, neptune=True)
    ax.set_xlim(h[0], h[-1])
    a, al = ax.get_legend_handles_labels()
    b, bl = second.get_legend_handles_labels()
    ax.legend(b + a, bl + al, fontsize=7.4, loc='upper center')
    vals = outer_resid(h)
    for j, n in enumerate(OUTER):
        y = vals[:, j] if symlog else np.abs(vals[:, j])
        low.plot(h, y, lw=1.6, color=PLANET_COLORS[j], label=n)
    low.set_xlim(h[0], h[-1])
    low.set_yscale('symlog', linthresh=.05) if symlog else low.set_yscale('log')
    low.set_ylabel('Signed residual (%) [symlog]' if symlog else 'Absolute residual (%) [log]')
    low.set_xlabel(r'Harmonia semi-major axis $a_H$ (AU)')
    low.axhline(0, color=GRAY, lw=.7) if symlog else None
    low.axvline(H_OPT, color=CRIMSON, linestyle='--', lw=1.1)
    low.axvline(H_SILVER, color=ORANGE, linestyle='-.', lw=1.1)
    low.axvline(H_PI, color=TEAL, linestyle=':', lw=1.1)
    low.axvline(H_NEPTUNE, color=GRAY, linestyle=(0, (2, 3)), lw=1.1)
    low.legend(loc='lower left' if not symlog else 'upper left', fontsize=8, ncol=2)
    if symlog:
        ax.set_title('RMSE / HSI with signed residuals (descriptive symlog display)')
        name = 'srhf_residuals_symlog'
    else:
        ax.set_title('RMSE / HSI with absolute residuals (log display)')
        name = 'srhf_residuals_log'
    fig.tight_layout(rect=(0, .025, 1, 1))
    fig.text(.5, .009, f'Neptune zero at {H_NEPTUNE:.9f} AU differs from outer-five optimum {H_OPT:.9f} AU.',
             ha='center', fontsize=8.5, color=GRAY)
    return save(fig, name, folder)


def figure_ratios_full(folder):
    x = np.arange(len(NAMES))
    obs = np.array([OBS.get(name, np.nan) for name in NAMES])
    pred = np.array([PRED[name] for name in NAMES])
    fig, ax = base((10.5, 6.4))
    ax.plot(x, pred, 'o-', color=INDIGO, lw=2, label='Fixed SRHF prediction')
    ax.plot(x, obs, 's-', color=ROBIN_EGG, lw=2, label='Adopted observations (Harmonia missing)')
    ax.scatter([NAMES.index('Harmonia')], [H_SILVER], s=100, color=ORANGE,
               zorder=5, label='Hypothetical Harmonia node')
    ax.set_xticks(x, NAMES, rotation=30)
    ax.set_ylabel('Semi-major axis (AU)')
    ax.set_title('Fixed SRHF vs adopted orbital distances (AU, not ratios)')
    ax.legend(loc='upper left', fontsize=9)
    return save(fig, 'srhf_ratios_full', folder)


def figure_ratios_zoom(folder):
    names = ['Mars', *OUTER]
    obs = np.array([OBS[n] for n in names])
    silver = np.array([PRED[n] for n in names])
    fitted = np.array([PRED['Mars'], *[canonical.outer_predictions(H_OPT)[n] for n in OUTER]])
    fig, ax = base((10, 6.3))
    x = np.arange(len(names))
    ax.plot(x, obs/silver, 'o-', color=INDIGO, lw=2,
            label='Observed / fixed SRHF predicted')
    ax.plot(x, obs/fitted, 's--', color=CRIMSON, lw=2,
            label='Observed / fitted outer-five predicted')
    ax.axhline(1, color=GRAY, lw=1, linestyle=':')
    ax.set_xticks(x, names)
    ax.set_ylabel('Observed / predicted (dimensionless)')
    ax.set_title('Mars–Pluto observed/predicted ratios (Mars not fitted)')
    ax.legend(fontsize=9)
    return save(fig, 'srhf_ratios_zoom', folder)


def figure_percent_deviation(folder):
    # Nine and only nine adopted observations. Harmonia is deliberately NOT an x tick.
    names = list(OBS_NAMES)
    x = np.arange(len(names))
    pct = np.array([100*(PRED[n]-OBS[n])/OBS[n] for n in names])
    score = canonical.score(tuple(names), PRED)['mape_pct']
    fig, (ax, lower) = plt.subplots(2, 1, figsize=(11, 8),
                                   gridspec_kw={'height_ratios': [3, 1.05]})
    fig.patch.set_facecolor(BG)
    for axes in (ax, lower):
        axes.set_facecolor(BG)
        axes.set_axisbelow(True)
        axes.grid(color=GRID, linewidth=.8)
    ax.plot(x, pct, 'o-', color=INDIGO, lw=2, label='Fixed SRHF signed residual (%)')
    ax.axhline(0, color=GRAY, lw=1, linestyle='--')
    ax.set_xticks(x, names, rotation=30)
    ax.set_ylabel('Model − adopted observation (%)')
    ax.set_title('Fixed SRHF deviations: nine observations, no Harmonia observation')
    ax.text(.98, .95, f'Nine-body MAPE = {score:.3f}% (descriptive mean absolute error)',
            transform=ax.transAxes, va='top', ha='right', fontsize=9,
            bbox={'boxstyle': 'round', 'facecolor': 'white', 'alpha': .9})
    ax.legend(loc='lower left', fontsize=9)
    # Three theoretical references vs a post-hoc fitted optimum; NOT observations.
    values = 100*(np.array([H_SILVER, H_OPT, H_PI])/H_OPT - 1)
    lower.scatter(range(3), values, c=[ORANGE, CRIMSON, TEAL], s=75, zorder=3)
    lower.axhline(0, color=GRAY, lw=.8)
    lower.set_xlim(-.4, 2.4)
    lower.set_ylim(-.11, .11)
    lower.set_xticks(range(3), ['Silver (fixed)', 'outer-five fit', r'$\pi$ (fixed)'])
    lower.set_ylabel('Node difference vs fit (%)')
    lower.set_title('Harmonia reference nodes: mathematical/fitted comparison, not observations',
                    fontsize=10)
    fig.tight_layout(h_pad=1.6)
    return save(fig, 'srhf_percent_deviation', folder)


def figure_log_validation(folder):
    names = list(NAMES)
    x = np.arange(len(names))
    observed = np.array([OBS.get(n, np.nan) for n in names])
    predicted = np.array([PRED[n] for n in names])
    mape = canonical.score(tuple(OBS_NAMES), PRED)['mape_pct']
    fig, ax = base((11, 6.5))
    ax.plot(x, observed, 's-', color=ROBIN_EGG, lw=2.3,
            label='Adopted observations (no Harmonia observation)')
    ax.plot(x, predicted, 'o--', color=INDIGO, lw=2,
            label='Fixed SRHF algebraic prediction')
    ax.scatter([names.index('Harmonia')], [H_SILVER], color=ORANGE, s=90,
               zorder=6, label='Hypothetical Harmonia node')
    ax.set_yscale('log')
    ax.set_xticks(x, names, rotation=30)
    ax.set_ylabel('Semi-major axis (AU, logarithmic scale)')
    ax.set_title('Adopted orbital distances vs fixed SRHF predictions')
    ax.text(.48, .97, f'Nine-observation MAPE: {mape:.3f}%',
            transform=ax.transAxes, va='top', fontsize=10,
            bbox={'boxstyle': 'round', 'facecolor': 'white', 'alpha': .9})
    ax.legend(fontsize=8.5, loc='upper left')
    return save(fig, 'srhf_log_validation', folder)


RENDERERS = {
    'srhf_harmonia_orbit': figure_harmonia_orbit,
    'srhf_harmonia_optimisation': figure_harmonia_optimisation,
    'srhf_rmse_hsi_basin': figure_rmse_hsi_basin,
    'srhf_residuals_comparison': figure_residuals_comparison,
    'srhf_hsi_values': figure_hsi_values,
    'srhf_residuals_log': lambda folder: figure_residuals_log(folder, False),
    'srhf_residuals_symlog': lambda folder: figure_residuals_log(folder, True),
    'srhf_ratios_full': figure_ratios_full,
    'srhf_ratios_zoom': figure_ratios_zoom,
    'srhf_percent_deviation': figure_percent_deviation,
    'srhf_log_validation': figure_log_validation,
}


def render(name, folder=None):
    if name not in RENDERERS:
        raise ValueError(f'Unknown frozen figure generator: {name}')
    target = Path(folder) if folder is not None else ROOT / 'v3.1' / 'figures'
    return RENDERERS[name](target)
