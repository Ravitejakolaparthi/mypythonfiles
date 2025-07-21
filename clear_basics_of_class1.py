# creaition of a class or blue print for a objec
# object -> car
class car():  # class class_name () :       *** data_members -> attribites and member_funciton -> methods
            
            model_no  = 15012 # it is defined here is same for every object


              # i want to crate what things i must include in my car print
              # i describe them using a method "__init__" method syntax "  def __init__(self_name,thing1,...):
              # __init__ it is a method used to initillize  oject of the class
              # it is same as constructor in cpp  and java
              # where constructor work is assign values to the object 

            # declaration of attribuitres are used by method og __init__   
            def __init__(self,body_cost,milage):    #syntax  : def __init__("self",parameter1,parameter2,....)   self_keyword  -> in classes  refers to binding arguments and attribites of an object
                self.body_cost = body_cost          #          self.parameter1  = parameter1             
                self.milage = milage                #          self.parameter2  = parameter2
            
            def fun(self):          # method in py
                print(self.body_cost)
                print(self.milage)      
    
     # i created a class or small blue print of a car
    # now i must create a car using blue print
# for creation of a car using class syntax : object_name = class_name(input_vals,....)
Rolls = car(15000000,12)  # car1  # assing data  to  attribites  of object
Cruser = car(1200000,20)  # car2

# only created object can access methods
# for printing 
Rolls.fun()   # calling member function
Cruser.fun()

print(Cruser.model_no) # acessing attritbites of a class
print(Rolls.model_no)

                 
    