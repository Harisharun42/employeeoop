class employee:
    no_of_emps=0
    raise_amount=1.04

    def __init__(self,fn,ln,sal):
        self.fn=fn
        self.ln=ln
        self.sal=sal
        employee.no_of_emps +=1

    def fullname(self):
            print(self.fn+self.ln)

    def isseniorjunior(self):
             if self.sal>2000:
                 print('senior')
             else:
                 print('junior')

                 
    def raise_salary(self):
            self.sal=self.sal*self.raise_amount



    @classmethod
    def changeraiseamount(cls,raiseamount):
        cls.raiseamount=raiseamount

    @staticmethod
    def greet():
        print('good morn')




emp1=employee('harish','raju',2000)
emp2=employee('arun','raju',3000)
emp2.rasie_amount=1.08


print(employee.no_of_emps)
print(emp1.__dict__)
print(emp2.__dict__)

print(emp1.sal)
print(emp2.sal)
emp1.raise_salary()
emp2.raise_salary()
print(emp1.sal)
print(emp2.sal)




emp1.greet()
