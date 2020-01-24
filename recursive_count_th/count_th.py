
def count_th(word):

    if len(word) < 2:
        return 0
    if word[0] == "t" and word[1] == "h":
        return 1 + count_th(word[1:])
    else:
        return count_th(word[1:])

    print(count_th)

    pass
