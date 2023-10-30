class codeexport:
    def __init__(self) -> None:
        
        self.folder_name = input("Enter your Project name ") 
        
        self.pyfile_name = input("Enter python file name (default : main )")
        if self.pyfile_name == "":

            self.pyfile_name  = "main"
        self.utilsused = []
        self.foldercreate()

    def clear(self,t_sec :int = 0 ):
        import os
        import time
        time.sleep(t_sec)
        os.system('cls')


    def selectstack(self):

        utils = {
            1:"mysql",
            2:"work in progress"
        }
        try:
            no_of_database = int(input("enter no of databases to use in the project (default : 2) : "))
        except:
            no_of_database = 2
        for i in range (no_of_database):
            self.projectutils()
            try : 
                util = int(input(f"select Slno for database {i + 1 } (default 1 ) : "))
            except :
                util = 1
            self.utilsused.append(util)
            self.clear()

        return self.utilsused




    def projectutils(self):
        from prettytable import PrettyTable
        x = PrettyTable()
        x.field_names = ["SL NO.", "Util",]
        x.add_row([1, 'MYSQL'])
        print(x)
    
    # create folder and files required by the user
    def foldercreate(self):
        import os
        if not os.path.exists(self.folder_name):
            os.mkdir(self.folder_name)
        pyfile = f"./{self.folder_name}/{self.pyfile_name}.py"
        with open(pyfile, "w") as new_file:
            pass

    def codeexp(self):
        f1 = open(f'./{self.folder_name}/{self.pyfile_name}.py' , "a")
        import inspect
        function_code = inspect.getsource(self.clear)
        filepath = f"./{self.folder_name}/{self.pyfile_name}.py"
        with open(filepath, "a") as new_file:
            new_file.write(function_code)

    
obj = codeexport()

obj.foldercreate()
obj.codeexp()