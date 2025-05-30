Forecast Markup Language (FML) – Tag Reference Cheat Sheet
Version 1.0 (For MSCFT v3.1B)

Purpose:
FML tags allow structured input into GPT for compliant, clean output using the Master SWARM Consensus Forecasting Template (MSCFT). Tags act as scaffolding only and are not printed in the final output.

Tag Categories:

1. Structural Tags <mscft>...</mscft> — Wraps the entire forecast entry
   \<forecast\_title>...\</forecast\_title> — Title of the forecast <forecaster>...</forecaster> — Name of the forecaster
   \<initial\_question\_framing>...\</initial\_question\_framing> — Start of question framing section
   \<refinement\_and\_analysis>...\</refinement\_and\_analysis> — Refinement & analysis section
   \<inside\_outside\_view>...\</inside\_outside\_view> — Inside/outside view section
   \<data\_anomaly\_log>...\</data\_anomaly\_log> — Log for data/source integrity concerns
   \<probability\_allocation>...\</probability\_allocation> — Forecast probability section
   \<final\_forecast\_summary>...\</final\_forecast\_summary> — Final probability summary
   \<why\_might\_you\_be\_wrong>...\</why\_might\_you\_be\_wrong> — Risk/uncertainty introspection

2. Field-Level Tags <question>...</question> — The forecasting question <clarifications>...</clarifications> — List of clarifying details
   \<key\_sources>...\</key\_sources> — List of source materials
   \<key\_developments>...\</key\_developments> — List of key developments <interpretation>...</interpretation> — Narrative analysis
   \<inside\_view>...\</inside\_view> — Perspective from within the scenario
   \<outside\_view>...\</outside\_view> — Analogy/historical perspective
   \<date\_range>...\</date\_range> — Time period affected
   \<observed\_anomaly>...\</observed\_anomaly> — Data issues observed
   \<identified\_cause>...\</identified\_cause> — Cause of anomaly <implication>...</implication> — How it impacts the forecast
   \<action\_taken>...\</action\_taken> — What was done to address it <bucket>...</bucket> — Repeated blocks for probability outcomes <outcome>...</outcome> — Description of each bucket <probability>...</probability> — Assigned probability <rationale>...</rationale> — Justification for the allocation

3. List & Formatting Tags

<li>...</li> — Single bullet item
<b>...</b> — Bold text (ignored in plaintext)
<i>...</i> — Italic text (ignored in plaintext)
<u>...</u> — Underlined text (ignored in plaintext)
<note>...</note> — Comment for GPT, not included in output
<checkbox>...</checkbox> — Checkbox items (used for anomaly/action logging)

Use Guidelines:

* Do not nest tags improperly (e.g., <bucket> inside \<inside\_view>).
* Use lowercase tags for consistent parsing.
* Avoid using tags in your final output (they are for GPT input only).
* All forecasts must conform to MSCFT v3.1B structure.

Recommended File Placement:
GitHub Path: /docs/Markup.md

Author: Brian Helip
Maintainer: OpenAI Copilot – MSCFT Project Support
License: MIT (if repository is public)
