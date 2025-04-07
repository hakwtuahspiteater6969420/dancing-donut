import time
import os

def print_donut(frame):
    donut_frames = [
        [
            "      .-^-.",
            "    .'=^=^='.",
            "   /=^=^=^=^=\\",
            "  :^= HAPPY =^;",
            "  |^ DONUT!  ^|",
            "  :^=^=^=^=^=^;",
            "   \\=^=^=^=^=/",
            "    `.=^=^=.'",
            "      `~~~`"
        ],
        [
            "      .-^-.",
            "    .'=^=^='.",
            "   /=^=^=^=^=\\",
            "  :^= DANCING =^;",
            "  |^ DONUT!  ^|",
            "  :^=^=^=^=^=^;",
            "   \\=^=^=^=^=/",
            "    `.=^=^=.'",
            "      `~~~`"
        ]
    ]
    for line in donut_frames[frame]:
        print(line)

def dancing_donut():
    frame = 0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_donut(frame)
        frame = (frame + 1) % 2
        time.sleep(0.5)

if __name__ == "__main__":
    dancing_donut()
