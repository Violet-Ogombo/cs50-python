answer= (
    input(
        "What is the answer to the Great questioN  of Life, the Universe, and Everything?  "
    )
    .strip() #removes any leading and trailing spaces.
    .lower() #converts the input to lowercase.
)
if answer in {"42", "Forty two", "forty-two"}:
    print("Yes")
else:
    print("No")
