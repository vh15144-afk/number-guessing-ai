# Comprehensive Technical Report: Enhanced Number Guessing AI Engine

**Project Title:** Multi-Layered Number Guessing AI with CSP, Knowledge Representation, and Explainable AI  
**Repository:** `vh15144-afk/number-guessing-ai`  
**Version:** `v2.0`  
**Student Register Number:** `15144`  

---

## Abstract
This report details the architectural enhancement of the Number Guessing AI system from a basic binary search algorithm to a multi-layered decision-making framework. The updated system incorporates Constraint Satisfaction Problem (CSP) formulation, Knowledge Representation and Reasoning (KRR), and an Explainable/Responsible AI (XAI) auditing layer. Theoretical bounds and experimental traces confirm that combining forward checking with Knowledge Base (KB) inference reduces the worst-case search space while guaranteeing explainability, mathematical fairness, and auditability.

---

## 1. System Architecture & Overview

The system is structured into three primary processing layers:

1. **Knowledge & Reasoning Layer (KRR):** Accepts domain clues (facts) and executes logical inference rules to filter out candidate values before search execution.
2. **Constraint Satisfaction Problem (CSP) Layer:** Represents candidate numbers as domain variables, applying Forward Checking and the Minimum Remaining Values (MRV) heuristic to split the search space efficiently.
3. **Applied & Responsible AI Layer:** Audits every candidate state transition, generating real-time natural language explanations (XAI) and tracking fairness/bias metrics.

---

## 2. CSP Formulation & Constraint Propagation

### Problem Mapping
- **Variables ($V$):** $X$, representing the hidden secret integer.
- **Domains ($D$):** $D_X = \{1, 2, 3, \dots, 100\}$.
- **Constraints ($C$):**
  - Directional bounds: $C_{\text{higher}} \implies X > g_k$, $C_{\text{lower}} \implies X < g_k$.
  - Arithmetic properties: $C_{\text{parity}} \implies X \pmod 2 = 0 \lor X \pmod 2 \neq 0$.
  - Divisibility: $C_{\text{div5}} \implies X \pmod 5 = 0$.

### Algorithmic Strategy
- **Forward Checking:** Upon receiving directional feedback, all values in $D_X$ violating the directional constraint are immediately pruned.
- **MRV Heuristic:** At step $k$, the agent selects the median value $g_k = D_X[\lfloor \vert{}D_X\vert{} / 2 \rfloor]$, which guarantees halving the active search domain under unconstrained bounds.

---

## 3. Knowledge Base & Reasoning Layer

### First-Order / Propositional Rules
The system models domain knowledge through a rule base:

$$\text{Rule 1: } \text{IsEven}(X) \implies \forall n \in D_X, (n \pmod 2 \neq 0 \implies \text{Prune}(n))$$
$$\text{Rule 2: } \text{IsOdd}(X) \implies \forall n \in D_X, (n \pmod 2 = 0 \implies \text{Prune}(n))$$
$$\text{Rule 3: } \text{DivisibleBy5}(X) \implies \forall n \in D_X, (n \pmod 5 \neq 0 \implies \text{Prune}(n))$$

### Inference Trace
When secret $X = 42$:
1. Fact added: `parity = EVEN`.
2. KB rule evaluates $D_X$: All odd numbers are eliminated, pruning 50 values immediately ($\vert{}D_X\vert{}: 100 \rightarrow 50$).
3. Search loop executes on the remaining restricted domain, reaching solution in fewer attempts.

---

## 4. Experimental Results & Comparison

| Metric | Phase-1 (Binary Search) | Phase-2 Extension (CSP + KB + XAI) |
| :--- | :--- | :--- |
| **Initial Search Space** | 100 values | 100 values |
| **Domain Reduction via KB** | 0 values | Up to 50–90 values pruned pre-search |
| **Worst-Case Guesses** | 7 attempts | $\le 6$ attempts (with KB pruning) |
| **Explainability (XAI)** | Raw state integers | Full natural language step justification |
| **Time Complexity** | $O(\log N)$ | $O(\log N)$ |
| **Space Complexity** | $O(1)$ | $O(N)$ active domain representation |

---

## 5. Responsible AI, Governance & XAI

### Explainable AI (XAI)
Every decision step emits a trace entry describing:
- Active state bounds and remaining domain size.
- Number of candidate values pruned in the current step.
- Mathematical justification behind the selected candidate.

### Fairness & Accountability
- **Algorithmic Bias:** The system uses deterministic median partitioning, ensuring uniform search performance across all integers $x \in [1, 100]$ without favoring specific numerical ranges.
- **Privacy & Safety:** No personal identification data is stored or transmitted during execution.

---

## 6. Conclusion
The Phase-2 extension successfully elevates the Number Guessing AI into a robust decision engine. By integrating CSP domain reduction, rule-based inference, and transparent audit logging, the system provides high efficiency alongside full explainability.
