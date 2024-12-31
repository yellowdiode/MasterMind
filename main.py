import random

secret = ["g", "g", "g", "g"]
guess = ["g", "g", "g", "g"]


def Score(secret, guess):
    score = [0, 0]
    secret_copy = list(secret)
    bulbs = len(guess)
    for bulb in range (0, bulbs):
        for i in range(0, bulbs):
            if guess[bulb] == secret_copy[i]:
                if guess[bulb] == secret_copy[bulb]:
                    score[0] += 1
                    secret_copy[bulb] = "jdsfk"
                else:
                    for e in range (0, bulbs):
                        if guess[bulb] == guess[e]:
                            if guess[e] == secret_copy[e]:
                                score[0] += 1
                                secret_copy[e] = "jdsfk"
                    if guess[bulb] == secret_copy[i]:
                        score[1] += 1
                        secret_copy[i] = "dshfsj"
                break
    return score


# def Score3(secret, guess):
#    score = [0, "w", 0, "r"]
#    guess_copy = list(guess)
#    for secret_idx in range(0, 4):
#        if secret[secret_idx] == guess[secret_idx]:
#            score[0] += 1
#            continue
#        for guess_idx in range(0, 4):
#            if secret[secret_idx] == guess_copy[guess_idx] and secret[guess_idx] != guess_copy[guess_idx]:
#                score[2] += 1
#                guess_copy[guess_idx] = None
#                break
#    print(score)


def append_guesses(guesses, guess, idx, num_colors):
    for color in range(num_colors):
        guess[idx] = color
        if idx == 0:
            guesses.append(list(guess))
        else:
            append_guesses(guesses, guess, idx-1, num_colors)
# append_guesses(guesses, [None] * num_pegs, num_pegs - 1, num_colors)


def worst_case(guesses, guess):
    poss_scores = []

    for a_guess in guesses:
        found = None
        a_score = Score(a_guess, guess)
        for elem in poss_scores:
            if elem[0] == a_score[0] and elem[1] == a_score[1]:
                elem[2] += 1
                found = True
                break
        if not found:
            poss_scores.append([a_score[0], a_score[1], 1])

    best_pos_scores = -1
    for i in range(0, len(poss_scores)):
        if poss_scores[i][2] > best_pos_scores:
            best_pos_scores = poss_scores[i][2]
    return best_pos_scores


def real_guess(guesses):
    next_guess = None
    best_worst = len(guesses)+1
    for a_guess in guesses:
        curr_worst = worst_case(guesses, a_guess)
        if curr_worst < best_worst:
            next_guess = [a_guess]
            best_worst = curr_worst
        elif curr_worst == best_worst:
            next_guess.append(a_guess)
    return random.choice(next_guess)


guesses = []

prev_guess = []
prev_score = []
num_guesses = 0
guess_count = 0

if __name__ == '__main__':

    num_colors = int(input("how many colors are there: "))
    num_pegs = int(input("how many spots for pegs are there: "))
    print()
    print()
    print()
    print()
    print()
    append_guesses(guesses, [None] * num_pegs, num_pegs - 1, num_colors)

    while len(guesses) > 1:
        prev_guess = real_guess(guesses)
        print(prev_guess)
        num_whites = int(input("How many whites are there: "))
        num_reds = int(input("How many reds are there: "))
        prev_score = [num_whites, num_reds,]
        guess_count += 1
        print()

        for i in range(len(guesses)-1, -1, -1):
            if Score(guesses[i], prev_guess) != prev_score:
                # print("Score: ", Score(guesses[i], prev_guess),"prev score: ", prev_score)
                guesses[i] = guesses[-1]
                guesses.pop()

    if len(guesses) == 0:
        print("Either you messed up scoring or you are trying to trick me... You can't.")
    else:
        print(guesses[0], "Haha, I won in", guess_count, "tries")





