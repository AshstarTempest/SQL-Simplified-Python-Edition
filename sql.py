class MySql:
    def __init__(self):
        self.list_of_tables = []

    def clear(self):
        import os
        os.system('cls')

    def connection(self):
        import mysql.connector as m
        con = m.connect(host="localhost", user="root",
                        password="12345678", database="school")
        cur = con.cursor()

        return con,cur
    
    


    #this function takes a dict as input with field name and its value and prints it in cmd 
    def desc(self ,data : dict):

        from prettytable import PrettyTable
        sql_table = PrettyTable()
        sql_table.field_names = ["Field", "value",]
        for i , j in data.items():
            sql_table.add_row([i,j])
        print(sql_table)

    def querygen(self, table_name: str):
        column_data = self.initial_data()
    
        # no of columns excluding sl_no and id
        data = {
            'sl_no': 'int',
            'ID': 'varchar(30)',
        }
        str1 = f"create table {table_name} (SL_no int primary key auto_increment, ID varchar(30)"
    
        for i in range(2, len(column_data)):
            column_name = column_data[i]
            while True:
                try:
                    tyype = input(f"Enter type of column for {column_name}, str / int : ")
                    if tyype == "int":
                        type_value = 'int'
                    elif tyype == "str":
                        type_value = 'varchar(30)'
                    else:
                        raise ValueError("Invalid input. Please enter 'str' or 'int'.")
                    data[column_name] = type_value
                    newstr = ' , ' + list(data.keys())[-1] + ' ' + data[list(data.keys())[-1]]
                    str1 += newstr
                    break
                except ValueError as e:
                    print(e)
    
        self.clear()
        self.desc(data)
        print(str1 + ')')
        return str1 + ')'

    
    def interference(self):
        #create temp interference for mysql standalone project 
        
        pass
    
    def create_table(self , table_order : str):
        con, cur = self.connection()
        table_name = input(f"enter {table_order} Table name :  ")
        cur.execute(self.querygen(table_name))
        con.commit()
        print("______SUCCESSFULLY CREATED______")
        con.close()
        self.list_of_tables.append(table_name)
        self.querygen(table_name)
        
    
    def databaseconn():
        pass


    def initial_data(self):
        default_data = ["Sl_no", "ID", "Firstname", "lastname", "age"]
        while True:
            try:
                fields = input("enter no of fields (default=5) : ")
                if fields == "":
                    fields = 5
                fields = int(fields)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number of fields.")
    
        field_data = []
        for i in range(fields):
            if i <= 4:
                data = input(f"enter {i} field (default: {default_data[i]}): ")
            else:
                data = input(f"enter {i} field ")
    
            if data == "":
                data = default_data[i]
            field_data.append(data)
        return field_data

    def osmsg(self,msg):
        print(msg)


    def createdatabases(self):
        no_of_databases = int(input("Enter no of databases : "))
        
        for i in range(no_of_databases):
            if i == 0 :
                self.create_table("Primary")
            elif i == 1 :
                self.create_table("Secondary")
            elif i == 2 :
                self.create_table("Tertiary ")
                self.osmsg("Recommended not to create more that this ")
            else:
                self.create_table(str(i) + "th ")

        return self.list_of_tables
    
    # this function mains to inset data in the created database
    def insertdata(self):
        pass

    # this function generates random n digit phone no 
    def randphonegen(self,n):
        india_phone = "+91"
        import random 
        for i in range(n):
            if i ==0:
                india_code+=str(random.randrange(1, 10))
            india_code+=str(random.randrange(0,10))
        return india_phone

    







obj = MySql()
#data = MySql.initial_data(input("enter no of fields (default=5) :  "))
#query=obj.querygen(input("enter Table name :  "))
# database = obj.createdatabases()
# print(database)
print(obj.randphonegen(10))