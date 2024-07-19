# Wordle Analysis
Goal: Check assumptions about the nature of the wordle solutions.
Namely: 
1. It feels like some words appear as answers more frequently than others.
2. If feels like wordle words are not extremely uncommon, nor extremely common.
3. I have heard that wordle never uses plurals as solutions (few words have a trailing "s").

## Step 2: Pivoting
It appears that wordle has never had repeating solution words.
Instead of doing the analysis on the solutions. I'll try to make a bot which solves the wordles most effectively with the assumption that only the remaining words are possible solutions.

Steps:

1. Get letter frequency
2. Get letter frequency at positons
3. Get words with the most overlap for most frequent letters 