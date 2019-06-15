a = list("ABCDGH")
b = list("AEDFHR")
print(a)
print(b)

def maxLen(a, b, an, bn):
    if an < 0 or bn < 0:
        return 0
    if a[an] == b[bn]:
        return 1 + maxLen(a, b, an-1, bn-1)
    else:
        return max(maxLen(a, b, an, bn-1), maxLen(a, b, an-1, bn))
        
print(maxLen(a, b, len(a) -1 , len(b) - 1))
