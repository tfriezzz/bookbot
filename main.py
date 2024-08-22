def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    file_words = file_contents.split()
    word_count = len(file_words)
    character_count = file_contents.lower()

    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]



    print(word_count)

main()
