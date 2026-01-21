print("Hello User")
name= "NiNeD_EyE"
print("I am", name)
name= input("What is your name?") # Ask User for their name
What is your name?
print("Hello", name, "!") # Greet them
while True:
     name= input("What is your name?") # Ask User for their name
     print("Hello", name, "!") # Greet them
     repeat= input("Do you want to continue? (yes/no): ")
     if repeat.lower() != "yes":
         break