#import libraries here

def main():
  def check_letter(letter):
      vowels = ['a', 'e', 'i', 'o', 'u']
      if letter.lower() in vowels:
          print("Entered alphabet is a vowel!")
      elif letter.lower() == 'y':
          print("Sometimes it is a vowel, and sometimes it is a consonant!")
      else:
          print("Entered alphabet is a consonant!")

  while True:
      user_input = input("Enter a letter of the alphabet: ")
      if len(user_input) == 1 and user_input.isalpha():
          check_letter(user_input)
          break
      else:
          print("Please enter a single letter of the alphabet!")

  pass

if __name__ == "__main__":
  main()
