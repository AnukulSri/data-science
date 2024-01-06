class Fan: # creating the class
    brand ='Orient'  # properties of class fan
    blade_size = '1200' # properties of class fan
    rpm = 380 # properties of class fan

    def start(self, speed= 1): # self is used to join the function with class
        print(f'fan is starting at {speed} speed')


if __name__=='__main__':
    f= Fan() # creating the object of fan class
    g =Fan() # creating object of fan class

    f.start(2) # calling the function start
    g.start(3) # calling the function start with different parameter 

    print(f.blade_size,g.blade_size) # accessing the properties of class 
    print(f.rpm,g.rpm)
    print(f.brand,g.brand)

    f.blade_size = 1000 # changing the properties of fan class
    f.brand='usha'
    f.rpm = 400

    print(f.blade_size,g.blade_size)
    print(f.brand,g.brand)
    print(f.rpm,g.rpm)