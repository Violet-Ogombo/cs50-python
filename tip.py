#Call dollars_to_float and percentage_to_float.
#Calculate the tip and print the result formatted to two decimal places
def main ():
    dollars= dollars_to_float(input("How much was the meal? "))
    percent= percentage_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"leave ${tip:.2f}")

def dollars_to_float(d):
    # Remove the leading strip '$' and convert the remaining string to a float
    return float(d.lstrip('$'))

def percentage_to_float(p):
    # Remove the trailing strip '%' and convert the remaining string to a float
    return float(p.rstrip('%')) / 100

if __name__ == "__main__":
    main()
