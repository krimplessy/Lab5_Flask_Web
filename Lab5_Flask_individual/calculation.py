import math

def get_angle(vec_1, vec_2):
    try:
        sum_tmp = 0
        for i in range(len(vec_1)):
            sum_tmp += vec_1[i]*vec_2[i]
        sum_tmp = abs(sum_tmp)

        sqr_tmp_1 = 0
        sqr_tmp_2 = 0
        for i in range(len(vec_1)):
            sqr_tmp_1 += vec_1[i] * vec_1[i]
            sqr_tmp_2 += vec_2[i] * vec_2[i]
        sqr_tmp_1 = math.sqrt(sqr_tmp_1)
        sqr_tmp_2 = math.sqrt(sqr_tmp_2)
        sqr_tmp_1 *= sqr_tmp_2

        return math.degrees(math.acos(sum_tmp/sqr_tmp_1))
    except:
        return "division by zero"
    

def sum(vec_1, vec_2):
    return [vec_1[i] + vec_2[i] for i in range(len(vec_1))]

def vec_mul(vec_1, vec_2):
    result = [0] * len(vec_1)
    for i in range(len(vec_1)):
        next_i = (i + 1) % len(vec_1)
        prev_i = (i - 1) % len(vec_1)
        result[i] = vec_1[next_i] * vec_2[prev_i] - vec_1[prev_i] * vec_2[next_i]
    return result
