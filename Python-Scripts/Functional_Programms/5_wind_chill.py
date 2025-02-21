'''5. Write a program WindChill.java that takes two double command-line arguments t
and v and prints the wind chill. Use Math.pow(a, b) to compute ab. Given the
temperature t (in Fahrenheit) and the wind speed v (in miles per hour), the
National Weather Service defines the effective temperature (the wind chill) to be:

Note: the formula is not valid if t is larger than 50 in absolute value or if v is larger
than 120 or less than 3 (you may assume that the values you get are in that range).'''



def get_input():
    temprature=int(input('Enter the temparature: '))
    wind=int(input('Enter the wind: '))
    return temprature,wind

def is_valid_input(temprature,wind):
    return (temprature <= 50) and (3 <= wind <= 120)

def calculate_wind_chill(temprature,wind):
    return 35.74 + 0.6215*(temprature) + (0.4275*(temprature) - 35.75)* (wind ** 0.16)



def main():

    while True:
        temprature,wind=get_input()

        if is_valid_input(temprature,wind):
            wind_chill=calculate_wind_chill(temprature,wind)
            print(f'The wind chill for {temprature} temparature and {wind} wind is: {wind_chill : .2f}')
            break

        else:
            print(f'The Entered Temperature and Wind is Not in Range. Please re-eneter the values again!:')   
    

if __name__=='__main__':
    main()