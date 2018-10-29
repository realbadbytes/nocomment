# Why

Enable Python developers to document their code flawlessly and easily by removing the requirement for a developer to know standard docstring syntax, like RST.

# How

git clone http://github.com/realbadbytes/nocomment

cd nocomment

sudo python3 -m pip install -r requirements.txt

./core.py [target module]

NOTE: Target module must be in current directory. Omit .py extension for target module when running the tool. Output will be test_output.py

# Show me

**Before nocomment**

 ```python
#!/usr/bin/python3

class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
   
    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print ("Name : ", self.name,  ", Salary: ", self.salary)

emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__ )
```

```
user@ubuntu:~/nocomment$ ./core.py employee_class
10/28/2018 11:24:48 PM nocomment starts
Employee.__doc__: Common base class for all employees
Employee.__name__: Employee
Employee.__module__: employee_class
Employee.__bases__: (<class 'object'>,)
Employee.__dict__: {'__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__module__': 'employee_class', '__init__': <function Employee.__init__ at 0x7f1a8057ab70>, 'empCount': 2, '__dict__': <attribute '__dict__' of 'Employee' objects>, 'displayCount': <function Employee.displayCount at 0x7f1a8057abf8>, 'displayEmployee': <function Employee.displayEmployee at 0x7f1a8057ac80>, '__doc__': 'Common base class for all employees'}
10/28/2018 11:24:48 PM Found classe(s): [<class 'employee_class.Employee'>]
Enter brief function description for displayCount: Show number of Employees.
10/28/2018 11:24:55 PM Ingesting doc for displayCount with signature (self)
Enter type and description for parameter param:self in displayCount: self object
Enter return value description: None
Enter brief function description for __init__: Employee class initializer
10/28/2018 11:25:17 PM Ingesting doc for __init__ with signature (self, name, salary)
Enter type and description for parameter param:self in __init__: self object
Enter type and description for parameter param:name in __init__: Employee name
Enter type and description for parameter param:salary in __init__: Employee salary
Enter return value description: None
Enter brief function description for displayEmployee: Show Employee information.
10/28/2018 11:25:43 PM Ingesting doc for displayEmployee with signature (self)
Enter type and description for parameter param:self in displayEmployee: self object
Enter return value description: None
10/28/2018 11:25:50 PM Generating Restview docstring for displayCount
10/28/2018 11:25:50 PM Generating Restview docstring for __init__
10/28/2018 11:25:50 PM Generating Restview docstring for displayEmployee
```

**After nocomment**

```python
#!/usr/bin/python3

class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
    """ Employee class initializer
    
    :param self: self object
    :param name: Employee name
    :param salary: Employee salary
    :returns: None
    """
    
        self.name = name
        self.salary = salary
        Employee.empCount += 1
   
    def displayCount(self):
    """ Show number of Employees.
    
    :param self: self object
    :returns: None
    """
    
        print ("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
    """ Show Employee information.
    
    :param self: self object
    :returns: None
    """
    
        print ("Name : ", self.name,  ", Salary: ", self.salary)

emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__ )
```

