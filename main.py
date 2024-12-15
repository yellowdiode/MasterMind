secret = ["g", "g", "g", "g"]
guess = ["g", "g", "g", "g"]


def Score(secret, guess):
    score = [0, "w", 0, "r"]
    secret_copy = list(secret)
    for bulb in range (0, 4):
        for i in range(0, 4):
            if guess[bulb] == secret_copy[i]:
                if guess[bulb] == secret_copy[bulb]:
                    score[0] += 1
                    secret_copy[bulb] = "jdsfk"
                else:
                    for e in range (0, 4):
                        if guess[bulb] == guess[e]:
                            if guess[e] == secret_copy[e]:
                                score[0] += 1
                                secret_copy[e] = "jdsfk"
                    if guess[bulb] == secret_copy[i]:
                        score[2] += 1
                        secret_copy[i] = "dshfsj"
                break
    print(score)


def Score3(secret, guess):
    score = [0, "w", 0, "r"]
    guess_copy = list(guess)
    for secret_idx in range(0, 4):
        if secret[secret_idx] == guess[secret_idx]:
            score[0] += 1
            continue
        for guess_idx in range(0, 4):
            if secret[secret_idx] == guess_copy[guess_idx] and secret[guess_idx] != guess_copy[guess_idx]:
                score[2] += 1
                guess_copy[guess_idx] = None
                break
    print(score)




def test(secret, guess):
    print("secret: ", secret, " guess: ", guess)
    Score(secret, guess)
    Score3(secret, guess)
    print()

if __name__ == '__main__':
    test(["a", "x", "x", "x"], ["a", "y", "y", "y"])
    test(["a", "a", "x", "a"], ["a", "b", "c", "d"])
    test(["a", "a", "x", "a"], ["b", "a", "a", "d"])
    test(["a", "a", "c", "d"], ["a", "a", "a", "a"])
    test(["a", "b", "c", "d"], ["a", "b", "c", "d"])
    test(["b", "a", "c", "d"], ["a", "b", "c", "d"])
    test(["a", "b", "c", "d"], ["a", "a", "a", "a"])
    test(["a", "b", "c", "d"], ["x", "a", "a", "a"])
    test(["a", "a", "c", "c"], ["a", "a", "a", "c"])
    test(["a", "c", "c", "a"], ["a", "c", "a", "c"])
