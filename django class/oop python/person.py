from datetime import datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
    
    def to_calculate_age(self):
        today = datetime.today()
        age = today.year - self.date_of_birth.year

        
        if today < datetime(today.year, self.date_of_birth.month, self.date_of_birth.day):
            age -= 1

        return age


person = Person(name="Rajat", country="Nepal", date_of_birth="2004-03-19")
print(f"{person.name} from {person.country} is {person.to_calculate_age()} years old.")