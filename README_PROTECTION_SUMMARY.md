# 🔒 Discovery Protection Summary

## Overview

This document summarises historical cryptographic provenance records for the Solar System harmonic architecture research. Associated public proof artifacts are tracked under `proof/` and `v3.0/proof/`.

GPG signatures, cryptographic hashes and OpenTimestamps receipts can provide file-specific integrity, signing-key and timestamped-existence evidence when independently verified. They do not independently establish scientific authorship, originality, priority or correctness.

---

## 🧾 Protection Methodology

| Layer | Verification scope |
|:------|:-------------------|
| GPG signature (`.asc`) | Tests whether a signature matches particular file bytes under a specified public key. |
| SHA-256 manifest (`_proof.txt`) | Records file digests against which file integrity can be checked. |
| OpenTimestamps receipt (`.ots`) | Can establish an upper bound on the existence time of committed bytes, subject to successful receipt and blockchain-anchor verification. |

These mechanisms do not themselves validate scientific interpretations or independently establish the identity of an original discoverer.

---

## 🔍 Verification

Historical public artifacts are available in `proof/` and `v3.0/proof/`. Verify each artifact against its corresponding original file rather than inferring validity from its filename or historical status label.

For a given file and its corresponding proof files, typical commands are:

```bash
sha256sum <file>
gpg --verify <file>.asc <file>
ots verify <file>.ots
```

Additional privately retained evidence, if required, must be evaluated separately.
## 📗 Discovery Record

**Historical research subject:** The Harmonic Quantization Law of the Solar System

**Historical evidence methods:** OpenTimestamps + GPG

**Historical verification date recorded:** October 25, 2025

**Author:** Salah-Eddin Gherbi  
**ORCID:** 0009-0005-4017-1095  
**Contact:** salahealer@gmail.com

## 📜 Citation

Gherbi, S.-E. (2025). *The Harmonic Architecture of the Solar System: Discovery Protection Record*. 
Private cryptographic archive (OpenTimestamps + GPG verification). 
Available from author upon request for verification purposes.

## ⚖️ Licensing and evidence scope

**Copyright © 2025 Salah-Eddin Gherbi**

This is a historical provenance description, not a certification of scientific priority or discovery.

The v3.1 manuscript is distributed under CC BY-NC 4.0. The specifically enumerated author-controlled Python source files in `software/srhf-v3.1/` have separate MIT licensing. Historical repository materials and third-party dependencies retain their applicable terms.
