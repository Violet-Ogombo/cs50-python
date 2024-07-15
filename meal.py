def main():
    # Prompt the user for input
    time = input("What's the time? ")
    # Convert the time to hours
    hours_float = convert(time)
    
    # Determine and print the meal time
    if 7.0 <= hours_float <= 8.0:
        print("Breakfast time")
    elif 12.0 <= hours_float <= 13.0:
        print("Lunch time")
    elif 18.0 <= hours_float <= 19.0:
        print("Dinner time")

def convert(time):
    """Converts a time string in 24-hour format to hours as a float."""
    # Split the time string into hours and minutes
    hours, minutes = map(int, time.split(":"))
    # Calculate the total number of hours
    total_hours = hours + minutes / 60.0
    return total_hours

if __name__ == "__main__":
    main()
