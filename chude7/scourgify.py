import csv
import sys


def main():
    # 1. Kiểm tra số lượng đối số dòng lệnh
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    students = []

    # 2. Đọc tệp CSV đầu vào
    try:
        with open(input_file, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Cột "name" có dạng "Last, First" -> split để tách Last và First
                last, first = row["name"].split(", ")
                students.append(
                    {
                        "first": first,
                        "last": last,
                        "house": row["house"],
                    }
                )
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

    # 3. Ghi dữ liệu đã làm sạch ra tệp CSV đầu ra
    with open(output_file, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        # Ghi hàng tiêu đề (first, last, house)
        writer.writeheader()
        # Ghi toàn bộ dữ liệu sinh viên
        writer.writerows(students)


if __name__ == "__main__":
    main()