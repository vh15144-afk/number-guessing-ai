# Number Guessing AI · Constraint Satisfaction & Reasoning Engine (v2.0)

An interactive and automated Decision-Making AI agent engineered to solve bounded integer search problems using **Constraint Satisfaction Problem (CSP)** models, **Knowledge Representation & Logical Inference**, and **Explainable AI (XAI)** principles.

---

## Key Extension Features (v2.0)

1. **CSP Search Engine Layer:**
   - **Forward Checking:** Dynamically prunes search domain upon directional feedback (`higher`/`lower`).
   - **Minimum Remaining Values (MRV) Heuristic:** Selects median candidate values to maximize entropy reduction per step.

2. **Knowledge Representation & Reasoning Layer:**
   - **Logical Inference:** Infers domain filtering rules from propositional facts (e.g., parity and divisibility clues).
   - **Rule Engine:** Combines constraints with domain bounds before search execution.

3. **Applied & Responsible AI Layer:**
   - **Explainable AI (XAI):** Outputs step-by-step audit logs explaining domain size reductions, pruned candidates, and mathematical justifications for every guess.
   - **Fairness & Governance:** Deterministic logic eliminates bias, ensuring uniform performance across all valid secret number ranges.

---

## Project Structure

```text
number-guessing-ai/
├── src/
│   └── main.py              # Enhanced CSP, Knowledge Base & Responsible AI Engine
├── tests/
│   ├── test_inputs.txt      # Sample input dataset
│   └── test_csp_logic.py    # Automated unit tests for CSP and logic modules
├── docs/
│   └── report.md            # Extended technical report (v2.0)
├── LICENSE                  # MIT License
└── README.md                # Project documentation
