# 🧠 MSCFT-BIO GPT Template Usage Guide

## Purpose

This template is designed to analyze ranked gene expression signals using structured CSV input.

It extracts patterns, clusters, and signal behavior from preprocessed biological data.

---
## Quick Start

Data Preparation → README.md
Project Overview → Structured Gene Signal Forecasting.md
GPT Usage → GPT Template Usage Guide.md

---
## Input Requirements

The GPT requires a clean CSV file with the following structure:

gene_index,gene_total

Rules:

* Exactly 2 columns
* Header must be included
* Data must be numeric
* Sorted from highest to lowest gene_total
* Recommended size: 30–100 rows (optimal ~50)
---
Example:

```
gene_index,gene_total 
25121,323.14860632
11117,314.95693496
38683,286.06591218
```

---

## Upload Process

1. Open the MSCFT-BIO GPT template
2. Upload your CSV file (e.g., gpt_input.csv)
3. Ensure the file preview displays correctly
4. Do not paste raw data into chat unless necessary

## Execution
## Execution

Once the file is uploaded, use the MSCFT-BIO GPT to analyze the dataset.

### Custom GPT Link
Use the MSCFT-BIO custom GPT here:  
https://chatgpt.com/g/g-69ea7b14d5c88191a6ea23aea0629c20-mscf-bio-v1-0

### Usage Instructions
1. Open the custom GPT using the link above
2. Upload your cleaned `gpt_input.csv` file
3. Run the prompt provided in the Prompt Template section

The GPT is designed to read ranked `gene_index,gene_total` data and return structured signal analysis, including:
- Pattern detection
- Cluster behavior (high, mid, low signal groups)
- Inflection points
- Top-performing genes

Do not upload raw gene matrices. Use only processed CSV data generated from the data preparation workflow.

---

## Prompt Template
Once your CSV is uploaded, use the following prompt:
```text
Analyze the dataset and identify patterns, clusters, inflection points, and top-performing signals.
Focus on:
- Distribution behavior of gene_total values
- Any clustering or tiering (high, mid, low signal groups)
- Sharp drop-offs or inflection points
- Outliers or anomalies
Do not give generic explanations. Be specific to the numeric patterns observed.
Data:
gene_index,gene_total
25121,323.14860632
11117,314.95693496
38683,286.06591218
```
---
## Expected Output

The GPT will return structured analysis including:

* Distribution patterns across gene_total values
* Cluster groupings (high, mid, low signal bands)
* Inflection points where signal drops sharply
* Identification of top-performing genes
* Detection of anomalies or outliers

## Interpretation Guidelines

* Higher gene_total = stronger aggregate signal
* Early rank positions carry the most significance
* Sharp drop-offs indicate structural transitions in the dataset
* Clusters may represent functional groupings (not confirmed biology)

## Limitations

This template does NOT:

* Identify gene names or functions
* Perform pathway analysis
* Provide biological or clinical conclusions

All outputs are pattern-based and require external validation.
## Common Errors

Incorrect results usually come from bad input data:

* Missing header
* Unsorted values
* Extra columns
* Non-numeric values
* Too many rows (context overflow)

If output looks wrong → fix the CSV, not the prompt.

## Best Practices

* Always validate CSV before upload
* Keep datasets small and focused
* Use consistent preprocessing methods
* Compare multiple runs for stability

## Workflow Summary

Prepare Data → Export CSV → Upload → Run Analysis → Interpret Patterns

## Final Rule

Garbage in = garbage out.

Clean data produces reliable signal patterns.

---

