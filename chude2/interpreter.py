# Nhập biểu thức toán học
expression = input("Expression: ").strip()

# Tách biểu thức thành 3 phần x, y, z dựa vào khoảng trắng
x, y, z = expression.split(" ")

# Đổi x và z từ chuỗi chữ sang số thực (float)
x = float(x)
z = float(z)

# Thực hiện phép tính theo dấu y
if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z

# In kết quả (luôn lấy 1 chữ số thập phân)
print(f"{result:.1f}")