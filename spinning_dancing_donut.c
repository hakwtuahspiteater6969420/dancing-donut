#include <ncurses.h>
#include <unistd.h> // For usleep function

#define DELAY 30000

// Function to print a donut at a specific position
void print_donut(WINDOW *win, int x, int y, int frame) {
    const char *donut_frames[2][10] = {
        {
            "        _ _ _ _ _ _ ",
            "     /             \\",
            "   /  O       O     \\",
            "  /   O       O      \\",
            " /    O       O       \\",
            "|    OOOOOOOOOOO       |",
            "|    O         O       |",
            " \\    O       O       /",
            "  \\    O     O       /",
            "   \\_ _ _ _ _ _ _ _ /"
        },
        {
            "        _ _ _ _ _ _ ",
            "     /             \\",
            "   /  O       O     \\",
            "  /   O       O      \\",
            " /    O       O       \\",
            "|    OOOOOOOOOOO       |",
            "|    O         O       |",
            " \\    O       O       /",
            "  \\    O     O       /",
            "   \\_ _ _ _ _ _ _ _ /"
        }
    };

    for (int i = 0; i < 10; i++) {
        mvwprintw(win, y + i, x, donut_frames[frame][i]);
    }
}

// Function to clear the donut at a specific position
void clear_donut(WINDOW *win, int x, int y) {
    for (int i = 0; i < 10; i++) {
        mvwprintw(win, y + i, x, "                     ");
    }
}

int main() {
    int x = 0, y = 0;
    int max_x, max_y;
    int frame = 0;
    int direction_x = 1, direction_y = 1;

    // Initialize ncurses
    initscr();
    noecho();
    curs_set(FALSE);
    timeout(0);

    // Get the size of the window
    getmaxyx(stdscr, max_y, max_x);

    while (1) {
        // Clear the previous donut
        clear_donut(stdscr, x, y);

        // Update the position
        x += direction_x;
        y += direction_y;

        // Check for boundaries and change direction if necessary
        if (x <= 0 || x >= max_x - 21) direction_x = -direction_x;
        if (y <= 0 || y >= max_y - 10) direction_y = -direction_y;

        // Print the new donut
        print_donut(stdscr, x, y, frame);
        frame = (frame + 1) % 2;

        // Refresh the window
        refresh();

        // Delay
        usleep(DELAY);
    }

    // End ncurses mode
    endwin();
    return 0;
}
