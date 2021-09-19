from function import show_result, taking_data_voter

def Reg_server(name,sex,zone,city,password):
    if password == '' or password == ' ':
        print("Error: Missing Fileds")
        return -1
    vid = taking_data_voter(name,sex,zone,city,password)
    print("Registered Voter with\n\n VOTER I.D. = " + str(vid))


def Register():
    while True:
        name = input('name: ')
        sex = input('sex(M/F)')
        zone = input('zone: ')
        city = input('city: ')
        password = input('password: ')
        n = input('Enter 1 to confirm: ')
        if n == '1':
            Reg_server(name, sex, zone, city, password)
            break
        else:
            print('Register ')
            continue


def showVotes():

    result = show_result()
    print("BJP : ",result['bjp'])
    print("Congress : ",result['cong'])
    print("AAP : ", result['aap'])
    print("Shiv Seva : ", result['ss'])
    print("NOTA : ", result['nota'])
