# 🧬 MSCFT-BIO Data Preparation Guide

## Overview

This guide defines the required preprocessing workflow for running gene expression data through MSCFT-BIO templates using GPT.

The key constraint:

> **Large Language Models (LLMs) cannot process raw biological datasets directly.**

They require **compressed, structured signal**, not full matrices.

## 🚨 Why Data Preparation Is Required

Raw gene datasets (e.g., NIH matrices) are too large and unstructured for reliable LLM processing.

### Raw Input (Not Usable)
33,000 rows × 16 columns

### Processed Input (Required)
50 rows × 2 columns
Without preprocessing:
* Context overload occurs
* Structure is lost
* Outputs become inconsistent or meaningless

### Core Principle

> **LLMs interpret patterns — they do not compute datasets**

## ⚙️ Processing Pipeline

Excel → Notepad++ → GPT
* **Excel** = computation engine
* **Notepad++** = formatting + validation
* **GPT** = pattern interpretation

## 📊 Step-by-Step Instructions

### 1. Load Dataset

Open the raw CSV in Excel.

### 2. Compute Aggregated Signal

Add a new column (`gene_total`) using:

   excel
=SUM(B2:P2)


Fill down for all rows.

### 3. Sort Data

Sort by `gene_total`:

* Order: **Largest → Smallest**

### 4. Extract Top Signal

Select the top **30–50 rows** only.

### 5. Flatten Structure

Create a clean export column:

   excel
=A2&","&Q2

This produces:
25121,323.14860632

### 6. Export to Clean CSV

Copy the generated column into Notepad++.

Add header:
gene_index,gene_total

Final format:
gene_index,gene_total
25121,323.14860632
11117,314.95693496


Save as:
gpt_input.csv

## 🧪 Validation Rules

### If the system fails:

> **The data is incorrect — not the template**


### Signs of Bad Input

* Vague or generic output
* Structure ignored
* Numbers misinterpreted
* Template instability

### Signs of Good Input

* Clear tier detection
* Inflection points identified
* Stable structured output
* Consistent interpretation

## 🧠 What This Enables

Once properly formatted, GPT can:

* Detect expression tiers
* Identify inflection points
* Recognize distribution patterns
* Suggest biological relevance

## ⚠️ Important Limitations

This dataset contains:

* No gene identities
* No pathway data
* No experimental metadata

Therefore:

* Pattern analysis = **reliable**
* Biological labeling = **speculative**

## ✅ Final Rule

> **Fix the data, not the template**

## 📌 Summary

```
Raw Matrix → Aggregation → Ranking → Extraction → CSV → GPT Analysis
```

---

## 🧾 Notes

* Always keep original dataset unchanged
* Work on a separate processed copy
* Never input full raw datasets into GPT
* Always validate CSV before use

## 🧬 Folder Recommendation

/data
  /raw
  /processed
/docs
  README.md
---

