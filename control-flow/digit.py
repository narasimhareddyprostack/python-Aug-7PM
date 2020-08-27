list1 = ["","one", "two","three","four", "five", "six", "seven", "eight", "nine","ten", "Eleven","Twelve","Thirteen"]
alltens = ["","","twenty","thirty","forty", "Fifty", "sixty", "Seventy", "Eigty", "Ninty"]

n = int(input("Please Enter Number:"))
if n == 0:
    print("Zero")
elif n<=19:
    print(list1[n])
elif n<=99:
    print(alltens[n//10]+''+list1[n%10])
else:
    print("Please Enter 0 to 99 only")