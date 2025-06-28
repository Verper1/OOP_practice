from Bank import BankAccount


def test_function():
    account = BankAccount(100)
    account.deposit(50)
    account.withdraw(30)
    assert account.get_balance() == 120  # Первое знакомство с тестами
