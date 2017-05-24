from fractions import Fraction
from copy import deepcopy

Q_size = 0


def convert_matrix(mat):
    global Q_size
    mat_len = len(mat)
    frac_mat = [[0 for i in range(mat_len)] for j in range(mat_len)]
    for i in range(mat_len):
        sum_line = sum(mat[i])
        if sum_line == 0:
            Q_size = i
            break
        else:
            for j in range(mat_len):
                if mat[i][j]:
                    frac_mat[i][j] = Fraction(mat[i][j], sum_line)
    return frac_mat


def get_Q(mat):
    global Q_size
    Q_mat = []
    for i in range(Q_size):
        Q_mat.append(mat[i][:Q_size])
    return Q_mat


def get_I(mat):
    global Q_size
    I_mat = [[0 for i in range(Q_size)] for j in range(Q_size)]
    for i in range(Q_size):
        I_mat[i][i] = 1
    return I_mat

def get_R(mat):
    global Q_size
    R_mat = []
    for i in range(Q_size):
        R_mat.append(mat[i][Q_size:])
    return R_mat


def get_I_minus_Q(mat):
    global Q_size
    mat_b = [[0 for i in range(Q_size)] for j in range(Q_size)]
    for i in range(Q_size):
        mat_b[i][i] = 1

    for i in range(Q_size):
        for j in range(Q_size):
            mat[i][j] = mat_b[i][j] - mat[i][j]

    return mat


def inverse_IQ(mat):
    global Q_size
    for i in range(Q_size):
        if mat[i][i] != 1:
            numerator = 1 / mat[i][i]
            for j in range(Q_size * 2):
                mat[i][j] = mat[i][j] * numerator
        for k in range(i+1, Q_size):
            if mat[k][i] != 0:
                multiper_num = -mat[k][i]
                for j in range(Q_size * 2):
                    mat[k][j] = mat[i][j] * multiper_num + mat[k][j]
    for i in range(Q_size-1, -1, -1):
        for k in range(i-1, -1, -1):
            if mat[k][i] != 0:
                multiper_num = -mat[k][i]
                for j in range(Q_size * 2):
                    mat[k][j] = mat[i][j] * multiper_num + mat[k][j]
    F_mat = []
    for i in range(Q_size):
        F_mat.append(mat[i][Q_size:])
    return F_mat


def get_F_R(F_mat, R_mat):
    F_R_mat = [0 for i in range(len(R_mat[0]))]
    for i in range(len(R_mat[0])):
        for j in range(len(F_mat[0])):
            F_R_mat[i] += F_mat[0][j] * R_mat[j][i]
    print F_R_mat
    print F_R_mat


frac_mat = convert_matrix([[0,1,0,0,0,1], [4,0,0,3,2,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]])
print "frac_mat"
print frac_mat
Q_mat = get_Q(frac_mat)
print "Q_mat"
print Q_mat
I_mat = get_I(frac_mat)
print "I_mat"
print I_mat
I_minus_Q = get_I_minus_Q(Q_mat)
print "I_minus_Q"
print I_minus_Q
for i in range(Q_size):
    I_minus_Q[i].extend(I_mat[i])
print "I_minus_Q"
print I_minus_Q
F_mat = inverse_IQ(I_minus_Q)
print "F_mat"
print F_mat
R_mat = get_R(frac_mat)
print "R_mat"
print R_mat
get_F_R(F_mat, R_mat)
