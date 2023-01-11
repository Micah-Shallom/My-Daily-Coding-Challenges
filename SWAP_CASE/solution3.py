def swap_case(s):
    return ".".join(map(str.swapcase , s.split('.')))

if __name__ == "__main__" :
    s = "Www.HackerRank.com"
    result = swap_case(s)
    print(result)