import csv


def get_most_used_letters(possible_solutions:list[dict]) -> list[tuple[str,int]]:
    alphabet = ['a','b','c','d','e','f','g',
                'h','i','j','k','l','m','n',
                'o','p','q','r','s','t','u',
                'v','w','x','y','z']

    letter_frequency = [0] * len(alphabet)

    for word_features in possible_solutions:
        for i, letter in enumerate(alphabet):
            letter_frequency[i] += word_features[letter + '_max']

    top_letters = sorted(zip(alphabet,letter_frequency),key=lambda x: x[1])

    return top_letters
        
def data_setup(possible_solutions:list[dict]) -> list[dict]:
    alphabet = ['a','b','c','d','e','f','g',
                'h','i','j','k','l','m','n',
                'o','p','q','r','s','t','u',
                'v','w','x','y','z']
    
    for word_features in possible_solutions:
        word_features['duplicate_letters'] = 0
        for letter in alphabet:
            word_features[letter] = int(word_features[letter])
            word_features[letter+'_max'] = int(word_features[letter+'_max'])
            if word_features[letter] > 1:
                word_features['duplicate_letters'] = 1

    return possible_solutions

def score_words(possible_solutions:list[dict],top_letters:list[tuple[str,int]]) -> list[dict]:
    duplicate_weight = 10

    for word_features in possible_solutions:
        word_features['score'] = 0
        for rank, word_count in enumerate(top_letters):
            word_features['score'] += word_features[word_count[0]] * rank
        word_features['score'] -= word_features['duplicate_letters'] * duplicate_weight

    return possible_solutions

def get_top_choices(possible_solutions:list[dict]) -> list:
    top_choices = []
    best_score = 0

    for word_features in possible_solutions:
        if word_features['score'] == best_score:
            print(word_features['score'])
            print(word_features['solution_word'])
            top_choices.append(word_features['solution_word'])
        if word_features['score'] > best_score:
            top_choices = []
            top_choices.append(word_features['solution_word'])
            best_score = word_features['score']
            print(word_features['score'])
            print(word_features['solution_word'])

    return top_choices


def wordle_bot():
    with open('data/letter_breakdown.csv') as f:
        reader = csv.DictReader(f)
        all_words = list(reader)

    all_words = data_setup(all_words)

    top_letters = get_most_used_letters(all_words)
    all_words = score_words(all_words,top_letters)
    
    top_choices = get_top_choices(all_words)

    print(top_choices)


if __name__=="__main__":
    wordle_bot()