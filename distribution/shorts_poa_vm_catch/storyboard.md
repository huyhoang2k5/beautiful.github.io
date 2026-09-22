# Storyboard: How RustChain Catches a Cloud VM Live (YouTube Shorts)

**Format:** 1080x1920 (Vertical 9:16)  
**Duration:** 52 seconds  
**Visual Style:** High-contrast developer terminal, neon blue (#38bdf8) and red (#dc2626) overlays, energetic sound cues.

---

### Shot 1: The Hook (00:00 - 00:06)
- **Visual:** Close-up screen recording of bash prompt executing `./attest_hardware --verify`. Text flashes RED: `[ALERT] EMULATED HYPERVISOR DETECTED`.
- **Text Overlay (Bold Yellow):** "CAN YOU FAKE VINTAGE HARDWARE?"
- **Audio Cue:** Fast digital glitch / buzzer sound.

### Shot 2: The Whales vs. Vintage Setup (00:06 - 00:18)
- **Visual:** Split screen. Top half: AWS EC2 dashboard with high-spec instance. Bottom half: Physical photo of vintage 2004 Power Mac G4 or Pentium III chassis.
- **Text Overlay:** "AWS Cloud (64 Cores) vs. G4 Mac (2004)"
- **Graphic:** RustChain PoA logo transitioning in the center.

### Shot 3: The Live Catch (00:18 - 00:35)
- **Visual:** Terminal output running the RustChain cycle attestation script. Graph shows steady cycle line for real silicon, then fluctuating erratic curve for QEMU hypervisor.
- **Highlight Box (Red):** `Jitter: 0.142ms > Max Allowable 0.080ms`
- **Text Overlay:** "BUSTED: CPU Timing Jitter Anomalies"
- **Audio Cue:** Stamp sound effect: "REJECTED".

### Shot 4: Real Hardware Wins (00:35 - 00:48)
- **Visual:** Terminal on physical hardware running `python miner/headless_miner.py`. Output flashes bright green: `Attestation Verified: Genuine PowerPC G4 7447A | Multiplier: 4.8x | Mining Slot Awarded`.
- **Text Overlay:** "GENUINE SILICON: 4.8x MULTIPLIER"
- **Audio Cue:** Success chime.

### Shot 5: Outro & Attribution (00:48 - 00:52)
- **Visual:** Clean card displaying:
  - Repository: `github.com/Scottcjn/Rustchain`
  - Created by: `@huyhoang2k5` (Elyan Labs Contributor)
- **Text Overlay:** "Explore Proof of Antiquity on GitHub"
