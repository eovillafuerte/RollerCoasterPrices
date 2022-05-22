print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
  print ("you can ride the rollercoaster!")
  age = int(input('What is your age?'))
  if age < 12:
    bill = 5
    print('Child tickets are $5')
  elif age <= 17:
    bill = 7
    print('Youth tickets are $7')
  else:
    bill = 12
    print('Adult tickets are $12')
    
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo.upper() == "Y":
    bill += 3

  print(f"Your final bill is {bill}")
                      
else:
  print('Sorry you cannot ride')
# number = int(input("Which number do you want to check? "))

# if number % 2 == 0:
#     print('This is an an even number.')

# else:
#     print('This is an odd number')


