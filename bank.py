user = input("Greeting: ").strip().lower()

if user.startswith("hello"):
    print("$0")
elif user.startswith("h") and not user.startswith("hello"):
    print("$20")
else: 
    print("$100")

#if user.startswith("hello"): Checks if the input starts with "hello"
#elif user.startswith("h") and not user.startswith("hello"): Checks if the input starts with "h" but not "hello".
#else: Handles all other cases.
#strip(): Removes any leading and trailing whitespace
#lower(): Converts the input to lowercase to ensure case-insensitivity.
