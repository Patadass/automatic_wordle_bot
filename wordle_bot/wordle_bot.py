import random
from scraper import open_web
from scraper import type_word
from scraper import color_scraper


# x=585 y=774

def get_dictionary_of_allowed_words():
    dictionary = []
    with open('wordle-La.txt', 'r') as f:
        for line in f:
            dictionary.append(line.rstrip('\n'))
        f.close()
    return dictionary


def get_starting_word(what_wordle):
    word = random.choice(get_dictionary_of_allowed_words())
    type_word(word, what_wordle)
    return word


def get_letter_color(word, row, what_wordle):
    print(word)
    letter_color = color_scraper(row, what_wordle)
    print(letter_color)
    return letter_color.upper()


def get_not_letters(letter_color, word):
    # get the letters that are not in the word in not_letters and not_letters_pos
    # TODO:not_letters_pos is not used anywhere so far
    not_letters = []
    not_letters_pos = []
    i = 0
    can_skip = False
    for color in letter_color:
        if color == 'Y' or color == 'G':  # if the letter is green of yellow just skip
            i += 1
            continue

        j = 0
        for letter in word:
            # if it isn't we check if the same letter appears again in the word and check if that on is G or Y
            if letter == word[i]:
                if letter_color[j] == 'Y' or letter_color[j] == 'G':
                    can_skip = True
            j += 1

        if can_skip:
            can_skip = False
            i += 1
            continue

        if color == 'N':  # this if statement might be useless if we get to here I think color must be N
            not_letters.append(word[i])
            not_letters_pos.append(i)
        i += 1
    return not_letters, not_letters_pos


def check_for_not_letters(not_letters, word):
    for letter in word:
        if letter in not_letters:
            return True
    return False


def word_checking_algorithm(letter_color, word, old_word):
    i = 0
    can_skip = False
    for color in letter_color:
        if color == 'N':
            i += 1
            continue
        if color == 'G':
            if word[i] != old_word[i]:
                can_skip = True
                break
        if color == 'Y':
            has_letter = False
            if word[i] != old_word[i]:
                if old_word[i] in word:
                    has_letter = True
            else:
                can_skip = True
                break
            if not has_letter:
                can_skip = True
                break
        i += 1
    return can_skip


def wordle_bot(dictionary, word, what_wordle):
    row = 0
    letter_color = get_letter_color(word, row, what_wordle)
    row += 1
    old_word = word
    not_letters, not_letters_pos = get_not_letters(letter_color, word)
    i = 0
    counter_for_over = 0
    for word in dictionary:
        if check_for_not_letters(not_letters, word):
            i += 1
            continue
        if word_checking_algorithm(letter_color, word, old_word):
            i += 1
            continue
        counter_for_over += 1
        if counter_for_over > 5:
            counter_for_over -= 1
            break

        old_word = word
        type_word(word, what_wordle)
        letter_color = get_letter_color(word, row, what_wordle)
        row += 1
        is_over = True
        for color in letter_color:
            if color != 'G':
                is_over = False
                break
        if is_over:
            break
        not_letters, not_letters_pos = get_not_letters(letter_color, word)
        i += 1


def main():
    what_wordle = 2
    open_web(what_wordle)
    wordle_bot(get_dictionary_of_allowed_words(), get_starting_word(what_wordle), what_wordle)


if __name__ == "__main__":
    main()
