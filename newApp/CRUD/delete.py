from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.EmployeeData

#Function to delete record form mongodb
def delete():
    try:
        identifiacion = input("\n Enter employee id to delete \n")
        db.Employees.delete_many({"id":identifiacion})
        print('\n Deletion succesfully \n')
    except ImportError:
        platform_specific_module = None