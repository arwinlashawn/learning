import datetime

class Employee:

	num_of_emps = 0
	raise_amount = 1.04
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

		Employee.num_of_emps += 1

	def fullname(self):
		return f"{self.first} {self.last}"

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amount = amount 

	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# to turn a regular method into a classmethod, add a decorator

# to change the raise_amount to 5%
Employee.set_raise_amt(1.05)


# print(emp_1.raise_amount)
# print(Employee.raise_amount)
# print(emp_2.raise_amount)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

# static methods don't pass anything automatically
# behave like regular functions, we include them in the class
# because they have some logical connection to the class

my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))
