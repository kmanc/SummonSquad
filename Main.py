import GetData, DoMath, API
import argparse


def main():

    parser = argparse.ArgumentParser(usage=' Main.py -s <list of five summoners> -r <region> -c <number of champs>')
    parser.add_argument('-s', dest='summoners', type=str, nargs='+', help='summoners to build a team for')
    parser.add_argument('-r', dest='region', type=str, help='region (NA, EUW, etc)')
    parser.add_argument('-c', dest='champs', type=int, help='number of top champions to check')
    args = parser.parse_args()
    
    # Make sure the inputs are there 
    if args.summoners is None or args.region is None or args.champs is None:
        print(parser.usage)
        exit(0)
    if len(args.summoners) != 5:
        print(parser.usage)
        exit(0)
    summoners = args.summoners
    region = args.region
    num_champs = args.champs

    # Set max and min for champs
    if num_champs < 15:
        num_champs = 15
    if num_champs > 30:
        num_champs = 30
    
    # Normalize summoner names (no spaces, no upper case) because the api can get cranky if you don't
    summoners = [name.lower().replace(" ", "") for name in summoners]

    # Get a dictionary that maps champion id to champion name
    champ_id_to_name = API.champion_lookup(region)
    # Get the champion name for later use, because 'champion 35' doesn't mean much to people
    champ_id_to_name = {key: value['name'] for key, value in champ_id_to_name.items()}

    summoner_data = {}
    # Create a of champions and the summoners that play them (includes score based on mastery)
    for player in summoners:
        summoner_id, summoner_name, account_id = GetData.get_summoner_data(player, region)
        champ_points_pair = GetData.get_summoners_mastery(summoner_id, summoner_name, num_champs, region)
        champ_counters = GetData.lanes_and_roles(account_id, summoner_name, champ_points_pair, region)
        GetData.percentages(champ_counters)
        summoner_data[summoner_name] = GetData.data_compile(summoner_name, champ_counters,
                                                            champ_id_to_name, champ_points_pair)

    # Get the squad
    # Build the dream
    # Using a basic genetic algorithm, we go through possible teams and find the best one we can
    try:
        population = DoMath.populate_generation(summoner_data, 200)
        population = DoMath.mutate(population, summoner_data)
        health = 0
        new_health = 1
        while health / new_health < .99:
            health = DoMath.grade_generation(population)
            population = DoMath.evolve(population)
            new_health = DoMath.grade_generation(population)

        dream_team = population[0]
        # Parse the final output for the website
        formatted_dream_team = ('{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},'
                                '{11},{12},{13},{14},{15},{16},{17},{18},{19}'.format(dream_team[0][4], dream_team[0][0],
                                                                                      dream_team[0][2], dream_team[1][4],
                                                                                      dream_team[1][0], dream_team[1][2],
                                                                                      dream_team[2][4], dream_team[2][0],
                                                                                      dream_team[2][2], dream_team[3][4],
                                                                                      dream_team[3][0], dream_team[3][2],
                                                                                      dream_team[4][4], dream_team[4][0],
                                                                                      dream_team[4][2], dream_team[0][1],
                                                                                      dream_team[1][1], dream_team[2][1],
                                                                                      dream_team[3][1], dream_team[4][1] ))

    except:
        exit('You woke up, the dream is gone')
        
    # Output for the website
    print(formatted_dream_team)
    return formatted_dream_team
    
if __name__ == '__main__':
    main()