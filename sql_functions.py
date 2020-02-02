import sqlite3
import os
import psycopg2
import psycopg2.extras

table1_schema= """CREATE TABLE IF NOT EXISTS Notifications(
   chat_id INTEGER PRIMARY KEY, 
   Tournament_1 TEXT, 
   Days_left_1 INTEGER, 
   Tournament_2 TEXT, 
   Days_left_2 INTEGER,
   Tournament_3 TEXT, 
   Days_left_3 INTEGER,
   Tournament_4 TEXT, 
   Days_left_4 INTEGER,
   Tournament_5 TEXT, 
   Days_left_5 INTEGER,
   Tournament_6 TEXT, 
   Days_left_6 INTEGER);
"""

table2_schema="""CREATE TABLE IF NOT EXISTS Userdata(
       chat_id INTEGER PRIMARY KEY, 
       first_name TEXT,
       last_name TEXT,
       username TEXT);"""



class sql_db:
    
    def __init__(self, name):
        self.name = name

        
    def create_table(self, create_table_sql):
        """
        CREATE TABLE new_table(
           id INTEGER PRIMARY KEY, 
           column 1 TEXT, 
           col 2 TEXT, 
           col 3 INTEGER,
           ... )
        """
        print('connect')
        conn = psycopg2.connect(self.name, sslmode='require')
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.close()
       
            
    def query(self, query):
        conn = psycopg2.connect(self.name, sslmode='require')
        c = conn.cursor()
        c.execute(query)
        res= c.fetchall()
        conn.close()
        return res
    
    def execute(self, command):
        conn = psycopg2.connect(self.name, sslmode='require')
        c = conn.cursor()
        c.execute(command)
        conn.commit()
        conn.close()
        
    
    def delete_table(self, table_name):
        delete_command = "DROP TABLE {}".format(table_name)
        conn = psycopg2.connect(self.name, sslmode='require')
        c = conn.cursor()
        try:
            c.execute(delete_command)
            conn.commit()
        except:
            return False
        return True
    
    def display_all(self):
        conn = psycopg2.connect(self.name, sslmode='require')
        c = conn.cursor()
        c.execute('SELECT * FROM sqlite_master')
        for table in c.fetchall():
            print(table)
        return c.fetchall()  
        conn.close()
    

    def add_columns(self, table, col_data, col_type):
        """ Add column(s) to table """
        conn = psycopg2.connect(self.name, sslmode='require')
        c = conn.cursor()
        for data, typ in zip(col_data, col_type):
            c.execute("ALTER TABLE {tn} ADD COLUMN {cn} {ct}".
            format(tn=table, cn=data, ct=typ))
            conn.commit()    
        conn.close()
        
    def delete_columns(self, table, cols):
        """Delete column(s) from table
           table: name of table
           cols: list of columns to delete
        """
        conn = psycopg2.connect(self.name, sslmode='require')
        c = conn.cursor()
        #Get info of current table
        table_info = self.table_col_info(table)
        
        #Remove the undesired columns and corresponding data types
        columns = [row[1] for row in table_info if row[1] not in cols]
        types=[row[2] for row in table_info if row[1] in columns]
        
        #Make new table with desired columns
        create_command = """CREATE TABLE new_table ({})""".format(', '.join([''.join(str(i)+" "+str(j)) for i,j in zip(columns, types)]))
        c.execute(create_command)
        
        #Insert Data into new table
        c.execute("""INSERT INTO new_table({0}) SELECT {0} FROM {1}""".format(','.join([', '.join(str(i) for i in columns)]),table))
        conn.commit()
        
        #Delete old table
        self.delete_table(table)
        self.display_all()
        
        #Rename new table to match the old one
        conn = psycopg2.connect(self.name, sslmode='require')
        c = conn.cursor()
        c.execute('ALTER TABLE new_table RENAME TO {}'.format(table))
        
        
        conn.commit()
        conn.close()
    
    def val_in_row(self, table, val, row_num):
        """Check if a given value is present in a row"""   

        #Get column names of table
        columns = self.table_col_names(table)
        

        all_rows=self.all_rows(table)
        flag=False
        for col in columns:
            if val==all_rows[row_num-1][col]:
                flag=True
        return flag
        
    def delete_row(self, table, col, val):
        """Delete row from table"""
        conn = psycopg2.connect(self.name, sslmode='require')
        c = conn.cursor()
        if(type(val)== str):
            c.execute("DELETE from {tn} WHERE {cn} = {val}".format(tn=table, cn=col, val=val))
        else:
            c.execute("DELETE from {tn} WHERE {cn} = {val}".format(tn=table, cn=col, val=str(val)))  
        conn.commit()
        conn.close()
        
    def insert_values(self, table, cols, vals):
        """Insert values into specifed columns"""
        conn = psycopg2.connect(self.name, sslmode='require')
        c = conn.cursor()
        c.execute("INSERT INTO {0} ({1}) VALUES ({2})".format(table,','.join(str(i) for i in cols), ','.join("'"+str(i)+"'" for i in vals)))
        conn.commit()    
        conn.close
                          
    def update(self, table, col, new_val, key, key_val):
        """Update entry in a table where condition key=key_val is met"""

        conn = psycopg2.connect(self.name, sslmode='require')
        c = conn.cursor()
        if(type(new_val) == str):
            c.execute("UPDATE {tn} SET {cn}='{val}' WHERE {key}={key_val}".format(tn=table, cn=col, val=new_val, key=key, key_val=key_val))
        else:
            c.execute("UPDATE {tn} SET {cn}= {val} WHERE {key}={key_val}".format(tn=table, cn=col, val=new_val, key=key, key_val=key_val))
        conn.commit()
        conn.close()

    
    def all_rows(self, table, prt=False):
        """Display all rows in a table"""
        conn = psycopg2.connect(self.name, sslmode='require')
        # conn.row_factory = sqlite3.Row
        c = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        c.execute("SELECT * FROM {}".format(table))
        all_rows=c.fetchall()
        if(prt):
            for row in all_rows:
                print(row) 
        conn.close()
        return all_rows


    def table_col_names(self, table_name):
        """ Returns a list of tuples with column informations:
        (id, name, type, notnull, default_value, primary_key)
        """
        conn = psycopg2.connect(self.name, sslmode='require')
        c = conn.cursor()
        c.execute("SELECT * FROM {}".format(table_name))
        colnames = [desc[0] for desc in c.description]
        # c.execute('PRAGMA TABLE_INFO({})'.format(table_name))
        # info = c.fetchall()
        return colnames



    

