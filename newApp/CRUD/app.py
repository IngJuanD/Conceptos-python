import insert,read,update,delete

class Programa:
    def __init__(self) -> None:
        self.dato = 1

    def menu(self):

        while self.dato:
            selection = input('\n Select 1 to insert, 2 to update, 3 to read, 4 to delete\n')

            if selection == '1':
                insert.insert()
            elif selection == '2':
                update.update()
            elif selection == '3':
                read.read()
            elif selection == '4':
                delete.delete()
            else:
                print('\n INVALID SELECTION \n')

persona1 = Programa()
persona1.menu()        