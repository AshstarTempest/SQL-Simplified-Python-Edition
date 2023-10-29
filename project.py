# to create a project so that it can help to make a school class 12 project using csv , binary , mysql, text
folder_name = "Project"  # where the files will be stored


def projectutils():
    from prettytable import PrettyTable
    x = PrettyTable()
    x.field_names = ["SL NO.", "Util",]
    x.add_row([1, 'CSV'])
    x.add_row([2, 'BINARY'])
    x.add_row([3, 'TEXT'])
    x.add_row([4, 'MYSQL'])
    print(x)


def managementsys(sys):
    import os

    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    filepath = f"./Project/{sys}.py"
    with open(filepath, "w") as new_file:
        pass


def initial_data():
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


def csvusers(sys, initial_data):
    import csv
    f = open(f"./Project/{sys}.csv", 'a')
    writer = csv.writer(f)
    writer.writerow(initial_data)
    f.close()


def Binaryusers(sys, initial_data):
    import pickle as p
    f = open(f"./Project/{sys}.dat", 'ab')
    p.dump(initial_data, f)
    f.close()


def Textusers(sys, initial_data):
    f = open(f"./Project/{sys}.txt", 'w')
    f.writelines(initial_data)
    f.close()


def MYsqlusers(sys, initial_data):
    import mysql.connector as m
    con = m.connect(host="localhost", user="root",
                    password="12345678", database="school")
    cur = con.cursor()
    cur.execute(f"create table {sys} ({initial_data[0]} int primary key auto_increment, {initial_data[1]} varchar(10), {
                initial_data[2]} varchar(30), {initial_data[3]} varchar(30), {initial_data[4]} int)")

    # Use the execute() method to execute the query with parameters
    con.commit()
    con.close()


def codeexport(func_name, file):
    import inspect
    function_code = inspect.getsource(func_name)
    filepath = f"./Project/{file}.py"
    with open(filepath, "a") as new_file:
        new_file.write(function_code)


def main():

    # sys will be the name of the project u want to create

    sys = input(
        "Enter which management system you want to make(eg: School , Hospital) : ")
    managementsys(sys)  # creates a python file with the name
    data = initial_data()
    csvusers(sys, data)
    # Binaryusers(sys, data)
    # Textusers(sys, data)
    MYsqlusers(sys, data)
    # codeexport(MYsqlusers, sys)


def mysqlmanagement(name, initial_data):
    import mysql.connector as m
    con = m.connect(host="localhost", user="root",
                    password="12345678", database="school")
    cur = con.cursor()
    cur.execute(f"create table {name} ({initial_data[0]} int primary key auto_increment, {
                initial_data[1]} varchar(30), {initial_data[2]} varchar(30), {initial_data[3]} int)")

    # Use the execute() method to execute the query with parameters
    con.commit()
    con.close()


def csvlmanagement(name, initial_data):
    import csv
    f = open(f"./Project/{name}.csv", 'a')
    writer = csv.writer(f)
    writer.writerow(initial_data)
    f.close()


main()
