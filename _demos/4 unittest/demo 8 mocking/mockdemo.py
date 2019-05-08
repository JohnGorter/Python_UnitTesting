import unittest
from unittest.mock import Mock

class Database:
    def insertPerson(self, name):
        print("person " + name + " inserted into the database")
    
class PersonForm:

    def registerPerson(self, name, database):
        if (name == ""):
            print("skip no name")
        else:
            database.insertPerson(name)

class PersonFormTest(unittest.TestCase):
    def test_register_person_with_john(self):
        PersonForm().registerPerson("john", Database())
        self.assertTrue(True)



PersonForm().registerPerson("john", Database())
