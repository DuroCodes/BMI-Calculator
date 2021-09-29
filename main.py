from termcolor import colored as c
from os import system as sys

sys("clear")

print(c("██████╗ ███╗   ███╗██╗", "red"), "     ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ ")
print(c("██╔══██╗████╗ ████║██║", "yellow"), "    ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗")
print(c("██████╔╝██╔████╔██║██║", "green"), "    ██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝")
print(c("██╔══██╗██║╚██╔╝██║██║", "cyan"), "    ██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗")
print(c("██████╔╝██║ ╚═╝ ██║██║", "blue"), "    ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║")
print(c("╚═════╝ ╚═╝     ╚═╝╚═╝", "magenta"), "     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝")

UNIT_SYSTEM = input("\nWould you like to use metric or imperial system? [m/i]: ")
METRIC_LIST = ["m", "me", "met", "metr", "metri", "metric"]

BMI_DICTIONARY = {
  1: ("Severely Underweight", "magenta"),
  2: ("Underweight", "blue"),
  3: ("Normal", "green"),
  4: ("Overweight", "yellow"),
  5: ("Obese", "red"),
}

def metricBMI():

  weightKG = float(input("\nInput weight in KGs: "))
  heightCM = float(input("Input height in CMs: "))
  heightM = heightCM / 100

  BMI = round(weightKG / heightM**2, 2)
  return BMI

def imperialBMI():

  weightLBS = float(input("\nInput weight in LBs: "))
  heightIMP = input("Input height [Feet' Inches\"]: ").strip("\"").replace(" ", "").split("'")

  heightFT = float(heightIMP[0])
  heightIN = float(heightIMP[1])
  heightINs = heightFT*12 + heightIN

  BMI = round(703*weightLBS / heightINs**2, 2)
  return BMI

if(UNIT_SYSTEM.lower() in METRIC_LIST):
  BMI = metricBMI()
else:
  BMI = imperialBMI()

if BMI < 16:
  BMI_INDEX = 1
elif BMI >= 16 and BMI < 18.5:
  BMI_INDEX = 2
elif BMI >= 18.5 and BMI < 25:
  BMI_INDEX = 3
elif BMI >= 25 and BMI < 30:
  BMI_INDEX = 4
elif BMI > 30:
  BMI_INDEX = 5

sys("clear")
print(f"\nYour BMI is: {BMI} ({c(BMI_DICTIONARY[BMI_INDEX][0], BMI_DICTIONARY[BMI_INDEX][1])})")