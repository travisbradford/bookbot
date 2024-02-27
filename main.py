def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = count_words(text)
    letters = count_letters(text)
    #print(text)
    #print(count)
    #print(letters)
    make_report(count, letters, book_path)

    
def make_report(count, letters, book_path):
    list_of_dicts = []
    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words found in the document")
    for char, frequency in letters.items(): 
        if char.isalpha():
            list_of_dicts.append({'char': char, 'frequency': frequency})
    
    def sort_on(item):
        return item['frequency']
    sorted_list_of_dicts = sorted(list_of_dicts, key=sort_on, reverse=True)
    
    for item in sorted_list_of_dicts:
        print(f"The '{item['char']}' character was found {item['frequency']} times.")

    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    word_count = 0
    words = text.split()
    for word in words:
        word_count += 1
    return word_count 

def count_letters(text):
    letters = {}
    lwr = text.lower()
    for letter in lwr:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    
    return letters


main()

