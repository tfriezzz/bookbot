def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    file_words = file_contents.split()
    word_count = len(file_words)
    character_count = file_contents.lower()
    letter_count = {}


    for letter in character_count:
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1


    dictionary_list = list(letter_count.items())

    sorted_list = sorted(dictionary_list, key=lambda letter: letter[1], reverse=True)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    for letter, count in sorted_list:
       print(f"The {letter} character was found {count} times")
    print("--- End report ---")


        

main()
