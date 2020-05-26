

class Film:
    """ A section of data on a film from the Studio Ghibli API.

    Attributes:
        title (str): The title of the film
        id (str): The Studio Ghibli ID of the film
        people ([Person]): A list of the people in the film
    """
    def __init__(self, title, id, people=[]):
        """ Create a Film object.

        Args:
            title (str):The title of the film
            id (str): The Studio Ghibli ID of the film
            people ([Person]): A list of people in the film
        """
        self.title = title
        self.id = id
        self.people = [] + people

    def add_person_by_name(self, name):
        """ Append a name to the list of people in this film.

        Args:
            name (str): The name of the person
        """
        self.people.append({'name': name})

    def as_json(self):
        """Return the Film object as JSON."""
        json = {
            'title': self.title,
            'people': self.people
        }
        return json
