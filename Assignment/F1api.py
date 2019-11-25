import http.client
import requests
import json

conn = http.client.HTTPSConnection("api.sportradar.us")


def get_user_driver_input():
    x = 1
    while x == 1:
        print("Enter the drivers 3 letter code for their information\n\nLewis Hamilton: ham\nSebastian Vettle: vet\n"
              "Kimi Raikkonen: rai\nMax Verstappen: ver\nValtteri Botas: bot\nDaniel Ricciardo: ric\nNico Hulkenberg: hul\n"
              "Sergio Perez: per\nKevin Magnussen: mag\nCarlos Sainz JR: sai\nFernando Alonso: alo\nEsteban Ocon:oco\n"
              "Charles Leclerc: lec\nRomain Grosjean: gro\nPierre Gasly: gas\nStoffel Vandoorne:van\nMarcus Ericsson: eri\n"
              "Lance Stroll: str\nBrendon Hartley: har\nSergey Sirotkin: sir\n")
        # User chooses the competitor they want info about
        competitor = input("Choose competitor")
        if competitor == 'ham':
            competitor_id = 'sr:competitor:7135'
            x = 2
        if competitor == 'vet':
            competitor_id = 'sr:competitor:7610'
            x = 2
        if competitor == 'rai':
            competitor_id = 'sr:competitor:4538'
            x = 2
        if competitor == 'ver':
            competitor_id = 'sr:competitor:178318'
            x = 2
        if competitor == 'bot':
            competitor_id = 'sr:competitor:41600'
            x = 2
        if competitor == 'ric':
            competitor_id = 'sr:competitor:41603'
            x = 2
        if competitor == 'hul':
            competitor_id = 'sr:competitor:39412'
            x = 2
        if competitor == 'per':
            competitor_id = 'sr:competitor:46337'
            x = 2
        if competitor == 'mag':
            competitor_id = 'sr:competitor:135592'
            x = 2
        if competitor == 'sai':
            competitor_id = 'sr:competitor:189029'
            x = 2
        if competitor == 'alo':
            competitor_id = 'sr:competitor:4521'
            x = 2
        if competitor == 'oco':
            competitor_id = 'sr:competitor:184751'
            x = 2
        if competitor == 'lec':
            competitor_id = 'sr:competitor:269471'
            x = 2
        if competitor == 'gro':
            competitor_id = 'sr:competitor:37294'
            x = 2
        if competitor == 'gas':
            competitor_id = 'sr:competitor:381362'
            x = 2
        if competitor == 'van':
            competitor_id = 'sr:competitor:250229'
            x = 2
        if competitor == 'eri':
            competitor_id = 'sr:competitor:136140'
            x = 2
        if competitor == 'str':
            competitor_id = 'sr:competitor:302866'
            x = 2
        if competitor == 'har':
            competitor_id = 'sr:competitor:41601'
            x = 2
        if competitor == 'sir':
            competitor_id = 'sr:competitor:135594'
            x = 2
        elif competitor != ('ham'or'vet'or'rai'or'ver'or'bot'or'ric'or'hul'or'per'or'mag'or'sai'or'alo'or'oco'or'lec'or
                            'gro'or'gas'or'van'or'eri'or'str'or'har'or'sir'):
            competitor = 'an invalid competitor, please choose again.'
        print("You have chosen", competitor)
    return competitor_id


def get_user_team_input():
    x = 1
    while x == 1:
        print("Enter the teams code for their information\n\nMercedes: merc\nFerrari: ferr\nRed Bull Racing: rbr\n"
              "Renault: ren\nHaas: haas\nMcLaren: mcl\nRacing Point: race\nAlfa Romeo Racing: alfa\n"
              "Scuderia Toro Rosso: scud\nWilliams: will\nForce India: ind")
        # User chooses the team they want info about
        team = input("Choose team")
        if team == 'merc':
            team_id = 'sr:competitor:41127'
            x = 2
        if team == 'ferr':
            team_id = 'sr:competitor:4510'
            x = 2
        if team == 'rbr':
            team_id = 'sr:competitor:4978'
            x = 2
        if team == 'ren':
            team_id = 'sr:competitor:4512'
            x = 2
        if team == 'haas':
            team_id = 'sr:competitor:242902'
            x = 2
        if team == 'mcl':
            team_id = 'sr:competitor:4514'
            x = 2
        if team == 'race':
            team_id = 'sr:competitor:496090'
            x = 2
        if team == 'alfa':
            team_id = 'sr:competitor:4515'
            x = 2
        if team == 'scud':
            team_id = 'sr:competitor:5771'
            x = 2
        if team == 'will':
            team_id = 'sr:competitor:4511'
            x = 2
        if team == 'ind':
            team_id = 'sr:competitor:7137'
            x = 2
        elif team != ('merc'or'ferr'or'rbr'or'ren'or'haas'or'mcl'or'race'or'alfa'or'scud'or'will'or'ind'):
            team = 'an invalid team, please choose again.'
        print("You have chosen", team)
    return team_id


def get_competitor_info(competitor_id):
    # uses the competitor ID the user has chosen and retrieves info using the API
    url = 'https://api.sportradar.us/formula1/trial/v2/en/competitors/'+competitor_id+'/profile.json?api_key=wb825w3qegqenjt95ue3muut'
    info = requests.get(url)
    data = json.dumps(info.json(), indent=4)
    print(data)


def get_team_info(team_id):
    # uses the team ID the user has chosen and retrieves info using the API
    url = 'http://api.sportradar.us/formula1/trial/v2/en/competitors/'+team_id+'/profile.json?api_key=wb825w3qegqenjt95ue3muut'
    info = requests.get(url)
    data = json.dumps(info.json(), indent=4)
    print(data)


def get_seasons():
    # Retrieves info on F1 seasons
    url = 'http://api.sportradar.us/formula1/trial/v2/en/seasons.json?api_key=wb825w3qegqenjt95ue3muut'
    info = requests.get(url)
    data = json.dumps(info.json(), indent=4)
    print(data)


def get_user_stage_summary():
    # Retrieves a summary of info about a stage, including tracks, racers and teams involved
    x = 1
    while x == 1:
        print("Enter which stage you would like information on\nF1 2018: f12018\nAustralia 2018: aus2018\n"
              "Bahrain 2018: bah2018\nChina 2018: chi2018\nAzerbaijan 2018: aze2018\nSpain 2018: esp2018\n"
              "Monaco 2018: mon2018\nCanada 2018: can2018\nFrance 2018: fra2018\nOsterreich 2018: ost2018\n"
              "Britain 2018: bri2018\nGermany 2018: deu2018\nMagyar 2018: mag2018\nBelgium 2018: bel2018\n"
              "Italy 2018: ita2018\nSingapore 2018: sin2018\nRussia 2018: rus2018\nJapan 2018: jap2018\n"
              "USA 2018: usa2018\nMexico 2018: mex2018\nBrasil 2018: bra2018\nAbu Dhabi 2018: abu2018\n\n"
              
              "F1 2019: f12019\nAustralia 2019: aus2019\nBahrain 2019: bah2019\nChina 2019: chi2019\n"
              "Azerbaijan 2019: aze2019\nSpain 2019: esp2019\nMonaco 2019: mon2019\nCanada 2019: can2019\n"
              "France 2019: fra2019\nOsterreich 2019: ost2019\nBritain 2019: bri2019\nGermany 2019: deu2019\n"
              "Magyar 2019: mag2019\nBelgium 2019: bel2019\nItaly 2019: ita2019\nSingapore 2019: sin2019\n"
              "Russia 2019: rus2019\nJapan 2019: jap2019\nUSA 2019: usa2019\nMexico 2019: mex2019\n"
              "Brasil 2019: bra2019\nAbu Dhabi 2019: abu2019\n\n")
        stage = input()
        # 2018 Stages
        if stage == 'f12018':
            stage_id = 'sr:stage:324771'
            x = 2
        if stage == 'aus2018':
            stage_id = 'sr:stage:324773'
            x = 2
        if stage == 'bah2018':
            stage_id = 'sr:stage:324991'
            x = 2
        if stage == 'chi2018':
            stage_id = 'sr:stage:325209'
            x = 2
        if stage == 'aze2018':
            stage_id = 'sr:stage:325427'
            x = 2
        if stage == 'esp2018':
            stage_id = 'sr:stage:325645'
            x = 2
        if stage == 'mon2018':
            stage_id = 'sr:stage:325863'
            x = 2
        if stage == 'can2018':
            stage_id = 'sr:stage:326081'
            x = 2
        if stage == 'fra2018':
            stage_id = 'sr:stage:326299'
            x = 2
        if stage == 'ost2018':
            stage_id = 'sr:stage:326517'
            x = 2
        if stage == 'bri2018':
            stage_id = 'sr:stage:326735'
            x = 2
        if stage == 'deu2018':
            stage_id = 'sr:stage:326935'
            x = 2
        if stage == 'mag2018':
            stage_id = 'sr:stage:327171'
            x = 2
        if stage == 'bel2018':
            stage_id = 'sr:stage:327389'
            x = 2
        if stage == 'ita2018':
            stage_id = 'sr:stage:327607'
            x = 2
        if stage == 'sin2018':
            stage_id = 'sr:stage:327825'
            x = 2
        if stage == 'rus2018':
            stage_id = 'sr:stage:328043'
            x = 2
        if stage == 'jap2018':
            stage_id = 'sr:stage:328261'
            x = 2
        if stage == 'usa2018':
            stage_id = 'sr:stage:328479'
            x = 2
        if stage == 'mex2018':
            stage_id = 'sr:stage:328697'
            x = 2
        if stage == 'bra2018':
            stage_id = 'sr:stage:328915'
            x = 2
        if stage == 'abu2018':
            stage_id = 'sr:stage:329133'
            x = 2

        # 2019 stages
        if stage == 'f12019':
            stage_id = 'sr:stage:426678'
            x = 2
        if stage == 'aus2019':
            stage_id = 'sr:stage:427875'
            x = 2
        if stage == 'bah2019':
            stage_id = 'sr:stage:428093'
            x = 2
        if stage == 'chi2019':
            stage_id = 'sr:stage:428311'
            x = 2
        if stage == 'aze2019':
            stage_id = 'sr:stage:428311'
            x = 2
        if stage == 'esp2019':
            stage_id = 'sr:stage:428747'
            x = 2
        if stage == 'mon2019':
            stage_id = 'sr:stage:428965'
            x = 2
        if stage == 'can2019':
            stage_id = 'sr:stage:429183'
            x = 2
        if stage == 'fra2019':
            stage_id = 'sr:stage:429183'
            x = 2
        if stage == 'ost2019':
            stage_id = 'sr:stage:429621'
            x = 2
        if stage == 'bri2019':
            stage_id = 'sr:stage:429839'
            x = 2
        if stage == 'deu2019':
            stage_id = 'sr:stage:430057'
            x = 2
        if stage == 'mag2019':
            stage_id = 'sr:stage:430313'
            x = 2
        if stage == 'bel2019':
            stage_id = 'sr:stage:430531'
            x = 2
        if stage == 'ita2019':
            stage_id = 'sr:stage:430749'
            x = 2
        if stage == 'sin2019':
            stage_id = 'sr:stage:430967'
            x = 2
        if stage == 'rus2019':
            stage_id = 'sr:stage:431185'
            x = 2
        if stage == 'jap2019':
            stage_id = 'sr:stage:431403'
            x = 2
        if stage == 'usa2019':
            stage_id = 'sr:stage:431839'
            x = 2
        if stage == 'mex2019':
            stage_id = 'sr:stage:431621'
            x = 2
        if stage == 'bra2019':
            stage_id = 'sr:stage:432057'
            x = 2
        if stage == 'abu2019':
            stage_id = 'sr:stage:432275'
            x = 2

        elif x != 2:
            stage = 'an invalid stage, please try again.'
        print("you have chosen", stage)
    return stage_id


def get_stage_summary(stage_id):
    url = 'http://api.sportradar.us/formula1/trial/v2/en/sport_events/' + stage_id + '/summary.json?api_key=wb825w3qegqenjt95ue3muut'
    info = requests.get(url)
    data = json.dumps(info.json(), indent=4)
    print(data)


def main():
    x = 1
    while x == 1:
        print("Hello, please enter the following commands:\nFor information on drivers, enter: drivers\n"
              "For information on teams, enter: teams\nFor information on stages, enter: stages\n"
              "For information on seasons, enter: seasons\nAnd to exit, enter: exit\n")
        choice = input()
        if choice == 'drivers':
            get_competitor_info(get_user_driver_input())  # retrieves driver information
        if choice == 'teams':
            get_team_info(get_user_team_input())  # retrieves team information
        if choice == 'stages':
            get_stage_summary(get_user_stage_summary())  # retrieves stage information
        if choice == 'seasons':
            get_seasons()  # retrieves information about the seasons
        if choice == 'exit':
            x = 2  # sets x above the value required to keep the 'while loop' going, ending the program.


if __name__ == "__main__":
    main()