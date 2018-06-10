def centuryFromYear(year):
    num =None
    for x in range(1, 2100, 100):
        if year == x+99:
            num = (year)/100
            break
        elif year >= x and year <= x + 98:
            num = (year / 100)+1
            break
    return int(num)


#Easiest solution
def check_century(year):
    return (year+99)//100


print(centuryFromYear(2000))

#Palindrome
def checkPalindrome(inputString):
    print(inputString[::-1])
    return inputString == inputString[::-1]

checkPalindrome("abaaba")