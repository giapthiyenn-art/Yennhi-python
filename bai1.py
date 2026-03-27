a = 16
b = 3
c = 5

print("=== PHÉP TOÁN SỐ HỌC ===")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a ** b =", a ** b)

print("\n=== TOÁN TỬ SO SÁNH ===")
print("a > b:", a > b)
print("a < b:", a < b)
print("a == b:", a == b)
print("a != b:", a != b)

print("\n=== TOÁN TỬ GÁN ===")
x = a
x += b
print("x += b:", x)

x = a
x *= b
print("x *= b:", x)

x = a
x /= b
print("x /= b:", x)

print("\n=== TOÁN TỬ LOGIC ===")
print("(a > b) and (b < c):", (a > b) and (b < c))
print("(a > b) or (b > c):", (a > b) or (b > c))
print("not(a > b):", not(a > b))

print("\n=== TOÁN TỬ BIT ===")
print("a & b =", a & b)   
print("a | b =", a | b)   
print("~a =", ~a)        
print("a ^ b =", a ^ b)   
print("a << 3 =", a << 3) 
print("a >> 2 =", a >> 2) 