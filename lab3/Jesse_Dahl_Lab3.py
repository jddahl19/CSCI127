#THIS IS THE FINISHED LAB

# --------------------------------------
# CSCI 127, Lab 3
# September 18, 2018
# Jesse Dahl
# --------------------------------------

def count_vowels(sentence):
    a = sentence.count("a")
    e = sentence.count("e")
    i = sentence.count("i")
    o = sentence.count("o")
    u = sentence.count("u")

    total_vowels = (a+e+i+o+u)
    return(total_vowels)

def count_vowels_iterative(sentence):
    total_vowels = 0
    vowels = ['a', 'e', 'i', 'o', 'u']

    for i in sentence:
        if i in vowels:
            total_vowels += 1
    return(total_vowels)


def remove_iterative(sentence):
    white_space = " "
    for i in sentence:
        if white_space in sentence:
            sentence = sentence.replace(white_space, "")
    return(sentence)


# --------------------------------------

def main():
    answer = "yes"
    while (answer == "yes") or (answer == "y"):
        sentence = input("Please enter a sentence to evaluate: ")
        sentence = sentence.lower()     # convert to lowercase
        print()
        print("Number of vowels using count     =", count_vowels(sentence))
        print("Number of vowels using iteration =", count_vowels_iterative(sentence))
        print("Using iteration = |" + remove_iterative(sentence) + "|")
        print()
        answer = input("Would you like to continue: ").lower()
        print()

# --------------------------------------

main()
