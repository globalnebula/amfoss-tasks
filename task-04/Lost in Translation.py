def can_say_hello(s):
    target = "hello"
    i = 0
    
    for char in s:
        if char == target[i]:
            i += 1 
        if i == len(target):
            return "YES"  
    
    return "NO" 

s = input()

result = can_say_hello(s)
print(result)
