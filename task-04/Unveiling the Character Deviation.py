def count_differing_indices(s):
    reference = "amfoss"
    count = 0
    for i in range(len(reference)):
        if s[i] != reference[i]:
            count += 1
    return count


t = int(input("Enter the number of test cases: "))

for _ in range(t):
    s = input("Enter the string: ")
    result = count_differing_indices(s)
    print("Number of differing indices:", result)
