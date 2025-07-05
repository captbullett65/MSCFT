MSCFT Version History
## \[1.3 D ]  - 2025-06-28
## \[1.3 C ]  - 2025-06-28
## \[1.3 B] – 2025-06-02

### Added
* added Access limitation Header [1.3 D]
* BIN Tagging Guide added to `/docs`
* New BIN-integrated template: `MSCFT-Template-Plain-BIN-v3.1B.txt`
* Forecasting Tools section added to `README.md`

### Notes

* BIN tags support classification of changes as Bias, Information, or Noise
* Helps with audit trails and structured forecast introspection

## \[3.1 C ]  - 2025-06-28
Added a header for use with GPT-4o                               

[DO NOT INCLUDE THIS SECTION IN FORECAST OUTPUT]

This MSCFT template is aligned with GPT-4o capabilities and assumes Research mode is used when current data is needed.

After specifying your forecast question, resolution criteria, and bucket structure, include the following line before generation begins:

Use the information retrieved to frame your reasoning and support structured forecasting as defined in the previously memorized MSCFT Template 3.1B – BIN Integrated. No improvisation. No format deviation.

[END OF NON-OUTPUT SECTION]

MSCFT Template (Version 3.1C)



## \[3.1 B] – 2025-05-31

### Fixed

* Corrected Probability Allocation section bucket phrasing for audit alignment.
* Bucket labels now match GJO structure:

  * 2 or fewer
  * Between 3 and 5
  * Between 6 and 8
  * Between 9 and 12
  * Between 13 and 16
  * Between 17 and 21
  * 22 or more

## \[3.1 B] – 2025-05-30

### Added

* Inside-Outside View Structuring subsection added after "Interpretation".
* Updated template labeled as MSCFT Version 3.1 B for beta testing.

### Notes

* This version integrates LLM-assisted calibration via structured outside view analysis.
* Beta feedback encouraged before promoting to 3.2.

## \[3.0] – Placeholder

### Initial public release

* Full seven-section MSCFT structure.
* Error tracking and audit log system implemented.

## \[2.9] – Placeholder

### Internal alpha release

* Anomaly tracking and phrasing refinement trials.

## 🔒 Backups

Historical forecasts and index versions are stored in `/ backup-log.md/ ` as timestamped ZIPs.

MSCFT is maintained to ensure traceability, clarity, and reproducibility in judgment forecasting. Feedback and improvements are welcome via pull requests or issues.
