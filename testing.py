import sqlite3
#connection = sqlite3.connect("TDC.db")
#cursor = connection.cursor()
'''
cursor.execute("CREATE TABLE keys (consumerkey TEXT, accesstoken TEXT, refreshtoken TEXT)")

cursor.execute(f"INSERT INTO keys VALUES ('{consumer_key}', '{access_token}', '{refresh_token}')")

cursor.commit()


'''

'''
rows = (cursor.execute("SELECT accesstoken, consumerkey FROM keys").fetchall())[0][0]
print(rows)
'''


class KeyConnection:

    def __init__(self):
        self.connection = sqlite3.connect("TDC.db")
        self.cursor = self.connection.cursor()

    def get_at(self):
        at = (self.cursor.execute("SELECT accesstoken FROM keys").fetchall())[0][0]
        return at

    def get_ck(self):
        ck = (self.cursor.execute("SELECT consumerkey FROM keys").fetchall())[0][0]
        return ck

    def get_rt(self):
        rt = (self.cursor.execute("SELECT refreshtoken FROM keys").fetchall())[0][0]
        return rt

    def replace_at(self, new_token):

        (self.cursor.execute(f"UPDATE keys SET accesstoken = '{new_token}'"))
        self.connection.commit()

    def replace_rt(self, new_token):

        (self.cursor.execute(f"UPDATE keys SET refreshtoken = '{new_token}'"))
        self.connection.commit()
