![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Last Commit](https://img.shields.io/github/last-commit/captbullett65/MSCFT)
![Repo Size](https://img.shields.io/github/repo-size/captbullett65/MSCFT)
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=captbullett65.MSCFT)

> The Master SWARM Consensus Forecasting Template — a structured, auditable forecasting framework integrating human and LLM collaboration.
> # Master SWARM Consensus Forecasting Template (MSCFT)

A forecasting framework for structured, auditable multi-agent forecasting using language models and human inputs. Includes trusted agent profiles, disqualification logs, and version-controlled templates.

Created and maintained by: Brian Helip  
MIT License – Use with credit.  


[Forecast Index](forecast-index.md)

# MSCFT

Master SWARM Consensus Forecasting Template — structured methodology for forecast framing, analysis, and audit.

# Master SWARM Consensus Forecasting Template (MSCFT)

The Master SWARM Consensus Forecasting Template (MSCFT) is a structured framework for developing, documenting, and auditing long-range, short-range forecasts across domains such as innovation, geopolitics, and public policy. This repository supports consistent forecasting practices for projects like the Good Judgment Open Vehicle Innovation Challenge (2025 & 2027), enabling transparent, high-quality judgment-based analysis.

## How to Use the MSCFT

This section provides full instructions for using the MSCFT template with or without forecasting platforms.

### Key Use Cases

* Good Judgment Open, Range, RAND (RFI), Metaculus, and IARPA (crowdsourcing) projects
* Personal forecasting or journaling for learning
* Team-based scenario planning or risk analysis
* Academic use in economics, politics, policy, and technology domains

### Key Principles

* The MSCFT structure helps reduce bias, improve information processing, and limit noise — consistent with the BIN model.
* It is ideal for LLM-assisted workflows: the forecaster leads, while the LLM helps generate, clarify, refine, and validate reasoning.
* You can use it independently or collaboratively — forecasts are reproducible and ready for comparison.

### Background and Design Inspiration

MSCFT incorporates best practices drawn from applied forecasting, intelligence analysis, and structured analytic techniques. Notably, its framework and structure were influenced by the program/project management philosophies used in NASA’s [APPEL Knowledge Services](https://appel.nasa.gov/program-project-management/), where lifecycle discipline, auditability, and structured reasoning are foundational.

This makes MSCFT suitable for long-term forecasting initiatives, research, and collaborative problem solving — not just one-off predictions.

### Step-by-Step Instructions

#### 1. Forecast Title

Give your forecast a specific, clear name.

#### 2. Initial Question Framing

* **Question:** Copy or write the question you’re answering.
* **Clarifications:** Add key dates, assumptions, definitions, or known values.
* **Key Sources:** List any data, news, reports, or research supporting your reasoning.

#### 3. Refinement & Analysis

* **Key Developments:** What’s happening that affects the forecast?
* **Interpretation:** Connect trends or scenarios to your reasoning.

*Tip: Use an LLM to generate analogies, test assumptions, or find outside views to strengthen your analysis.*

#### 4. Data Anomaly & Source Integrity Log

Note any irregularities in your data (e.g., outdated info, contradictions, or missing pieces). If clean, write “No anomalies noted.”

#### 5. Probability Allocation

* Indicate whether the forecast is **binary** (Yes/No) or **multi-bucket** (ranges or categories).
* Use buckets that add to **100%**.
* Follow official platform formats when applicable (e.g., GJO), or define your own clearly.

**Example (Multi-Bucket):**

* 10% — Less than 2%
* 40% — Between 2% and 3%
* 30% — Between 3% and 4%
* 20% — 4% or more

**Example (Binary):**

* 70% — Yes
* 30% — No

#### 6. Final Forecast Summary

Write a short 3–5 sentence summary of your prediction and why you believe it’s likely.

#### 7. Why Might You Be Wrong?

List 2–3 possible failure points:

* Surprise events
* Bad assumptions
* Low-quality data

#### 8. Inside-Outside View Comparison *(Optional – v3.1B Beta)*

* **Inside View:** Forecast based on context, intent, timing, or players.
* **Outside View:** Compare against base rates or historical analogs.

### Using MSCFT Without a Platform

If you're not posting to GJO or Metaculus:

* Treat this as your personal forecasting log.
* Save entries in `.txt` or `.docx` format with version numbers or timestamps.
* Track results over time and update forecasts as new data arrives.

### Final Notes

* MSCFT is LLM-friendly by design — think of the model as a copilot, not a replacement for your reasoning.
* Keep your forecasts replicable, transparent, and structured for post-analysis.
* This methodology draws structural inspiration from NASA’s APPEL Knowledge Services, used in high-integrity program and project management.

---
## 📌 Purpose

This project provides a standardized, auditable process for producing and maintaining high-integrity forecast logs. The MSCFT framework helps forecasters:
- Clearly frame and refine questions.
- Identify and document anomalies or source integrity concerns.
- Allocate probability using consistent buckets or binary formats.
- Introspect on potential sources of forecast error.
- Maintain internal validation logs and track performance over time.

  ## Forecasting Tools

- [MSCFT Template (v3.1B – Standard)](docs/MSCFT-Template-Plain-v3.1B.txt)
- [MSCFT Template (v3.1B – BIN Tagging Integrated)](docs/MSCFT-Template-Plain-BIN-v3.1B.txt)
- [BIN Tagging Guide](docs/BIN-Tagging-Guide.md)


## 🧭 Structure

The core template includes **Eight required sections** for each forecast:

1. Forecast Title  
2. Initial Question Framing  
3. Refinement & Analysis
4. Inside-Outside View Structuring
5. Data Anomaly & Source Integrity Log  
6. Probability Allocation  
7. Final Forecast Summary  
8. Why Might You Be Wrong? (two perspectives required)

All forecasts must follow this structure exactly.

## 📂 Repository Layout
/docs/       → MSCFT documentation, FML reference, and forecast index  
/examples/   → Completed forecasts  
/logs/       → Audit trails and validation notes  
/templates/  → Plain-text and Markdown versions of the MSCFT forecast template  
/backups/    → Versioned snapshots of forecasts and logs  



## ✅ Forecasting Standards

- Use only **approved Good Judgement Open and RANGE  bucket phrasing**:
  - 2 or fewer  
  - Between 3 and 5  
  - Between 6 and 8  
  - Between 9 and 12  
  - Between 13 and 16  
  - Between 17 and 21  
  - 22 or more

- Ensure probability totals **add to exactly 100%**.
- Confirm if the question is **binary (Yes/No)** or **multi-range**.
- Include **rationale** and **error introspection** in all forecasts.


🧠 How to Contribute (add this at the end of the section)
To begin forecasting, download the MSCFT Template (v3.1B) from the /templates/ directory in either .txt or .md format.

To summarize:
- Start with the MSCFT template in `/docs/`.
- Save completed logs in `/examples/`.
- Record audits or validations in `/logs/`.
- Update `forecast-index.md` with a working link to your file.

CHANGELOG.md
## [3.1 B] - 2025-05-30
### Added
- Inside-Outside View Structuring subsection added after "Interpretation".
- Updated template labeled as MSCFT Version 3.1 B for beta testing.

### Notes
- This version integrates LLM-assisted calibration via structured outside view analysis.
- Beta feedback encouraged before promoting to 3.2.

## 🔒 Backups

Historical forecasts and index versions are stored in `/ backup-log.md/ ` as timestamped ZIPs.

MSCFT is maintained to ensure traceability, clarity, and reproducibility in judgment forecasting. Feedback and improvements are welcome via pull requests or issues.

[Attribution Record: MSCFT_Raif_Attribution_GitHub](docs/MSCFT_Raif_Attribution_GitHub.md)
 




