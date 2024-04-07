#import libraries here

def main():
    chinese_zodiac = {2000: "Dragon",2001: "Snake",2002: "Horse",2003: "Sheep",2004: "Monkey",2005: "Rooster",2006: "Dog",2007: "Pig",2008: "Rat",2009: "Ox",2010: "Tiger",2011: "Hare"}

    year = int(input("Enter the year [ex. 2021]: "))

    if year < 0:
        print("Invalid year!")
    else:
        zodiac_year = year % 12
        animal = chinese_zodiac.get(zodiac_year + 2000)  # Add 2000 to align with the start of the cycle


        print(f"{year} is the year of the {animal}")



  pass

if __name__ == "__main__":
  main()
