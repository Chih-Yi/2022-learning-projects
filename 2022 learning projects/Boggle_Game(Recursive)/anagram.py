"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop
DICTIONARY = []


def main():
    """
    TODO:
    """
    ####################
    #                  #
    #       TODO:      #
    #                  #
    ####################
    print("Welcome to stanCode \"Anagram Generator\" (or -1 to quit)")
    global DICTIONARY
    DICTIONARY = read_dictionary()
    while True:
        start = time.time()
        word = input("Find anagrams for: ")
        if word == EXIT:
            break
        else:
            print('Searching...')
            lst = find_anagrams(word)
            print(len(lst), 'anagrams:', lst)
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    word_list = []
    with open(FILE, 'r') as f:
        for line in f:
            word_list.append(line.strip())
    return word_list


def find_anagrams(s):
    lst = find_anagrams_helper(s, '', [], [])
    return lst


def find_anagrams_helper(s, ans_str, index_list, ans_list):
    """
    :param index_list: word location for duplicated words
    :param ans_list: final answer
    :param ans_str: for one anagram
    :param s: original word
    :return:
    """
    if len(index_list) == len(s):
        for i in index_list:
            ans_str = ans_str + s[int(i)]
        if ans_str in DICTIONARY:
            if ans_str not in ans_list:
                ans_list.append(ans_str)
                # print(index_list)
                print('Found:', ans_str)
                print('Searching...')
        return
    else:
        for i in range(len(s)):
            sub_str = ''
            for j in index_list:
                sub_str = sub_str + s[int(j)]
            # print(sub_str, has_prefix(sub_str))
            if has_prefix(sub_str):
                if i not in index_list:
                    find_anagrams_helper(s, ans_str, index_list + [i], ans_list)
            else:
                return
        return ans_list


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    for word in DICTIONARY:
        if word.startswith(str(sub_s)):
            return True
    return False


if __name__ == '__main__':
    main()
