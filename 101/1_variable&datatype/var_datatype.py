### String
name = "101 Python"
print(name)

### integer
a = 10
print(a)

### Single line assignment
name,a = "Hello World",10

### Type is a class which defines the type of a class inside the (x)
print("name", type(name))
print("a",type(a),"\n")

### Typecasting

### Explicitly Cast
b = "4" ### This is not string this is 
print("b: ",b,type(b))

### After explicit Typecast
b = int(b)
print("b: ",b,type(b))

###########################################################################################################################################################################

### 1. List Datatype
l1 = ["Hello","1234","2.56",9986]
print("List: ",l1,type(l1))

### Assign List data to different variables
### var1,var2,var3 = l1  ### error occured because number of elements are not same as number of variable
var1,var2,var3,var4= l1
print("var 1",var1)
print("var 2",var2)
print("var 3",var3)
print("var 4",var4)

### 2. Tuple Datatype
t1 = (1,2,3,4,"HelloWorld")
print("Tuple: ",t1,type(t1))

### 3. Dictionaries datatype
dic = {'a':"Hello",'b':"World",'c':"My",'d':"name"}
print("Dictionary: ",dic,type(dic))

### 4. Boolean
bool = False
print(type(bool))

### 5. Range
r = range(8)
print(type(r))

### 6. Bytes
byte = b"Hello2"
print(type(byte))

print("\n")

print(type("a"))
print(type(b))
print(type(l1))
print(type(t1))
print(type(dic))
print(type(bool))
print(type(r))
print(type(byte))
print("\n")
print(a)
print(b)
print(l1)
print(t1)
print(dic)
print(bool)
print(r)
print(byte)

