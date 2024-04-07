#import libraries here

def main():
  x=float(input("Enter x: "))
  y=float(input("Enter y: "))

  if -1 <= x <= 2 and -2 <= y <= 3 :
      print("The point is in the shaded area")
  else:
      print("The point is not in the shaded area")
  
  pass

if __name__ == "__main__":
  main()
