# Data taken from "https://wordsrated.com/tools/wordsfinder/past-wordle-answers/"

from datetime import datetime

def clean_copied_data():
    with open("data/wordle_answers.txt") as f:
        answer_lines = f.readlines()

    with open("data/wordle_answers.csv", mode='w') as f:
        f.write("id,date,solution_word\n")

        for line in answer_lines:
            if line[0] == '-':
                data = line.split()
                id=data[2]
                date = datetime.strptime(" ".join(data[3:6]),'(%B %d, %Y):').date()
                solution_word = data[6].lower()
                f.write(f"{id},{date},{solution_word}\n")

if __name__=="__main__":
    clean_copied_data()
