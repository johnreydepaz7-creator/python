from user_profile import UserProfile
from message import intro, get_age_status

MAX_ATTEMPT = 3

def collect_user_data() -> UserProfile:
    for attempt in range(1, MAX_ATTEMPT + 1):
        try:
            user_name = input("Please Enter your name(MUST): ")
            user_age = int(input("Please Enter your age(MUST): "))
            user_desire = input("Please Enter your desire(MUST): ")
            return UserProfile(user_name=user_name, user_age=user_age, user_desire=user_desire)
        
        except ValueError:
            remaining_attempts = MAX_ATTEMPT - attempt
            print(f"Invalid input. \nPlease try again.\n\n")
            if remaining_attempts > 0:
                print(f"You have {remaining_attempts} attempt(s) left.\n")
        
    raise Exception("Maximum attempts reached. Exiting the program.")


def main() ->  None:
    try:
        user_profile = collect_user_data()
        print(intro(user_profile))
        print(get_age_status(user_profile))
    except Exception as e:
        print(f"An error occurred: {e}")




if __name__ == "__main__":
    main()