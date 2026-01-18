def bank_operation(balance, deposit, withdraw):
    balance = balance + deposit - withdraw
    result = (
        f"Initial Balance : {balance - deposit + withdraw}\n"
        f"Deposit : {deposit}\n"
        f"Withdraw : {withdraw}\n"
        f"Final Balance : {balance}"
    )
    return result

if __name__ == "__main__":
    print(bank_operation(1000, 500, 300))