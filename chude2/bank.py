# nhắc người dùng nhập lời chào và đưa chữ hoa về chữ thường rồi xóa khoảng trắng
greeting = input ("Greeting: ").lower().strip()

#kiểm tra các điều kiện
if greeting[0:5]=="hello":
    print("$0")
elif greeting[0]=="h":
    print("$20")
else:
    print("$100")