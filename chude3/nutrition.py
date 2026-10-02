

# Danh sách tên trái cây
fruits = [
    "apple", "avocado", "banana", "cantaloupe", "grapefruit", 
    "grapes", "honeydew melon", "kiwifruit", "lemon", "lime", 
    "nectarine", "orange", "peach", "pear", "pineapple", 
    "plums", "strawberries", "sweet cherries", "tangerine", "watermelon"
]

# Danh sách calo tương ứng theo đúng vị trí (chỉ số)
calories = [
    130, 50, 110, 50, 60, 
    90, 50, 90, 15, 20, 
    60, 80, 60, 100, 50, 
    70, 50, 100, 50, 80
]


item = input("Item: ").strip().lower()

# Nếu trái cây có trong danh sách fruits
if item in fruits:
    # Tìm vị trí (index) của trái cây đó
    index = fruits.index(item)
    # Lấy calo ở vị trí tương ứng
    print(f"Calories: {calories[index]}")