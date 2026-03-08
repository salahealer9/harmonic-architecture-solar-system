# Provenance & Cryptographic Integrity Record

This file documents the cryptographic authorship verification for the manuscript 
submitted to Frontiers in Astronomy and Space Sciences (2025).

Verification files and full instructions are located in `v3.0/proof/`.

**Manuscript:** *The Harmonic Architecture of the Solar System: A Silver-Ratio-Based Hypothesis for Planetary Spacing*  
**Author:** Salah-Eddin Gherbi  

This document provides a complete, verifiable cryptographic provenance record for the files archived in this repository. The goal is to ensure **authorship proof**, **content integrity**, and **long-term reproducibility** using SHA-256 hashing, GPG digital signatures, and OpenTimestamps (OTS) Bitcoin calendar attestations.

---

## 1. SHA-256 Digest (Content Integrity)

The SHA-256 hash uniquely identifies the ZIP file contents:

```
56ff9ec4415a94ae0b3e29eaa9865eb22337481d24121ad8b5f3c32c90607a2b
```

To verify on any system:

```bash
sha256sum harmonic_architecture_frontiers_v1.zip
```

The output must match the hash above exactly.

---

## 2. GPG Digital Signature (Authorship Verification)

The ZIP archive is signed with the author's private GPG key using a detached,
ASCII-armored signature.

```bash
gpg --verify harmonic_architecture_frontiers_v1.zip.asc harmonic_architecture_frontiers_v1.zip
```

A successful verification confirms authorship and that the file has not been
altered since signing.

---

## 3. OpenTimestamps (OTS) Proof

The OTS receipt proves the ZIP existed no later than the moment the timestamp
was submitted to the Bitcoin calendar servers.

```bash
ots verify harmonic_architecture_frontiers_v1.zip.ots
```

If fully confirmed, verification will show:

- `anchored in Bitcoin`
- `timestamp commitment included`
- `proof valid`

If the result shows `pending`, verify again later — confirmation occurs after
Bitcoin calendar aggregation, typically within a few hours.

---

## 4. Files Required for Verification

Keep these files together to enable full independent verification:

```
harmonic_architecture_frontiers_v1.zip
harmonic_architecture_frontiers_v1.zip.sha256
harmonic_architecture_frontiers_v1.zip.asc
harmonic_architecture_frontiers_v1.zip.ots
README_PROVENANCE.md
```

---

## 5. Contact

**Author:** Salah-Eddin Gherbi  
**Email:** salahealer@gmail.com  
**GitHub:** https://github.com/salahealer9  
**ORCID:** 0009-0005-4017-1095
