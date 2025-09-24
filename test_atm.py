import unittest
from atm import atm_withdrawal
# import pdb
# primitive debugging, n, c, p

class TestAtmWithdrawal(unittest.TestCase):

    def test_insufficient_funds(self):
        # pdb.set_trace()
        message, new_balance = atm_withdrawal(100, 150)
        self.assertEqual(message, "Insufficient funds")
        self.assertEqual(new_balance, 100)
    
    def test_invalid_amount(self):
        message, new_balance = atm_withdrawal(100, -20)
        self.assertEqual(message, "Invalid amount")
        self.assertEqual(new_balance, 100)
    
    def test_successful_transaction(self):
        message, new_balance = atm_withdrawal(150, 50)
        self.assertEqual(message, "Transaction successful")
        self.assertEqual(new_balance, 100)
    
if __name__ == "__main__":
    unittest.main()
    