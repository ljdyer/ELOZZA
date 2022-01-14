import re
from random import choice

PREPROCESS_SUBS = [
    # Pairs of strings to substitute in preprocessing
    ('my', 'your'),
    ('I', 'you'),
]

QUESTION_RESPONSE_REGEXES = [
    # Where questions
    (r'^where(?:\'s|\sis)\s(.+)$', r'\1 is wherever you put it.'),
    (r'^where\sdo\s(.+)$', r"If I knew where \1 I'd be there already."),
    (r'^where\sdoes\s(.+)$', r"If I knew where \1s I'd be there already."),
    # What questions
    (r'^what(?:\'s|\sis)\smy name?', r'My name is ELOZZA.'),
    (r'^what(?:\'s|\sis)\s(.+)$', r'\1 is a social construct.'),
    (r'^what\sdo\s(.+)\s(.+)$',
     r"Perhaps you should be asking what \1 DON'T \2."),
    (r'^what\sdoes\s(.+)\s(.+)$',
     r"Perhaps you should be asking what \1 DOESN'T \2."),
    # Who questions
    (r'^who(?:\'s|\sis)\s(.+)$',
     r'\1 is the thing that looks back when \1 looks in the mirror.'),
    (r'^who\s(.+)$',
     r'Does it really matter who \1? What matters is that someone \1.'),
    # Which questions
    (r'^which\s(.*)(?:\'s|\sis)\s(.+)$',
     r'Whichever \1 you think is \2 is \2.'),
    # When questions
    (r'^when(?:\'s|\sis)\s(.+)$',
     r'\1 is some time in the past, the present, or the future.'),
    (r'^when\sdo\s(.+)$',
     r"\1 when it's the right time to do so."),
    (r'^when\sdo\s(.+)$',
     r"\1s when it's the right time to do so."),
]

AMBIGUOUS_ANSWERS = [
    # Answers for when ELOZZA didn't understand
    "I'm not sure I'm well placed to answer that one.",
    "I'd rather not answer that one if it's all the same to you.",
    "Do I look like I know everything?",
    "Alright, you got me. I don't have the answer to everything.",
    "What is this, the Spanish inquisition?"
]


def preprocess(input: str) -> str:
    """Carry out preprocessing on user input"""

    output = input
    # String substitutions to deal with first/third person
    for word1, word2 in PREPROCESS_SUBS:
        # @ marks used to prevent words being swapped then swapped back again
        output = re.sub(fr'\b{word1}\b', f'_{word2}_', output)
        output = re.sub(fr'\b{word2}\b', f'_{word1}_', output)
    output = re.sub(r'_', '', output)
    # Remove question mark
    output = re.sub(r'\?', '', output)
    return output


def respond(input: str) -> str:
    """Apply question and response regexes to preprocessed user input"""

    for search, replace in QUESTION_RESPONSE_REGEXES:
        output, replaced = re.subn(search, replace, input, flags=re.I)
        if replaced:
            break
    else:
        output = choice(AMBIGUOUS_ANSWERS)
    # Capitalize first letter (but leave any capital letters in rest of string)
    return output[0].upper() + output[1:]


def elozza_response(input: str) -> str:
    """Get ELOZZA's response to the user's input"""

    preprocessed_input = preprocess(input)
    output = respond(preprocessed_input)
    return output


def main():
    """Have a conversation with ELOZZA.
    
    ELOZZA responds to user questions until the user types 'quit'"""

    user_input = ''
    while user_input != 'quit':
        user_input = input("# ")
        if user_input == "quit":
            break
        else:
            print(elozza_response(user_input))


if __name__ == '__main__':
    main()
