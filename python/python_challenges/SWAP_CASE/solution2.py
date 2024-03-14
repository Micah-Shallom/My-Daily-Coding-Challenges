def swap_case(s):
    return ".".join(["".join([letter.lower() if letter.isupper() else letter.upper() for letter in each]) for each in s.split('.')])

if __name__ == "__main__" :
    s = "Www.HackerRank.com"
    result = swap_case(s)
    print(result)
