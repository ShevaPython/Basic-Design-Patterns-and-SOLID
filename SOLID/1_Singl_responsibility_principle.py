import os



"""
SRP -- принцип единственной отвецтвености
"""


class Journal:
    """
    Журнал для хранения и удаления записей
    """

    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(F"{self.count} : {text}")
        self.count += 1

    def remove_entry(self, position):
        del self.entries[position]

    def __str__(self):
        return "\n".join(self.entries)

    def save(self, filename):
        """Добавления вторичной отвественности и нарушения принципа SRP"""
        with open(filename, "w") as f:
            f.write(str(self))

    # def load(self, filename):
    #     """Добавления вторичной отвественности и нарушения принципа SRP"""
    #     pass
    #
    # def load_from_web(self, uri):
    #     """Добавления вторичной отвественности и нарушения принципа SRP"""
    #     pass


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, "w") as f:
            f.write(str(journal))


journal = Journal()
journal.add_entry(F"I cried today")
journal.add_entry(F"I like Python")
print(F'My journal: \n{journal}')

file = os.path.join(os.getcwd(), "journal.txt")
PersistenceManager.save_to_file(journal, file)
