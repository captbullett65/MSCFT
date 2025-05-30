# Contributing to MSCFT

Thank you for your interest in contributing to the Master SWARM Consensus Forecasting Template (MSCFT) repository!

## Getting Started

- Use the plain-text MSCFT template located in `/docs/MSCFT-Template-Plain.txt` to begin your forecast.
- Save completed forecasts in the `/examples/` directory. Use descriptive filenames like `vehicle-innovation-2025-q3-forecast.txt`.
- Log audits or internal validations in the `/logs/` directory with timestamps and, if applicable, versioned source links.
- Add each new forecast to the `forecast-index.md` in the root or `/docs/` folder using working relative links.

## Forecast Standards

All forecasts **must follow the seven-section MSCFT structure**:
1. Forecast Title  
2. Initial Question Framing  
3. Refinement & Analysis  
4. Data Anomaly & Source Integrity Log  
5. Probability Allocation  
6. Final Forecast Summary  
7. Why Might You Be Wrong? (2 prompts)

Ensure the following:
- Use **standard bucket phrasing** when applicable:
  - 2 or fewer  
  - Between 3 and 5  
  - Between 6 and 8  
  - Between 9 and 12  
  - Between 13 and 16  
  - Between 17 and 21  
  - 22 or more  
- All probability allocations must sum to **100%**.
- Identify whether the question is **binary** (Yes/No) or **multi-bucket**.
- Include clear **rationale** and **error introspection** in each forecast.

## Forecast Markup Language (FML) Tagging Standards

When submitting forecasts via GPT or for preprocessing, use [Forecast Markup Language (FML)](docs/Markup.md) tags to structure your input. These tags help GPT produce clean, compliant MSCFT outputs.

You must read the [FML Tag Reference Cheat Sheet](docs/Markup.md) before submitting forecasts that use tagging. Improper tagging or nesting may lead to incorrect parsing or template violations.

## Style Guide

- All final forecasts should be plain text (no Markdown in output).
- Use lowercase tags in FML input.
- Submit DOCX logs only in the `/logs/` directory.
- Avoid tables or embedded formatting unless explicitly required.

## Submitting Your Contribution

- Fork the repository.
- Create a feature branch for your edits.
- Open a pull request with a clear description.
- Reference the forecast question and include a link to your example file and any relevant log entry.





