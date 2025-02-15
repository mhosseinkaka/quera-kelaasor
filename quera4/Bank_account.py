
class Bank_account:

    """
    یک کلاس برای مدیریت حساب بانکی

    این کلاس امکان ایجاد حساب بانکی، واریز و برداشت از حساب را فراهم می‌کند

    Attributes:
        balance (int): موجودی فعلی حساب بانکی که به صورت پیش‌فرض صفر است
    """

    def __init__(self, balance: int = 0):
        self.balance = balance


    def deposit(self, amount: int) -> int:

        """
        واریز مبلغ به حساب بانکی

        Args:
            amount (int): مبلغی که باید به حساب واریز شود

        Returns:
            int: موجودی حساب پس از واریز

        assert:
            AssertionError: اگر مقدار ورودی از نوع عدد نباشد.
        """
        
        assert type(amount) == int, "enter your amount correctly"
        self.balance += amount
        return self.balance

    def withdraw(self, amount: int) -> int:

        """
        برداشت مبلغ از حساب بانکی

        Args:
            amount (int): مبلغی که باید از حساب برداشت شود

        Returns:
            int: موجودی حساب پس از برداشت

        assert:
            AssertionError: اگر مقدار ورودی از نوع عدد نباشد.
        """

        assert type(amount) == int, "enter your amount correctly"
        if amount > self.balance:  
            print("Insufficient funds!")  
            return self.balance  
        else:  
            self.balance -= amount  
            return self.balance 

# test_case_1
account = Bank_account()
account.deposit(100)  
account.withdraw(50)  
print(account.balance)


# test_case_2
account = Bank_account()
account.deposit(100)  
account.withdraw(150)  
print(account.balance)