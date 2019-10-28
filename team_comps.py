from pprint import pprint
# def get_data():
#     for key in data:
#         tier_S.append(key)
#         print("KEY = " + key)
#     return tier_S

def get_data():
    pprint(data)
    return data

def build_data(input):
    user_data.append(input)
    print(user_data)

tier_S = []
user_data = []

data = {
    'void_brawlers' : ['khazix',
                 'blitzcrank',
                 'reksai',
                 'vi',
                 'akali',
                 'chogath',
                 'jinx',
                 'kaisa']
    ,
    'imperial_knights' : ['darius',
                    'garen',
                    'mordekaiser',
                    'poppy',
                    'katarina',
                    'draven',
                    'sejuani',
                    'kayle',
                    'swain']
}