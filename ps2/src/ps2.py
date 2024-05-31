def find_mcnugget_combination_for_generic(n, packages):
    combinations = set()
    boxes_of_a, boxes_of_b, boxes_of_c, total = 0, 0, 0, 0
    while total < n:
        while total < n:
            while total < n:
                boxes_of_a += 1
                total =  boxes_of_c * packages[2] + boxes_of_b * packages[1] + boxes_of_a * packages[0]
                if total == n:
                    combinations.add((boxes_of_a, boxes_of_b, boxes_of_c))
            boxes_of_a = 0
            boxes_of_b += 1
            total = boxes_of_c * packages[2] + boxes_of_b * packages[1]
            if total == n:
                combinations.add((boxes_of_a, boxes_of_b, boxes_of_c))
        boxes_of_a, boxes_of_b = 0, 0
        boxes_of_c += 1
        total = boxes_of_c * packages[2]
        if total == n:
            combinations.add((boxes_of_a, boxes_of_b, boxes_of_c))
    return combinations

