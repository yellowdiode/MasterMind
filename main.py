import random

secret = ["g", "g", "g", "g"]
guess = ["g", "g", "g", "g"]


def Score(secret, guess):
    score = [0, "w", 0, "r"]
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
                        score[2] += 1
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


guesses = []
#creation = [0, 0, 0, 0]
#def generator(guesses, creation):
#    for i in range (1, 7):
#        creation[0] = i
#        for e in range(1, 7):
#            creation[1] = e
#            for a in range(1, 7):
#                creation[2] = a
#                for o in range(1, 7):
#                    creation[3] = o
#                    guesses.append(list(creation))
#    return guesses


#def test(secret, guess):
#    print("secret: ", secret, " guess: ", guess)
 #   Score(secret, guess)
  #  print()

prev_guess = []
prev_score = []
num_guesses = 0

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
        prev_guess = guesses[random.randint(0, len(guesses) - 1)]
        print(prev_guess)
        num_whites = int(input("How many whites are there: "))
        num_reds = int(input("How many reds are there: "))
        prev_score = [num_whites, "w", num_reds, "r"]
        print()

        for i in range(len(guesses)-1, -1, -1):
            if Score(guesses[i], prev_guess) != prev_score:
                # print("Score: ", Score(guesses[i], prev_guess),"prev score: ", prev_score)
                guesses[i] = guesses[-1]
                guesses.pop()

    if len(guesses) == 0:
        print("Either you messed up scoring or you are trying to trick me... You can't.")
    else:
        print(guesses[0], "Haha, I won.")






    #append_guesses(guesses, [None] * 4, 4 - 1, 6)
    #print(guesses)
    #print(generator(guesses, creation))
    #test(["a", "x", "x", "x"], ["a", "y", "y", "y"])
    #test(["a", "a", "x", "a"], ["a", "b", "c", "d"])
    #test(["a", "a", "x", "a"], ["b", "a", "a", "d"])
    #test(["a", "a", "c", "d"], ["a", "a", "a", "a"])
    #test(["a", "b", "c", "d"], ["a", "b", "c", "d"])
    #test(["b", "a", "c", "d"], ["a", "b", "c", "d"])
    #test(["a", "b", "c", "d"], ["a", "a", "a", "a"])
    #test(["a", "b", "c", "d"], ["x", "a", "a", "a"])
    #test(["a", "a", "c", "c"], ["a", "a", "a", "c"])
    #test(["a", "c", "c", "a"], ["a", "c", "a", "c"])
