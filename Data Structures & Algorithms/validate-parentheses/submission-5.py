class Solution:
    def isValid(self, s: str) -> bool:
        matchClose = {')' : '(', ']' : '[', '}' : '{', }
        myStack = []

        for i in s:
            if i in matchClose.keys():
                if myStack and myStack[len(myStack) - 1] == matchClose[i]:
                    myStack.pop()
                else:
                    return False
            else:
                myStack.append(i)

            print(myStack)
        
        return True if not myStack else False