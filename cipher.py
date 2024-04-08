alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
sentence = input("Input the string you wish to encrypt").lower()
shift = int(input("Please enter your shift: "))
new_string = ""

for item in sentence:
    if item != " ":
        spot = alphabet.index(item)
        encrypt = (spot + shift) % len(alphabet)
        new_string = new_string + alphabet[encrypt]
    else:
        new_string = new_string + item
print(new_string)
