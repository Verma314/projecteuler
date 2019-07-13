

def swapper ( string , i, j):
    string = list(string)
    temp = string[i]
    string[i] = string[j]
    string[j] = temp
    return ''.join(string)


def generatePermutation(string,start,end):
    if ( start == end - 1):
        theList.append(string)
        
    for i in range(start,end):
        string = swapper ( string, start, i)
        generatePermutation ( string, start + 1, end)
        string = swapper (string, start, i)


theList = []
str = "0123456789"  
n = len(str);  
print("All the permutations of the string are: ");  
generatePermutation(str,0,n);
theList.sort()
print(theList[999999])
# answer is 2783915460
