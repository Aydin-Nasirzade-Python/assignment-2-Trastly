#import libraries here

def main():
  def determine_zodiac_sign(month, day):
      if month.lower() == "december":
          if 1 <= day <= 21:
              return "Sagittarius"
          elif 22 <= day <= 31:
              return "Capricorn"
      elif month.lower() == "january":
          if 1 <= day <= 19:
              return "Capricorn"
          elif 20 <= day <= 31:
              return "Aquarius"
      elif month.lower() == "february":
          if 1 <= day <= 18:
              return "Aquarius"
          elif 19 <= day <= 29:
              return "Pisces"
      elif month.lower() == "march":
          if 1 <= day <= 20:
              return "Pisces"
          elif 21 <= day <= 31:
              return "Aries"
      elif month.lower() == "april":
          if 1 <= day <= 19:
              return "Aries"
          elif 20 <= day <= 30:
              return "Taurus"
      elif month.lower() == "may":
          if 1 <= day <= 20:
              return "Taurus"
          elif 21 <= day <= 31:
              return "Gemini"
      elif month.lower() == "june":
          if 1 <= day <= 20:
              return "Gemini"
          elif 21 <= day <= 30:
              return "Cancer"
      elif month.lower() == "july":
          if 1 <= day <= 22:
            return "Cancer"
          elif 23 <= day <= 31:
              return "Leo"
      elif month.lower() == "august":
          if 1 <= day <= 22:
              return "Leo"
          elif 23 <= day <= 31:
              return "Virgo"
      elif month.lower() == "september":
          if 1 <= day <= 22:
              return "Virgo"
          elif 23 <= day <= 30:
              return "Libra"
      elif month.lower() == "october":
          if 1 <= day <= 22:
              return "Libra"
          elif 23 <= day <= 31:
              return "Scorpio"
      elif month.lower() == "november":
          if 1 <= day <= 21:
              return "Scorpio"
          elif 22 <= day <= 30:
              return "Sagittarius"
      return None

  while True:
      month = input("Enter a month [ex. March]: ")
      day = int(input("Enter the day [ex. 12]: "))
      if month.lower() in ["january", "february", "march", "april", "may", "june","july", "august", "september", "october", "november", "december"]:
        if 1 <= day <= 31:
              zodiac_sign = determine_zodiac_sign(month, day)
              if zodiac_sign:
                  print("Your zodiac sign is", zodiac_sign)
              else:
                  print("Either a month or a day is invalid!")
              break
      print("Either a month or a day is invalid!")
  
  pass

if __name__ == "__main__":
  main()
