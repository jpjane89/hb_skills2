string1 = "I do not like green eggs and ham."
list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "San", "I", "am"]

"""
Write a function that takes a string and produces a dictionary with
all distinct elements as the keys, and the number of each element as
the value
Bonus: do the same for a file (i.e. twain.txt)
"""
def count_unique(string1):

    count_dict = {}

    words = string1.split(" ")

    for word in words:
        word = word.strip(",.")
        if word not in count_dict:
            count_dict[word] = 1
        else:
            count_dict[word] += 1
    
    return count_dict
"""
Given two lists, (without using the keyword 'in' or the method 'index')
return a list of all common items shared between both lists
"""
def common_items(list1, list2):

    common_items = []

    for num in list1:
        for num2 in list2:
            if num == num2 and num not in common_items:
                common_items.append(num)

    return common_items

"""
Given two lists, (without using the keyword 'in' or the method 'index')
return a list of all common items shared between both lists. This time,
use a dictionary as part of your solution.
"""
def common_items2(list1, list2):
    
    common_items = {}

    combined_lists = list1.extend(list2)

    for num in combined_lists:
        common_items[num] = common_items.get(num, 0) + 1

    return common_items.keys()

"""
Given a list of numbers, return list of number pairs that sum to zero
"""
def sum_zero(list1):

    zero_combos = []

    for num in list1:
        neg_num = -1*num
        if neg_num in list1:
            zero_combos.append((num, neg_num))

    return zero_combos

def sum_zero_no_dup(list1):

    zero_combos = {}

    for num in list1:
        neg_num = -1*num
        if neg_num in list1 and num not in zero_combos.values():
            zero_combos[num] = neg_num

    return zero_combos.items()

"""
Given a list of words, return a list of words with duplicates removed
"""
def find_duplicates(words):

    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    no_dups = word_count.keys()

    return no_dups

"""
Given a list of words, print the words in ascending order of length
Bonus: do it on a file instead of the list provided
Bonus: print the words in alphabetical order in ascending order of length
"""
def word_length(words):
    
    word_length_dict = {}

    for word in words:
        length = len(word)
        word_length_dict[length] = word_length_dict.get(length, []) + [word]
    
    lengths = word_length_dict.keys()
    lengths.sort()

    for length in lengths:
        word_length_dict[length].sort()
        for word in word_length_dict[length]:
            print word

"""
Here's a table of English to Pirate translations
English     Pirate

sir         matey
hotel       fleabag inn
student     swabbie
boy         matey
madam       proud beauty
professor   foul blaggart
restaurant  galley
your        yer
excuse      arr
students    swabbies
are         be
lawyer      foul blaggart
the         th'
restroom    head
my          me
hello       avast
is          be
man         matey

Write a program that asks the user to type in a sentence and then
print the sentece translated to pirate.
"""

def make_trans_lists(filename):

    word_pairs = {}

    my_file = open(filename)

    for line in my_file:
        line = line.strip()
        words = line.split()
        word_pairs[words[0]] = words[1]

    for word in word_pairs:
        word_pairs[word] = word_pairs[word].replace("-"," ")

    return word_pairs

def main():

    word_pairs = make_trans_lists("pirate_trans.txt")

    input_sentence = raw_input("Type in a sentence for me to translate to Pirate-speak>> ")

    input_words = input_sentence.split(" ")

    translation_words = []

    for word in input_words:
        word = word.strip(".,!?:;()")
        translation = word_pairs.get(word, word)
        translation_words.append(translation)

    translated_text = " ".join(translation_words)

    print translated_text

if __name__ == "__main__":
    main()