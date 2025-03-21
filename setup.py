import curses
import random
import time

# Function to create the dancing umbrella effect
def dancing_umbrella(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)  # Make the window non-blocking
    stdscr.timeout(100)  # Set a timeout for input to make the animation loop

    # Define the umbrella parts
    umbrella_top = [
        "   @   ",
        "  # #  ",
        " #   # ",
        " #   # ",
    ]

    umbrella_handle = [
        "    |    ",
        "    |    ",
        "    |    ",
        "    |    ",
    ]

    # Set initial window size
    height, width = stdscr.getmaxyx()

    while True:
        # Clear the screen
        stdscr.clear()

        # Randomize the characters used for the umbrella parts
        top_char = random.choice(["@", "#", "$", "%", "&"])
        handle_char = random.choice(["@", "#", "$", "%", "&"])

        # Create the umbrella animation by printing lines at different vertical positions
        for i, line in enumerate(umbrella_top):
            stdscr.addstr(i, (width // 2) - len(line) // 2, line.replace(umbrella_top[0][0], top_char))

        for i, line in enumerate(umbrella_handle):
            stdscr.addstr(i + len(umbrella_top), (width // 2) - len(line) // 2, line.replace(umbrella_handle[0][0], handle_char))

        # Refresh the screen to display the new frame
        stdscr.refresh()

        # Sleep to control the speed of the animation
        time.sleep(0.2)

# Run the dancing umbrella animation using curses
curses.wrapper(dancing_umbrella)
