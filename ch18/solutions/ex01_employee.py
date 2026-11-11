class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def monthly_pay(self):
        return self.salary // 12


class Manager(Employee):
    def __init__(self, name, salary, allowance):
        super().__init__(name, salary)
        self.allowance = allowance  # 달마다 받는 직책 수당

    def monthly_pay(self):
        return super().monthly_pay() + self.allowance


staff = [Employee("박준호", 42000000), Manager("이서연", 60000000, 300000)]
for person in staff:
    print(f"{person.name}: {person.monthly_pay():,}원")
