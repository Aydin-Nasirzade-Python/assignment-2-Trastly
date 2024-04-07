#import libraries here

def main():
  x = float(input("Enter x: "))
  y = float(input("Enter y: "))

  if (y>= 0 and x>= 0 and x**2 + y**2 <= 1 and y>=x) or (y>= -x and y>= 0 and x<= 0 and x**2 + y**2 <= 1) or (x>= 0 and y<= 0 and y>= -x and x**2 + y**2 <=1) or (y<= 0 and x<= 0 and x**2 + y**2 <= 1 and y>= x) or (x**2 + y**2 >= 1 and y<= 0 and y<= x and x<=0) or (x>= 0 and y<= 0 and x**2 + y**2 >= 1 and y<= -x) :
      print("The point is in the shaded areea")
  else :
      print("The point is not in the shaded area")
  pass

if __name__ == "__main__":
  main()
