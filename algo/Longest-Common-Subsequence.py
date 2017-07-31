def longest_common_subsequence(str1, str2):
    x_axis = len(str1)
    y_axis = len(str2)
    dp_matrix = [['' for i in range(y_axis+1)] for j in range(x_axis+1)]
    for i in range(1, x_axis+1):
        for j in range(1, y_axis+1):
            if str1[i-1] == str2[j-1]:
                new_str = dp_matrix[i-1][j-1] + str1[i-1]
            else:
                new_str = dp_matrix[i-1][j]
            dp_matrix[i][j] = (new_str, dp_matrix[i][j-1])[len(dp_matrix[i][j-1]) > len(new_str)]
    print dp_matrix

longest_common_subsequence("BDCADA", "ABCDBA")
