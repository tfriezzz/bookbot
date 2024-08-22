def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    file_words = file_contents.split()
    word_count = len(file_words)
    character_count = file_contents.lower()
    letter_count = {}


    for letter in character_count:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1


    print(word_count)
    print(letter_count)


main()
