from elozza import elozza_response

questions = [
    "What's your name?",
    "What's the time?",
    "What is your favourite colour?",
    "Who's the president?",
    "Who is America?",
    "Where's my money?",
    "Where is my mind?",
    "Which colour's the best?",
    "Which of these dishes is the most delicious?",
    "When's the next presidential election?",
    "When is the best time to go to bed?",
    "What do polar bears eat?",
    "When does the Pope go to bed?",
    "Where do the ainu live?",
    "Could you please tell me the way to Tipperary?"
]


# ====================
def main():
    """Print ELOZZA's responses to some test questions"""

    for q in questions:
        print(f'{q} -> {elozza_response(q)}')


# ====================
if __name__ == '__main__':
    main()
