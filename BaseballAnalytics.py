from collections import Counter
YEAR = 0
LEAGUE = 1
TEAM = 2
GAMES_PLAYED = 3
GAMES_WON = 4
GAMES_LOST = 5
WON_WS = 6
RUNS = 7
AT_BAT = 8
HITS = 9
DOUBLES = 10
TRIPLES = 11
HOME_RUNS = 12
ATTENDANCE = 13
NON_INT_COLS = [LEAGUE, TEAM, WON_WS]

def find_team_with_most_championships(all_data):
    win_once = []
    team = []

    for row in all_data:
        if row[WON_WS] == True:
            win_once.append(row[TEAM])
            #if row[TEAM] not in team:
            #    team.append(row[TEAM])

    print(win_once)
    wins = dict()
    for team in win_once:
        if team not in wins:
            wins[team] = 1
        else:
            wins[team] = wins[team] + 1
        print(wins)

    most = 0
    for team in wins:
        if wins[team] > most:
            most = wins[team]

    print(most)
    for key, value in wins.items():
        if value == most:
            return key

def question5_same_number_of_games(all_data):
    years_played = []
    years_result = []
    for row in all_data:
        if row[YEAR] not in years_played:
            years_played.append(row[YEAR])
    # print("years:", years_played)

    for year in years_played:
        games_played = []
        for row in all_data:
            if row[YEAR] == year:
                if row[GAMES_PLAYED] not in games_played:
                    games_played.append(row[GAMES_PLAYED])

        if len(games_played) == 1:
            # print("TRUE, all teams played the same number of games")
            years_result.append(year)

    print("Result = ", years_result)


def question4_highest_percentage_games_won(all_data):
    percentage = 0
    line = 0
    for row in all_data:
        if row[WON_WS] == False:
            percentage_won = row[GAMES_WON] / row[GAMES_PLAYED]
            # print(percentage_won)
            if percentage_won > percentage:
                percentage = percentage_won
                line = row

    print(line)


def question3_lowest_percentage_games_won(all_data):
    percentage = 100
    line = 0
    '''
    for row in all_data:
        if row[WON_WS] == True:
            #print(row)
            games_won_percentage = row[GAMES_WON] / row[GAMES_PLAYED]
            print(games_won_percentage)
            if games_won_percentage < percentage:
                percentage = games_won_percentage
                line = row
    '''
    for row in all_data:
        games_won_percentage = row[GAMES_WON] / row[GAMES_PLAYED]
        print(games_won_percentage)
        if games_won_percentage < percentage and row[WON_WS] == True:
            # print(row)
            percentage = games_won_percentage
            line = row

    print(line)


def question2_total_attendance_1999(all_data):
    # what was the total attendance of all games in 1999

    total_attendance = 0
    for row in all_data:
        if row[YEAR] == 1999:
            # print(row[ATTENDANCE])
            total_attendance += row[ATTENDANCE]

    print("total", total_attendance)


def question1_max_home_run(all_data):
    # print("just to test with con for now -- ")
    # print("home run of 1916 Boston is", all_data[0][HOME_RUNS])
    temp = 0
    line = 0
    print("1st time line is", type(line))
    for row in all_data:

        if row[HOME_RUNS] > temp:
            temp = row[HOME_RUNS]
            line = row
    print(line)
    print("2nd time line is", type(line))
    # print(line)
    # print(temp)


'''temp = 0
    count = 0
    for line, row in enumerate(all_data):
        # print(line, "and", row)
        if row[HOME_RUNS] > temp:
            temp = row[HOME_RUNS]
            count = line
            print("trigger at", all_data[count])
'''


# print(count)
# print(temp)
# print(all_data[count])
# data = all_data[count]
# print("The team that has the most HR is", data[TEAM], "in year", data[YEAR], "with", data[HOME_RUNS], "home runs")


def main():
    all_data = []
    with open('Teams.csv', 'r') as fh:
        headers = fh.readline()

        for line in fh:
            # print(line)
            data = line.strip().split(',')
            # print("here", data)
            for i in range(len(data)):
                if i not in NON_INT_COLS:
                    data[i] = int(data[i])
                elif i == WON_WS:
                    data[i] = (data[i] == 'Y')

            # print(data)
            all_data.append(data)

    # print(all_data)
    # for row in all_data:
    #    print(row)

    # question1_max_home_run(all_data)
    # question2_total_attendance_1999(all_data)
    # question3_lowest_percentage_games_won(all_data)
    # question4_highest_percentage_games_won(all_data)
    #question5_same_number_of_games(all_data)
    print(find_team_with_most_championships(all_data))


main()
