in_list = []
t = int(input())
for _ in range(t):
    tc = input().split()
    in_list.append(tc)

for tc in in_list:
    num1_str, num2_str = tc[0], tc[1]
    num1_list = list(num1_str)
    num2_list = list(num2_str)
    num1_len, num2_len = len(num1_list), len(num2_list)
    b_flag, b_index = False, 0

    if num1_len != num2_len:
        for i in range(num1_len):
            if i == 0:
                num1_list[i] = '9'
            else:
                num1_list[i] = '0'
        for i in range(num2_len - num1_len, num2_len):
            if i == num2_len - num1_len:
                num2_list[i] = '0'
            else:
                num2_list[i] = '9'
    else:
        for i in range(num1_len):
            if num1_list[i] == num2_list[i]:
                continue
            else:
                b_flag = True
                b_index = i
                break
        if b_flag:
            for i in range(b_index + 1, num1_len):
                if i == b_index + 1:
                    num1_list[i] = '9'
                    num2_list[i] = '0'
                else:
                    num1_list[i] = '0'
                    num2_list[i] = '9'

    updated_num1_str = "".join(num1_list)
    updated_num2_str = "".join(num2_list)
    updated_num1 = int(updated_num1_str)
    updated_num2 = int(updated_num2_str)

    rem1, rem2, rem_diff, s = 0, 0, 0, 0
    while True:
        if updated_num1 == 0:
            rem1 = 0
        else:
            rem1 = updated_num1 % 10
            updated_num1 = updated_num1 // 10
        if updated_num2 == 0:
            rem2 = 0
        else:
            rem2 = updated_num2 % 10
            updated_num2 = updated_num2 // 10
        rem_diff = abs(rem1 - rem2)
        s = s + rem_diff
        if updated_num1 == 0 and updated_num2 == 0:
            break

    print(s)

