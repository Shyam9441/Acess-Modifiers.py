#Global scope(public scope)
class Employee:
    int: str ="new"
    fullName : str ="old"
emp = Employee()
print(emp.int)

#Partially private(protected)

class employee :
    _firstName :str = "sam"
    _lastName : str ="raj"
emp = employee()
print(emp._firstName)

#strictly private scope
class employee :
    __firstName :str ="Shyam"
    __latName:str ="Raj"
emp=employee()
print(emp.__firstName)
