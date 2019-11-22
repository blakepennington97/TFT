import calculate
import team_comps
import champ_and_item
from scrape import scrape

user_input = []


class Dumb():
    lockmode = False



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


def format_and_print_results(best_team, missing):
    lines = ['', '', '']
    i = 0
    print(" Your current team: %s\n\n" % team_comps.user_team)
    print(text_colors.BOLD + "   Recommended teams                              Recommended champions\n" + text_colors.END_COLOR)
    for team in best_team:
        lines[i] = (text_colors.PURPLE + str(team) + text_colors.END_COLOR + text_colors.GREEN + "  --->  " +
                    text_colors.END_COLOR + text_colors.YELLOW + str(missing[i]) + text_colors.END_COLOR)
        i += 1
    for line in lines:
        print(line)


def get_user_input():
    user_input_string = input("What champions do you have? \n(Type \"l\" and team number that you want to lock, index starts with 0)\n")
    user_input_string = user_input_string.split(" ")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

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
            Dumb.lockmode = True
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

    if Dumb.lockmode:
        missing = calculate.single_recommend(lock_team)
        format_and_print_results(lock_team, missing)
    else:
        missing = calculate.recommend(best_team)
        format_and_print_results(best_team, missing)


print("\n\nScraping latest meta data...")
_temp, team_comps.team_data = scrape()
print("Updating champion list with latest...")
champ_and_item.update()
print("Done.\n\n")
print("Welcome to our plugin!")
print("This will recommend you team(s) based on what champions you have  :)\n\n")

while 1:
    get_user_input()
