

text = input("Input: ")

print("Output: ",end="")

# Danh sách các nguyên âm
vowels = "aeiouAEIOU"

# Duyệt từng ký tự trong văn bản
for char in text:
    # Nếu ký tự KHÔNG nằm trong danh sách nguyên âm thì in ra
    if char not in vowels:
        print(char, end="")

