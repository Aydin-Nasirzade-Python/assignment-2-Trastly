#import libraries here

def main():
    def determine_zodiac_animal(year):
        zodiac_animals = {
            2000: "Dragon",
            2001: "Snake",
            2002: "Horse",
            2003: "Sheep",
            2004: "Monkey",
            2005: "Rooster",
            2006: "Dog",
            2007: "Pig",
            2008: "Rat",
            2009: "Ox",
            2010: "Tiger",
            2011: "Hare"
        }
        return zodiac_animals.get(year)

    while True:
        year = int(input("Enter the year [ex. 2021]: "))
        if year >= 0:
            zodiac_animal = determine_zodiac_animal(year)
            if zodiac_animal:
                  print(f"{year} is the year of the {zodiac_animal}")
                break
            else:
                print("Invalid year!")
        else:
            print("Invalid year!")


  pass

if __name__ == "__main__":
  main()
