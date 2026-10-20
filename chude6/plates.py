def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Độ dài từ 2 đến 6 ký tự
    if not (2 <= len(s) <= 6):
        return False

    # Hai ký tự đầu tiên phải là chữ cái
    if not s[:2].isalpha():
        return False

    # Không được có dấu chấm, khoảng trắng...
    if not s.isalnum():
        return False

    # Nếu có số thì các số phải nằm ở cuối
    for i, char in enumerate(s):
        if char.isdigit():
            # Số đầu tiên không được là 0
            if char == "0":
                return False

            # Tất cả ký tự sau đó phải là số
            if not s[i:].isdigit():
                return False

            break

    return True


if __name__ == "__main__":
    main()