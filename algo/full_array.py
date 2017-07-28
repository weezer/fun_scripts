def full_array(string):
    result = [[]]
    for i in string:
        result_len = len(result)
        temp_result = []
        for j in range(result_len):
            current = result.pop()
            for pos in range(len(current)+1):
                temp_result.append(current[:pos] + [i] + current[pos:])
        result.extend(temp_result)
    return result

print full_array("123")