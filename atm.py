def atm_withdrawal(balance, amount):
    if amount > balance:
        return "Insufficient funds", balance
    if amount <= 0:
        return "Invalid amount", balance
    if balance > amount:
        balance -= amount
        return "Transaction successful", balance