# User Profile Program

A simple Python command-line program that collects a user's name, age, and desire, then prints a short introduction and whether the user is an adult or a minor.

## Project structure

```text
.
├── main.py          # Runs the program and handles user input
├── user_profile.py  # Stores and validates user data with a dataclass
├── message.py       # Builds output messages
└── README.md        # Project notes and progress
```

## Current features

- Uses a `dataclass` to store user data.
- Validates user input:
  - name cannot be empty
  - age must be between 0 and 150
  - desire cannot be empty
- Avoids global variable dependence for user data.
- Uses `try/except` for error handling.
- Separates responsibilities across three files:
  - `user_profile.py` handles the data model and validation.
  - `message.py` handles message formatting.
  - `main.py` handles program flow and input.
- Uses type hints on functions.
- Restarts the input process when invalid input is entered.
- Limits invalid input attempts to 3 tries.

## How to run

Run the program from `main.py`:

```bash
python main.py
```

## Example output

```text
Please Enter your name: Alex
Please Enter your age: 20
Please Enter your desire: to become a better programmer
I am Alex, I'm 20 years old
I want to become a better programmer.
I am an Adult
```

## Progress notes

### Day 2 updates

Completed:

- Data is stored in a dataclass.
- Input validation was added.
- Global variable dependence was removed.
- Error handling with `try/except` was added.
- Code was separated across `user_profile.py`, `message.py`, and `main.py`.
- Type hints were added to functions.

### Part 2 updates

Completed:

- Added an input loop that restarts when invalid input is entered.
- Added a maximum attempt limit so the input loop is not infinite.

## Still to improve

- Remove direct I/O from `user_profile.py` and `message.py` when those files are run directly.
- Improve the age error message so invalid numbers and non-number input can show clearer messages.
- Consider replacing `exit()` with cleaner program returns for better style and testing.
- empty desire, all three fields are re-asked from scratch.

## Notes

The main program should be started from `main.py`. The other files are helper modules used by the main program.
