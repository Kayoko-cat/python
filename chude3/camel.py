# camel.py

# Nhập tên biến ở dạng camelCase
camel = input("camelCase: ")

print("snake_case: ", end="")


for char in camel:
    # Nếu ký tự là chữ in hoa
    if char.isupper():
        # In ra dấu gạch dưới và chữ đó ở dạng in thường
        print("_" + char.lower(), end="")
    else:
        # Nếu là chữ in thường thì in ra bình thường
        print(char, end="")


print()