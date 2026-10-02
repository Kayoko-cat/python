def convert(time):
    # Tách giờ và phút bằng dấu ":"
    hours, minutes = time.split(":")
    
    # Đổi phút sang dạng thập phân của giờ 
    hours = float(hours)
    minutes = float(minutes)
    
    return hours + (minutes / 60)

def main():
    time_input = input("What time is it? ")
    
    # Gọi hàm convert để đổi thời gian nhập vào thành dạng số
    time = convert(time_input.strip())
    
    # Kiểm tra các khoảng thời
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")
    else :
        print("free time")

if __name__ == "__main__":
    main()