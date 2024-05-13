from pymongo import MongoClient

#Creating connection with MongoDB
client = MongoClient('localhost:27017')
db = client.EmployeeData

#Function to insert data into mongo db
def insert():
    try:
        employeeId = input('Enter Employee id: ')
        employeeName = input('Enter Name: ')
        employeeAge = input('Enter Age: ')
        employeeCountry = input('Enter Country: ')

        db.Employees.insert_one( #Insert database with elements
            {
                "id":employeeId,
                "name":employeeName,
                "age":employeeAge,
                "country":employeeCountry

            }
        )
        print('Inserted data successfully')

    except ImportError:
        platform_specific_module = None #View error type
        

