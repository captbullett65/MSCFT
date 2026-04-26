# 🧠 MSCFT-BIO GPT Template Usage Guide

## Purpose

This template is designed to analyze ranked gene expression signals using structured CSV input.

It extracts patterns, clusters, and signal behavior from preprocessed biological data.

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

Example:

25121,323.14860632
11117,314.95693496
38683,286.06591218

---

## Upload Process

1. Open the MSCFT-BIO GPT template
2. Upload your CSV file (e.g., gpt_input.csv)
3. Ensure the file preview displays correctly
4. Do not paste raw data into chat unless necessary

## Execution

Once the file is uploaded, prompt the system with:

Analyze the dataset and identify patterns, clusters, inflection points, and top-performing signals.
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

