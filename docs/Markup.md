# Forecast Markup Language (FML) – Tag Reference Cheat Sheet
Version 1.0 (For MSCFT v3.1B)

## Purpose
FML tags allow structured input into GPT for compliant, clean output using the Master SWARM Consensus Forecasting Template (MSCFT). Tags act as scaffolding only and are not printed in the final output.

## Tag Categories

### 1. Structural Tags
`<mscft>` – Wraps entire forecast  
`<forecast_title>` – Forecast title  
`<forecaster>` – Name of forecaster  
`<initial_question_framing>` – Starts question framing section  
`<refinement_and_analysis>` – Begins refinement/analysis section  
`<inside_outside_view>` – Inside-outside reasoning  
`<data_anomaly_log>` – Data anomaly section  
`<probability_allocation>` – Allocation section  
`<final_forecast_summary>` – Final call  
`<why_might_you_be_wrong>` – Risk introspection

### 2. Field-Level Tags
`<question>` – The forecast question  
`<clarifications>` – Clarifying details  
`<key_sources>` – Sources list  
`<key_developments>` – Key events  
`<interpretation>` – Narrative reasoning  
`<inside_view>` / `<outside_view>` – Contextual and analogical views  
`<date_range>` / `<observed_anomaly>` – Source review  
`<identified_cause>` / `<implication>` / `<action_taken>` – Anomaly logging  
`<bucket>` – A probability scenario group  
`<outcome>` / `<probability>` / `<rationale>` – Per-scenario metadata

### 3. Formatting & List Tags
`<li>` – Bullet item  
`<b>` – Bold (ignored in plaintext)  
`<i>` – Italic (ignored in plaintext)  
`<u>` – Underline (ignored in plaintext)  
`<note>` – Internal notes (not included in output)  
`<checkbox>` – Used in action and anomaly sections

## Guidelines
- Do **not** nest improperly (e.g., `<bucket>` inside `<inside_view>`).
- Use **lowercase tags** for consistency.
- Only GPT needs the tags — final MSCFT output will be plaintext.

## File Path
GitHub: `/docs/Markup.md`  
Required by: `CONTRIBUTING.md`

**Maintainer:** Brian Helip  
**Support:** OpenAI Copilot – MSCFT Project  
**License:** MIT
