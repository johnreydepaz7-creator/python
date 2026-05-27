from user_profile import USER
from message import intro, get_age_status

def main() ->  None:
    if USER is not None:
        print(intro(USER))
        print(get_age_status(USER))
    else:
        print("User profile is not valid. Please try again.")



if __name__ == "__main__":
    main()