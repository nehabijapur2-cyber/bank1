from bank import bank_operation

def test_case1():
    assert bank_operation(1000, 500, 300) == "Initial Balance : 1000\nDeposit : 500\nWithdraw : 300\nFinal Balance : 1200"
