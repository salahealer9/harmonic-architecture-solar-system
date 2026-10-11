# SRHF v3.1 — Third-party dependencies (not distributed)

This curated package contains only the author's original Python sources and documentation. It does **not** include Python interpreter binaries, NumPy, Matplotlib, any wheel or other third-party distribution, fonts, codecs, or generated figures. Dependencies must be obtained, verified and installed separately under their own licenses and copyright terms. In particular the SRHF MIT source license does not license them.

**Direct requirements:** NumPy and Matplotlib. The private offline clean-install B6-B3 test used Linux x86-64, CPython 3.11.2 and the following **exact 11 wheel versions** (two direct and nine transitive):

- `contourpy==1.3.3`
- `cycler==0.12.1`
- `fonttools==4.66.1`
- `kiwisolver==1.5.1`
- `matplotlib==3.9.2`
- `numpy==1.26.4`
- `packaging==26.3`
- `pillow==12.3.0`
- `pyparsing==3.3.3`
- `python-dateutil==2.9.0.post0`
- `six==1.17.0`

The companion `requirements-b6b3-linux-cp311-hashed.txt` identifies SHA-256 digests of the **specific Linux wheel files** verified and used in the private installation. It is not a cross-platform resolver lock or a promise that future package downloads will have those same wheel hashes. The original private wheelhouse is neither included nor authorized for public redistribution. B6-B3 verified `pip check`, 11/11 generator executions and 11/11 byte-identical reference PNGs; another operating system, library version, font installation or rendering backend may produce different PNG bytes while preserving numerical agreement.

## Licence overview (informational; not substitutes for complete upstream terms)

| Component | Recorded licensing context for separately installed software |
| --- | --- |
| NumPy | BSD-3-Clause style; component-specific terms may apply |
| Matplotlib | Matplotlib development-team license; distinct bundled fonts/backend components may have separate terms |
| contourpy | BSD-3-Clause |
| cycler | BSD-style |
| fontTools | MIT/Expat core; component-specific terms where applicable |
| kiwisolver | BSD-3-Clause and Kiwi component notices |
| packaging | Apache-2.0 OR BSD licensing choice |
| Pillow | MIT-CMU and component-specific terms |
| pyparsing | MIT/Expat core; example-specific exceptions if present |
| python-dateutil | BSD and Apache contribution context |
| six | MIT/Expat |

Any future decision to bundle or redistribute wheels, fonts or third-party components requires a **separate exact-byte rights and notice review**. The original full license texts were compared to the acquired wheels in B6-B2 (19 text identities, zero mismatches and zero additional notice groups in the bounded census). This comparison is evidence, not an independent legal opinion. The existing Debian Pillow and kiwisolver metadata peculiarities are historical environment observations, not new pins for this wheel set.

This public v3.1.0 edition distributes only its 13 author-controlled Python source files and the accompanying five documentation/licensing/requirements members. It does not distribute the manuscript, generated figures, wheels, binaries, fonts or private audit evidence. The separately published manuscript is https://doi.org/10.5281/zenodo.23301593.
