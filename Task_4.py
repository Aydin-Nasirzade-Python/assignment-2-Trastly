#import libraries here

def main():
    def determine_chinese_zodiac(year):
        zodiac_animals = {0: "Dragon",1: "Snake",2: "Horse",3: "Sheep",4: "Monkey",5: "Rooster",6: "Dog",7: "Pig",8: "Rat",9: "Ox",10: "Tiger",11: "Hare"}
        if year >= 0:
            animal_index = (year - 2000) % 12
            return zodiac_animals[animal_index]
        else:
            return None

    while True:
        year = int(input("Enter the year [ex. 2021]: "))
        if year >= 0:
            zodiac_animal = determine_chinese_zodiac(year)
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
