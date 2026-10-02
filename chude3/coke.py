

amount_due = 50

# Lặp lại cho đến khi trả đủ tiền 
while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    
    # Nhập đồng xu
    coin = int(input("Insert Coin: "))
    
    # Chỉ xử lý các mệnh giá hợp lệ: 25, 10, 5
    if coin == 25 or coin == 10 or coin == 5:
        amount_due = amount_due - coin

# In số tiền thối lại (trị tuyệt đối của amount_due khi âm)
print(f"Change Owed: {abs(amount_due)}")