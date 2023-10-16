talents = float(input("Enter talents: "))

pounds = float(input("Enter pounds: "))

lots = float(input("Enter lots: "))




weight = (talents*20*32*13.3)+(pounds*32*13.3)+(lots*13.3)

weight_kg = (weight//1000)

remaining_grams= weight%1000




print(f"The weight in modern units: {weight_kg:.2f} kg and {remaining_grams:.2f} grams")
