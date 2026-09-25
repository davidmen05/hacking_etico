class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return "El monto a depositar debe ser positivo"
        self.balance += amount
        return f"Depósito exitoso. Nuevo saldo: ${self.balance}"

    def withdraw(self, amount):
        if amount <= 0:
            return "El monto a retirar debe ser positivo"
        if amount > self.balance:
            return f"Fondos insuficientes. Saldo actual: ${self.balance}"
        self.balance -= amount
        return f"Retiro exitoso. Nuevo saldo: ${self.balance}"

    def display(self):
        return f"Titular: {self.owner} | Saldo: ${self.balance}"


cuenta1 = BankAccount("David", 100)
print(cuenta1.display())

print(cuenta1.deposit(50))
print(cuenta1.withdraw(30))
print(cuenta1.withdraw(500))
print(cuenta1.deposit(-10))

print(cuenta1.display())