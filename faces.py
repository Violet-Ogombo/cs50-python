def convert(input):
    #Convert emoticons in the text to their corresponding emoji.

    #Args:input_text (str): The input string containing emoticons.

    #Returns:str: The string with emoticons converted to emoji.

    input = input.replace(':)', '🙂')
    input = input.replace(':(', '🙁')
    return input

def main():

    #Prompt the user for input, convert emoticons to emoji, and print the result.

    user_text = input("Type emoticon: ")
    converted_input = convert(user_text)
    print(converted_input)

if __name__ == "__main__":
    main()
