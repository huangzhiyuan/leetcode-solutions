class Solution(object):
    def addTwoNumbers(self,l1,l2):
        return self.intToList(self.listToInt(l1)+self.listToInt(l2))
		
    def listToInt(self,l):
        #l.reverse()
        x=l[::-1]
        sum=0
        for i in range(len(x)):
            sum = 10*sum+x[i]
        print sum
        return sum
		
    def intToList(self,x):
        l=[]
        while x:
            l.append(x%10)
            x/=10
        print l
        return l
