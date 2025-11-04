[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17521488.svg)](https://doi.org/10.5281/zenodo.17521488)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17432971.svg)](https://doi.org/10.5281/zenodo.17432971)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)

# The Harmonic Architecture of the Solar System
### Verification and Reproduction Scripts for *“The Gravitational Quantization Law: A Universal Harmonic Framework for Planetary Orbits”*

**Author:** Salah-Eddin Gherbi  
**Affiliation:** Independent Researcher, United Kingdom  
**ORCID:** [0009-0005-4017-1095](https://orcid.org/0009-0005-4017-1095)  
**Contact:** salahealer@gmail.com  
**Concept DOI:** [10.5281/zenodo.17477597](https://doi.org/10.5281/zenodo.17477597)  
**Latest Version:** [10.5281/zenodo.17521488](https://doi.org/10.5281/zenodo.17521488)  
**License:** [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)  

---

## 📘 Overview
This repository contains the core analytical and visualization scripts accompanying the published research:

> **Salah-Eddin Gherbi (2025)**  
> *The Harmonic Architecture of the Solar System: A Geometric and Resonant Analysis*  
> **Version 2.0** — Extended validation with empirical testing framework  
> Zenodo DOI: [10.5281/zenodo.17521488](https://doi.org/10.5281/zenodo.17521488)

> **Salah-Eddin Gherbi (2025)**  
> *The Gravitational Quantization Law: A Universal Harmonic Framework for Planetary Orbits*  
> **Version 1.0** — Initial harmonic framework  
> Zenodo DOI: [10.5281/zenodo.17432971](https://doi.org/10.5281/zenodo.17432971)

The research reinterprets Kepler's celestial harmony using the Celtic Cross harmonic model — a geometric framework based on algebraic ratios of √2 and its derivatives. The model accurately predicts planetary spacing, identifies the lost planet Harmonia at ≈ 2.14 AU, and demonstrates that the Solar System obeys a quantized harmonic order.

All included Python scripts reproduce the published figures, tables, and numerical results of the paper.

---

## 🚀 Version History

### Version 2.0 (November 2025) — Extended Validation & Testability
**Expands the quantitative and methodological foundations**, refining both empirical validation and theoretical testability of the Celtic Cross harmonic model.

**Key Enhancements:**
- **Empirical Validation**: Detailed statistical analysis demonstrating all planetary semi-major axes fit within sub-percent deviation (MAPE ≈ 0.72%, RMSE ≈ 0.11 AU)
- **Comparative Performance**: Outperforms classical Keplerian and Titius–Bode formulations by over an order of magnitude
- **Falsifiability Framework**: Explicit testable predictions, including harmonic node at 2.14 AU for future observational verification
- **Enhanced Reproducibility**: Complete cryptographic verification and timestamped analysis pipeline

**DOI:** [10.5281/zenodo.17521488](https://doi.org/10.5281/zenodo.17521488)

### Version 1.0 (October 2025) — Initial Framework
- Initial harmonic framework for Solar System
- Celtic Cross geometric model based on √2 ratios
- Harmonia orbital prediction at 2.14 AU
- Foundational scripts and verification proofs

**DOI:** [10.5281/zenodo.17432971](https://doi.org/10.5281/zenodo.17432971)

---

## 🔬 Research Evolution

**From Pattern to Predictive Framework:**
- **v1.0**: Established the core harmonic model and geometric foundation
- **v2.0**: Transformed into a testable scientific framework with:
  - **Quantitative validation** (0.72% MAPE across full solar system)
  - **Comparative benchmarking** vs. classical models
  - **Falsifiability criteria** for empirical testing
  - **Cryptographic reproducibility** guarantees

The model now stands as a **predictive, testable framework** rather than just a descriptive pattern.

---

## 📄 Research Records

### Version 2.0 — Extended Validation & Testability
**Salah-Eddin Gherbi (2025)**  
*The Harmonic Architecture of the Solar System: A Geometric and Resonant Analysis*  
**Zenodo DOI:** [10.5281/zenodo.17521488](https://doi.org/10.5281/zenodo.17521488)

📥 **PDF:** [`Gherbi_2025_Harmonic_Architecture_Solar_System_v_2.pdf`](./Gherbi_2025_Harmonic_Architecture_Solar_System_v_2.pdf)

*This version expands quantitative foundations with detailed empirical validation and explicit falsifiability tests, strengthening the model's scientific positioning.*

### Version 1.0 — Initial Framework  
**Salah-Eddin Gherbi (2025)**  
*The Gravitational Quantization Law: A Universal Harmonic Framework for Planetary Orbits*  
**Zenodo DOI:** [10.5281/zenodo.17432971](https://doi.org/10.5281/zenodo.17432971)

📥 **PDF:** [`Gherbi_2025_Harmonic_Architecture_Solar_System_v1_1.pdf`](./Gherbi_2025_Harmonic_Architecture_Solar_System_v1_1.pdf)

*This version establishes the core harmonic model and geometric foundation*

All computational models, harmonic optimization scripts, and figure-generation tools are included here for open verification.

---
# 📁 Repository Contents

## 🔹 1. Harmonic Model & Core Constants

Defines the fundamental ratios and geometric principles underlying the Celtic Cross framework.

| Script | Description |
|--------|-------------|
| `celtic_kepler_symbolic_verification.py` | Symbolic verification of the Celtic Cross ratios (√2 system) vs Kepler's geometric polyhedral ratios. |
| `celtic_full_system_verification.py` | Full model validation across the Solar System, comparing predicted and observed orbital distances. |
| `celtic_full_system_rmse.py` | Computes global RMSE to quantify overall model precision. |

## 🔹 2. Optimization & Harmonic Stability

Scripts demonstrating how the optimal harmonic node (2.14 AU) and minimal residual basin are identified.

| Script | Description |
|--------|-------------|
| `harmonia_position_optimization.py` | Empirical optimization of Harmonia's orbital position using RMSE minimization. |
| `harmonic_dual_optimization.py` | Joint RMSE–HSI comparison showing harmonic equilibrium near 2.145 AU. |
| `harmonic_basin_compact.py` | Compact illustration of the harmonic basin and stability valley around the optimum node. |

## 🔹 3. Planetary Ratios & Comparative Analysis

Compares model predictions, residuals, and ratios across planetary scales.

| Script | Description |
|--------|-------------|
| `harmonia_ratio_verification.py` | Tabulates harmonic ratios between planets including the theoretical Harmonia node. |
| `celtic_vs_kepler_comparison.py` | Quantitative error comparison between Kepler's and Celtic geometric models. |
| `celtic_mape_optimization.py` | Optimization of MAPE (mean absolute percentage error) across outer planets. |

## 🔹 4. Visualization & Figures

All published figures reproduced from the study, illustrating model accuracy and geometric harmony.

| Script | Description |
|--------|-------------|
| `harmonia_orbit_node_2_14.py` | Diagram of the Solar System showing the 2.14 AU harmonic node and asteroid belt context. |
| `harmonic_ladder_RMSE_HSI_Residuals_symlog_final.py` | Dual-axis plot of RMSE and HSI with symmetric log residuals (final publication figure). |
| `planetary_harmonic_percent_deviation_with_inset.py` | Percentage deviation plot with inset zoom around the Harmonia node. |

### `/figures/`
Rendered figures corresponding to each script.  
These are direct outputs of the models and are suitable for citation or publication.

### `/proofs/` *(not public in all releases)*
Contains `.asc`, `.ots`, and `_proof.txt` files documenting authorship, SHA-256 checksums, and blockchain timestamps for verification integrity.

## 🔹 5. Access to Extended Materials

Additional analytical and verification scripts (full suite of 26) are retained in a private research repository.

Researchers interested in the complete dataset, verification proofs, or replication materials may request access directly from the author at [salahealer@gmail.com](mailto:salahealer@gmail.com).

---

## 🧮 Computational Environment
All code was written in **Python 3**, using standard scientific libraries:
- `numpy`  
- `matplotlib`  
- `scipy`

All numerical results were computed in double precision.  
Plots use consistent color palettes (gold–indigo) for visual clarity.

---

## 🔒 Authorship and Integrity

All research scripts and results are **cryptographically timestamped** and **digitally signed** to ensure authorship integrity and reproducibility.  
A private `/proof/` archive (excluded from this repository) contains verified OpenTimestamps (`.ots`) proofs, GPG signatures (`.asc`), and manifest files (`_proof.txt`) for each script.  
These materials are securely stored offline and available for independent verification upon formal request.

The **full research implementation**, including advanced optimization and analysis scripts, will be released following the publication of the author’s forthcoming book.  
**Meanwhile, qualified researchers may request access to these extended materials for verification or collaborative purposes.**

**Access Policy:**  
Access to the private repository containing full source files and verification materials may be granted to verified researchers or collaborators upon formal request. Contact the author at [salahealer@gmail.com](mailto:salahealer@gmail.com) for details.

---

## 🧪 How to Reproduce the Figures

1. **Clone or download** this repository:  
   ```bash
   git clone https://github.com/salahealer9/harmonic-architecture-solar-system.git
   cd harmonic-architecture-solar-system/scripts
   ```
2. **Install required packages** (Python 3.10+):
   ```bash
   pip install numpy matplotlib scipy
   ```
4. **Run the scripts** to regenerate all figures:
   ```bash
   python celtic_kepler_symbolic_verification.py
   python celtic_full_system_verification.py
   python celtic_full_system_rmse.py
   python harmonia_position_optimization.py
   python harmonic_dual_optimization.py
   python harmonic_basin_compact.py
   python harmonia_ratio_verification.py
   python celtic_vs_kepler_comparison.py
   python celtic_mape_optimization.py
   python harmonia_orbit_node_2_14.py
   python harmonic_ladder_RMSE_HSI_Residuals_symlog_final.py
   python planetary_harmonic_percent_deviation_with_inset.py
   ```
   Each script will automatically produce .pdf and .png outputs in the working directory.
   
---

## 🧭 Verification Notes
For details on digital signatures and cryptographic timestamps, see the *Authorship and Integrity* section above.  
All original research files were timestamped and signed for integrity using:

- **.asc** → GPG digital signature  
- **.ots** → OpenTimestamps blockchain proof  
- **_proof.txt** → SHA-256 manifest  

Verification materials are stored in the private `/proof/` archive and are available for independent validation upon request.

---

## 📜 Citation
If you use or reference this repository, please cite:

> **Gherbi, S.-E. (2025)**. *The Harmonic Architecture of the Solar System: Verification and Reproduction Scripts*.  
> Zenodo. DOI: [10.5281/zenodo.17521488](https://doi.org/10.5281/zenodo.17521488)
> 
```bibtex
@software{gherbi_2025_harmonic_architecture,
  author    = {Salah-Eddin Gherbi},
  title     = {The Harmonic Architecture of the Solar System: A Geometric and Resonant Analysis},
  year      = {2025},
  publisher = {Zenodo},
  version   = {2.0},
  doi       = {10.5281/zenodo.17521488}
}
```

For citation of Version 1.0, please take a look at the Version History section.

---

## 📜 License
This repository is licensed under the  
[**Creative Commons Attribution–NonCommercial 4.0 International (CC BY–NC 4.0)**](https://creativecommons.org/licenses/by-nc/4.0/).  

© 2025 Salah-Eddin Gherbi.  
You may share and adapt this material for non-commercial purposes, provided appropriate credit is given.

---

## 🌠 Acknowledgment

All computations, analyses, and visualizations were independently developed by **Salah-Eddin Gherbi** as part of original research into the harmonic-geometric structure of the Solar System.

For academic collaboration, verification requests, or replication studies, please contact:  
**📧 salahealer@gmail.com**

---

## 🔒 Integrity Verification
All original research scripts and figures have been cryptographically timestamped and digitally signed to ensure authenticity and provenance.  
A public summary of the verification process is available here:  
➡️ [**README_PROTECTION_SUMMARY.md**](./README_PROTECTION_SUMMARY.md)

---

## 📬 Contact
**Author:** Salah-Eddin Gherbi  
**Email:** [salahealer@gmail.com](mailto:salahealer@gmail.com)  
**ORCID:** [0009-0005-4017-1095](https://orcid.org/0009-0005-4017-1095)  
**Repository:** [Harmonic Architecture Solar System](https://github.com/salahealer9/harmonic-architecture-solar-system)

