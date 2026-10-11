# Provenance & Cryptographic Integrity Record

This is a historical provenance note for the 2025 Frontiers submission. It does not certify the corrected v3.1 manuscript or the separate v3.1.0 software release.

The associated ZIP, detached signature, SHA-256 file and OpenTimestamps receipt are publicly tracked under `v3.0/proof/`.

**Manuscript:** *The Harmonic Architecture of the Solar System: A Silver-Ratio-Based Hypothesis for Planetary Spacing*  
**Author:** Salah-Eddin Gherbi

These artifacts support file-specific verification, subject to checking the signatures, hashes and timestamp receipts. They do not independently prove scientific priority or correctness.

---

## 1. SHA-256 Digest (Content Integrity)

The historical SHA-256 digest recorded for the archived ZIP is:

```
56ff9ec4415a94ae0b3e29eaa9865eb22337481d24121ad8b5f3c32c90607a2b
```

To verify on any system:

```bash
sha256sum v3.0/proof/harmonic_architecture_frontiers_v1.zip
```

The output must match the hash above exactly.

---

## 2. GPG Digital Signature (Authorship Verification)

The ZIP archive is signed with the author's private GPG key using a detached,
ASCII-armored signature.

```bash
gpg --verify v3.0/proof/harmonic_architecture_frontiers_v1.zip.asc v3.0/proof/harmonic_architecture_frontiers_v1.zip
```

A successful signature verification confirms that the signature matches the supplied file under the specified public key. Identification of the signer and scientific authorship require separate evidence.

---

## 3. OpenTimestamps (OTS) Proof

If independently validated and anchored, an OTS receipt can establish that the committed file bytes existed no later than the relevant blockchain timestamp. It does not independently establish authorship or the date of a scientific discovery.

```bash
ots verify v3.0/proof/harmonic_architecture_frontiers_v1.zip.ots
```

If fully confirmed, verification will show:

- `anchored in Bitcoin`
- `timestamp commitment included`
- `proof valid`

If the result shows `pending`, verify again later — confirmation occurs after
Bitcoin calendar aggregation, typically within a few hours.

---

## 4. Files Required for Verification

The following files are tracked together under `v3.0/proof/` for independent verification:

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
