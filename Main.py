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
    
    # Create a dict of the summoners and their respective champion/mastery data
    for player in summoners:
        #summoner_data[player] = data_grabber._gimme_data(player, champs)
        summoner_id, summoner_name = data_grabber.get_summoner_data(player)
        champ_points_pair = data_grabber.get_summoners_mastery(summoner_id, summoner_name, num_champs)
        champ_counters = data_grabber.lanes_and_roles(summoner_id, summoner_name, champ_points_pair)
        data_grabber.percentages(champ_counters)
        structured_data = data_grabber.data_compile(summoner_id, summoner_name, champ_counters, champ_points_pair)
        summoner_data.update(structured_data)

    build_team = DoMath()
    # Get the squad
    # Build the dream
    try:
        dream_team = build_team.compute_team(summoner_data)
    except:
        exit('You woke up, the dream is gone')
        
    # Output for the website
    print(dream_team)
    return dream_team
    
if __name__ == '__main__':
    main()