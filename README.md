[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18816002.svg)](https://doi.org/10.5281/zenodo.18816002)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17521488.svg)](https://doi.org/10.5281/zenodo.17521488)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17432971.svg)](https://doi.org/10.5281/zenodo.17432971)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)

# The Harmonic Architecture of the Solar System
### Verification and Reproduction Scripts for the Silver-Ratio Harmonic Framework (SRHF)

📦 **Version 3.0 released:** Revised and expanded manuscript — submitted to
*Frontiers in Astronomy and Space Sciences*, archived on Zenodo as the definitive preprint.

**Author:** Salah-Eddin Gherbi  
**Affiliation:** Independent Researcher, United Kingdom  
**ORCID:** [0009-0005-4017-1095](https://orcid.org/0009-0005-4017-1095)  
**Contact:** salahealer@gmail.com  
**Concept DOI (always resolves to latest):** [10.5281/zenodo.17432971](https://doi.org/10.5281/zenodo.17432971)  
**Latest Version DOI:** [10.5281/zenodo.18816002](https://doi.org/10.5281/zenodo.18816002)  
**License:** [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)

---

## 📘 Overview

This repository contains the analytical and visualisation scripts accompanying the research:

> **Salah-Eddin Gherbi (2026)**  
> *The Harmonic Architecture of the Solar System:  
> A Silver-Ratio-Based Hypothesis for Planetary Spacing*  
> **Version 3.0** — Revised and expanded manuscript, definitive preprint  
> Zenodo DOI: [10.5281/zenodo.18816002](https://doi.org/10.5281/zenodo.18816002)

This research is the companion paper to the author's book:

> **Salah-Eddin Gherbi (2026)**  
> *Scala Harmonica: The Geometry of Planetary Resonance*

The research reinterprets planetary spacing using the Celtic Cross harmonic model — a
geometric framework based on algebraic ratios of √2 and its derivatives. The model
accurately predicts planetary semi-major axes, identifies the hypothesised lost planet
*Harmonia* at ≈ 2.14 AU, and demonstrates that the Solar System obeys a quantised
harmonic order. All included Python scripts reproduce the published figures, tables,
and numerical results of the paper.

---

## 🚀 Version History

### Version 3.0 (2026) — Revised Manuscript, Definitive Preprint

Substantially revised version submitted to *Frontiers in Astronomy and Space Sciences*,
archived on Zenodo as the definitive preprint. This version supersedes v2.0.

**Key Changes:**
- Revised and expanded manuscript with improved presentation and cleaner mathematical
  exposition
- Updated SRHF geometric construction figure (`srhf_geometry_circles.png`) now shows
  the full Celtic Cross geometry with labelled harmonic constants $(A, B, C, D)$
- Refined section structure with clearer separation of empirical results, comparative
  analysis, and speculative connections
- All quantitative results unchanged: MAPE ≈ 0.72%, RMSE ≈ 0.11 AU
- Python scripts updated to reflect consistent SRHF terminology throughout

**DOI:** [10.5281/zenodo.18816002](https://doi.org/10.5281/zenodo.18816002)

📥 **PDF:** [`v3.0/Gherbi_2026_Harmonic_Architecture_Solar_System_v3.pdf`](./v3.0/Gherbi_2026_Harmonic_Architecture_Solar_System_v3.pdf)

---

### Version 2.0 (November 2025) — Extended Validation & Testability

Expanded quantitative and methodological foundations, refining both empirical
validation and theoretical testability of the Celtic Cross harmonic model.

**Key Enhancements:**
- Empirical validation: MAPE ≈ 0.72%, RMSE ≈ 0.11 AU across all planetary orbits
- Comparative performance: outperforms classical Keplerian and Titius–Bode models by
  over an order of magnitude
- Falsifiability framework: explicit testable predictions including harmonic node at
  2.14 AU
- Enhanced reproducibility: cryptographic verification and timestamping pipeline

**DOI:** [10.5281/zenodo.17521488](https://doi.org/10.5281/zenodo.17521488)

📥 **PDF:** [`Gherbi_2025_Harmonic_Architecture_Solar_System_v_2.pdf`](./Gherbi_2025_Harmonic_Architecture_Solar_System_v_2.pdf)

---

### Version 1.0 (October 2025) — Initial Framework

Initial harmonic framework for the Solar System. Celtic Cross geometric model based
on √2 ratios. Harmonia orbital prediction at 2.14 AU. Foundational scripts and
verification proofs.

**DOI:** [10.5281/zenodo.17432971](https://doi.org/10.5281/zenodo.17432971)

📥 **PDF:** [`Gherbi_2025_Harmonic_Architecture_Solar_System_v1_1.pdf`](./Gherbi_2025_Harmonic_Architecture_Solar_System_v1_1.pdf)

---

## 🔬 Research Evolution

| Version | Focus | Key achievement |
|---------|-------|-----------------|
| v1.0 | Core harmonic model | Celtic Cross geometry, Harmonia prediction |
| v2.0 | Testable framework | Quantitative validation, falsifiability criteria |
| v3.0 | Definitive preprint | Revised manuscript, improved exposition, journal submission |

---

## 📁 Repository Structure

```
harmonic-architecture-solar-system/
│
├── v3.0/                          ← Version 3.0 (current)
│   ├── scripts/                   ← Python scripts for v3.0
│   ├── figures/                   ← Output figures for v3.0
│   └── proof/                     ← Cryptographic provenance for v3.0
│
├── scripts/                       ← Scripts from v1.0–v2.0 (preserved)
├── figures/                       ← Figures from v1.0–v2.0 (preserved)
├── proof/                         ← Proof archive from v1.0–v2.0 (preserved)
│
├── Gherbi_2025_Harmonic_Architecture_Solar_System_v1_1.pdf
├── Gherbi_2025_Harmonic_Architecture_Solar_System_v_2.pdf
├── README.md
├── README_PROVENANCE.md
└── README_PROTECTION_SUMMARY.md
```

> **Note:** The `scripts/`, `figures/`, and `proof/` folders at the repository root
> belong to **v1.0 and v2.0**. All v3.0 materials are self-contained within the
> `v3.0/` subfolder.

---

## 📂 Version 3.0 Contents

### 🔹 `v3.0/scripts/` — Python Scripts

All scripts have been updated to reflect consistent SRHF terminology throughout.
The underlying computations, constants, and outputs are unchanged from v2.0.

| Script | Description |
|--------|-------------|
| `srhf_harmonia_optimisation.py` | RMSE optimisation of the Harmonia node over [2.12, 2.18] AU |
| `srhf_harmonia_orbit.py` | Solar System diagram showing the 2.14 AU harmonic node and asteroid belt context |
| `srhf_hsi_values.py` | Harmonic Symmetry Index curve showing the narrow stability basin |
| `srhf_log_validation.py` | Observed and predicted semi-major axes on logarithmic scale |
| `srhf_percent_deviation.py` | Percentage deviation plot with 0.72% mean absolute error band |
| `srhf_ratios_full.py` | Full-system observed-to-predicted ratios from Mercury to Pluto |
| `srhf_ratios_zoom.py` | Zoomed ratios for Mars–Pluto range highlighting ≲1.5% deviations |
| `srhf_residuals_comparison.py` | Percentage residuals comparing algebraic, empirical, and π²/³ Harmonia nodes |
| `srhf_residuals_log.py` | Logarithmic residuals showing Neptune's zero crossing at the empirical optimum |
| `srhf_residuals_symlog.py` | Symmetric logarithmic residuals revealing harmonic inversion and stability region |
| `srhf_rmse_hsi_basin.py` | Dual-axis RMSE and HSI plot showing the harmonic equilibrium basin |

### 🔹 `v3.0/figures/` — Output Figures

| Figure | Description |
|--------|-------------|
| `srhf_geometry_circles.png` | Full Celtic Cross geometry with labelled harmonic constants $(A, B, C, D)$ — updated figure for v3.0 |
| `srhf_harmonia_optimisation.png` | RMSE optimisation curve |
| `srhf_harmonia_orbit.png` | Harmonia node orbit diagram |
| `srhf_harmonic_ladder.png` | Complete Solar System harmonic ladder expressed in terms of δ_s |
| `srhf_hsi_values.png` | Harmonic Symmetry Index |
| `srhf_log_validation.png` | Log-scale validation |
| `srhf_percent_deviation.png` | Percentage deviations |
| `srhf_quantum_celestial.png` | Quantum–Celestial analogy: Bohr model vs SRHF |
| `srhf_ratios_full.png` | Full-system ratios |
| `srhf_ratios_zoom.png` | Mars–Pluto zoom |
| `srhf_residuals_comparison.png` | Residuals comparison |
| `srhf_residuals_log.png` | Logarithmic residuals |
| `srhf_residuals_symlog.png` | Symlog residuals |
| `srhf_rmse_hsi_basin.png` | RMSE–HSI harmonic basin |

### 🔹 `v3.0/proof/` — Cryptographic Provenance

This folder contains the integrity and authorship verification package for the v3.0
manuscript and associated scripts, consistent with the methodology described in
[`README_PROVENANCE.md`](./README_PROVENANCE.md).

| File | Description |
|------|-------------|
| `harmonic_architecture_frontiers_v1.zip` | ZIP archive of all submitted files |
| `harmonic_architecture_frontiers_v1.zip.sha256` | SHA-256 content digest |
| `harmonic_architecture_frontiers_v1.zip.asc` | GPG detached signature (authorship proof) |
| `harmonic_architecture_frontiers_v1.zip.ots` | OpenTimestamps Bitcoin-anchored timestamp |
| `README_PROVENANCE.md` | Full provenance and verification instructions |

To verify integrity independently:
```bash
sha256sum harmonic_architecture_frontiers_v1.zip
gpg --verify harmonic_architecture_frontiers_v1.zip.asc harmonic_architecture_frontiers_v1.zip
ots verify harmonic_architecture_frontiers_v1.zip.ots
```

---

## 📂 Previous Version Contents (root-level)

> The `scripts/`, `figures/`, and `proof/` folders at the repository root contain
> materials from **v1.0 and v2.0** and are preserved for continuity and
> reproducibility.

### 🔹 `scripts/` (v1.0–v2.0)

| Script | Description |
|--------|-------------|
| `celtic_kepler_symbolic_verification.py` | Symbolic verification of Celtic Cross ratios vs Kepler's polyhedral ratios |
| `celtic_full_system_verification.py` | Full model validation across the Solar System |
| `celtic_full_system_rmse.py` | Global RMSE computation |
| `harmonia_position_optimization.py` | Empirical optimisation of Harmonia's orbital position |
| `harmonic_dual_optimization.py` | Joint RMSE–HSI comparison |
| `harmonic_basin_compact.py` | Harmonic basin and stability valley |
| `harmonia_ratio_verification.py` | Harmonic ratio tabulation including Harmonia node |
| `celtic_vs_kepler_comparison.py` | Quantitative error comparison |
| `celtic_mape_optimization.py` | MAPE optimisation across outer planets |
| `harmonia_orbit_node_2_14.py` | Solar System diagram with 2.14 AU node |
| `harmonic_ladder_RMSE_HSI_Residuals_symlog_final.py` | Dual-axis RMSE/HSI with symlog residuals |
| `planetary_harmonic_percent_deviation_with_inset.py` | Percentage deviation with inset zoom |

---

## 🧮 Computational Environment

All code written in **Python 3**, using standard scientific libraries:

- `numpy` 1.26
- `matplotlib` 3.9
- `scipy` 1.13

All numerical results computed in double precision. Figures exported in PDF/PNG
at 600 DPI using Matplotlib.

---

## 🧪 How to Reproduce the v3.0 Figures

1. **Clone or download** this repository:
   ```bash
   git clone https://github.com/salahealer9/harmonic-architecture-solar-system.git
   cd harmonic-architecture-solar-system/v3.0/scripts
   ```

2. **Install required packages** (Python 3.10+):
   ```bash
   pip install numpy matplotlib scipy
   ```

3. **Run the scripts:**
   ```bash
   python srhf_harmonia_optimisation.py
   python srhf_harmonia_orbit.py
   python srhf_hsi_values.py
   python srhf_log_validation.py
   python srhf_percent_deviation.py
   python srhf_ratios_full.py
   python srhf_ratios_zoom.py
   python srhf_residuals_comparison.py
   python srhf_residuals_log.py
   python srhf_residuals_symlog.py
   python srhf_rmse_hsi_basin.py
   ```
   Each script produces `.pdf` and `.png` outputs in the working directory.

---

## 🔒 Authorship and Integrity

All research scripts and results are **cryptographically timestamped** and
**digitally signed** to ensure authorship integrity and reproducibility.
The `v3.0/proof/` folder contains the complete provenance package for this version.
Root-level `proof/` materials cover v1.0 and v2.0.

See [`README_PROVENANCE.md`](./README_PROVENANCE.md) for full verification
instructions including SHA-256, GPG, and OpenTimestamps procedures.

---

## 📜 Citation

Please cite the latest version using the v3.0 DOI:

> **Gherbi, S.-E. (2026)**. *The Harmonic Architecture of the Solar System:
> A Silver-Ratio-Based Hypothesis for Planetary Spacing*. Version 3.0.
> Zenodo. DOI: [10.5281/zenodo.18816002](https://doi.org/10.5281/zenodo.18816002)

```bibtex
@article{gherbi_2026_harmonic_architecture,
  author    = {Gherbi, Salah-Eddin},
  title     = {The Harmonic Architecture of the Solar System:
               A Silver-Ratio-Based Hypothesis for Planetary Spacing},
  year      = {2026},
  publisher = {Zenodo},
  version   = {3.0},
  doi       = {10.5281/zenodo.18816002}
}

@book{gherbi_2026_scala_harmonica,
  author    = {Gherbi, Salah-Eddin},
  title     = {{Scala Harmonica: The Geometry of Planetary Resonance}},
  publisher = {Vektor Publishing},
  year      = {2026},
  isbn      = {9781837095209}
}
```

For citation of specific earlier versions, see the Version History section above.

---

## 📜 License

This repository is licensed under the
[**Creative Commons Attribution–NonCommercial 4.0 International (CC BY–NC 4.0)**](https://creativecommons.org/licenses/by-nc/4.0/).

© 2026 Salah-Eddin Gherbi.  
You may share and adapt this material for non-commercial purposes,
provided appropriate credit is given.

---

## 🔒 Integrity Verification

All original research scripts and figures have been cryptographically timestamped
and digitally signed to ensure authenticity and provenance.

➡️ [`README_PROVENANCE.md`](./README_PROVENANCE.md) — full verification instructions  
➡️ [`README_PROTECTION_SUMMARY.md`](./README_PROTECTION_SUMMARY.md) — public summary

---

## 📬 Contact

**Author:** Salah-Eddin Gherbi  
**Email:** [salahealer@gmail.com](mailto:salahealer@gmail.com)  
**ORCID:** [0009-0005-4017-1095](https://orcid.org/0009-0005-4017-1095)  
**Repository:** [harmonic-architecture-solar-system](https://github.com/salahealer9/harmonic-architecture-solar-system)
