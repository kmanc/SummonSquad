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
    if len(args.summoners) != 5 or args.region == None or args.champs == None:
        print(parser.usage)
        exit(0)
    summoners = args.summoners
    region = args.region
    champs = args.champs

    # Set max and min for champs
    if champs < 5:
        champs = 5
    if champs > 25:
        champs = 25
    
    # Normalize summoner names (no spaces, no upper case) because the api can get cranky if you don't
    for name in range(len(summoners)):
        summoners[name] = summoners[name].lower()
        summoners[name] = summoners[name].replace(" ", "")

    summonerList = []
    data_grabber = GetData()
    computations = DoMath()
    
    # Get a list of the summoners and their respective champion/mastery data
    for player in summoners:
        summoner_data = data_grabber._gimme_data(player, champs, region)
        summonerList.append(summoner_data)

    print(summonerList)
    # Get the squad
    # Build the dream
    try:
        dream_team = computations._compute_team(summonerList, summoners)
    except:
        exit('You woke up, the dream is gone')
        
    # Output for the website
    print (dream_team)
    return (summonerList, summoners)    
    
if __name__ == '__main__':
    main()