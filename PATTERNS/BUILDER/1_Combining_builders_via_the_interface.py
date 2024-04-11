"""
Работа с 2 строителями но с нарушениям принципа рткрытости и закрытости!!
"""


class Person:
    def __init__(self):
        # имя фамилия отчество
        self.name = None
        self.first_name = None
        self.last_name = None

        # работа
        self.company_name = None
        self.position = None
        self.salary = None

    def __str__(self):
        return (F"Name: {self.name}, First Name: {self.first_name} , Last Name: {self.last_name} \n"
                F"Company Name: {self.company_name}, Position: {self.position}, Salary: {self.salary}")


class PersonBuilder:
    """
    Base builder
    """

    def __init__(self, person=Person()):
        self.person = person

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    @property
    def name(self):
        return PersonNameBuilder(self.person)

    def build(self):
        return self.person


class PersonJobBuilder(PersonBuilder):
    """
    1 builder
    """

    def __init__(self, person):
        super().__init__(person)

    def add_company(self, company_name):
        self.person.company_name = company_name
        return self

    def add_position(self, position):
        self.person.position = position
        return self

    def add_salary(self, salary):
        self.person.salary = salary
        return self


class PersonNameBuilder(PersonBuilder):
    """
    2 builder
    """
    def __init__(self, person):
        super().__init__(person)

    def add_name(self, name):
        self.person.name = name
        return self

    def add_first_name(self, first_name):
        self.person.first_name = first_name
        return self

    def add_last_name(self, last_name):
        self.person.last_name = last_name
        return self


pb = PersonBuilder()
person = pb.name.add_name('John').add_first_name('Walls').add_last_name('Broke').works.add_position(
    'Best Company').add_position('Programming').add_salary('1000').build()
print(person)
