# BIN Tagging Guide for MSCFT Forecasts (v1.0)

This guide helps forecasters using the Master SWARM Consensus Forecasting Template (MSCFT) to classify the origin of changes or anomalies in data and probability assessments using the BIN model:
- **B** = Bias
- **I** = Information
- **N** = Noise

## Purpose
BIN tagging supports better introspection, auditability, and long-term calibration by distinguishing between meaningful and misleading forecast changes.

---

## Where to Tag in the MSCFT

BIN Tags should be added in two locations:

1. **Refinement & Analysis → Interpretation**  
   Tag any observed shifts in crowd, institutional, or personal forecast weights with (B), (I), or (N).

   **Example:**  
   “The recent +11.2% shift in the 'Before 25 July 2025' bucket appears to reflect speculative early resolution bets rather than new information (N).”

2. **Data Anomaly & Source Integrity Log**  
   Use BIN tags to classify the source of any anomalies in source quality or signal interpretation.

   **Example:**  
   “Observed crowd spike (27 May): +11% in high-volatility bucket without matching macroeconomic release. Tagged as (N).”

---

## BIN Tag Definitions

- **(B) Bias**
  - Personal, cognitive, institutional, or structural bias.
  - Examples: optimism bias, herd behavior, wishful thinking.

- **(I) Information**
  - New credible data or signal with analytical implications.
  - Examples: government report, earnings release, policy speech.

- **(N) Noise**
  - Volatility, crowd shifts, speculative positioning, or unsubstantiated movement.
  - Examples: unexplained jumps in crowd forecasts, thin-trading periods.

---

## Optional: Summary Tag at Bottom of Each MSCFT

Add a final audit line:

`BIN Summary: [Main driver of this forecast update — e.g., (I)]`

If multiple tags apply, use:  
`BIN Summary: Mixed (I/N)`

---

## GitHub Instructions: Adding This File to MSCFT Repository

1. Open your GitHub repository in the browser.
2. Navigate to the `/docs` folder (or create it if it doesn't exist).
3. Click **Add File** > **Create new file**.
4. Name it: `BIN-Tagging-Guide.md`
5. Paste this full guide into the editor window.
6. Scroll down to commit:
   - Add commit message: `Add BIN tagging guide v1.0`
   - Select **Commit directly to the main branch**
7. Click **Commit new file**

The BIN Tagging Guide will now be part of your official forecasting documentation.

---

