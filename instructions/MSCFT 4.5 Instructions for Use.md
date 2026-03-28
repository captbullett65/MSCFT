MSCFT Instructions for Use Version: v4.5 – Master Swarm Consensus Forecasting Template

Overview:
The Master Swarm Consensus Forecasting Template (MSCFT) v4.5 is a structured,
node-based reasoning and forecasting system designed for human–LLM collaboration.
It integrates BIN analysis, time-series modeling, retrieval-augmented reasoning, and meta-validation into a full execution pipeline.

This version expands beyond earlier SWARM models by incorporating Nodes A–G and Node M (Memento CBR), enabling modular, auditable, and scalable structured reasoning.

---

Step-by-Step Instructions:

1. Load the MSCFT Template  
Copy and paste the full MSCFT v4.5 template into your working environment.  
Ensure plain text formatting is maintained.

2. Define the Forecast Question  
Clearly state the forecasting question.  
Include resolution criteria (PRAMs): dates, thresholds, assumptions, and source references.

3. Set the Bucket Structure  
Provide a binary (Yes/No) or time-based set of probability buckets.  
All outputs must total 100%.

Example (Binary):

 Yes:...[ ]% 
 
 No:....[ ]% 

Example (Time Buckets):

Before Q1 2026:....[ ]%  
Q2–Q3 2026:..........[ ]%  
Q4 2026:..................[ ]%  
Not before 2027:..[ ]%

---

4. Execute Node Pipeline (STRICT ORDER)

A → B → C → D → E → M → F → G

Do not skip nodes. Maintain execution order.

---

Node Execution Guide:

Node A — Research  
Prompt: "Start with Node A."  
Task: Frame the question, define scope, list sources, establish priors and constraints.

Node B — Analysis (BIN Integrated)  
Prompt: "Proceed to Node B."  
Task: Apply Bias, Information, Noise analysis.  
Includes sub-nodes:
B.1 Drivers  
B.2 Constraints  
B.3 Incentives  
B.3.a Strategic Intelligence  
B.4 Historical Analogues  
B.5 Risk Modeling  

Node C — Synthesis  
Prompt: "Proceed to Node C."  
Task: Generate structured forecast using MSCFT.MS-CMT logic.  
Defines probability distribution and rationale.

Node D — Interpretation  
Prompt: "Proceed to Node D."  
Task: Apply entropy, Markov, or KL divergence analysis.  
Used for uncertainty classification and regime shifts.

Node E — Time-Series Modeling  
Prompt: "Proceed to Node E."  
Task: Apply modeling where temporal dynamics are relevant.  
Includes E.1–E.7 (neural, ETS, Fourier, entropy, etc.)

Node M — Memento CBR (Pre-Execution Memory Node)  
Prompt: "Proceed to Node M."  
Task: Apply case-based reasoning using prior state-action patterns.  
Positioned before Node F.  
Does not override Nodes A–E.

Node F — Retrieval / Tools (RAG)  
Prompt: "Proceed to Node F."  
Task: Execute retrieval, tool use, and external data integration.

Node G — Meta-Curation  
Prompt: "Proceed to Node G."  
Task: Validate sources, ensure integrity, track execution, finalize audit.

---

5. Produce Structured Output  

Output must follow MSCFT format:

- Forecast Title  
- Question Framing  
- Analysis  
- Inside/Outside View  
- Data Integrity Log  
- Node Execution  
- Probability Allocation  
- Final Summary  
- Error Analysis  

---

6. Validate and Audit  

Ensure:
- Logical consistency  
- Proper probability distribution  
- Node completeness  
- Source traceability  

---

Key Principles:

- Always execute in order: A → B → C → D → E → M → F → G  
- Do not skip or merge nodes  
- Validate each node before proceeding  
- Maintain structured output discipline  

---

Best Practices:

- Start a new chat session for each forecast  
- Re-paste the template every session  
- Enforce plain text (no markdown tables)  
- Do not allow the model to skip ahead  
- Maintain human-in-the-loop validation  

---

Final Note:

MSCFT v4.5 is a structured reasoning system designed for clarity, auditability, and real-world application. Human validation is required at all stages.

