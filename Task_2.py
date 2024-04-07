#import libraries here

def main():
  def determine_season(month, day):
      if (month == "March" and day >= 20) or (month == "April") or (month == "May") or (month == "June" and day < 21):
          return "Spring"
      elif (month == "June" and day >= 21) or (month == "July") or (month == "August") or (month == "September" and day < 22):
          return "Summer"
      elif (month == "September" and day >= 22) or (month == "October") or (month == "November") or (month == "December" and day < 21):
          return "Fall"
      else:
          return "Winter"

  while True:
      month = input("Enter name of the month [ex. June]: ")
      day = int(input("Enter the day [ex. 5]: "))
      if month.capitalize() in ["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"]:
          if 1 <= day <= 31:
              season = determine_season(month.capitalize(), day)
              print(f"{month} {day} is in {season}")
              break
      print("Invalid input!")

  pass

if __name__ == "__main__":
  main()
