from dataclasses import dataclass

@dataclass
class UserProfile:
     user_name: str
     user_age: int
     user_desire: str

     def __post_init__(self):
          self.user_name = self.user_name.strip()
          self.user_desire = self.user_desire.strip()


          if not self.user_name:
               raise ValueError("Name cannot be empty")
          if not 0 <= self.user_age <= 150:
               raise ValueError("Age must be between 0 and 150")
          if not self.user_desire:
               raise ValueError("Desire cannot be empty")

if __name__ == "__main__":
    print("please run the main.py to execute the program")
    exit()