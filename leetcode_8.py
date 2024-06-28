
def myAtoi(s):
        # if str is empty -> return 0
        if(s == None or len(s) == 0):
            return 0
        
        # check negative
        if(s[0] == '-'):
            isNegative = True
            i = 1
        else:
            isNegative = False
            i = 0
        
        result = 0
        for i in range(len(s)):
            char = s[i]
            if(char == '-'):
                isNegative = True

            if(char.isdigit()):
                digit = ord(char) - ord('0')
            
            # if isNegative is True -> positive number
                if(not isNegative):
                    result = result * 10 + digit
                else:
                    result = result * 10 - digit

        return result

print(myAtoi("words and 987"))