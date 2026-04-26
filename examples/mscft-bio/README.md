# MSCFT-BIO Example

This example demonstrates how to run the MSCFT-BIO pipeline using a preprocessed gene signal dataset.

## Files in This Example

- GSE27255_clean.csv → Cleaned dataset used for GPT analysis 

## How to Run

 1. Open the file:
   examples/mscft-bio/GSE27255_clean.csv

2. Open the MSCFT-BIO GPT:
   [ https://chatgpt.com/g/g-69ea7b14d5c88191a6ea23aea0629c20-mscft-bio-v1-0 ]
 
3. Upload ONLY ONE file to GPT:
- GSE27255_clean.csv (recommended)
- GSE27255_Sample_150rows.csv (smaller test)

4. Open: mscft-bio/GPT Template Usage Guide.md
5. Copy the prompt from the Prompt Template section
6. Paste it into GPT and run
---

## Expected Result

The system will return:
- Signal distribution patterns
- Cluster groupings
- Inflection points
- Outliers
