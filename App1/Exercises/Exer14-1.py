from modules.convert14 import state_of_water

water_temp = None
while not water_temp:
    water_temp = input("Enter the water temperature:")

    try:
        water_temp = float(water_temp)
    except ValueError:
        water_temp=None
        print("Try again and this time enter a number...")

print(f"Your water is {state_of_water(water_temp)}")