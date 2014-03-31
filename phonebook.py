"""Usage: phonebook.py create <phonebook>
          phonebook.py lookup <query> -b <phonebook>
          phonebook.py add <name> <phone_number> -b <phonebook>
          phonebook.py change <name> <phone_number> -b <phonebook>
          phonebook.py remove <name> -b <phonebook>
          phonebook.py reverse-lookup <phone_number> -b <phonebook>

Options:
  -h --help
"""
import sqlite3
from docopt import docopt

def createTable(name, cursor):
    try:
        cursor.execute("CREATE TABLE %s (name text, number text)" % name)
    except sqlite3.OperationalError as err:
        print err
        return

    print "created phonebook " + name + " in database."

def lookup(name, phonebook, cursor):
    #try:
    values = cursor.execute(("SELECT * FROM %s  WHERE name = '%s'") % 
                            (phonebook, name))
    return values

def tableExists(table, cursor):
    rows = cursor.execute("""
            SELECT name FROM sqlite_master WHERE type='table' AND name='%s';
            """ % table)
    if rows.rowcount == -1:
        return False
    else:
        return rows

def add(name, phone_number, phonebook, cursor):
    try:
        cursor.execute(("""INSERT INTO %s VALUES ('%s', '%s')""") % 
                       (phonebook, name, phone_number))
    except sqlite3.OperationalError as err:
        print err

def change(name, phone_number, phonebook, cursor):
    try:
        cursor.execute(("UPDATE %s SET number = '%s' WHERE name='%s'") % 
                       (phonebook, phone_number, name))
    except sqlite3.OperationalError as err:
        print err

def remove(name, phonebook, cursor):
    try:
        cursor.execute(("DELETE FROM %s WHERE name='%s'") % (phonebook, name))
    except sqlite3.OperationalError as err:
        print err

def reverse_lookup(number, phonebook, cursor):
    values = cursor.execute("SELECT * FROM %s WHERE number='%s'" % (phonebook, number))

def main():
    args = docopt(__doc__)
    conn = sqlite3.connect('phonebook.db')
    c = conn.cursor()
    if args['create']:
        createTable(args['<phonebook>'], c)
    elif args['add']:
        add(args['<name>'], args['<phone_number>'], args['<phonebook>'], c) 
    elif args['lookup']:
        rows = lookup(args['<query>'], args['<phonebook>'], c)
        for row in rows:
            print row
    elif args['change']:
        change(args['<name>'], args['<phone_number>'], args['<phonebook>'], c)
    elif args['remove']:
        remove(args['<name>'], args['<phonebook>'], c)
    elif args['reverse-lookup']:
        reverse_lookup(args['<phone_number>'], args['<phonebook>'], c)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()

