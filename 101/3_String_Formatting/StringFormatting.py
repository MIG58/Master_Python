### Python Strings are immutable (means string cannot be changed )
### Quotes
str0 = "Hello World I am a Strings"
str1 = 'I am a Single quotes Strings'

### Multiline String
### It prints as it is writtern (predefined as <pre> </pre>)
multi_str = """ 
    I am a 
Multi Line 
String\n"""

print(str0)
print(str1)
print(multi_str) 

### Double Quote inside string

str4 = "I\"m a String"
str5 = 'I\'m a String'

print(str4)
print(str5)

### Escape Squences
str6 = "\\ \x41 \x42 \x43" ### Print hexa decimal using String
print(str6)

str7 = "a" * 10 ### Prints 10 times a
print(str7)


### String Functions
str0 = "Hello World I am a Strings"
str1 = "Hello World"
### str1='HelloIam S i n  g  l  e  q  u  o  t  e  s  S  t  r  i  n  g  s'
### Index 01234567 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26

### Len()
print("Length of str1: ",len(str1))
 
### substrings
print("am" in str1) ### return bool (if "am" is present in str1)
print("Bye" in str0,"\n")

### starts with
print(str1.startswith("I"))
print(str1.endswith("s")) ### Case sensitive 's' & 'S'
print(str1.index("World")) ### prints 1st char index only

###Upper/Lower Case
print(str1.upper())
print(str1.lower())

### Ex - if fetched a password and needs to remove spaces
### strip()
mypass = "   My Secret Password    "
print(mypass)
print(mypass.strip())

### Replace 
### Replace any char with another
mypass = "   My Secret Password    !@###$%^&**()-+    "
print(mypass)
print(mypass.replace("!@###$%^&**()-+","").strip())
print(mypass.replace("Password","PassCode").strip())

### Split
mypass = "   My Secret Password    "
print(mypass.split(","))
print(mypass.split()) ### Splits every word

### Encode 
str1 = "I am String"
print(str1.encode())

### Rjust & Ljust (used in exploit dev)
print(str1.rjust(20))
print(str1.rjust(25,"X"))
print(str1.ljust(20))
print(str1.ljust(25,"X"))

### Concat
### + : Overloaded Operator
print(str1 +" + "+ str0+ " Length: "+str(len(str1)))

print(type("1"+"1"))

### String Formater
a = "Michael"
print("This is Hello for {}".format(a))
print("Formated Sequence: This is Hello for {4} {3} {2} {1} {0}".format(a,1,2,3,4))
print("{l1} is the size of str0".format(l1=len(str0)))

### f - defines format string
str1_len = len(str1)
print(f"str1 has length of : {str1_len}")
print(f"str1 has length of in float: {str1_len:.2f}") ### float
print(f"str1 has length of in Bin: {str1_len:b}") ### in bin
print(f"str1 has length of in Octal: {str1_len:o}") ### in octal
print(f"str1 has length of in Hexa: {str1_len:x}") ### in Hexadecimal

print("String str1 is %d char long!"% len(str1))
print("String str1 is %x char long!"% len(str1))
print("String str1 is %f char long!"% len(str1))
