class Employee:
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def display_count(self):
        print("Total Employee %d" % (Employee.emp_count))

    def display_employee(self):
        print("Name:", self.name, ", Salary:", self.salary)


employee1 = Employee("emname", 900)
employee1.display_count()
employee1.display_employee()
employee2 = Employee("lllsss", 9923)
employee1.display_count()
employee1.display_employee()
employee2.display_count()
employee2.display_employee()

print(hasattr(employee1, 'age'))
print(getattr(employee1, "age"))
print(setattr(employee1, "age", 8))
delattr(employee1, "age")
