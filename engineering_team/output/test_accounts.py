import unittest
from accounts import Account, get_share_price

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account = Account(user_id='user123')

    def test_initial_values(self):
        self.assertEqual(self.account.user_id, 'user123')
        self.assertEqual(self.account.balance, 0.0)
        self.assertEqual(self.account.shares, {})
        self.assertEqual(self.account.transactions, [])

    def test_deposit_funds(self):
        self.account.deposit_funds(100.0)
        self.assertEqual(self.account.balance, 100.0)
        self.assertEqual(self.account.transactions, [('deposit', 100.0)])

    def test_withdraw_funds(self):
        self.account.deposit_funds(100.0)
        self.account.withdraw_funds(50.0)
        self.assertEqual(self.account.balance, 50.0)
        self.assertEqual(self.account.transactions, [('deposit', 100.0), ('withdraw', 50.0)])

        with self.assertRaises(ValueError):
            self.account.withdraw_funds(100.0)

    def test_buy_shares(self):
        self.account.deposit_funds(1000.0)
        self.account.buy_shares('AAPL', 2)
        self.assertEqual(self.account.balance, 700.0)
        self.assertEqual(self.account.shares, {'AAPL': 2})
        self.assertEqual(self.account.transactions[-1], ('buy', 'AAPL', 2, 150.0))

        with self.assertRaises(ValueError):
            self.account.buy_shares('TSLA', 2)

    def test_sell_shares(self):
        self.account.deposit_funds(1000.0)
        self.account.buy_shares('AAPL', 2)
        self.account.sell_shares('AAPL', 1)
        self.assertEqual(self.account.balance, 850.0)
        self.assertEqual(self.account.shares, {'AAPL': 1})
        self.assertEqual(self.account.transactions[-1], ('sell', 'AAPL', 1, 150.0))

        with self.assertRaises(ValueError):
            self.account.sell_shares('AAPL', 2)

    def test_calculate_portfolio_value(self):
        self.account.deposit_funds(1000.0)
        self.account.buy_shares('AAPL', 2)
        portfolio_value = self.account.calculate_portfolio_value()
        self.assertEqual(portfolio_value, 700.0 + 2 * 150.0)

    def test_calculate_profit_loss(self):
        self.account.deposit_funds(1000.0)
        self.account.buy_shares('AAPL', 2)
        self.assertEqual(self.account.calculate_profit_loss(), (700.0 + 2 * 150.0) - 1000.0)

    def test_report_holdings(self):
        self.assertEqual(self.account.report_holdings(), {})
        self.account.buy_shares('AAPL', 2)
        self.assertEqual(self.account.report_holdings(), {'AAPL': 2})

    def test_report_transaction_history(self):
        self.assertEqual(self.account.report_transaction_history(), [])
        self.account.deposit_funds(100.0)
        self.assertEqual(self.account.report_transaction_history(), [('deposit', 100.0)])

if __name__ == '__main__':
    unittest.main()