#import libraries here

def main():
  def determine_color(wavelength):
      if 380 <= wavelength < 450:
        return "Violet"
      elif 450 <= wavelength < 495:
          return "Blue"
      elif 495 <= wavelength < 570:
          return "Green"
      elif 570 <= wavelength < 590:
          return "Yellow"
      elif 590 <= wavelength < 620:
          return "Orange"
      elif 620 <= wavelength <= 750:
          return "Red"
      else:
          return None

  while True:
      wavelength = int(input("Enter the wavelength in nm: "))
      if 380 <= wavelength <= 750:
          color = determine_color(wavelength)
          if color:
              print("The relevant color is", color)
              break
      print("Invalid input!")

  pass

if __name__ == "__main__":
  main()
