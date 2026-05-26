from user_profile import user_name, user_age, user_desire
from message import intro, get_age_status

def main() ->  None:
    print(intro(user_name, user_age, user_desire))
    print(get_age_status(user_age))

if __name__ == "__main__":
    main()