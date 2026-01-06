
class Employee:

    def __init__(self,first_name,last_name,pay):
        self._first_name = first_name
        self._last_name = last_name
        self._pay = pay

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def pay(self):
        return self._pay

    @pay.setter
    def pay(self,value):
        if not value:
            raise ValueError("pay value should not be empty")
        elif value <=0:
            raise ValueError("pay value should not be less than 0")
        else:
            self._pay = value

    @staticmethod
    def create_employee_objects():
        emp_1 = Employee('Dinesh', 'Pandey', 50000)
        emp_2 = Employee('Rakesh', 'Pandey', 75000)
        emp_3 = Employee('Abha', 'Pandey', 50000)
        emp_4 = Employee('Aka', 'Pandey', 75000)
        return [emp_1,emp_2,emp_3,emp_4]