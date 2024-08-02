while True:
    word = input()
    reverse_word = ''.join(reversed(word))

    if word == "0":
        break
    elif word == reverse_word:
        print("yes")
    else:
        print("no")