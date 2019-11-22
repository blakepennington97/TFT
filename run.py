import calculate
import team_comps
import champ_and_item
from scrape import scrape
from pprint import pprint

user_input = []


class text_colors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END_COLOR = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def is_int(check):
    try:
        int(check)
        return True
    except ValueError:
        return False


def get_user_input():
    user_input_string = input("What champions do you have? \n(Type \"l\" and team number that you want to lock, index starts with 0)\n")
    user_input_string = user_input_string.split(" ")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    lockmode = False
    lock_team = []
    best_team = calculate.match(user_input_string)

    check = user_input_string[0]

    if len(user_input_string) == 1 and is_int(check[1]) and check[0] == 'l':
        index = int(check[1])
        if index > len(best_team) or index < 1:
            if len(best_team) == 0:
                print(text_colors.RED + "There's no enough data in the best team, fail to print" + text_colors.END_COLOR)
            else:
                print(text_colors.RED + "Invalid input of index, please enter a valid index" + text_colors.END_COLOR)
        elif best_team[index - 1][0] is not None:
            lockmode = True
            lock_team.append(best_team[index - 1][0])
            print("You've already locked team: ", lock_team)
    # elif len(user_input_string) > 1:
    #     print(text_colors.RED + "There are too many inputs to lock a team, please just enter \"l\" and team number" + text_colors.END_COLOR)
    else:
        for i in user_input_string:
            if '-' in i:
                team_comps.delete_champ(i)
            else:
                team_comps.add_champ(i)

    if lockmode is True:
        missing = calculate.recommend(lock_team)
        print(text_colors.YELLOW + "Recommended team(s) ----> %s\n" % lock_team + text_colors.END_COLOR)
    else:
        missing = calculate.recommend_multiple(best_team)
        print(text_colors.YELLOW + "Recommended team(s) ----> %s\n" % best_team + text_colors.END_COLOR)

    print(text_colors.BLUE + "Recommended champion(s) ----> %s\n" % missing+ text_colors.END_COLOR)


print("\n\nScraping latest meta data...")
_temp, team_comps.team_data = scrape()
print("Updating champion list with latest...")
champ_and_item.update()
print("Done.\n\n")
print("Welcome to our plugin!")
print("This will recommend you team(s) based on what champions you have  :)\n\n")

while 1:
    get_user_input()
