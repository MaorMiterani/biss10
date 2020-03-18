def can_moshe_buy(startPriceOld, startPriceNew, savingPerMonth, percentLossByMonth):
    money = startPriceOld
    priceOld = startPriceOld
    month = 0
    while(money < startPriceNew):
        month += 1
        priceOld *= 1 - (percentLossByMonth * month)
        money = priceOld + (savingPerMonth * month)
    return (month, money - startPriceNew)











def main():
    print(can_moshe_buy(2000,8000,1000,0.05))

if __name__ == '__main__':
    main()
