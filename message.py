from user_profile import UserProfile

def intro(profile: UserProfile) -> str:
    return (
        f"I am {profile.user_name}, I'm {profile.user_age} years old"
        f"\nI want {profile.user_desire}."
    )  

def get_age_status(profile : UserProfile) -> str:
    
    if profile.user_age >= 18:
        return "I am an Adult"
    else:
        return "I am a Minor" 
    
if __name__ == "__main__":
    print("Please run the main.py to execute the program")
    exit()
    
