def answer(weekd, value):
    ret = 0
    weekd.toupper()
    if weekd == 'SATURDAY' or 'SAT':
        value = value * 0.95
    elif  weekd == 'SUNDAY' or 'SUN':
        value = value * 0.9
    else :
        value *= 1
    # END: You code here
    return ret

# Please don't change the code below!!!
def main():
    weekday = input("Enter the weekday: ") 
    amt = input("Enter an amount: ") 
    amt = float( "{:.2f}".format(float(amt)) )
    print( answer(weekday,amt) )

if __name__ == "__main__":
    main()
# Please don't change the code above!!!