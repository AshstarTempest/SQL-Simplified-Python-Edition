class MySql:
    def __init__(self):
        self.list_of_tables = []
        self.last_id = None
        self.table_contents = []
    

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
        sql_table_contents = {}
        from prettytable import PrettyTable
        sql_table = PrettyTable()
        sql_table.field_names = ["Field", "value",]
        for i , j in data.items():
            sql_table.add_row([i,j])
            sql_table_contents[i] = j
        self.table_contents.append(sql_table_contents)
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
    def insertdata_before(self , table_no :int = 0):
        con, cur = self.connection()
        id = self.IDgen(6)
        name = self.random_name_gen()
        age = self.agegen()
        st = f"inset into {self.list_of_tables[table_no]} ({self.table_contents[table_no][1],self.table_contents[table_no][2],self.table_contents[table_no][3],self.table_contents[table_no][4]}) values  ({id},{name[0]},{name[1]},{age}) "
        cur.execute(st)
        con.commit()
        con.close()
        print(st)
    def insertdata_after(self , table_name :str ):
        con, cur = self.connection()
        id = self.IDgen(6)
        name = self.random_name_gen()
        age = self.agegen()
        st = f"insert into {table_name} (ID,Firstname,lastname ,age) values ('{id}','{name[0]}','{name[1]}',{age}) "
 
        cur.execute(st)
        con.commit()
        con.close()
    
        return "data Successfully inserted"

    # this function generates random n digit phone no 
    def randphonegen(self,n):
        india_phone = "+91"
        import random 
        for i in range(n):
            if i ==0:
                india_code+=str(random.randrange(1, 10))
            india_code+=str(random.randrange(0,10))
        return india_phone
    # This helps to generate a n no of words id which can be seqential or totally random 
    def IDgen(self,No_of_letters:int,randomstate:bool=False,const_char:str= "E"):
        import random
        import string 
        id = []
        
        const_id = []
        alphabets = list(string.ascii_letters)
        if randomstate == True:
            for i in range(No_of_letters):
                id.append(random.choice(alphabets))
            return "".join(id)
        if randomstate == False :
            if self.last_id != None:
                temp_id = int("1" + self.last_id[1:])
                self.last_id = const_char + str(temp_id+1)[1:]
                return self.last_id

                
                
                pass
            else:
                pass
            for i in range(No_of_letters-1):
                if i < No_of_letters -2:
                    const_id.append('0')
                else:
                    const_id.append('1')
            #print(f"-------{const_id}-----------")
            self.last_id =const_char+  "".join(const_id)
            
            return self.last_id
            

    def random_name_gen(self,split_names:bool = True):
        import data
        import random
        if split_names == True:
            first_names = data.indian_student_first_names
            last_names = data.indian_student_last_names
            names = [random.choice(first_names),random.choice(last_names)]
            return names
        first_names = data.indian_student_first_names
      #  print(first_names)
        last_names = data.indian_student_last_names
        name = random.choice(first_names) + " " + random.choice(last_names)

        return name
    
    def generate_institute_name(self):
        import random
        import data
        prefixes = data.prefixes
        nouns = data.nouns
        adjectives = data.adjectives
        prefix = random.choice(prefixes)
        noun = random.choice(nouns)
        adjective = random.choice(adjectives)
        
        # Randomly select the order of words
        order = random.choice(["prefix-noun", "noun-prefix", "adjective-noun", "noun-adjective"])
        
        if order == "prefix-noun":
            name = f"{prefix} {noun}"
        elif order == "noun-prefix":
            name = f"{noun} {prefix}"
        elif order == "adjective-noun":
            name = f"{adjective} {noun} college"
        elif order == "noun-adjective":
            name = f"{noun} {adjective} college"
    
        return name

    def agegen(self):
        import random
        age = random.randrange(18, 45)
        return age
    


    







obj = MySql()
#data = MySql.initial_data(input("enter no of fields (default=5) :  "))
#query=obj.querygen(input("enter Table name :  "))
#database = obj.createdatabases()
# print(database)
#print(obj.randphonegen(10))

#print(obj.IDgen(6,False,"A"))
#print(obj.random_name_gen())
#print(obj.generate_institute_name())


# print(obj.agegen())
for i in range(25000):
    print(obj.insertdata_after('gu'))