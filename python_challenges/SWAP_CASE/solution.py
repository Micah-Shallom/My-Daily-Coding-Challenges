def swap_case(s):
    arr = []
    for each in s.split('.'):
        letarr = []
        for letter in each:
            if letter.isupper():
                letter = letter.lower()
            else:
                letter = letter.upper()
            letarr.append(letter)
        arr.append("".join(letarr))
    return '.'.join(arr)

if __name__ == "__main__" :
    s = "Www.HackerRank.com"
    result = swap_case(s)
    print(result)