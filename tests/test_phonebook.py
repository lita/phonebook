import unittest
import os
import sqlite3

import phonebook

class TestPhoneBook(unittest.TestCase):
    def setUp(self):
        conn = sqlite3.connect('unittest.db')
        self.c = conn.cursor()

    def testCreateTable(self):
        phonebook.createTable('unittest', c)
        t = self.c.execute("SELECT unittest FROM sqlite_master WHERE type='table'")
        self.assertTrue(t)

if __name__ == '__main__':
    unittest.main()