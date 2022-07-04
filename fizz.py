for i in range(1, 301):

    buzzes = []
    if i % 3 == 0:
        buzzes.append("Fizz")
    if i % 13 == 0:
        buzzes.append("Fezz")
    if i % 5 == 0:
        buzzes.append("Buzz")
    if i % 7 == 0:
        buzzes.append("Bang")
    if i % 11 == 0:
        buzzes = list(filter(lambda x: x == "Fezz", buzzes))
        buzzes.append("Bong")
    if i % 17 == 0:
        buzzes.reverse()

    if len(buzzes) > 0:
        print("".join(buzzes))
    else:
        print(i)