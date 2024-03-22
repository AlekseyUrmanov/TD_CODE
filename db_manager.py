import json
import sqlite3



class db_operator:

    def __init__(self, db_name):
        self.db_name = db_name

        self.conn = sqlite3.connect('{}.db'.format(self.db_name))
        self.cursor = self.conn.cursor()


    def create_table(self, table_name):

        self.cursor.execute('''CREATE TABLE
                        {} (
                        id INTEGER PRIMARY KEY,
                        stock TEXT
                        )'''.format(table_name))
        self.conn.commit()

    def add_div_data(self, data_raw, stock, table_name, cash):

        def mod_raw_for_db(raw, stock, cash):
            new_dict = {}
            call_map = raw['callExpDateMap']
            put_map = raw['putExpDateMap']

            new_dict['stock'] = stock
            new_dict['callExpDateMap'] = call_map
            new_dict['putExpDateMap'] = put_map
            new_dict['cash'] = cash

            new_dict = str(new_dict)
            return new_dict

        inserting_data = mod_raw_for_db(data_raw, stock, cash)
        self.cursor.execute("INSERT INTO {} (stock) VALUES (?)".format(table_name), (inserting_data,))
        self.conn.commit()

    def add_strdPL_data(self, row, table_name):

        self.cursor.execute("INSERT INTO {} (stock) VALUES (?)".format(table_name), (row,))
        self.conn.commit()

    def pull_data(self, desired_id=None, table_name=None):

        if desired_id:
            self.cursor.execute("SELECT * FROM {} WHERE id = ?".format(table_name), (desired_id,))
            pulled_rows = self.cursor.fetchone()
        else:
            self.cursor.execute("SELECT * FROM {}".format(table_name))
            pulled_rows = self.cursor.fetchall()

        self.conn.commit()

        return pulled_rows










#json_data = eval(row[1])
#frames = tdc.sort_data_into_data_frames(json_data)
#print(frames)
