import math

def print_menu():
    print("\n========== Scientific Calculator ==========")
    print(" 1. Addition         (a + b)")
    print(" 2. Subtraction      (a - b)")
    print(" 3. Multiplication   (a * b)")
    print(" 4. Division         (a / b)")
    print(" 5. Power            (a ^ b)")
    print(" 6. Square Root      (√a)")
    print(" 7. Sine             (sin a)  [degrees]")
    print(" 8. Cosine           (cos a)  [degrees]")
    print(" 9. Tangent          (tan a)  [degrees]")
    print("10. Logarithm base10 (log a)")
    print("11. Natural Log      (ln a)")
    print("12. Absolute Value   (|a|)")
    print(" 0. Exit")
    print("===========================================")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a number.")

def calculate():
    print("🧮 Welcome to Scientific Calculator (Python Version)")

    while True:
        print_menu()
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("❌ Invalid choice! Enter a number.")
            continue

        if choice == 0:
            print("👋 Goodbye!")
            break

        # Two input operations
        if 1 <= choice <= 5:
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
        elif 6 <= choice <= 12:
            a = get_number("Enter number: ")

        if choice == 1:
            print(f"✅ Result: {a} + {b} = {a + b}")

        elif choice == 2:
            print(f"✅ Result: {a} - {b} = {a - b}")

        elif choice == 3:
            print(f"✅ Result: {a} * {b} = {a * b}")

        elif choice == 4:
            if b == 0:
                print("❌ Error: Division by zero!")
            else:
                print(f"✅ Result: {a} / {b} = {a / b}")

        elif choice == 5:
            print(f"✅ Result: {a} ^ {b} = {a ** b}")

        elif choice == 6:
            if a < 0:
                print("❌ Error: Square root of negative number!")
            else:
                print(f"✅ Result: √{a} = {math.sqrt(a)}")

        elif choice == 7:
            print(f"✅ Result: sin({a}°) = {math.sin(math.radians(a)):.4f}")

        elif choice == 8:
            print(f"✅ Result: cos({a}°) = {math.cos(math.radians(a)):.4f}")

        elif choice == 9:
            print(f"✅ Result: tan({a}°) = {math.tan(math.radians(a)):.4f}")

        elif choice == 10:
            if a <= 0:
                print("❌ Error: log of non-positive number!")
            else:
                print(f"✅ Result: log({a}) = {math.log10(a):.4f}")

        elif choice == 11:
            if a <= 0:
                print("❌ Error: ln of non-positive number!")
            else:
                print(f"✅ Result: ln({a}) = {math.log(a):.4f}")

        elif choice == 12:
            print(f"✅ Result: |{a}| = {abs(a)}")

        else:
            print("❌ Invalid choice! Try again.")

if __name__ == "__main__":
    calculate()
