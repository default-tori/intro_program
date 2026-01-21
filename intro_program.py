print("Hello User")
name= "NiNeD_EyE"
print("I am", name)
while True:
     name= input("What is your name?") # Ask User for their name
     print("Hello", name, "!") # Greet them
     repeat= input("Do you want to continue? (yes/no): ")
     if repeat.lower() != "yes":
         break