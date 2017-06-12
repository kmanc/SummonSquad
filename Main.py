from GetData import GetData
from DoMath import DoMath
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
    if num_champs < 5:
        num_champs = 5
    if num_champs > 20:
        num_champs = 20
    
    # Normalize summoner names (no spaces, no upper case) because the api can get cranky if you don't
    summoners = [name.lower().replace(" ", "") for name in summoners]

    summoner_data = {}
    data_grabber = GetData(region)
    # Create a of champions and the summoners that play them (includes score based on mastery)
    for player in summoners:
        summoner_id, summoner_name = data_grabber.get_summoner_data(player)
        champ_points_pair = data_grabber.get_summoners_mastery(summoner_id, summoner_name, num_champs)
        champ_counters = data_grabber.lanes_and_roles(summoner_id, summoner_name, champ_points_pair)
        data_grabber.percentages(champ_counters)
        summoner_data[summoner_name] = data_grabber.data_compile(summoner_name, champ_counters, champ_points_pair)

    build_team = DoMath()
    # Get the squad
    # Build the dream
    # Using a basic genetic algorithm, we go through possible teams and find the best one we can
    try:
        population = build_team.populate_generation(summoner_data, 200)
        population = build_team.mutate(population, summoner_data)
        health = 0
        new_health = 1
        while health / new_health < .99:
            health = build_team.grade_generation(population)
            population = build_team.evolve(population)
            new_health = build_team.grade_generation(population)

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