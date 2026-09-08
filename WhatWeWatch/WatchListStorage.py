import csv

class WatchList():
    def __init__(self, path:str=None):
        if path:
            # Open the CSV file safely using a 'with' block
            with open(path, mode='r', encoding='utf-8') as file:
                # Create a DictReader object
                csv_reader = csv.DictReader(file)
                
                # Convert all rows into a list of dictionaries
                self.watch_list = list(csv_reader)

    def print_list(s):
        for item in s.watch_list:
            print()
            print("Movie Name: ", item['movie'])
            print("Is Seen: ", item['is_seen'])
            print("Date Seen: ", item['date'])

    def get_watchlist(s):
        return s.watch_list

    def add_to_watchlist(s, movie:str, is_seen:bool, date:str):
        item = {
            'movie':movie,
            'is_seen':is_seen,
            'date':date
        }
        s.watch_list.append(item)

    def add_to_watchlist(s, movie_info:dict):
        s.watch_list.append(movie_info)

    def save(s, path):
        # Open the CSV file safely using a 'with' block
        with open(path, mode='w', encoding='utf-8') as file:
            fn = s.watch_list[0].keys()
            print(fn)
            # Create a DictReader object
            csv_writer = csv.DictWriter(file, fieldnames=fn)
            
            # Convert all rows into a list of dictionaries
            csv_writer.writeheader()
            csv_writer.writerows(s.watch_list)