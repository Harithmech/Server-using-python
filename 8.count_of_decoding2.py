class Solution:
    def numDecodings(self, s):
	    if not s:
		    return 0
        f = 1
	    if s[0] == "0":
            se = 0
        else:
            se = 1


        for i in range(2, len(s)+1):
        
            temp = 0
		    if 0 < int(s[i-1:i]) <= 9:    #(2)
			    temp += se
		    if 10 <= int(s[i-2:i]) <= 26: #(3)
			    temp += f 
            f = se
            se = temp
	    return se 

ob = Solution()
print(ob.numDecodings("1234"))