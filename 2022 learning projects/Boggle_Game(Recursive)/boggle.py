"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
DICTIONARY = []


def main():
    """
    TODO:
    """
    start = time.time()
    ####################
    #                  #
    #       TODO:      #
    #                  #
    ####################
    read_dictionary()
    words = []
    row1 = input("1 row of letters: ").lower()
    if len(row1.split()) == 4:
        words.append(row1.split())
    else:
        print('Illegal input')
        return
    row2 = input("2 row of letters: ").lower()
    if len(row2.split()) == 4:
        words.append(row2.split())
    else:
        print('Illegal input')
        return
    row3 = input("3 row of letters: ").lower()
    if len(row3.split()) == 4:
        words.append(row3.split())
    else:
        print('Illegal input')
        return
    row4 = input("4 row of letters: ").lower()
    if len(row4.split()) == 4:
        words.append(row4.split())
    else:
        print('Illegal input')
        return
    # print(words)
    lst = []
    for i in range(4):
        for j in range(len(words)):
            find_words(words, i, j, '', lst, [])
            # lst.append(ans_str)
    print(lst)
    print('There are', len(lst), 'words in total')
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_words(words, row, col, cur_str, ans_list, path):
    cur_str = cur_str + words[row][col]
    if [row, col] in path:
        return
    else:
        path.append([row, col])
        # print('path:', path, cur_str)
        if len(cur_str) >= 4:
            if cur_str in DICTIONARY:
                if cur_str not in ans_list:
                    print("Found:", cur_str, "at", row, col)
                    ans_list.append(cur_str)
                    # print(ans_list)

        if has_prefix(cur_str):
            if row < 3:
                find_words(words, row + 1, col, cur_str, ans_list, path)
            if col < 3:
                find_words(words, row, col + 1, cur_str, ans_list, path)
            if col < 3 and row < 3:
                find_words(words, row + 1, col + 1, cur_str, ans_list, path)
            if row > 0:
                find_words(words, row - 1, col, cur_str, ans_list, path)
            if row > 0 and col < 3:
                find_words(words, row - 1, col + 1, cur_str, ans_list, path)
            if col > 0:
                find_words(words, row, col - 1, cur_str, ans_list, path)
            if col > 0 and row < 3:
                find_words(words, row + 1, col - 1, cur_str, ans_list, path)
            if col > 0 and row > 0:
                find_words(words, row - 1, col - 1, cur_str, ans_list, path)
            path.pop()
        else:
            path.pop()
            return


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    with open(FILE, 'r') as f:
        for line in f:
            if len(line) >= 4:
                DICTIONARY.append(line.strip())


def has_prefix(sub_s):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for ele in DICTIONARY:
        if ele.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
