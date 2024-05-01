def main():
    story()

def story():
    while True:
        try:
            name = input("What is the character name? ")
            age = int(input("What is the age of the character? "))
        except ValueError:
            print("Please write only a number")
            break

        print(f"Hi, I'm {name} and I'm {age} years old.")

if __name__ == "__main__":
    main()