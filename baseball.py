import statsapi

for team in statsapi.lookup_team('atl'):
    print(team)

bravesid = 144

# GET REQUEST
statsapi.get('team', {'teamId':144})


# strider pitching stats test
# print( statsapi.player_stats(next(x['id'] for x in statsapi.get('sports_players',{'season':2022,'gameType':'W'})['people'] if x['fullName']=='Spencer Strider'), 'pitching', 'career') )