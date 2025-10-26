import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar, root_scalar

# --- Constants (Celtic model parameters) ---
A = np.sqrt(2)
B = A + 1
C = 2*A - 1
D = A - 1

# --- Observed outer planets (AU) ---
planets = ["Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
observeds = np.array([5.204, 9.559, 19.185, 30.156, 39.482])

# --- Prediction model ---
def predict_outer(a_lp):
    factor = a_lp * (1 + A)
    return np.array([
        factor,                    # Jupiter
        factor * C,                # Saturn
        2 * factor * C,            # Uranus
        factor * (B / D),          # Neptune
        2 * factor * (A + B)       # Pluto
    ])

# --- RMSE and HSI definitions ---
def rmse(a_lp):
    preds = predict_outer(a_lp)
    return np.sqrt(np.mean((preds - observeds)**2))

def hsi(a_lp):
    preds = predict_outer(a_lp)
    residuals_pct = (preds - observeds) / observeds * 100
    return np.std(residuals_pct)

# --- Find empirical optimum (RMSE min) ---
result = minimize_scalar(rmse, bounds=(2.12, 2.18), method='bounded')
opt_a_lp = result.x
opt_rmse = result.fun

# --- Analytic candidates ---
pi_val = np.pi**(2/3)
celtic_val = (2*A*C)/(1 + A)

# --- Sample range ---
a_range = np.linspace(2.12, 2.18, 2000)
rmse_vals = np.array([rmse(a) for a in a_range])
hsi_vals  = np.array([hsi(a)  for a in a_range])

# --- Neptune residual zero crossing ---
def neptune_residual(a_lp):
    return predict_outer(a_lp)[3] - observeds[3]

try:
    root_result = root_scalar(neptune_residual, bracket=(2.12, 2.18), method='brentq', xtol=1e-12)
    neptune_zero_a = root_result.root
except Exception:
    neptune_zero_a = None

# --- Planet residuals (% of observed) ---
residuals_pct = np.array([
    (predict_outer(a) - observeds) / observeds * 100 for a in a_range
])

# --- Colour palette ---
gold = "#D4AF37"
indigo = "#2B2F8A"
teal = "#1F7A8C"
crimson = "#B22222"
celtic_col = "#E07A1A"
dark_gray = "#404040"
planet_colors = {
    "Jupiter": "#4169E1",
    "Saturn": "#DAA520",
    "Uranus": "#40E0D0",
    "Neptune": "#4682B4",
    "Pluto": "#CD5C5C"
}

# --- Plotting ---
plt.style.use('ggplot')
fig, (ax1, ax3) = plt.subplots(2, 1, figsize=(9, 9), gridspec_kw={'height_ratios': [2.2, 1]})
fig.patch.set_facecolor('#f8f8f8')

# === PANEL 1: RMSE & HSI ===
ax2 = ax1.twinx()
ax1.plot(a_range, rmse_vals, color=indigo, linewidth=2.2, label='RMSE (AU)')
ax2.plot(a_range, hsi_vals, color=gold, linewidth=2.0, label='HSI (σ of % residuals)')

ax1.set_xlabel(r'Harmonia position $a_{\rm H}$ (AU)', fontsize=12)
ax1.set_ylabel('RMSE (AU)', color=indigo, fontsize=12)
ax2.set_ylabel('HSI (σ of % residuals)', color=gold, fontsize=12)
ax1.tick_params(axis='y', labelcolor=indigo)
ax2.tick_params(axis='y', labelcolor=gold)
ax1.set_xlim(2.12, 2.18)
ax1.grid(color='black', alpha=0.3)

# Vertical markers
ax1.axvline(opt_a_lp, color=crimson, linestyle='--', linewidth=1.8)
ax1.text(opt_a_lp + 0.0006, max(rmse_vals)*1, f'Optimum = {opt_a_lp:.6f} AU',
         color=crimson, fontsize=10, va='top')

ax1.axvline(celtic_val, color=celtic_col, linestyle='-.', linewidth=1.6)
ax1.text(celtic_val - 0.0035, max(rmse_vals)*0.785, f'Celtic = {celtic_val:.6f} AU',
         color=celtic_col, fontsize=9, ha='right')

ax1.axvline(pi_val, color=teal, linestyle=':', linewidth=1.6)
ax1.text(pi_val + 0.0006, max(rmse_vals)*0.78, f'π^(2/3) = {pi_val:.6f} AU',
         color=teal, fontsize=9, va='bottom')

if neptune_zero_a is not None:
    ax1.axvline(neptune_zero_a, color=dark_gray, linestyle=':', linewidth=1.2)
    ax1.text(neptune_zero_a + 0.0006, max(rmse_vals)*0.59,
             f'Neptune resid = 0 at {neptune_zero_a:.6f} AU', color=dark_gray, fontsize=8, va='top')

# Legend
lines = [
    plt.Line2D([0],[0], color=indigo, lw=2.2),
    plt.Line2D([0],[0], color=gold, lw=2.0),
    plt.Line2D([0],[0], color=crimson, lw=1.8, linestyle='--'),
    plt.Line2D([0],[0], color=celtic_col, lw=1.6, linestyle='-.'),
    plt.Line2D([0],[0], color=teal, lw=1.6, linestyle=':')
]
labels = ['RMSE (AU)', 'HSI (σ of % residuals)', 'Empirical optimum', 'Celtic 2AC/(1+A)', 'π^(2/3)']
ax1.legend(lines, labels, loc='upper left', frameon=True, fontsize=9)
ax1.set_title("Harmonic Ladder Optimization: RMSE & HSI vs Harmonia Position", fontsize=14, pad=12)

# === PANEL 2: Per-planet residuals (symlog) ===
for i, planet in enumerate(planets):
    ax3.plot(a_range, residuals_pct[:, i], color=planet_colors[planet],
             linewidth=1.6, label=planet)

# Horizontal equilibrium bands (±0.1%, ±1%)
for band, alpha in [(1, 0.15), (0.1, 0.25)]:  # Smaller band = darker (more important)
    ax3.axhspan(-band, band, color='gray', alpha=alpha)

ax3.set_yscale('symlog', linthresh=0.05)
ax3.axhline(0, color='black', linewidth=0.8)
ax3.axvline(opt_a_lp, color=crimson, linestyle='--', linewidth=1.2)
ax3.axvline(celtic_val, color=celtic_col, linestyle='-.', linewidth=1.2)
ax3.axvline(pi_val, color=teal, linestyle=':', linewidth=1.2)

ax3.set_xlim(2.12, 2.18)
ax3.set_xlabel(r'Harmonia position $a_{\rm H}$ (AU)', fontsize=12)
ax3.set_ylabel('Residuals (%) [symlog]', fontsize=12)
ax3.grid(alpha=0.3, which='both')
ax3.legend(loc='upper right', ncol=3, fontsize=9)
ax3.set_title("Per-planet Residuals across Harmonic Ladder (symmetric log scale)", fontsize=12, pad=10)

plt.tight_layout()
plt.savefig("harmonic_ladder_RMSE_HSI_Residuals_symlog_final.png", dpi=300, bbox_inches='tight')
plt.show()
