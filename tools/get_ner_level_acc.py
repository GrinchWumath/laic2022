from .help import flatten_lists


def _find_tag(labels, B_label="B-COM", I_label="I-COM", O_label="O-COM"):
    result = []
    lenth = 0
    for num in range(len(labels)):
        if labels[num] == B_label:
            song_pos0 = num
        #if labels[num] == B_label and labels[num + 1] == E_label:
        #    lenth = 2
        #   result.append((song_pos0, lenth))

        if labels[num] == I_label and labels[num - 1] == B_label:
            lenth = 2
            for num2 in range(num, len(labels)):
                if labels[num2] == I_label and labels[num2 - 1] == I_label:
                    lenth += 1
                if labels[num2] == O_label or labels[num2]==B_label:
                    result.append((song_pos0, lenth))
                    break
        if labels[num] == O_label:
            lenth = 1
            song_pos0 = num
            result.append((song_pos0, lenth))

    return result


tags = [("B-Defendants_vehicle", "I-Defendants_vehicle","O"),
        ("B-defendants_driving_conditions","I-defendants_driving_conditions","O"),
        ("B-Violations_of_the_defendant", "I-Violations_of_the_defendant","O"),
        ("B-Place_of_action", "I-Place_of_action","O"),
        ("B-Name_of_carrier", "I-Name_of_carrier","O"),
        ("B-Other_participants", "I-Other_participants","O"),
		("B-Participants_vehicle", "I-Participants_vehicle","O"),
		("B-driving_conditions_of_the_participant", "I-driving_conditions_of_the_participant","O"),
		("B-Violations_by_participants", "I-Violations_by_participants","O"),
        ("B-Identification_of_defendants_responsibility", "I-Identification_of_defendants_responsibility","O"),
        ("B-Identification_of_participants_responsibility", "I-Identification_of_participants_responsibility","O"),
        ("B-Summary_of_the_defendants_conduct", "I-Summary_of_the_defendants_conduct","O")]


def find_all_tag(labels):
    result = {}
    O_label=tags[0]
    for tag in tags:
        res = _find_tag(labels, B_label=tag[0], I_label=tag[1], O_label=tag[2])
        result[tag[0].split("-")[1]] = res
    return result


def precision(pre_labels, true_labels):
    '''
    :param pre_tags: list
    :param true_tags: list
    :return:
    '''
    pre = []
    pre_labels = flatten_lists(pre_labels)
    true_labels = flatten_lists(true_labels)

    pre_result = find_all_tag(pre_labels)
    true_result = find_all_tag(true_labels)

    result_dic = {}
    for name in pre_result:
        for x in pre_result[name]:
            if result_dic.get(name) is None:
                result_dic[name] = []
            if x:
                if pre_labels[x[0]:x[0] + x[1]] == true_labels[x[0]:x[0] + x[1]]:
                    result_dic[name].append(1)
                else:
                    result_dic[name].append(0)
        # print(f'tag: {name} , length: {len(result_dic[name])}')

    sum_result = 0
    for name in result_dic:
        sum_result += sum(result_dic[name])
        # print(f'tag2: {name} , length2: {len(result_dic[name])}')
        result_dic[name] = sum(result_dic[name]) / len(result_dic[name])

    for name in pre_result:
        for x in pre_result[name]:
            if x:
                if pre_labels[x[0]:x[0] + x[1]] == true_labels[x[0]:x[0] + x[1]]:
                    pre.append(1)
                else:
                    pre.append(0)
    total_precision = sum(pre) / len(pre)

    return total_precision, result_dic