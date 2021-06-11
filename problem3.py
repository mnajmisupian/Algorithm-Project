from Problem1 import p1Q3 as P1

# P1.main()  # import main method from problem 1 and run
# mainfile.main()  # import articles from main.py and run
# sentimentscore = mainfile.score  # import scores aqcuired from running main() in main.py

# # store dictionary of all distances of each customers in one variable
# DISTANCE = P1.gotop3()

# # initialization of each couriers
# COURIER_NAME = ["cityLE", "posLaju", "gdex", "jnt", "dhl"]

def start(score):
    P1.main()  # import main method from problem 1 and run
    # mainfile.main()  # import articles from main.py and run
    sentimentscore = score  # import scores aqcuired from running main() in main.py

    # store dictionary of all distances of each customers in one variable
    DISTANCE = P1.gotop3()

    # initialization of each couriers
    COURIER_NAME = ["cityLE", "posLaju", "gdex", "jnt", "dhl"]
    DISTANCE = update_dict(DISTANCE, COURIER_NAME)  # update dictionary
    DISTANCE = update_dict_choice(DISTANCE, COURIER_NAME, sentimentscore)  # update dictionary distance times sentiment score
    DISTANCE = sort_dict(DISTANCE, COURIER_NAME)

def update_dict(DISTANCE, COURIER_NAME):
    distance_copy = DISTANCE.copy()  # create a copy of all distances
    for keys in distance_copy.keys():
        courier_dict = distance_copy[keys]
        distance_list = list(courier_dict.values())
        distance_sum = sum(distance_list)

        for i in range(0, len(courier_dict)):
            courier_dict[COURIER_NAME[i]] = 1 - (
                courier_dict[COURIER_NAME[i]] / distance_sum
            )

    return distance_copy


def calculate_score(dictionary, customer_index, courier_index, COURIER_NAME, sentimentscore):
    score = (
        (dictionary[customer_index])[COURIER_NAME[courier_index]]
        * sentimentscore[COURIER_NAME[courier_index]]
        * 1000
    )
    return score


def update_dict_choice(DISTANCE, COURIER_NAME, sentimentscore):
    distance_copy = DISTANCE.copy()
    for keys in distance_copy.keys():
        courier_dict = distance_copy[keys]
        for i in range(0, len(courier_dict)):
            courier_dict[COURIER_NAME[i]] = calculate_score(distance_copy, keys, i, COURIER_NAME, sentimentscore)
    return distance_copy


def sort_dict(DISTANCE, COURIER_NAME):
    distance_copy = DISTANCE.copy()
    placeholder = 0
    bestCourier = None
    valuelist = []
    for keys in distance_copy.keys():
        courier_dict = distance_copy[keys]
        for i in range(0, len(courier_dict)):

            if courier_dict[COURIER_NAME[i]] > placeholder:
                placeholder = courier_dict[COURIER_NAME[i]]
                bestCourier = COURIER_NAME[i]
        print("Best courier for customer " + str(keys) + " is " + bestCourier)


# DISTANCE = update_dict()  # update dictionary
# DISTANCE = update_dict_choice()  # update dictionary distance times sentiment score
# DISTANCE = sort_dict()  # sort and print best courier for each customers
