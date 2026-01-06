class A:
    def sample(self):
        print("Inside sample method")

    def sample(self, a):
        print("Inside sample method", a)

    def sample(self, a=0, b=0):
        print("Inside sample method", a + b)


obj = A()
obj.sample()


def addition(a=0.0, b=0.0, c=0.0):
    return a + b + c


print(addition()) #--> 0.0
print(addition(10, 20, 30)) #--> 60
print(addition(30.50, 40.45)) #--> 70.95
print(addition(a=20, b=30, c=40)) #--> 90
print(addition(20, c=50)) #-->70.0
print(addition(14, True)) #-->15
