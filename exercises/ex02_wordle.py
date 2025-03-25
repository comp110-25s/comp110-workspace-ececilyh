"""Wordle!"""

__author__: str = "730551362"


# Stage 1: Checking if a guessed character (within the guessed word) is contained in the secret word.
def contains_char(search_string: str, single_string: str) -> bool:
    """This checks if characters are in the word."""
    assert len(single_string) == 1, f"len('{single_string}') is not 1"
    idx: int = 0  # Local variables, not parameters. Do not need to be defined.
    while idx < len(search_string):
        if single_string == search_string[idx]:
            return True
        idx = idx + 1
    return False


# These named constants code for the emojis to appear in place of their names.
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = (
    "\U0001F7E8"  # Don't need to be in the definition. They make code more readible. Need to be in all caps.
)


# Stage 2: Assigns the correctly colored emoji to denote if the letters in the guessed word match the letters in the secret word.
def emojified(guess: str, secret: str) -> str:
    """Emojify the answers."""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    idx: int = 0
    out: str = ""
    while idx < len(secret):
        if contains_char(secret, guess[idx]):
            if guess[idx] == secret[idx]:
                out = out + GREEN_BOX
            else:
                out = out + YELLOW_BOX
        else:
            out = out + WHITE_BOX
        idx = idx + 1
    return out


# Stage 4: Checks that the length of the guessed word matches the length of the secret word.
def input_guess(n: int) -> str:
    """Checking number of characters."""
    guess: str = input(
        f"Enter a {n} character word:"
    )  # When asked to take in input, computer is taking in the user's input.
    while len((guess)) != n:
        guess = input(
            f"That wasn't {n} chars! Try again:"
        )  # == is for a check (bool value); = is for assigning value.
    return guess  # Printing puts it in the output, returning puts in the return value (final thing...RV in mem diagram).


# Combines the three previous stages to create Wordle's gameflow.
def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    game_loop: bool = True
    turn: int = 1
    while turn <= 6 and game_loop == True:
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(n=len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            game_loop = False
        turn = turn + 1
        if turn > 6:
            print(f"X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
