import itertools

def greedy_knapsack(weights, values, max_weight):
    # combine knapsack with values in list [(weight, value)]
    knap_list = list(zip(weights, values))

    #sort by value/weight ratio
    knap_list.sort(key=lambda x: x[1]/x[0], reverse=True)

    total_value = 0
    total_weight = 0
    knapsack = []

    # add highest value/weight ratio where there is room.
    for itm in knap_list:
        if total_weight + itm[0] <= max_weight:
            total_weight += itm[0]
            total_value += itm[1]
            knapsack.append(itm)

    print(knapsack)
    print('weight ' + str(total_weight))
    print('value ' + str(total_value))


def long_knapsack(weights, values, max_weight):
    # combine knapsack with values in list [(weight, value)]
    knap_list = list(zip(weights, values))

    # create a binary representation of selected items 1=selected 0=unselected
    # starting with all selected
    binary_rep = '1' * len(knap_list)
    str_binary = '0' + str(len(knap_list)) + 'b'
    # create a list of valid selections later select the best
    valid_selections = []

    while True:

        # check if the current binary representation is a good list and add results
        valid_selections.append(check_selection(knap_list, binary_rep, max_weight))

        # iterate to the next binary_rep
        if int(binary_rep) == 0:
            break
        else:
            binary_rep = int(binary_rep, 2) - 1
            binary_rep = format(binary_rep, str_binary)

    valid_selections = list(filter(None, valid_selections))
    valid_selections.sort(key=lambda x: x[2], reverse=True)
    max_value = valid_selections[0][2]

    for valid_selection in valid_selections:
        if valid_selection[2] == max_value:
            print(valid_selection)

def check_selection(knap_list, binary_rep, max_weight):
    total_value = 0
    total_weight = 0
    knapsack = []

    for select in range(0, len(binary_rep)):
        if total_weight + int(binary_rep[select]) * knap_list[select][0] <= max_weight:
            if binary_rep[select] != '0':
                total_weight += knap_list[select][0]
                total_value += knap_list[select][1]
                knapsack.append(knap_list[select])
        else:
            return None
    return [knapsack, total_weight, total_value]





kcal = [100, 100, 120, 130, 130, 130, 150, 180, 180, 200, 250, 250, 350, 350, 400, 420, 450, 480]
Euros = [90, 100, 110, 120, 120, 125, 130, 155, 160, 180, 200, 250, 300, 350, 410, 450, 480, 560]
max_kcal = 1550


long_knapsack(kcal, Euros, max_kcal)