from RiotAPI import RiotAPI

def main():
    api = RiotAPI('e6e27f9f-d47d-4b3f-96d4-3aab2c2b8cee')
    response = api.get_summoner_by_name('KmancXC')
    print (response)

if __name__ == '__main__':
    main()