# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

def print_rangoli(n):
    arrange_list = []
    each_letter = ''
    letters = ''
    
    for i in range(n):
        letters+=chr(97+i)
    for i in letters[::-1]:
        each_letter+='-'+i
        arrange_list.append(each_letter+each_letter[:-1][::-1])
        arrange_list[-1] = arrange_list[-1].strip('-')
            
    for i in arrange_list:
        print(i.center(len(arrange_list[-1]),'-'))
    for i in arrange_list[::-1][1:]:
        print(i.center(len(arrange_list[-1]),'-'))
    

if __name__ == "__main__":
    # n = int(input())
    n = 5
    print_rangoli(n)
    
