import math

print("POWER FACTOR CALCULATOR")
print("-----------------------")

print("1. Calculate Power Factor")
print("2. Calculate Apparent Power")

choice = int(input("Enter your choice (1-2): "))

if choice == 1:
    real_power = float(input("Enter Real Power (W): "))
    apparent_power = float(input("Enter Apparent Power (VA): "))

    if apparent_power == 0:
        print("Apparent Power cannot be zero.")
    else:
        power_factor = real_power / apparent_power
        print("Power Factor =", power_factor)

elif choice == 2:
    voltage = float(input("Enter Voltage (V): "))
    current = float(input("Enter Current (A): "))

    apparent_power = voltage * current
    print("Apparent Power =", apparent_power, "VA")

else:
    print("Invalid choice!")
