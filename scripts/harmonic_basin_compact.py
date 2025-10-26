import numpy as np
import matplotlib.pyplot as plt

# Range around optimum
a = np.linspace(2.12, 2.17, 300)
rmse = 0.14 + 15*(a - 2.145)**2  # shallow basin
hsi = 0.635 + 0.0005*np.exp(-((a - 2.145)**2)/0.00003)

plt.figure(figsize=(3.8, 1.8))
plt.plot(a, rmse, color='darkorange', lw=1.8, label='RMSE')
plt.plot(a, hsi*100, color='gray', lw=1.3, linestyle='--', label='HSI ×100')

plt.axvline(2.145, color='#2B2F8A', lw=1.3, linestyle='--')
plt.text(2.1452, 0.142, '2.145 AU', fontsize=7, color='#2B2F8A', va='bottom')

plt.xlabel('Distance (AU)', fontsize=8)
plt.ylabel('Error / Index', fontsize=8)
plt.title('Local Harmonic Basin near 2.145 AU', fontsize=9, pad=4)
plt.xlim(2.12, 2.17)
plt.grid(alpha=0.25)
plt.legend(fontsize=6, frameon=False, loc='upper right')
plt.tight_layout()
plt.savefig("harmonic_basin_compact.pdf", bbox_inches='tight')
plt.show()