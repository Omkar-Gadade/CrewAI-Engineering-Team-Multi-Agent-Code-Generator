import gradio as gr
from accounts import Account

# Create an instance of Account
account = Account(user_id="user1")

def deposit(amount):
    account.deposit_funds(amount)
    return f"Deposited ${amount}. Current balance: ${account.balance}"

def withdraw(amount):
    try:
        account.withdraw_funds(amount)
        return f"Withdrew ${amount}. Current balance: ${account.balance}"
    except ValueError as e:
        return str(e)

def buy_shares(symbol, quantity):
    try:
        account.buy_shares(symbol, quantity)
        return f"Bought {quantity} shares of {symbol}. Current holdings: {account.report_holdings()}"
    except ValueError as e:
        return str(e)

def sell_shares(symbol, quantity):
    try:
        account.sell_shares(symbol, quantity)
        return f"Sold {quantity} shares of {symbol}. Current holdings: {account.report_holdings()}"
    except ValueError as e:
        return str(e)

def portfolio_value():
    return f"Total portfolio value: ${account.calculate_portfolio_value()}"

def profit_loss():
    return f"Profit/Loss from initial deposit: ${account.calculate_profit_loss()}"

def transaction_history():
    return account.report_transaction_history()

with gr.Blocks() as demo:
    gr.Markdown("### Account Management System for Trading Simulation")
    with gr.Row():
        deposit_amount = gr.Number(label="Deposit Amount", value=0)
        deposit_btn = gr.Button("Deposit")
    deposit_output = gr.Textbox(label="Deposit Output")
    deposit_btn.click(deposit, inputs=[deposit_amount], outputs=deposit_output)

    with gr.Row():
        withdraw_amount = gr.Number(label="Withdrawal Amount", value=0)
        withdraw_btn = gr.Button("Withdraw")
    withdraw_output = gr.Textbox(label="Withdrawal Output")
    withdraw_btn.click(withdraw, inputs=[withdraw_amount], outputs=withdraw_output)

    with gr.Row():
        buy_symbol = gr.Textbox(label="Buy Symbol (AAPL/TSLA/GOOGL)", value="AAPL")
        buy_quantity = gr.Number(label="Buy Quantity", value=1)
        buy_btn = gr.Button("Buy Shares")
    buy_output = gr.Textbox(label="Buy Output")
    buy_btn.click(buy_shares, inputs=[buy_symbol, buy_quantity], outputs=buy_output)

    with gr.Row():
        sell_symbol = gr.Textbox(label="Sell Symbol (AAPL/TSLA/GOOGL)", value="AAPL")
        sell_quantity = gr.Number(label="Sell Quantity", value=1)
        sell_btn = gr.Button("Sell Shares")
    sell_output = gr.Textbox(label="Sell Output")
    sell_btn.click(sell_shares, inputs=[sell_symbol, sell_quantity], outputs=sell_output)

    value_btn = gr.Button("Portfolio Value")
    value_output = gr.Textbox(label="Portfolio Value")
    value_btn.click(portfolio_value, outputs=value_output)

    profit_loss_btn = gr.Button("Profit/Loss")
    profit_loss_output = gr.Textbox(label="Profit/Loss")
    profit_loss_btn.click(profit_loss, outputs=profit_loss_output)

    history_btn = gr.Button("Transaction History")
    history_output = gr.Textbox(label="Transaction History")
    history_btn.click(transaction_history, outputs=history_output)

demo.launch()