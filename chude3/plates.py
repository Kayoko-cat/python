def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # 1. Kiểm tra độ dài (từ 2 đến 6 ký tự)
    if len(s) < 2 or len(s) > 6:
        return False

    # 2. Hai ký tự đầu tiên phải là chữ cái
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # 3. Không chứa ký tự đặc biệt hay khoảng trắng (chỉ chứa chữ và số)
    if not s.isalnum():
        return False

    # 4. Kiểm tra vị trí số và số 0 ở đầu
    letters = ""
    digits = ""

    # Tách chữ và số ra hai biến riêng
    for char in s:
        if char.isalpha():
            letters += char
        else:
            digits += char

    # Nếu có chứa số trong biển số
    if len(digits) > 0:
        # Số đầu tiên xuất hiện không được là '0'
        if digits[0] == '0':
            return False

        # Bắt buộc toàn bộ chữ phải nằm trước, toàn bộ số phải nằm sau
        if letters + digits != s:
            return False

    return True

main()