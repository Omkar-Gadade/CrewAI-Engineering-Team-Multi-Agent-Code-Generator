# File: accounts.py

class Account:
    """
    A class to represent a trading user's account in a trading simulation platform.
    """

    def __init__(self, user_id):
        """
        Initialize the account with a user ID, zero balance, no shares, and empty
        transactions list.
        
        :param user_id: The unique identifier for the user.
        """
        self.user_id = user_id
        self.balance = 0.0
        self.shares = {}
        self.transactions = []
        self.initial_deposit = 0.0

    def deposit_funds(self, amount):
        """
        Deposit funds into the account and record an initial deposit if it's the first transaction.
        
        :param amount: The amount to add to the account balance.
        """
        if self.initial_deposit == 0:
            self.initial_deposit = amount
        self.balance += amount
        self.transactions.append(("deposit", amount))

    def withdraw_funds(self, amount):
        """
        Withdraw funds from the account if there are sufficient funds to cover the withdrawal.
        
        :param amount: The amount to withdraw from the account balance.
        :raises ValueError: If withdrawal is greater than the current balance.
        """
        if amount > self.balance:
            raise ValueError("Insufficient funds for withdrawal.")
        self.balance -= amount
        self.transactions.append(("withdraw", amount))

    def buy_shares(self, symbol, quantity):
        """
        Buy shares if the account has sufficient funds to cover the purchase price.
        
        :param symbol: The symbol of the share to buy.
        :param quantity: The quantity of shares to buy.
        :raises ValueError: If account funds are insufficient to buy the shares.
        """
        price = get_share_price(symbol)
        cost = price * quantity
        if cost > self.balance:
            raise ValueError("Insufficient funds to buy shares.")
        self.balance -= cost
        self.shares[symbol] = self.shares.get(symbol, 0) + quantity
        self.transactions.append(("buy", symbol, quantity, price))

    def sell_shares(self, symbol, quantity):
        """
        Sell shares if there are enough of the specified shares in the account.
        
        :param symbol: The symbol of the share to sell.
        :param quantity: The quantity of shares to sell.
        :raises ValueError: If there are insufficient shares to sell.
        """
        if self.shares.get(symbol, 0) < quantity:
            raise ValueError("Insufficient shares to sell.")
        price = get_share_price(symbol)
        revenue = price * quantity
        self.balance += revenue
        self.shares[symbol] -= quantity
        self.transactions.append(("sell", symbol, quantity, price))

    def calculate_portfolio_value(self):
        """
        Calculate the total value of the user's portfolio including current account balance and holdings.
        
        :return: The total value of the user's portfolio.
        """
        total_value = self.balance
        for symbol, qty in self.shares.items():
            total_value += qty * get_share_price(symbol)
        return total_value

    def calculate_profit_loss(self):
        """
        Calculate the net profit or loss from the initial deposit.
        
        :return: The profit or loss of the account relative to the initial deposit.
        """
        current_value = self.calculate_portfolio_value()
        return current_value - self.initial_deposit

    def report_holdings(self):
        """
        Provide a report of the current holdings in the account.
        
        :return: A dictionary of the current shares and their quantities.
        """
        return self.shares.copy()

    def report_transaction_history(self):
        """
        Provide a history of all transactions made on the account.
        
        :return: A list of tuples describing the transactions.
        """
        return self.transactions.copy()


def get_share_price(symbol):
    """
    A stub function providing fixed share prices for testing purposes. In a real-world
    application, this would interface with a live market data source.
    
    :param symbol: The symbol of the share to get the price for.
    :return: The current price of the given share symbol.
    """
    fixed_prices = {
        "AAPL": 150.0,
        "TSLA": 700.0,
        "GOOGL": 2800.0
    }
    return fixed_prices.get(symbol, 0.0)