amount_days = int(input("How many days temperature? "))
temperature_data = []

temperature_data = [float(input(f"Enter temperature of day {i+1}: ")) for i in range(amount_days)]
average = round(sum(temperature_data) / amount_days, 2)

def counterAboveAverage(list_data): 
    counter = 0 
    for i in list_data: 
        if i > average: 
            counter+=1 
    return counter

print("\n", "Average =", average, '\n',counterAboveAverage(temperature_data), "day(s) above average")


