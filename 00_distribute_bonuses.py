performance = [1, 2, 3, 2, 3, 5, 1]


def getBonuses(performance):
    num_of_empoyees = len(performance)
    # each employee begins witha bonus factor of 1x
    bonuses = [1] * num_of_empoyees

    previous_employee = 0
    current_employee = 1

    for current_employee in range(1, num_of_empoyees):
        if (performance[current_employee] > performance[previous_employee]):
            bonuses[current_employee] += 1
        previous_employee += 1

    #current_employee -= 1

    for previous_employee in range(num_of_empoyees - 2, -1, -1):
        if (performance[previous_employee] > performance[current_employee]):
            bonuses[previous_employee] += 1
        current_employee -= 1

    return bonuses


print(getBonuses(performance))
