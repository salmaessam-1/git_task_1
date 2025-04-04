class Mammal:
    def eat(self):
        print("Mammal is eating.")
        super().eat()  

class Human:
    def eat(self):
        print("Human is eating.")

class Employee(Mammal, Human):
    def eat(self):
        print("Employee is eating.")
        super().eat() 

emp = Employee()
emp.eat()


