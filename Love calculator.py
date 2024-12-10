#My solution
def calculate_love_score(name1, name2):
    full_name = f'{name1}{name2}'
    true = ["T", "R", "U", "E"]
    love = ["L", "O", "V", "E"]
    True_times = 0
    Love_times = 0
    for letter in full_name:
        if letter in true:
            True_times += 1
        if letter in love:
            Love_times += 1
    love_score = f'{True_times}{Love_times}'

    print(f'Love score = {love_score}')

calculate_love_score(name1="Kanye West".upper(), name2="Kim Kardashian".upper())

#teacher solution
def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()

    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e

    score = int(str(first_digit) + str(second_digit))
    print(score)


calculate_love_score("Kanye West", "Kim Kardashian")
