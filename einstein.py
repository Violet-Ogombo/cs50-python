def energy_calculation(m):
    c = 300000000  # Speed of light in meters per second
    return m * (c ** 2)  # Use ** for exponentiation
   
def main():
    m = int(input("Type m: "))  # Input mass from the user
    E = energy_calculation(m)  # Calculate energy
    print(f"The energy equivalent of mass is {E} joules.")  # Print the result

if __name__ == "__main__":
    main()  # Call the main function
