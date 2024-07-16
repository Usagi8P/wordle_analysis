def clean_possible_answers():
    with open("data/possible_answers.txt") as f:
        possible_answers = f.readlines()

    with open("data/possible_answers.csv", mode='w') as f:
        f.write("solution_word\n")

        for line in possible_answers:
            f.write(line.lower())


if __name__ == "__main__":
    clean_possible_answers()
