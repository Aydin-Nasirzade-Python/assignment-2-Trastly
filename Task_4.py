#import libraries here

def main():
    def determine_chinese_zodiac(year):
      zodiac_animals = {0: "Monkey",1: "Rooster",2: "Dog",3: "Pig",4: "Rat",5: "Ox",6: "Tiger",7: "Hare",8: "Dragon",9: "Snake",10: "Horse",11: "Sheep"}
      if year >= 0:
          animal_index = year % 12
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
