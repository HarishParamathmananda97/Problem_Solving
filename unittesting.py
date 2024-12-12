import unittest
from phonebook import PhoneBook



class PhoneBookTest(unittest.TestCase):
    def test_loopup_by_name(self):
        phonebook = PhoneBook()
        phonebook.add('Jerry','14321')
        number = phonebook.lookup('Jerry')
        self.assertEqual('14321', number)
        