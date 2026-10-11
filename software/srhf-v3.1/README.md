# SRHF v3.1 — Curated Python source reproduction package

This **source-only** package contains 13 unchanged SRHF Python sources: the canonical numerical model, a shared plotting module, and eleven plotting launchers. It contains **no** figures, manuscript, third-party package/wheel, font, virtual environment, private audit record, or repository/Git history.

## Reproduction

Preserve the directory structure shown in the package. The eleven launchers call `render()` from `v3.1/scripts/plotting.py`, which imports the canonical module from `audit/srhf_a0/canonical_srhf.py`. The model uses adopted rounded orbital semi-major axes, with Earth fixed as a 1 AU normalisation anchor.

The exact **tested** environment for byte-identical output was Debian Linux x86-64 / CPython 3.11.2, NumPy 1.26.4 and Matplotlib 3.9.2, with nine additional approved installed dependency distributions. See `requirements-b6b3-linux-cp311-hashed.txt` and `THIRD_PARTY_DEPENDENCIES.md`. In the private B6-B3 audit, all eleven wheels were independently downloaded, individually SHA-256 checked, installed offline in a fresh venv with system-site packages disabled, and passed `pip check`. All eleven generated figures matched the original frozen PNGs byte-for-byte; the corresponding numerical checks also passed. These are bounded measurements for this configuration, not a guarantee for other Python builds, operating systems, renderers or package versions.

Create a writable extraction root and install dependencies separately in a suitably controlled Python environment (the wheels themselves are not included). An example launcher command from the extracted root is:

```bash
MPLBACKEND=Agg python3 -E -s -B v3.1/scripts/srhf_harmonia_orbit.py
```

Each launcher writes its corresponding PNG to `v3.1/figures/` in the extracted root by default. The output directory may be newly created. No CLI options are required. The frozen Python files themselves should be left unchanged. Exact byte identity is renderer-specific.

## Scientific limits and names

The SRHF calculations are a **descriptive fixed algebraic orbital-distance prescription**, not an established theory of gravitational dynamics or a claim of statistically significant planetary spacing. The hypothesised Harmonia node is **unobserved** and excluded from nine-observation MAPE and RMSE. That population includes Pluto (an observed dwarf planet); Earth is the normalisation anchor. The standard `score()` fields are `n`, `mape_pct`, `rmse_au`, and `hsi_pct`; HSI is the population standard deviation of signed percentage residuals (percentage points), **not** a measure of physical orbital stability.

Two launcher filenames are historical: `srhf_ratios_full` graphs semi-major axes in AU, whereas `srhf_rmse_hsi_basin` graphs descriptive error/spread curves and **not** a dynamical stability basin. The titles and axes specify their actual meanings.

## License boundaries

The intended curated author's MIT source scope is the exact thirteen files in `SOURCE_LICENSE_SCOPE.md` accompanied by the complete original `LICENSE-CODE`. NumPy, Matplotlib and every other third-party dependency retain their independent terms; no such software is bundled. These notices do not relicense unrelated repository contents, previously released material, images or manuscripts.

**Public software edition (v3.1.0).** This curated 18-file source-only edition is intended for public release under the independently signed `software-v3.1.0` Git tag. The 13 Python source files, original MIT `LICENSE-CODE` and hashed dependency list are byte-identical to the private reviewed B6-D1 candidate; only the provisional release-status wording in the three accompanying documentation files was updated. The separately published v3.1 manuscript is available at https://doi.org/10.5281/zenodo.23301593. This software package does not contain the manuscript or its figures.
