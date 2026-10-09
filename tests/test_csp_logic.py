import unittest
from src.main import NumberGuessingCSP, KnowledgeBase, ResponsibleAIEngine

class TestEnhancedAI(unittest.TestCase):

    def test_csp_forward_checking(self):
        """Tests whether CSP forward checking correctly prunes the domain."""
        csp = NumberGuessingCSP(1, 100)
        self.assertEqual(len(csp.domain), 100)
        
        # If target is higher than 50, domain should shrink to [51, 100] (50 items)
        pruned = csp.apply_forward_checking(50, 'h')
        self.assertEqual(pruned, 50)
        self.assertEqual(len(csp.domain), 50)
        self.assertEqual(csp.domain[0], 51)

    def test_knowledge_base_inference(self):
        """Tests logical inference from facts in the Knowledge Base."""
        kb = KnowledgeBase()
        kb.add_fact("parity", "EVEN")
        kb.add_fact("divisible_by_5", True)
        
        filters = kb.infer_domain_filters()
        self.assertEqual(len(filters), 2)

    def test_full_search_engine(self):
        """Tests that ResponsibleAIEngine finds the target within logarithmic bounds."""
        engine = ResponsibleAIEngine()
        attempts = engine.run_enhanced_search(target_number=42)
        # Should complete in 7 or fewer attempts for range [1, 100]
        self.assertLessEqual(attempts, 7)

if __name__ == "__main__":
    unittest.main()
