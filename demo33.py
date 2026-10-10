class Enrollment:
    def __init__(self,n,d,p):
        self.name = n
        self.dob = d
        self.place = p
        print(f'Emp {self.name} enrollment is done')
    def display(self):
        print(f'About {self.name} detials:-')
        print(f'Name:{self.name} DOB:{self.dob} Place:{self.place}')
obj1 = Enrollment('Sandhaya','29th April','City-1')

obj2 = Enrollment('Silja','2nd Feb','City-2')

obj1.display()
obj2.display()
