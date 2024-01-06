# wap to calculate the grade of student based on the totalmarks

def marks(totalmarks):
    if totalmarks>=90:
        return 'A'
    elif totalmarks >= 80:
        return 'B'
    elif totalmarks >= 70:
        return 'C'
    elif totalmarks >=60:
        return 'D'
    else :
     return 'f'

if __name__=='__main__':
    grade = marks(56)
    print(grade)