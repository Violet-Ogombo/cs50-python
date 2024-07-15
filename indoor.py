def main():
    #prompts the user for some text
    text = input("Type some text: ")
    print(lowercase_output(text))

#converting the user input to lowercase
def lowercase_output(text):
#lower() method is called and returns the lowercase of the text string
    return text.lower()

main()
