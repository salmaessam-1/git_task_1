class Person:
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    def sleep(self, hours):
        if hours == 7:
            self.mood = "Happy"
        elif hours < 7:
            self.mood = "Tired"
        else:
            self.mood = "Lazy"
        print(f"{self.name} slept for {hours} hours and feels {self.mood}.")

    def eat(self, meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50
        print(f"{self.name} ate {meals} meals and health rate is {self.healthRate}%.")

    def buy(self, items):
        cost = items * 10 
        if self.money >= cost:
            self.money -= cost
            print(f"{self.name} bought {items} items and has {self.money} LE left.")
        else:
            print("Not enough money.")


class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = max(0, min(fuelRate, 100))
        self.velocity = max(0, min(velocity, 200))

    def run(self, velocity, distance):
        self.velocity = max(0, min(velocity, 200))  
        while distance > 0 and self.fuelRate > 0:
            self.fuelRate -= 10  
            distance -= 10
            print(f"Car {self.name} is running,Fuel: {self.fuelRate}%, Distance left: {distance} km.")
            if distance == 0:
             print(f"samy arrive the destination.")

        if self.fuelRate <= 0:
            print(f"Car {self.name} stopped, not enough fuel,Distance left: {distance} km.")

    def stop(self):
        self.velocity = 0
        print(f"Car {self.name} has stopped.")


class Employee(Person):
    def __init__(self, name, money, mood, healthRate, emp_id, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.emp_id = emp_id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    def work(self, hours):
        if hours == 8:
            self.mood = "Happy"
        elif hours > 8:
            self.mood = "Tired"
        else:
            self.mood = "Lazy"
        print(f"{self.name} worked for {hours} hours and feels {self.mood}.")

    def drive(self, distance):
        if self.car:
            self.car.run(60, distance)
        else:
            print(f"{self.name} doesn't have a car.")

    def refuel(self, gasAmount=100):
        if self.car:
            self.car.fuelRate = min(self.car.fuelRate + gasAmount, 100)
            print(f"Car refueled to {self.car.fuelRate}%.")
        else:
            print(f"{self.name} doesn't have a car.")


class Office:
    employeesNum = 0

    def __init__(self, name):
        self.name = name
        self.employees = []

    def hire(self, employee):
        self.employees.append(employee)
        Office.employeesNum += 1
        print(f"{employee.name} hired at {self.name}.")
             
    def fire(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                self.employees.remove(emp)
                Office.employeesNum -= 1
                print(f"{emp.name} fired from {self.name}.")
                return
        print("Fire")

    def get_all_employees(self):
        return [emp.name for emp in self.employees]
    
    def get_employee(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                return vars(emp)  
        return "Employee not found"
    
    def deduct(self, emp_id, deduction):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                emp.salary -= deduction
                print(f"{deduction} LE deduct from {emp.name}'s salary.New salary: {emp.salary}.")
                return
        print("Employee not found.")

    def reward(self, emp_id, reward):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                emp.salary += reward
                print(f"{reward} LE added to {emp.name}'s salary.New salary: {emp.salary}.")
                return
        print("Employee not found.")

    def calculate_lateness(self, targetHour, moveHour, distance, velocity):
        arrivalTime = moveHour + (distance / velocity)
        return "Late" if arrivalTime > targetHour else "On Time"

    def check_lateness(self, emp_id, moveHour):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                lateness_status = self.calculate_lateness(9, moveHour, emp.distanceToWork, 60)
                if lateness_status == "Late":
                    self.deduct(emp_id, 10)
                    print(f"{emp.name} was late! 10 LE deducted.")
                else:
                    self.reward(emp_id, 10)
                    print(f"{emp.name} was on time! 10 LE rewarded.")
                return lateness_status
        print("Employee not found.")
        return None     
           
    def change_emps_num(cls, num):
        cls.employeesNum = num
        print(f"employees count {cls.employeesNum}.")    

    
print("=======================================")

iti = Office("ITI Smart Village")    
Fiat = Car(name="Fiat128",fuelRate= 80,velocity= 0)    
emp1 = Employee(name="Samy", money=5000, mood="Neutral", healthRate=90, emp_id=101,car=Fiat, email="samy@iti.com",
                salary= 10000,distanceToWork= 20)
iti.hire(emp1)
emp1.drive(20)
emp1.work(8)
emp1.eat(2)
emp1.buy(5)
emp1.sleep(9)
lateness_status = iti.calculate_lateness(9, 10, 20, 60)
print(f"Lateness status: {lateness_status}")

print("=======================================")

emp2= Employee(name="Salma", money=3000, mood="Neutral", healthRate=90, emp_id=102, car=None, email="ali@example.com", 
              salary=8000, distanceToWork=20)
iti.hire(emp2)
emp2.work(3)
emp2.buy(300)
emp2.drive(50)
emp2.refuel(30)
emp2.eat(0)
emp2.sleep(5)
lateness_status = iti.calculate_lateness(9, 9, 20, 60)
print(f"Lateness status: {lateness_status}")

print("=======================================")

print("Employees after hiring:", [emp.name for emp in iti.employees])
employees_list = iti.get_all_employees()
print("Current Employees:", employees_list)

print("Employee 101 details:", iti.get_employee(101))
print("Employee 999 details:", iti.get_employee(100))

iti.deduct(101, 500)
iti.reward(102, 300)

lateness_status1 = iti.check_lateness(101, 8)  
lateness_status2 = iti.check_lateness(102, 9) 

iti.fire(101)
print("Employees after firing:", iti.get_all_employees())
iti.change_emps_num(1)


