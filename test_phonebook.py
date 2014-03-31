import unittest
import os
import sqlite3

import phonebook

class TestPhoneBook(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect('unittest.db')
        self.c = self.conn.cursor()

    def testAddAndLookup(self):
        phonebook.createTable('unittest', self.c)
        phonebook.add('Lita Cho', '510 938 3333', 'unittest', self.c)
        rows = phonebook.lookup('Lita Cho', 'unittest', self.c)
        self.assertTrue(rows.next()[1] == '510 938 3333')

    def testChange(self):
        phonebook.createTable('unittest', self.c)
        phonebook.add('Lita Cho', '510 938 3333', 'unittest', self.c)
        phonebook.change('Lita Cho', '333 333 3333', 'unittest', self.c)
        rows = phonebook.lookup('Lita Cho', 'unittest', self.c)
        self.assertTrue(rows.next()[1] == '333 333 3333')


    def tearDown(self):
        self.conn.close()
               

if __name__ == '__main__':
    unittest.main()