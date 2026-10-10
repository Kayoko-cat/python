months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def main():
    while True:
        date_input = input("Date: ").strip()
        
        # Trường hợp 1: Định dạng MM/DD/YYYY
        if "/" in date_input:
            parts = date_input.split("/")
            if len(parts) != 3:
                continue
            try:
                month = int(parts[0])
                day = int(parts[1])
                year = int(parts[2])
            except ValueError:
                continue
                
        # Trường hợp 2: Định dạng Month DD, YYYY
        elif "," in date_input:
            parts = date_input.split(",")
            if len(parts) != 2:
                continue
            left_part = parts[0].strip().split()
            if len(left_part) != 2:
                continue
            month_str = left_part[0]
            try:
                day = int(left_part[1])
                year = int(parts[1].strip())
                if month_str not in months:
                    continue
                month = months.index(month_str) + 1
            except ValueError:
                continue
        else:
            continue
            
        # Kiểm tra tính hợp lệ của ngày và tháng
        if 1 <= month <= 12 and 1 <= day <= 31:
            print(f"{year:04d}-{month:02d}-{day:02d}")
            break

if __name__ == "__main__":
    main()