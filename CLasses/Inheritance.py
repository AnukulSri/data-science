

from calendar import c


class Person: # base class

    def __init__(self,name,gender="female"): # creating a function
        self.name=name
        self.gender= gender
    
    def show(self):
        print("My details")
        print(f'Name: {self.name}')
        print(f"Gender: {self.gender}")
        print('---'*10)


class Student(Person): # inheriting the base class (person).

    def __init__(self, name, gender,klass,college,stream):
        super().__init__(name, gender) # setup if constructor

        self.klass = klass
        self.college = college
        self.stream = stream
    
    def another_show(self):
        print("More Details")
        print(f'college: {self.college}')
        print(f'class: {self.klass}')
        print(f'stream: {self.stream}')
        print('---'*10)

class coder(Student):

    def __init__(self, name, gender, klass, college, stream,prog_lang=[]):
        super().__init__(name, gender, klass, college, stream)
        self.prglang = prog_lang

    def coding_experience(self):
        if len(self.prglang)==0:
            print(f'I, {self.name} don\'t khow any programming language')
        else:
            print(f'I,{self.name} know following programming languages')
            for lang in self.prglang:
                print(f"=> {lang}")
            print('---'*10)

    def add_language(self,lang):
        self.prglang.append(lang)

if __name__ =='__main__':
     p=Person("Anukul",gender ='Male')
     p.show()


     stu = Student('Anukul','male','python','digipodium','data science')
     stu.show()
     stu.another_show()

     Coder = coder('John','male','9th','st.peters','PCM')
     Coder.show()
     Coder.another_show()
     Coder.coding_experience()

     print('After 1 year')
     Coder.add_language('Python')
     Coder.add_language('Html')
     Coder.add_language('PHP')
     Coder.coding_experience()


