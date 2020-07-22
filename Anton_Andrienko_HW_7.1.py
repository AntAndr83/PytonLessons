def season(num):

    if num == 12 or num == 1 or num == 2:
        return "winter"
    elif num == 3 or num == 4 or num == 5:
        return "spring"
    elif num == 6 or num == 7 or num == 8:
        return "summer"
    elif num == 9 or num == 10 or num == 11:
        return "fall"
    elif num < 1 or num > 12:
        return "error! input correct num of month"


result = season(int(input('input num of month: ')))

print(result)
