# counts number of words in a text
def count_num_words(text):
    number_of_words = text.split()
    return len(number_of_words)

# turns the uppercase letters to lowercase, then counts the number of each spesific letter
#text = "This text has Lower case and Upper Case Letters, and many many more that we all need to be aware of especially z"
def lower_and_count_letters(text):
    small_letters = text.lower()
    word_count = {}
    for i in small_letters:
        if i not in word_count:
            word_count[i] = 0
        if i in word_count:
            word_count[i] += 1
    return word_count

this_dic = {'t': 29493, 'h': 19176, 'e': 44538, ' ': 70480, 'p': 5952, 'r': 20079, 'o': 24494, 'j': 497, 'c': 9011, 'g': 5795, 'u': 10111, 'n': 23643, 'b': 4868, 'k': 1661, 'f': 8451, 'a': 25894, 's': 20360, 'i': 23927, ';': 1350, ',': 5962, 'm': 10206, 'd': 16318, '\n': 7630, 'y': 7756, 'w': 7450, 'l': 12306, 'v': 3737, '.': 3121, '-': 173, ':': 211, '2': 19, '3': 15, '0': 18, '1': 91, '[': 2, '#': 1, '4': 12, '5': 12, ']': 2, '&': 5, '8': 24, '/': 8, '*': 97, '’': 144, 'x': 691, '_': 124, 'q': 325, '?': 208, '—': 123, '6': 9, 'z': 235, '(': 35, ')': 35, '7': 18, 'æ': 28, '!': 201, '“': 506, '”': 316, '9': 9, 'ë': 2, '‘': 43, 'â': 8, 'ê': 7, 'ô': 1, '™': 57, '•': 4, '%': 1, '$': 2}
"""a_list_of_dictionaries = []
for letter in this_dic:
    value = this_dic[letter]
    a_list_of_dictionaries.append({"char": letter, "num": value})
a_list_of_dictionaries.sort(reverse=True, key=sort_on)
print(a_list_of_dictionaries)"""
    
def sorted_dictionary(a_dictionary):
    def sort_on(item):
        return item["num"]
    
    a_list_of_dictionaries = []

    for letter in a_dictionary:
        value = a_dictionary[letter]
        a_list_of_dictionaries.append({"char": letter, "num": value})
    a_list_of_dictionaries.sort(reverse=True, key=sort_on)
    only_letters_dict = []

    #the rest of this should be a used in main instead because the function i wanted is above.
    #in main i could write a loop to make use of the above function instead, like below
    for i in a_list_of_dictionaries:
        if i["char"].isalpha() == False:
            continue
        else: #This is utterly useless
            only_letters_dict.append(i) #Does nothing
    for i in only_letters_dict:
        print(f"{i["char"]}: {i["num"]}")