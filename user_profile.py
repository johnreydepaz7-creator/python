from dataclasses import dataclass

@dataclass
class UserProfile:
     user_name: str
     user_age: int
     user_desire: str

     def __post_init__(self):
          if not self.user_name.strip():
               raise ValueError("Name cannot be empty")
          if self.user_age < 0:
               raise ValueError("Age cannot be negative")
          if not self.user_desire.strip():
               raise ValueError("Desire cannot be empty")



try:
    USER = UserProfile(user_name = input("Please Enter your name: "),
                       user_age = int(input("Please Enter your age: ")),
                       user_desire = input("Please Enter your desire: "))
except ValueError:
     print(f"Invalid input")
     USER = None
     

if __name__ == "__main__":
    print("please run the main.py to execute the program")
    exit()