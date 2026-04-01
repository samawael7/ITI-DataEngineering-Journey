class AuditLogger:
    def log(self, message):
        print(f"LOG: {message}")
# دي الـ class الحقيقية اللي بتسجل العمليات
# في الـ test مش هنشغلها خالص — هنستبدلها بـ Mock


class BankAccount:
    def __init__(self, balance=0, logger=None):
        self.balance = balance
        self.logger = logger
    # بتعمل account برصيد ابتدائي وlogger
    # لو مفيش logger مش هتعمل حاجة — وده مهم عشان الـ Mock يشتغل


    def deposit(self, amount):
        self.balance += amount
        if self.logger:
            self.logger.log(f"Deposited {amount}")
        return self.balance
    # بتزود الرصيد وبتقول للـ logger اتعمل deposit بكام


    def withdraw(self, amount):
        if amount > self.balance:
            if self.logger:
                self.logger.log(f"Failed withdrawal of {amount}")
            raise ValueError("Insufficient funds")
        self.balance -= amount
        if self.logger:
            self.logger.log(f"Withdrew {amount}")
        return self.balance
    # لو المبلغ أكبر من الرصيد => تسجل الفشل وترمي ValueError
    # لو تمام => تنقص الرصيد وتسجل