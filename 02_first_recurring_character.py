# option 1 - using for loops


def first_recurring_char_opt1(s):
    num_of_letters = len(s)

    for letter in range(0, num_of_letters - 1):
        next_letter = letter + 1
        for next_letter in range(next_letter, num_of_letters - 1):
            if s[letter] == s[next_letter]:
                return s[letter]


print("Option 1:")
print(first_recurring_char_opt1('recurring'))
print(first_recurring_char_opt1('recuring'))
print(first_recurring_char_opt1('recuing'))


print("")

# option 2 - using set class


def first_recurring_char_opt2(s):
    seen_so_far = set()

    for character in s:
        if character in seen_so_far:
            return character
        seen_so_far.add(character)
    return None


print("Option 2:")
print(first_recurring_char_opt2('qwertty'))
print(first_recurring_char_opt2('qwerty'))
