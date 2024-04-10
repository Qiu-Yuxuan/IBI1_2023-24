def chocolate_calculator(total_money,price):
    """
    input: the total money the user has, the price of one chocolate bar 
    code: devide the total money by the price
    output: the the number of chocolate bars that can be bought and the changnes that will be left over
    """
    number=total_money//price
    change=total_money%price
    return(number,change)
#example
result=chocolate_calculator(100,7)
print('the number of bars and the changes are',result)
    