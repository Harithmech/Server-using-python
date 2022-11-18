# reference
# https://leetcode.com/problems/decode-ways/discuss/608268/Python-Thinking-process-diagram-(DP-%2B-DFS)


s = '11106'
l = len(s)


def isValid(code, le):
    if le == 1:
        return code >= 1 and code <= 9
    return code >= 10 and code <= 26


def count_of_decodings(i):
    # termination condition
    if i >= l:
        return 1
    ans = 0
    # check if singer integer is valid
    if isValid(ord(s[i])-ord('0'), 1):
        ans += count_of_decodings(i+1)
    # check for 2 integer is valid
    # here i-1 tom make sure you have atleast 2 elements left at end
    if((i < l-1) and isValid((ord(s[i])-ord('0'))*10 + (ord(s[i+1])-ord('0')), 2)):
        ans += count_of_decodings(i+2)
    return ans


print(count_of_decodings(0))


#The responsibility of the count_of_decodings function is to return the valid decodings 
#for the substring starting from length i. For doing that, it just needs to return the valid decodings of substrings starting from i+1, and i+2. It should not return all the answers accumulated in the variable "ans" till now.
