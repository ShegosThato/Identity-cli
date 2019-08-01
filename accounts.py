import sqlite3

class Account():

    #account details
    first_name = None
    last_name = None
    id_number = []

    

    #setters
    def set_first_name(self, name):
        self.first_name = name

    def set_last_name(self, sn):
        self.last_name = sn

    def set_id_number(self, id_num):
        self.id_number = id_num

    #getters
    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_id_number(self):
        return self.id_number

    def save_data(self):
        #connection to the database
        conn = sqlite3.connect('accounts.db')
        cursor = conn.cursor()
        try:
            cursor.execute("""CREATE TABLE Accounts(first_name text, last_name text, id_number int)
            """)
        except sqlite3.OperationalError:
            pass
        
        cursor.execute("INSERT INTO Accounts VALUES(?,?,?)",(self.get_first_name(), self.get_last_name(), self.get_id_number()))
        conn.commit()
        cursor.close()
        conn.close()
        print("Your account details have been saved")
        input()

    def list_all(self):
        conn = sqlite3.connect('accounts.db')
        cursor = conn.cursor()
        #retrieve all the data in the database
        all_data = cursor.execute("SELECT * FROM Accounts ORDER BY first_name")
        return all_data

    def search_firstname(self, name):
        conn = sqlite3.connect('accounts.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Accounts WHERE first_name="{nm}" '.\
        format(nm=name))
        search_data = cursor.fetchone()
        cursor.close()
        conn.close()
        return search_data

    def delete_account(self, id_num):
        conn = sqlite3.connect('accounts.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Accounts WHERE id_number="{id}" '.\
        format(id=id_num))
        conn.commit()
        cursor.close()
        conn.close()

