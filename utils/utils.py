def get_run(arg_dict, run=0):
    combinations =[]

    for key in arg_dict.keys():
        if isinstance(arg_dict[key], list):
            combinations.append(len(arg_dict[key]))

    selected_combinations = []
    for base in combinations:
        selected_combinations.append(run % base)
        run = int(run / base)

    counter=0
    result_dict = {}

    for key in arg_dict.keys():
        result_dict[key] = arg_dict[key]
        if isinstance(arg_dict[key], list):
            result_dict[key] = arg_dict[key][selected_combinations[counter]]
            counter+=1

    return result_dict
