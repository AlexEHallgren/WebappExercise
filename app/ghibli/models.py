
class Film:
    def __init__(self, title, id, people = []):
        self.title = title
        self.id = id
        self.people = [] + people

    def add_person_by_name(self, name):
        self.people.append(Person(name))

    def as_json(self):
        json = {
            "title": self.title,
            "people": [p.as_json() for p in self.people]
        }
        return json

class Person:
    def __init__(self, name):
        self.name = name
    
    def as_json(self):
        json = {
            "name": self.name
        }
        return json

