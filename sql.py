class MySql:
    def __init__(self):
        pass

    def clear(self):
        import os
        os.system('cls')

    def connection():
        import mysql.connector as m
        con = m.connect(host="localhost", user="root",
                        password="12345678", database="school")
        cur = con.cursor()
    

    #this function takes a dict as input with field name and its value and prints it in cmd 
    def desc(self ,data : dict):

        from prettytable import PrettyTable
        sql_table = PrettyTable()
        sql_table.field_names = ["Field", "value",]
        for i , j in data.items():
            sql_table.add_row([i,j])
        print(sql_table)

    def querygen(self,table_name: str):
        column_data = self.initial_data()
        
    # no of columns excluding sl_no and id

        data = {
            'sl_no': 'int',
            'ID': 'varchar(30)',
        }
        str1 = f"create table {table_name} (SL_no int primary key auto_increment, ID varchar(30)"
        for i in range(2,len(column_data)):
            column_name = column_data[i]
            
            tyype = input(f"Enter type of column for {column_name}, str / int : ")
            if tyype == "int":
                type_value = 'int'
            elif tyype == "str":
                type_value = 'varchar(30)'
            data[column_name] = type_value
            newstr = ' , ' + list(data.keys())[-1] +' ' +data[list(data.keys())[-1]]
            
            str1+=newstr
        self.clear()
        self.desc(data)
        return str1 + ')'
    

        
    


    def initial_data( self):
        default_data = ["Sl_no", "ID", "Firstname", "lastname", "age"]
        fields = input("enter no of fields (default=5) :  ")
        if fields == "":
            fields = 5

        field_data = []
        for i in range(int(fields)):
            if i <= 4:
                data = input(f"enter {i} field (default: {default_data[i]}): ")
            else:
                data = input(f"enter {i} field ")

            if data == "":
                data = default_data[i]
            field_data.append(data)
        return field_data

obj = MySql()
#data = MySql.initial_data(input("enter no of fields (default=5) :  "))
query=obj.querygen(input("enter Table name :  "))
print(query)
        
