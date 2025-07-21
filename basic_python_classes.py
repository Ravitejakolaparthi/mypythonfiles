class toys():  
     def __init__(self,name,id,cost): # creating class and declaring data members and member function in python
          self.name = name  # syntax : def _constructor_(parameters) 
          self.id = id
          self.cost = cost

toy1 = toys("car", 101, 1200)
toy2 = toys("bike", 102, 1300) 
toy3 = toys("barbie doll", 100, 1500)

print(toy1.name)
print(toy1.id)
print(toy1.cost)
              
