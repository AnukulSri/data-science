# constructor


class Paratha:

    def __init__(self,typ,price): # here we are defining a constructor
        self.type = typ
        self.price = price

    def display(self): # creating a fuinction in which we display the content
        print(f'{self.type}: {self.price} Rs.')


if __name__=="__main__": # checking if we are in main
    ap = Paratha("Aloo Paratha",30)
    bp = Paratha("Paneer Paratha",50)
    pp = Paratha("Pyaaz Paratha",40)
    cp = Paratha("Mooli Paratha",20)

    print("today menu")
    ap.display()
    bp.display()
    pp.display()
    cp.display()

