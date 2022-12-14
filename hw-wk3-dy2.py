class Employee:
    raise_amount = 1.05
    def __init__(self, first, last, job_title, salary, email):
        self.first_name = first
        self.last_name = last
        self.job_title = job_title
        self.salary = salary
        self.email = email
        self.full_name = first + " " + last

    def give_raise(self):
        self.salary *= self.raise_amount
        raise_percent = int(self.raise_amount * 100 - 100)
        return f"\n{self.first_name.title()} {self.last_name.title()} has just been given a %{raise_percent} raise, making his annual salary ${int(self.salary)} per year."


employee1 = Employee("timmy", "smith", "accountant", 60000, "timmy@smith.com")
employee2 = Employee("roger", "jones", "biochemist", 100000, "roger@jones.com")

print(employee1.give_raise())
print(employee2.give_raise())
print("="*50)

class Sales(Employee):
    def __init__(self, first, last, job_title, salary, email, phone_number):
        super().__init__(first, last, job_title, salary, email)
        self.phone_number = phone_number

    def send_email(self, customer_name):
        return (f"""\nDear {customer_name.title()},\n\nThank you for your interest in our product.
                    \nPlease let me know if you have any questions.
                    \nMy email is {self.email}, and my phone number is {self.phone_number}.\n\nAll the best,\n\n{self.full_name.title()}\n""")

salesman1 = Sales("walter", "white", "salesman", 75000, "iamthedanger@white.com", "(310)409-7415")
print(salesman1.send_email("Ronald McDonald"))
print("="*50)
salesman2 = Sales("jesse", "pinkman", "salesman", 50000, "alwaysnumbertwo@pinkman.com", "(323)326-7575")
print(salesman2.send_email("mike o'neil"))
print("="*50)
print(salesman2.send_email("hannah stern"))
print("="*50)
print(salesman2.give_raise())
print("="*50)


class Developer(Employee):
    def __init__(self, first, last, job_title, salary, email):
        super().__init__(first, last, job_title, salary, email)

    def write_code(self):
        return f"""\n{self.full_name.title()} is writing code!\nHis email is {self.email} if you want to get in touch with him\n"""

developer1 = Developer("harry", "hoozer", "developer", 100000, "ilovepython@baby.com")

print(developer1.write_code())
print("="*50)
print(developer1.give_raise())
print("="*50)

# EXERCISE 2
# I've imported the following code from a file called geometry.py

# import math

# def find_circle_area(r):
#     area = math.pi * (r**2)
#     return area

# print(find_circle_area(7))


# def find_hypotenuse(side1, side2):
#     hypotenuse = math.sqrt(side1 ** 2 + side2 ** 2)
#     return int(hypotenuse)

# print(find_hypotenuse(3, 4))

import geometry