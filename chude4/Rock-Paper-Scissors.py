import random

# Danh sách lựa chọn
options = ["rock", "paper", "scissors"]
user_wins = 0
computer_wins = 0

while user_wins < 3 and computer_wins < 3:
    print(f"\nĐiểm số - Bạn: {user_wins} | Máy: {computer_wins}")
    user_choice = input("Chọn (rock, paper, scissors): ").lower()
    
    if user_choice not in options:
        print("Lựa chọn không hợp lệ, nhập lại.")
        continue
        
    computer_choice = random.choice(options)
    print(f"Máy chọn: {computer_choice}")
    
    if user_choice == computer_choice:
        print("Hòa!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("Bạn thắng ván này!")
        user_wins += 1
    else:
        print("Máy thắng ván này!")
        computer_wins += 1

if user_wins == 3:
    print("\nBạn là người chiến thắng chung cuộc!")
else:
    print("\nMáy là người chiến thắng chung cuộc!")