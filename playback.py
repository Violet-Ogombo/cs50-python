def main():
    user_input = input("please type a text: ")
    new_text= replace_space_with_periods
    print (new_text(user_input))

def replace_space_with_periods(user_input):
    return user_input.replace(' ', '...')

main()
