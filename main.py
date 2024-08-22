def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    file_words = file_contents.split()
    word_count = len(file_words)
    print(word_count)

main()
