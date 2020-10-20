RANK = 0
COUNTRY = 1
RATING = 2
BYEAR = 3

def open_file(filename):
    #Returns a file_stream
    try:
        file_stream = open(filename, 'r')
        return file_stream
    except FileNotFoundError:    
        return None

def create_player_dict(file_stream):
    #Returns a dict for player where each entry is a player
    player_dict = {}

    for line in file_stream:
        rank, name, country, rating, byear = line.split(';')
        
        lastname, firstname = name.split(',')

        country = country.strip()
        firstname = firstname.strip()
        lastname = lastname.strip()

        key = '{} {}'.format(firstname, lastname)

        value_tuple = (int(rank), country, int(rating), int(byear))

        player_dict[key] = value_tuple

    return player_dict

def create_country_dict(player_dict):
    #Returns a dict for countries where each entry is
    #the country and the players in the country
    country_dict = {}

    for player, player_values in player_dict.items():
        country = player_values[COUNTRY]
        
        if country in country_dict:
            country_dict[country].append(player)
        else:    
            country_dict[country] = [player]
    
    return country_dict

def get_average_rating(player_list, player_dict):
    ratings = [player_dict[player][RATING] for player in player_list]
    average = sum(ratings)/len(ratings)
    
    return average

def print_header(header_str):
    print(header_str)
    print('-' * (len(header_str)-1))
    

def print_sorted(country_dict, player_dict):
    sorted_countries = sorted(country_dict.items())
    
    print_header('Players by country: ')

    for country, player_list in sorted_countries:
        player_count = len(player_list)
        average_rating = get_average_rating(player_list, player_dict)
        print('{} ({}) ({:.1f}):'.format(country, player_count, average_rating))

        for player in player_list:
            rating = player_dict[player][RATING]
            print('{:>40}{:>10d}'.format(player, rating))

    



def main():
    filename = input('Enter filename: ')
    file_stream = open_file(filename)
    
    if file_stream:
        player_dict = create_player_dict(file_stream)
        country_dict = create_country_dict(player_dict)
        print_sorted(country_dict, player_dict)

if __name__ == '__main__':
    main()
