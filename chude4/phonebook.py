phonebook = {}

while True:
    print("\n--- DANH BẠ ---")
    print("1. Thêm")
    print("2. Tìm kiếm")
    print("3. Xóa")
    print("4. Sửa")
    print("5. Thoát")
    
    choice = input("Chọn chức năng: ")
    
    if choice == "1":
        name = input("Nhập tên: ")
        phone = input("Nhập số điện thoại: ")
        phonebook[name] = phone
        print("Đã thêm!")
        
    elif choice == "2":
        name = input("Nhập tên cần tìm: ")
        if name in phonebook:
            print(f"Số điện thoại của {name}: {phonebook[name]}")
        else:
            print("Không tìm thấy.")
            
    elif choice == "3":
        name = input("Nhập tên cần xóa: ")
        if name in phonebook:
            del phonebook[name]
            print("Đã xóa!")
        else:
            print("Không tìm thấy.")
            
    elif choice == "4":
        name = input("Nhập tên cần sửa: ")
        if name in phonebook:
            new_phone = input("Nhập số điện thoại mới: ")
            phonebook[name] = new_phone
            print("Đã sửa!")
        else:
            print("Không tìm thấy.")
            
    elif choice == "5":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ.")