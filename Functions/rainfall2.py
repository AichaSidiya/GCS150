def main():
    rain_list=rainfall()
    total_year=annual(rain_list)
    average=avrg(rain_list,total_year)
    hmonth=high(rain_list)
    lmonth=low(rain_list)


def rainfall():
    rain=[]
    for month in range(1,13):
        print('month',month,':',end='')
        total_rainfall=int(input('enter the total rainfall for this month:'))
        rain.append(total_rainfall)
    return rain

def annual(rainfall_list):
    total=0
    for num in rainfall_list:
        total+=num
    print('The total rainfall of the year is:',total)
    return total

def avrg(rainfall_list,total):
    average=total/len(rainfall_list)
    print('The average monthly rainfall is:',average)
    return average

def high(rain):
    max_val=max(rain)
    max_index=rain.index(max_val)
    print('The highst rainfall was ',max_val,'in month',max_index+1)

def low(rain):
    min_val=min(rain)
    min_index=rain.index(min_val)
    print('The lowest rainfall was ',min_val,'in month',min_index+1)

main()
