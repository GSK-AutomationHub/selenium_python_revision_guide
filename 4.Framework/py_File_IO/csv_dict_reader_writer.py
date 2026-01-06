import csv
actor_movie_dict = {
    'shahrukh':'DDLG',
    'salman':'dabang',
    'amir':'3 idiots'
}

def csv_dict_writer(file_path):
    with open(file_path,'w',newline='') as file:
        fieldnames = ['actor','movie']
        csv_writer = csv.DictWriter(file,fieldnames=fieldnames,delimiter=',')
        csv_writer.writeheader()
        # for actor, movie in actor_movie_dict.items():
        #     csv_writer.writerow({'actor':actor, 'movie':movie})
        rows = [{'actor':actor,'movie':movie} for actor, movie in actor_movie_dict.items()]
        csv_writer.writerows(rows)

csv_dict_writer('actor_movie.csv')

def csv_dict_reader(file_path):
    with open(file_path,'r', newline='') as file:
        csv_reader = csv.DictReader(file,delimiter=',')
        for row in csv_reader:
            print(row)
    # Access by column name:
    print(row['movie'])

csv_dict_reader('actor_movie.csv')