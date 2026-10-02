#Nhắc người dùng trả lời câu hỏi và đổi tất cả thành chữ thường và xóa khoảng trắng dư thừa
answer = input("What is the answer to the Great Question of Life, the Universe,and Everything ").strip().lower()
# kiểm tra câu trả lời 
if answer =="42" or answer =="forty-two " or answer == "forty two":
    print("Yes")
else:
    print("No")