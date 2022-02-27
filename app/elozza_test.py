from elozza import elozza_response

questions = [
    # Where questions
    {
        'question': "Where's my money?",
        'answer_must_contain': 'your money is'
    },
    {
        'question': "Where is my mind?",
        'answer_must_contain': 'your mind is'
    },
    {
        'question': "Where do the ainu live?",
        'answer_must_contain': 'the ainu live'
    },
    {
        'question': "Where does the Pope shit?",
        'answer_must_contain': 'the Pope shits'
    },
    # When questions
    {
        'question': "When's the next presidential election?",
        'answer_must_contain': 'presidential election'
    },
    {
        'question': "When is the best time to go to bed?",
        'answer_must_contain': 'go to bed'
    },
    {
        'question': "When do the clocks go back?",
        'answer_must_contain': 'the clocks go back'
    },
    {
        'question': "When does Spring break start",
        'answer_must_contain': 'Spring break starts'
    },
    # What questions
    {
        'question': "What's your name?",
        'answer_must_contain': 'my name is'
    },
    {
        'question': "What's the time?",
        'answer_must_contain': 'the time is'
    },
    {
        'question': "What is your favourite colour?",
        'answer_must_contain': 'my favourite colour'
    },
    {
        'question': "What do polar bears eat?",
        'answer_must_contain': 'polar bears'
    },
    # Who questions
    {
        'question': "Who's the president?",
        'answer_must_contain': 'the president is'
    },
    {
        'question': "Who is America?",
        'answer_must_contain': 'America is'
    },
    {
        'question': 'Who stole the cookie from the cookie jar?',
        'answer_must_contains': 'stole the cookie from the cookie jar'
    },
    {
        'question': 'Who do you think you are?',
        'answer_must_contain': 'who I think I am'
    },
    {
        'question': 'Who am I?',
        'answer_must_contain': 'You are'
    },
    # Which questions
    {
        'question': "Which colour's the best?",
        'answer_must_contain': 'colour'
    },
    {
        'question': "Which of these dishes is the most delicious?",
        'answer_must_contain': 'dish'
    },
    # Unanswerable questions
    {
        'question': "Could you please tell me the way to Tipperary?"
    },
]


# ====================
def check_question(question_dict: dict):
    """Check ELOZZA's response to a question"""

    # Get the question and response
    question = question_dict['question']
    answer = elozza_response(question)

    # Print the question and answer
    print(f"{question_dict['question']} -> {answer}")

    # Check whether the answer contains the text specified in 'text_must_contain',
    # if specified
    if answer_must_contain := question_dict.get(
                                'answer_must_contain', None):
        try:
            assert answer_must_contain.lower() in answer.lower()
        except AssertionError:
            print()
            print('=== ERROR ===')
            print(f'Question: {question}')
            print(f'Answer: {answer}')
            print(f'Answer should contain: {answer_must_contain}')
            quit()


# ====================
def main():
    """Print ELOZZA's responses to some test questions"""

    for question_dict in questions:
        check_question(question_dict)

    print()
    print('Tests completed with no issues found.')


# ====================
if __name__ == '__main__':
    main()
