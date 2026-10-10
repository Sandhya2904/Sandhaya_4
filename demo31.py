fobj = open('C:\\Users\\karth\\emp.csv','r')
L = fobj.readlines()
fobj.close()

total = 0
for var in L:
    if 'sales' in var:
        var = var.strip()
        emp_list = var.split(",")
        ecost = emp_list[-1]
        total = total + int(ecost)
print(f"Sum of sales dept emp's cost:{total}")
 
 ## in Functional programming
"""
 >>> fobj = open('emp.csv','r')
>>>
>>> map(lambda a:a,open('emp.csv','r'))
<map object at 0x0000014A86B7DCC0>
>>>
>>> list(map(lambda a:a,open('emp.csv','r')))
['eid,ename,edept,ecity,ecost\n', '101,raj,sales,pune,1000\n', '102,leo,prod,bglore,2301\n', '230,raj,prod,pune,2300\n', '450,shan,sales,bglore,3401\n', '542,anu,HR,mumbai,4590\n', '321,bibu,sales,hyd,5419\n', '651,ram,hr,bglore,3130\n', '541,leo,admin,chennai,4913\n', '652,karthik,prod,bglore,3490\n', '742,anu,sales,mumbai,5901\n', '821,shan,prod,hyd,6000\n', '151,ram,prod,bglore,3000\n', '241,vijay,admin,chennai,3450\n', '252,anish,Hr,mumbai,5490']
>>>
>>> P1 = list(map(lambda a:a,open('emp.csv','r')))
>>>
>>> list(filter(lambda a:'sales' in a,P1))
['101,raj,sales,pune,1000\n', '450,shan,sales,bglore,3401\n', '321,bibu,sales,hyd,5419\n', '742,anu,sales,mumbai,5901\n']
>>>
>>>
>>> P1 = list(map(lambda a:a,open('emp.csv','r')))
>>> P2 = list(filter(lambda a:'sales' in a,P1))
>>>
>>> P3 = list(map(lambda a:a.split(",")[-1],P2))
>>> P3
['1000\n', '3401\n', '5419\n', '5901\n']
>>>
>>> functools.reduce(lambda a,b:int(a)+int(b),P3)
15721
>>>
>>> functools.reduce(lambda a,b:int(a)+int(b),map(lambda a:a.split(",")[-1],filter(lambda a:'sales' in a,map(lambda a:a,open('emp.csv','r'))))
... )
15721
>>>
"""
---------------------------------------------------------------------------------
Object Oriented Programming - style 
------------------------------------
class
object
method
inheritance 

class
object 

class - type - template/blueprint of an object
      - -----  mutable 
class className:
      ---------
	|->user defined 

class className:
     list of attributes

In python - using class name - we can access/modify/delete class attributes //mutable

class Emps:
   emp_id = 123
   emp_name = "Mr.AB"

Emps <-- ClassName

  +------------+
  | Emps      |
  +------------
  |  emp_id   | <== attribute
  |------------
  | emp_name  | <== attribute
  +-----------+

Emps.emp_id ->123
|
Emps.Emp_id ->AttributeError  Vs NameError 

Emp.edept = 'sales' # we can create new attribute
Emp.edept = 'Prod' # modification

del(Emp.edept) # we can delete 

-----------------------------------------------------------
>>> class Emps:
...     emp_id = 123
...
>>> Emps
<class '__main__.Emps'>
>>>
>>> emp_id
Traceback (most recent call last):
  File "<python-input-265>", line 1, in <module>
    emp_id
NameError: name 'emp_id' is not defined
>>>
>>> Emps.emp_id
123
>>> Emps.emp_id = 456
>>> Emps.emp_id
456
>>> Emps.emp_id
456
>>> Emps.emp_name = "Mr.ABC"
>>> Emps.emp_name
'Mr.ABC'
>>> Emps.emp_id = 904
>>> Emps.emp_id
904
>>> Emp.Emp_id
Traceback (most recent call last):
  File "<python-input-275>", line 1, in <module>
    Emp.Emp_id
    ^^^
NameError: name 'Emp' is not defined. Did you mean: 'emp'?
>>>
>>> Emps.Emp_id
Traceback (most recent call last):
  File "<python-input-277>", line 1, in <module>
    Emps.Emp_id
AttributeError: type object 'Emps' has no attribute 'Emp_id'. Did you mean: 'emp_id'?
>>>
>>> i = 10
>>> type(i)
<class 'int'>
>>>
>>> type(int)
<class 'type'>
>>> type(float)
<class 'type'>
>>> type(str)
<class 'type'>
>>> type(dict)
<class 'type'>
>>> type(list)
<class 'type'>
>>> type(set)
<class 'type'>
>>> type(tuple)
<class 'type'>
>>> type(bool)
<class 'type'>
>>>
>>> type(Emps)
<class 'type'>
>>>

	+-------------------+
	| [  ]   (white)    |  <== blueprint - class
	|                   |
	+----|    |---------+
    -------------------------------

+-----------------+
| [   ]  (white)  |
|                 |
+------|   |------+
-----------------------//real building - entity - object1 - 1st Block - 0x1234

+-----------------+
| [   ]  (white)  |
|                 |
+------|   |------+
-----------------------//real building - entity - object2 - 2nd Block - 0x3456

className() <== this is not a function - not initialized with def keyword
===========
  |->object creation



+--------------------------+
| [   ]  (white) ->(green) |
|                          |
+------|   |---------------+
-----------------------//real building - entity - object1 - 1st Block - 0x1234



>>> class Emps:
...     emp_id = 123
...
>>> Emps
<class '__main__.Emps'>
>>>
>>> emp_id
Traceback (most recent call last):
  File "<python-input-265>", line 1, in <module>
    emp_id
NameError: name 'emp_id' is not defined
>>>
>>> Emps.emp_id
123
>>> Emps.emp_id = 456
>>> Emps.emp_id
456
>>> Emps.emp_id
456
>>> Emps.emp_name = "Mr.ABC"
>>> Emps.emp_name
'Mr.ABC'
>>> Emps.emp_id = 904
>>> Emps.emp_id
904
>>> Emp.Emp_id
Traceback (most recent call last):
  File "<python-input-275>", line 1, in <module>
    Emp.Emp_id
    ^^^
NameError: name 'Emp' is not defined. Did you mean: 'emp'?
>>>
>>> Emps.Emp_id
Traceback (most recent call last):
  File "<python-input-277>", line 1, in <module>
    Emps.Emp_id
AttributeError: type object 'Emps' has no attribute 'Emp_id'. Did you mean: 'emp_id'?
>>>
>>>
>>> class Emps:
...     emp_id = 101
...
>>>
>>> Emps
<class '__main__.Emps'>
>>> Emps.emp_id
101
>>>
>>> Emps()
<__main__.Emps object at 0x0000014A850EAE40>
>>> Emps()
<__main__.Emps object at 0x0000014A86ABBB10>
>>>
>>> obj1 = Emps()
>>> obj2 = Emps()
>>>
>>> type(obj1)
<class '__main__.Emps'>
>>> type(obj2)
<class '__main__.Emps'>
>>>
>>> obj1.emp_id
101
>>> obj2.emp_id
101
>>> Emps.emp_id = 202
>>> obj1.emp_id
202
>>> obj2.emp_id
202
>>> obj1.emp_id = 'E-345' # object based initialization
>>> obj1.emp_id
'E-345'
>>> obj2.emp_id
202
>>> Emps.emp_id = 303
>>> obj1.emp_id
'E-345'
>>>
>>> obj2.emp_id
303
>>> obj2.emp_id = 'E-595' # object based initialization
>>>
>>> Emps.emp_id = 404
>>>
>>> obj1.emp_id
'E-345'
>>> obj2.emp_id
'E-595'
>>>
>>> obj3 = Emps()
>>> obj3.emp_id  ##<== ?
404
>>>

class box:
    def f1():
       print("Hello")


obj = box()
obj.f1() //methodcall => obj.f1() -> f1(obj)
				     ======== TypeError 

class box:
    def f1(self):
       print("self=",self)

obj1 = box()
obj1.f1() ----> f1(obj1)
# obj1 is same as self

 
obj2 = box()
obj2.f1() ---> f1(obj2)
# obj2 is same as self
 

obj2.f1(10,20,30) ==> f1(obj2,10,20,30)
			 ----


>>> def f1():
...     print("Hello")
...
>>> type(f1)
<class 'function'>
>>> f1()
Hello
>>>
>>> class box:
...     def f2():
...         print("Hello")
...
>>> obj = box()
>>> type(obj.f2)
<class 'method'>
>>>
>>> obj.f2()
Traceback (most recent call last):
>>>
>>> class box:
...     var = 120
...     def f1(self):
...         self.var = 500
...
>>> obj = box()
>>> # print(obj.var) -->(A)
>>> obj.f1()
>>> # print(obj.var) -->(B)
>>>
>>> obj = box()
>>> obj.var # A
120
>>> obj.f1() # f1(obj) -> self.var -> obj.var = 500
>>> obj.var
500
>>>
>>> class Cname:
...     def f1(self):
...         print("self=",self)
...
>>> obj1 = Cname()
>>> obj1
<__main__.Cname object at 0x0000014A850EAE40>
>>>
>>> obj1.f1()
self= <__main__.Cname object at 0x0000014A850EAE40>
>>>
>>>
######################
class DBI:
  def connect(self....):
      establish db connection

  def method1(self..):
     query1
  def method2(self..): 
     query2

------------------
obj = DBI()
obj.connect()
obj.method1('create table ...')

Vs
obj = DBI()
obj.method1('create table...') <== In oops - view - obj can invoke method1
--------------------------------   In Database - view - DB Error 

special method / dunder method
----------------------------------
 |_    __<name>__ <== pre-defined python attributes

__init__() <== method


>>> class box:
...     def f1(self):
...         print("non-constructor")
...
>>> box
<class '__main__.box'>
>>>
>>> box()
<__main__.box object at 0x0000014A86B312B0>
>>>
>>> obj = box()
>>> obj.f1() # methodCAll
non-constructor
>>>
>>> class box:
...     def __init__(self):
...         print("This is constructor Call")
...
>>> box()
This is constructor Call
<__main__.box object at 0x0000014A86B30440>
>>>
>>> obj = box()
This is constructor Call
>>>
>>>
>>> class box:
...     def __init__(self,a1,a2,a3=0,*a4,**a5):
...         print("Welcome")
...         print(a1,a2,a3,a4,a5)
...
>>> obj1 = box()
Traceback (most recent call last):
  File "<python-input-378>", line 1, in <module>
    obj1 = box()
TypeError: box.__init__() missing 2 required positional arguments: 'a1' and 'a2'
>>>
>>> obj1
<__main__.Cname object at 0x0000014A850EAE40>
>>> del(obj1)
>>>
>>> obj1 = box()
Traceback (most recent call last):
  File "<python-input-383>", line 1, in <module>
    obj1 = box()
TypeError: box.__init__() missing 2 required positional arguments: 'a1' and 'a2'
>>> obj1
Traceback (most recent call last):
  File "<python-input-384>", line 1, in <module>
    obj1
NameError: name 'obj1' is not defined. Did you mean: 'obj'?
>>>
>>> obj1 = box(10,20)
Welcome
10 20 0 () {}
>>> obj1 = box(10,20,30)
Welcome
10 20 30 () {}
>>> obj1 = box(10,20,30,40,50)
Welcome
10 20 30 (40, 50) {}
>>> obj1 = box(10,20,30,40,50,db="mysql")
Welcome
10 20 30 (40, 50) {'db': 'mysql'}
>>>
>>>
>>>
>>> '__len__' in dir(str)
True
>>>
>>> '__len__' in dir(int)
False
>>>
>>> '__len__' in dir(box)
False
>>>
>>> class box:
...     def __init__(self,a):
...         self.a = a
...     def __len__(self):
...         return self.a+100
...
>>> '__len__' in dir(box)
True
>>> obj = box(10)
>>>
>>> len(obj)
110
>>>
###################################################################################


    
