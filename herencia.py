
class animal:  
    pass


#__basses__ es para saber de donde esta heredando el metodo
#__subclasses__ es para saber a donde estas heredando los metodos
class tigre (animal):
    pass


print(animal.__subclasses__)
print(tigre.__bases__)