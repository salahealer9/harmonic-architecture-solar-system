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

# --- find empirical optimum (RMSE min) ---
result = minimize_scalar(rmse, bounds=(2.12, 2.16), method='bounded')
opt_a_lp = result.x
opt_rmse = result.fun

# --- analytic candidates ---
pi_val = np.pi**(2/3)
celtic_val = (2*A*C)/(1 + A)

# --- sample range for curves ---
a_range = np.linspace(2.12, 2.16, 2000)
rmse_vals = np.array([rmse(a) for a in a_range])
hsi_vals  = np.array([hsi(a)  for a in a_range])

# --- Neptune residual zero crossing (find a_lp where Neptune residual = 0) ---
def neptune_residual(a_lp):
    pred_nep = predict_outer(a_lp)[3]   # Neptune is index 3
    return pred_nep - observeds[3]

# attempt root finding inside the sampled interval (fallback to interpolation)
try:
    root_result = root_scalar(neptune_residual, bracket=(2.12, 2.16), method='brentq', xtol=1e-12)
    neptune_zero_a = root_result.root
except Exception:
    # fallback: linear interpolation on sampled data
    neptune_resid = np.array([predict_outer(a)[3] - observeds[3] for a in a_range])
    idx = np.where(np.sign(neptune_resid[:-1]) != np.sign(neptune_resid[1:]))[0]
    if len(idx) > 0:
        i = idx[0]
        # linear interp
        x0, x1 = a_range[i], a_range[i+1]
        y0, y1 = neptune_resid[i], neptune_resid[i+1]
        neptune_zero_a = x0 - y0 * (x1 - x0) / (y1 - y0)
    else:
        neptune_zero_a = None

# --- colors (gold / indigo palette) ---
gold = "#D4AF37"
indigo = "#2B2F8A"
teal = "#1F7A8C"
crimson = "#B22222"
celtic_col = "#E07A1A"  # warm contrast for Celtic marker
dark_gray = "#404040"   # Changed from 'grey' to dark gray for better contrast

# --- plotting ---
plt.style.use('ggplot')
fig, ax1 = plt.subplots(figsize=(9, 6.5))  # Slightly taller to accommodate legend

# RMSE on left axis (indigo)
ax1.plot(a_range, rmse_vals, color=indigo, linewidth=2.2, label='RMSE (AU)')
ax1.set_xlabel(r'Harmonia position $a_{\rm H}$ (AU)', fontsize=12)
ax1.set_ylabel('RMSE (AU)', color=indigo, fontsize=12)
ax1.tick_params(axis='y', labelcolor=indigo)
ax1.set_xlim(2.12, 2.16)

ax1.grid(color='black', alpha=0.6)
fig.patch.set_facecolor('#f8f8f8')  # Very light grey
ax1.set_facecolor('#f8f8f8')

# mark RMSE optimum
ax1.axvline(opt_a_lp, color=crimson, linestyle='--', linewidth=1.8)
ax1.text(opt_a_lp + 0.0006, max(rmse_vals)*1,
         f'Optimum = {opt_a_lp:.6f} AU', color=crimson, fontsize=10, va='top')

# secondary axis for HSI (gold)
ax2 = ax1.twinx()
ax2.plot(a_range, hsi_vals, color=gold, linewidth=2.0, label='HSI (σ of % residuals)')
ax2.set_ylabel('HSI (σ of % residuals)', color=gold, fontsize=12)
ax2.tick_params(axis='y', labelcolor=gold)

ax2.grid(color='gold', alpha=0.6)

# mark Celtic and pi^(2/3)
ax1.axvline(celtic_val, color=celtic_col, linestyle='-.', linewidth=1.6)
ax1.text(celtic_val - 0.0035, max(rmse_vals)*0.78,
         f'Celtic = {celtic_val:.6f} AU', color=celtic_col, fontsize=9, ha='right')

ax1.axvline(pi_val, color=teal, linestyle=':', linewidth=1.6)
ax1.text(pi_val + 0.0006, max(rmse_vals)*0.78,
         f'π^(2/3) = {pi_val:.6f} AU', color=teal, fontsize=9, va='bottom')

# Neptune zero crossing annotation - using dark gray for better contrast
if neptune_zero_a is not None:
    ax1.axvline(neptune_zero_a, color=dark_gray, linestyle=':', linewidth=1.2)
    ax1.text(neptune_zero_a + 0.0006, max(rmse_vals)*0.7,
             f'Neptune resid = 0 at {neptune_zero_a:.6f} AU', color=dark_gray, fontsize=8, va='top')

# combine legends manually (since two axes) - FIXED POSITION
lines = [plt.Line2D([0],[0], color=indigo, lw=2.2),
         plt.Line2D([0],[0], color=gold, lw=2.0),
         plt.Line2D([0],[0], color=crimson, lw=1.8, linestyle='--'),
         plt.Line2D([0],[0], color=celtic_col, lw=1.6, linestyle='-.'),
         plt.Line2D([0],[0], color=teal, lw=1.6, linestyle=':')]

labels = ['RMSE (AU)', 'HSI (σ of % residuals)', 'Empirical optimum', 'Celtic 2AC/(1+A)', 'π^(2/3)']
ax1.legend(lines, labels, loc='upper center', bbox_to_anchor=(0.3, 0.96), ncol=1, 
           frameon=True, fancybox=True, shadow=True, fontsize=9)

ax1.set_title('Harmonic Ladder Optimization: RMSE and HSI vs Harmonia Position', 
              fontsize=14)  

ax1.grid(alpha=0.25)

# save high-res files with tighter layout
plt.tight_layout()
plt.savefig("harmonic_ladder_RMSE_HSI_gold_indigo.png", dpi=300, bbox_inches='tight')
plt.savefig("harmonic_ladder_RMSE_HSI_gold_indigo.pdf", bbox_inches='tight')
plt.show()