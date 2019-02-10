"""Get yes or no program."""


def get_yes_or_no(message):
    """Get yes or no."""
    valid_input = False
    while not valid_input:
        # if input() is used user must place text in quotes for the function to
        # work properly, hence raw_input()
        answer = input(message)
        answer = answer.upper()  # convert answer to upper case
        if answer == 'Y' or answer == 'N':
            valid_input = True
        else:
            print('Please enter Y for yes or N for no.')
    return answer


response = get_yes_or_no('Do you like lima beans? Y)es or N)o:')
if response == 'Y':
    print('Great! They\'re very healthy!')
else:
    print('Too bad.  If cooked right, they\'re quite tasty.')
