#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
import sys
class Solution:
    def dataTypeSize(self, str):
        # Code here
        if (str == 'Character'):
            return 1
        elif(str == 'Integer' or str == 'Float'):
            return 4
        else:
            return 8
            

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        str = input()
        ob = Solution()
        res = ob.dataTypeSize(str)
        print(res)
# } Driver Code Ends