t1_int = 1
t1_float = 1.1

print("t1_int: ",t1_int)
print("t1_float: ",t1_float)
print(type(t1_int))
print(type(t1_float))

### Complex Numbers
t1_complex = 3.14j
print("t1_complex: ",t1_complex)
print(type(t1_complex))

### Hexadecimal Numbers - Shellcodes
t1_hexa = 0xa
print("t1_hexa: ",t1_hexa )
print(type(t1_hexa))

t1_octal = 0o10
print("t1_octal: ",t1_octal)
print(type(t1_octal))

### Addition

### Decimal 1 + Hexa 1 + octal 1 = 3 (int)
print(1+0x1+0o1)
print(type(1+0x1+0o1))

### Built-in function
 
### Absolute funtion
print(abs(4))
print(abs(-4))

### Round Function
print(round(8.1))
print(round(8.5))
print(round(8.6))

### Binary Function
print(bin(8))
print(bin(10))

### Hexa Function
print(hex(8))