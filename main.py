import abc


class Department:
    def __init__(self, name, code):
        self.__name = name
        self.__code = code
    
    def get_departament(self):
        return self.__name


# __code : o "__" torna a variavel private, não podendo ser instanciada diretamente
class Employee(abc.ABC):
    def __init__(self, code, name, salary):
        self.__code = code
        self.__name = name
        self.__salary = salary

    @abc.abstractmethod  # Torna o método abstrato, tornando obrigatório a implementação quando herdado
    def calc_bonus(self):
        pass

    @abc.abstractmethod
    def get_hours(self):
        return 8


class Manager(Employee):
    def __init__(self, code, name, salary):
        #super().__init__(code, name, salary)
        self.__code = code
        self.__name = name
        self.__salary = salary
        self.__departament = Department('managers', 1)

    def calc_bonus(self):
        return self.__salary * 0.15
    
    def get_departament(self):
        return self.__departament.get_departament()
    
    def set_departament(self, name):
        self.__departament.name = name
    
    def get_hours(self):
        return 8


class Seller(Manager):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('sellers', 2)
        self.__sales = 0

    def get_hours(self):
        return 8

    def get_departament(self):
        return self.__departament.get_departament()

    def set_departament(self, name):
        self.__departament.name = name
    
    def get_sales(self):
        return self.__sales
    
    def put_sales(self, sale):
        self.__sales += sale
    
    def calc_bonus(self):
        return self.__sales * 0.15


'''
# Testes

employee = Employee(123, 'Ana', 1000)
print(employee.code)
print(employee.name)
print(employee.salary)


seller = Seller(1234, 'Julia', 1000)
print(seller.get_departament())

manager = Manager(12345, 'Carol', 2000)
print(manager.get_departament())


#print(seller.get_sales())
#print(seller.code)
#print(seller.name)
#print(seller.salary)
'''