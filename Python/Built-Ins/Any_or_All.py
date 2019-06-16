x = int(input())
arr = input().split(' ')
def isPalindromic(y):
    temp=y
    rev=0
    while(y>0):
        dig=y%10
        rev=rev*10+dig
        y=y//10
    return temp==rev
print(all(0 < int(i) and any( isPalindromic(int(i)) for i in arr ) for i in arr))