
def intro(user_name: str, user_age: int, user_desire: str) -> str:
    return(f"I am {user_name}, I'm {user_age} years old and i want {user_desire}.")

def get_age_status(user_age:int) -> str:
    if user_age < 0:
        raise ValueError("Invalid Age")
    elif user_age >= 18:
        return("I am an Adult")
    else:
        return("I am a Minor")
    

if __name__ == "__main__":
    print("Please run the main.py to execute the program")
