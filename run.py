import calculate
import team_comps



def get_user_input():
    user_input_string = raw_input("What champions do you have?")
    print(user_input_string)
    team_comps.build_data(user_input_string)
    calculate.match(team_comps.user_data, team_comps.data)


while 1:
    team_comps.get_data()
    get_user_input()