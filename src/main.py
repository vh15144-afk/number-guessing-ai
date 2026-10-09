import random

# Personalization seed using student registration number
REGISTER_NUMBER = "15144"
random.seed(REGISTER_NUMBER)

# =====================================================================
# LAYER 1: CONSTRAINT SATISFACTION PROBLEM (CSP) ENGINE
# =====================================================================
class NumberGuessingCSP:
    """
    CSP Model for search space reduction.
    Variables: X (the target number)
    Domain: D = [1, 100]
    Constraints: Relational (<, >) and parity/divisibility conditions.
    """
    def __init__(self, low=1, high=100):
        self.domain = list(range(low, high + 1))
        self.constraints = []

    def apply_forward_checking(self, guess, feedback):
        """
        Prunes domain based on direction feedback using forward checking.
        """
        initial_size = len(self.domain)
        if feedback == 'h':  # Target is HIGHER than guess
            self.domain = [x for x in self.domain if x > guess]
        elif feedback == 'l':  # Target is LOWER than guess
            self.domain = [x for x in self.domain if x < guess]
        
        pruned_count = initial_size - len(self.domain)
        return pruned_count

    def apply_logical_constraint(self, constraint_fn, description):
        """
        Applies arc consistency (AC-3 style domain reduction) for custom constraints.
        """
        initial_size = len(self.domain)
        self.domain = [x for x in self.domain if constraint_fn(x)]
        self.constraints.append(description)
        pruned_count = initial_size - len(self.domain)
        return pruned_count

    def get_optimal_guess(self):
        """
        Minimum Remaining Values (MRV) heuristic: Selects the median 
        of the remaining constrained domain to maximize entropy reduction.
        """
        if not self.domain:
            return None
        mid_idx = len(self.domain) // 2
        return self.domain[mid_idx]


# =====================================================================
# LAYER 2: KNOWLEDGE & REASONING LAYER (PROPOSITIONAL / FOL RULES)
# =====================================================================
class KnowledgeBase:
    """
    Rule-based engine performing forward/backward logical inference 
    and managing uncertainty.
    """
    def __init__(self):
        self.facts = {}
        self.rules = []

    def add_fact(self, key, value):
        self.facts[key] = value

    def infer_domain_filters(self):
        """
        Infers mathematical properties from logical facts.
        Rule 1: IF target is EVEN -> Filter x % 2 == 0
        Rule 2: IF target is ODD  -> Filter x % 2 != 0
        Rule 3: IF target is MULTIPLE_OF_5 -> Filter x % 5 == 0
        """
        filters = []
        if self.facts.get("parity") == "EVEN":
            filters.append((lambda x: x % 2 == 0, "Rule Inferred: Target is Even"))
        elif self.facts.get("parity") == "ODD":
            filters.append((lambda x: x % 2 != 0, "Rule Inferred: Target is Odd"))

        if self.facts.get("divisible_by_5") is True:
            filters.append((lambda x: x % 5 == 0, "Rule Inferred: Target is divisible by 5"))

        return filters


# =====================================================================
# LAYER 3: APPLIED & RESPONSIBLE AI LAYER (EXPLAINABILITY & DRIVER)
# =====================================================================
class ResponsibleAIEngine:
    """
    Executes search with Explainable AI (XAI) traces and audit logging.
    """
    def __init__(self):
        self.csp = NumberGuessingCSP(1, 100)
        self.kb = KnowledgeBase()
        self.trace_log = []

    def log_explanation(self, step, guess, domain_size, pruned, reasoning):
        explanation = (
            f"[Step {step}] Guess: {guess} | Domain Remaining: {domain_size} "
            f"| Pruned: {pruned} values | Reasoning (XAI): {reasoning}"
        )
        self.trace_log.append(explanation)
        print(explanation)

    def run_enhanced_search(self, target_number):
        print(f"\n=== Starting Enhanced AI Search Engine [Seed: {REGISTER_NUMBER}] ===")
        print(f"Target Set (Hidden): {target_number}\n")

        # Step A: Apply Knowledge Base Inference
        if target_number % 2 == 0:
            self.kb.add_fact("parity", "EVEN")
        else:
            self.kb.add_fact("parity", "ODD")

        if target_number % 5 == 0:
            self.kb.add_fact("divisible_by_5", True)

        inferred_filters = self.kb.infer_domain_filters()
        for filter_fn, rule_desc in inferred_filters:
            pruned = self.csp.apply_logical_constraint(filter_fn, rule_desc)
            print(f"[Knowledge Inference] {rule_desc} -> Pruned {pruned} candidate values.")

        # Step B: Interactive/Automated CSP Guessing Loop
        attempts = 0
        while True:
            guess = self.csp.get_optimal_guess()
            attempts += 1

            if guess is None or len(self.csp.domain) == 0:
                print("Error: Contradictory constraints or empty search domain.")
                break

            if guess == target_number:
                self.log_explanation(
                    attempts, guess, len(self.csp.domain), 0,
                    f"Exact match found! Target state {guess} reached in {attempts} attempts."
                )
                break
            elif target_number > guess:
                feedback = 'h'
                reasoning = f"Target > {guess}. Forward checking pruned values <= {guess}."
            else:
                feedback = 'l'
                reasoning = f"Target < {guess}. Forward checking pruned values >= {guess}."

            pruned = self.csp.apply_forward_checking(guess, feedback)
            self.log_explanation(attempts, guess, len(self.csp.domain), pruned, reasoning)

        print(f"\nSearch Terminated Successfully in {attempts} Steps.")
        return attempts


if __name__ == "__main__":
    # Test execution with target number 42
    engine = ResponsibleAIEngine()
    engine.run_enhanced_search(target_number=42)
