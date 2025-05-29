# Contributing to MSCFT

Thank you for your interest in contributing!

## How to Contribute

- Use the `docs/MSCFT-Template-Plain.txt` file to start your forecast log.
- Place completed forecasts in the `examples/` directory.
- Log audits or internal validations in `logs/`.
- Use consistent bucket phrasing and ensure all percentages total to 100%
- Check if question is Binary (Y/N)

## Standards

- Forecasts must follow the 7-section MSCFT structure.
- All forecasts should include rationale and error introspection.

- # How to Contribute to the Master SWARM Consensus Forecasting Template (MSCFT)

## Getting Started

1. Use the plain-text MSCFT template (in `/docs/MSCFT-template.txt`) to begin any new forecast.
2. Save completed forecast logs in the `/examples/` directory. Filenames should reflect the question and date (e.g., `vehicle-innovation-2025-q3-forecast.txt`).
3. Log audits and internal validations in the `/logs/` directory. Include timestamps and versioned links where possible.

## Forecast Standards

- All forecasts **must follow the seven-section MSCFT structure**:
  1. Forecast Title  
  2. Initial Question Framing  
  3. Refinement & Analysis  
  4. Data Anomaly & Source Integrity Log  
  5. Probability Allocation  
  6. Final Forecast Summary  
  7. Why Might You Be Wrong? (2 prompts)

- Ensure all forecasts:
  - Use **consistent bucket phrasing** per GJ Open standards:
    - 2 or fewer  
    - Between 3 and 5  
    - Between 6 and 8  
    - Between 9 and 12  
    - Between 13 and 16  
    - Between 17 and 21  
    - 22 or more  
  - Sum all probability allocations to exactly **100%**.
  - Identify if the question is **binary** (Yes/No) or **multi-bucket**.
  - Include clear **rationale** and **error introspection**.

## Indexing

- Add each new forecast to the `forecast-index.md` file in the root or `/docs/` folder.
- Use functional relative links (e.g., `[Forecast Title](../examples/filename.txt)`).
- Verify all links are working—404 errors will result in removal.


