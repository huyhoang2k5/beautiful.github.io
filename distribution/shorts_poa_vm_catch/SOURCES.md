# Verified Sources & Technical References

Every factual claim in this script traces directly to verified codebase files and active consensus specifications in the official repository:

1. **Jitter & VM Detection Thresholds:**
   - Source: `Scottcjn/Rustchain` — `rip_200_round_robin_1cpu1vote.py` and `/attest/submit` validation handler.
   - Specification: Microsecond timing delta verification against calibrated baseline curves rejects hypervisor scheduling latency.

2. **Vintage Architecture Multipliers:**
   - Source: `Scottcjn/Rustchain` — Consensus tokenomics rules specifying higher baseline multipliers (up to 4.8x - 5.0x) for verified vintage architectures (G4, PowerPC, legacy x86) to equalize computational energy footprint.

3. **Canonical Wallet Pattern:**
   - Source: `Scottcjn/rustchain-bounties` — Issue #16988: `(?<![0-9A-Za-z])RTC[0-9a-f]{40}(?![0-9A-Za-z])`

4. **Live Reference Article:**
   - Full technical deep dive: [https://huyhoang2k5.github.io/solopreneur-kit/rustchain-mining-and-poa-tutorial/](https://huyhoang2k5.github.io/solopreneur-kit/rustchain-mining-and-poa-tutorial/)
