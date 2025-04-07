import time

def print_umbrella():
    umbrella = [
        "    .-^-.",
        "   /_/_\\_\\",
        "   |' ' ' ' ' ' ' ' ' |",
        "   |' ' ' ' ' ' ' ' ' |",
        "    \\_\\_\\_/\\_\\_\\_/",
        "       |     |",
        "       |     |",
        "       |     |",
        "       |     |",
        "       |     |",
        "       |     |",
        "       |     |",
        "       '-----'"
    ]
    for line in umbrella:
        print(line)

def laughing_sound():
    laughs = ["Ha", "HaHa", "HaHaHa", "HaHaHaHa", "HaHaHaHaHa"]
    for laugh in laughs:
        print(laugh)
        time.sleep(0.5)

def laughing_umbrella():
    print_umbrella()
    laughing_sound()

if __name__ == "__main__":
    laughing_umbrella()
