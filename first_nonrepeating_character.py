# First non-repeating character


def first_nonrepeating_character(a_str):
    char_map = {}
    for c in a_str:
        if char_map.get(c) is None:
            char_map[c] = 1
        else:
            char_map[c] += 1

    for c in a_str:
        if char_map[c] == 1:
            return c


# Run my algorithm
my_string = 'somethingthatiswrittenorsaid'
answer = first_nonrepeating_character(my_string)

# Print my result
print('Original string is: {}'.format(my_string))
print('The first non-repeating character is: {}'.format(answer))