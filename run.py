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
            print("Not enough money to buy the items.")

class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = max(0, min(fuelRate, 100))  # يجب أن يكون بين 0 و 100
        self.velocity = max(0, min(velocity, 200))  # يجب أن يكون بين 0 و 200

    def run(self, velocity, distance):
        self.velocity = max(0, min(velocity, 200))  # ضبط السرعة ضمن المدى
        while distance > 0 and self.fuelRate > 0:
            self.fuelRate -= 10  # كل 10 كم تقلل 10% من الوقود
            distance -= 10
            print(f"Car {self.name} is running... Fuel: {self.fuelRate}%, Distance left: {distance} km.")

        if self.fuelRate <= 0:
            print(f"Car {self.name} stopped due to empty fuel.")

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
            print(f"{self.name} doesn't have a car to drive.")

    def refuel(self, gasAmount=100):
        if self.car:
            self.car.fuelRate = min(self.car.fuelRate + gasAmount, 100)
            print(f"Car refueled to {self.car.fuelRate}%.")
        else:
            print(f"{self.name} doesn't have a car to refuel.")

class Office:
    employeesNum = 0

    def __init__(self, name):
        self.name = name
        self.employees = []

    def hire(self, employee):
        self.employees.append(employee)
        Office.employeesNum += 1
        print(f"Employee {employee.name} hired at {self.name}.")

    def fire(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                self.employees.remove(emp)
                Office.employeesNum -= 1
                print(f"Employee {emp.name} fired from {self.name}.")
                return
        print("Fire")

    def get_all_employees(self):
        return [emp.name for emp in self.employees]

    def calculate_lateness(self, targetHour, moveHour, distance, velocity):
        arrivalTime = moveHour + (distance / velocity)
        return "Late" if arrivalTime > targetHour else "On Time"

# إنشاء سيارة
my_car = Car("Fiat128", 80, 0)

# إنشاء موظف
samy = Employee("Samy", 5000, "Neutral", 90, 101, my_car, "samy@iti.com", 10000, 20)

# إنشاء مكتب
iti_office = Office("ITI Smart Village")

# تعيين الموظف
iti_office.hire(samy)

# الموظف يذهب إلى العمل
samy.drive(20)

# الموظف يعمل 8 ساعات
samy.work(8)

# الموظف يأكل وجبتين
samy.eat(2)

# الموظف يشتري 5 عناصر
samy.buy(5)

# حساب إذا كان الموظف متأخرًا
lateness_status = iti_office.calculate_lateness(9, 8, 20, 60)
print(f"Lateness status: {lateness_status}")
