def main():
    while True:
        fraction = input("Fraction: ")
        try:
            parts = fraction.split("/")
            if len(parts) != 2:
                continue
            x = int(parts[0])
            y = int(parts[1])
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                continue
            percentage = round((x / y) * 100)
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break
        except (ValueError, ZeroDivisionError):
            pass

if __name__ == "__main__":
    main()