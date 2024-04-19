[12:25 pm, 09/02/2024] Blen K: f strings
[12:25 pm, 09/02/2024] Blen K: name = input("whats your name? ")
print(f"Hello, {name}! 319 x 76 is {319*76}!")
[12:25 pm, 09/02/2024] Blen K: string methods
[12:25 pm, 09/02/2024] Blen K: text = "abcdefghijklmnop"
print(dir(text))
help(text.isupper)
print(text.isupper()) # is the text all uppercase?
print("ABC".isupper()) # is the text all uppercase?
print(text.upper()) # convert the text to uppercase
print(text.upper().isupper()) # is the text all uppercase? yes

new_text = text.upper()
print(text, new_text)
print("bannannnana". count("n"))
print("banabababnan".index("ana"))
print("banababanabnana".replace("ana", "XXYYZZ"))
sentence = "Hello, kind-sir; how many! I be of service today?"
print(sentence.replace(",","").replace(";","").replace"!", "").replace("-", "").replace


# elegant way to do it
punctuation = ".,;!?-"
for p in punctuation:
    sentence = sentence.replace(p, "")
print(sentence)

print("this is a sentence and I want the words".split(" "))

text = "Bob goes to school. Bob like to play tennis. I am friends with Bob. Such a nice guy Bob is."
print(text.find("Bob"))
print(text.rfind("Bob"))
# find all the positions of bob
i=0
while i < len(text):
    i = text.find("Bob", i)
    if i == -1:
        break
    print(i)
    i += 1

    [11: 37
    am, 20 / 02 / 2024] Cathrine
    Bakken: file_name = "x-file.txt"
    fd = open(file_name, "a")
    while True:
        line = input("Enter a line (or just press Enter to quit): ")
        if line:
            fd.write(line + "\n")
        else:
            break

    fd.close()
    [11: 37
    am, 20 / 02 / 2024] Cathrine
    Bakken: file_name = "x-file.txt"
    fd = open(file_name)  # r is inplicit
    print("here are the contents of the file:")

    for line in fd:
        #  print(line, end="")
        #  print(line.strip())
        print(line.replace("\n", ""))
    fd.close()

    #  fd = open(file_name)
    with open(file_name) as fd:
        print("Here are the 3 letter words!")
        for line in fd:
            words = line.split()
            for word in words:
                if len(word) == 3:
                    print(word)
    #  fd.close()