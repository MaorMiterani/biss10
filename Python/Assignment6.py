def can_moshe_buy(startPriceOld, startPriceNew, savingPerMonth, percentLossByMonth):
    money = startPriceOld
    month = 0
    priceOld = startPriceOld
    declinePercent = percentLossByMonth
    while(money < startPriceNew):
        month += 1
        if not month % 2:
            declinePercent = percentLossByMonth + (0.5 * (month / 2))
        priceOld *= ((100 - declinePercent)/100)
        money = priceOld + (savingPerMonth * month)
    return (month, round(money) - startPriceNew)











def main():
    print(can_moshe_buy(2000, 8000, 1000, 1.5))

if __name__ == '__main__':
    main()
