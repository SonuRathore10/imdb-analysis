import json
import csv

def title_table():
    try:
        with open("title.basics.tsv") as fd:
            rd = csv.reader(fd, delimiter="\t", quotechar='"')
            output = []
            for row in rd:
                output.append({
                    "tconst" : row[0],
                    "title_type": row[1],
                    "primary_title" : row[2],
                    "original_title": row[3],
                    "is_adult" : row[4],
                    "start_year": row[5],
                    "end_year" : row[6],
                    "runtime_minutes": row[7],
                })                
            
            output.pop(0)
            
            file = open( "titles.csv", "w")
            fileWriter = csv.writer(file , delimiter=",",quotechar='"')

            Header = ['tconst','title_type','primary_title','original_title','is_adult','start_year','end_year','runtime_minutes']

            fileWriter.writerow(Header)

            for x in output:
                te = [x['tconst'],x['title_type'],x['primary_title'],x['original_title'],x['is_adult'],x['start_year'],x['end_year'],x['runtime_minutes']]
                fileWriter.writerow(te)
            file.close()

    except Exception as err:
        print("This is the Error Messsage: ", err)

def genres_table():
    try:
        with open("title.basics.tsv") as fd:
            rd = csv.reader(fd, delimiter="\t", quotechar='"')
            output_genres = []
            genre_dict = {} 
            genre_id_counter = 1  

            for row in rd:
                tconst = row[0]
                genres = row[-1].split(",")

                for genre in genres:
                    genre = genre.strip()
                    if genre not in genre_dict:
                        genre_dict[genre] = genre_id_counter
                        genre_id_counter += 1

                    output_genres.append({
                        "tconst": tconst,
                        "genre_id": genre_dict[genre]
                    })

            if output_genres and output_genres[0]["tconst"] == "tconst":
                output_genres.pop(0)

            with open("genres.csv", "w", newline='') as file:
                writer = csv.writer(file, delimiter=",", quotechar='"')
                writer.writerow(['tconst', 'genre_id'])  
                for x in output_genres:
                    writer.writerow([x['tconst'], x['genre_id']])

            with open("genre_lookup.csv", "w", newline='') as lookup_file:
                lookup_writer = csv.writer(lookup_file, delimiter=",", quotechar='"')
                lookup_writer.writerow(['genre_id', 'genre'])  
                for genre, gid in genre_dict.items():
                    lookup_writer.writerow([gid, genre])

    except Exception as err:
        print("This is the Error Message: ", err)

def alternate_titles():
    try:

        with open("title.akas.tsv") as fd:
            rd = csv.reader(fd, delimiter="\t", quotechar='"')
            output_alternate_titles = []
            for row in rd:
                output_alternate_titles.append({
                    "tconst": row[0],
                    "ordering": row[1],
                    "title": row[2],
                    "region": row[3],
                    "language": row[4],
                    "is_original": row[-1],
                })

            output_alternate_titles.pop(0)
            
            with open("alternate_titles.csv", "w", newline='') as file:
                writer = csv.writer(file, delimiter=",", quotechar='"')
                writer.writerow(['tconst', 'ordering', 'title', 'region', 'language', 'is_original'])  
                for x in output_alternate_titles:
                    writer.writerow([x['tconst'], x['ordering'], x['title'], x['region'], x['language'], x['is_original'],])
    except Exception as err:
        print("This is the error: ", err)
        
def ratings_title():
    try:

        with open("title.ratings.tsv") as fd:
            rd = csv.reader(fd, delimiter="\t", quotechar='"')
            output_ratings = []
            for row in rd:
                print(row)
                output_ratings.append({
                    "tconst": row[0],
                    "average_rating": row[1],
                    "num_votes": row[2],
                })
            output_ratings.pop(0)
            with open("ratings.csv", "w", newline='') as file:
                writer = csv.writer(file, delimiter=",", quotechar='"')
                writer.writerow(['tconst', 'average_rating', 'num_votes'])  
                for x in output_ratings:
                    writer.writerow([x['tconst'], x['average_rating'], x['num_votes']])
    
    except Exception as err:
        print("This is the error: ", err)


def title_directors_producer():
    try:
        with open("title.crew.tsv") as fd:
            rd = csv.reader(fd, delimiter="\t", quotechar='"')
            next(rd)

            director_data = []
            writer_data = []

            for row in rd:
                tconst = row[0]
                directors = row[1]
                writers = row[2]

                if directors != "\\N":
                    for director in directors.split(","):
                        director_data.append([tconst, director.strip()])

                if writers != "\\N":
                    for writer in writers.split(","):
                        writer_data.append([tconst, writer.strip()])

            with open("title_directors.csv", "w", newline='', encoding="utf-8") as f1:
                writer1 = csv.writer(f1)
                writer1.writerow(['tconst', 'nconst']) 
                writer1.writerows(director_data)

            with open("title_writers.csv", "w", newline='', encoding="utf-8") as f2:
                writer2 = csv.writer(f2)
                writer2.writerow(['tconst', 'nconst'])  
                writer2.writerows(writer_data)


    except Exception as err:
        print("This is the error: ", err)

def episodes():
    try:
        with open("title.episode.tsv") as fd:
            rd = csv.reader(fd, delimiter="\t", quotechar='"')
            output_ratings = []
            for row in rd:
                print(row)
                output_ratings.append({
                    "tconst": row[0],
                    "parent_tconst": row[1],
                    "season_number": row[2],
                    "episode_number": row[3],
                })
            
            output_ratings.pop(0)

            with open("episodes.csv", "w", newline='') as file:
                writer = csv.writer(file, delimiter=",", quotechar='"')
                writer.writerow(['tconst', 'parent_tconst', 'season_number', 'episode_number'])  
                for row in output_ratings:
                    writer.writerow([row['tconst'], row['parent_tconst'], row['season_number'], row['episode_number']])
    
    except Exception as err:
        print("This is the error: ", err)

def principals_extraction():
    try:
        with open("title.principals.tsv") as fd:
            rd = csv.reader(fd, delimiter="\t", quotechar='"')
            output_principals = []
            for row in rd:
                output_principals.append({
                    "tconst": row[0],
                    "nconst": row[1],
                    "ordering": row[2],
                    "category": row[3],
                    "job": row[2],
                    "character_name": row[-1].replace("[","").replace("]","").replace('"',""),
                })
            
            output_principals.pop(0)

            with open("principals.csv", "w", newline='') as file:
                writer = csv.writer(file, delimiter=",", quotechar='"')
                writer.writerow(['tconst', 'nconst', 'ordering', 'category', 'job', 'character_name'])  
                for row in output_principals:
                    writer.writerow([row['tconst'], row['nconst'], row['ordering'], row['category'], row['job'], row['character_name']])
    
    except Exception as err:
        print("This is the error: ", err)


def people():
    try:
        with open("name.basics.tsv") as fd:
            rd = csv.reader(fd, delimiter="\t", quotechar='"')
            output_principals = []
            for row in rd:
                output_principals.append({
                    "nconst": row[0],
                    "primary_name": row[1],
                    "birth_year": row[2],
                    "death_year": row[3],
                })
            
            output_principals.pop(0)

            print(output_principals)

            with open("people.csv", "w", newline='') as file:
                writer = csv.writer(file, delimiter=",", quotechar='"')
                writer.writerow(['nconst', 'primary_name', 'birth_year', 'death_year'])  
                for row in output_principals:
                    writer.writerow([row['nconst'], row['primary_name'], row['birth_year'], row['death_year']])
    
    except Exception as err:
        print("This is the error: ", err)


def professions():
    try: 
        with open("name.basics.tsv") as fd:
            rd = csv.reader(fd, delimiter="\t", quotechar='"')
            output_professions = []

            for row in rd:

                nconst = row[0]
                profession_str = row[4]

                if profession_str != "\\N":
                    for profession in profession_str.split(","):
                        output_professions.append({
                            "nconst": nconst,
                            "profession": profession.strip()
                        })

            if output_professions and output_professions[0]["nconst"] == "nconst":
                output_professions.pop(0)

            with open("professions.csv", "w", newline='', encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(['nconst', 'profession'])  

                for item in output_professions:
                    writer.writerow([item['nconst'], item['profession']])

    except Exception as err:
        print("This is the error: ", err)


def known_for():
    try:
        with open("name.basics.tsv", encoding="utf-8") as fd:
            rd = csv.reader(fd, delimiter="\t", quotechar='"')
            output_known_for = []

            for row in rd:

                nconst = row[0]
                known_titles_str = row[5]

                if known_titles_str != "\\N":
                    for tconst in known_titles_str.split(","):
                        output_known_for.append({
                            "nconst": nconst,
                            "tconst": tconst.strip()
                        })


            if output_known_for and output_known_for[0]["nconst"] == "nconst":
                output_known_for.pop(0)

            with open("known_for.csv", "w", newline='', encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(['nconst', 'tconst']) 

                for item in output_known_for:
                    writer.writerow([item['nconst'], item['tconst']])


    except Exception as err:
        print("This is the error: ", err)


known_for()

if __name__ == "__main__":
    title_table()
    genres_table()
    alternate_titles()
    ratings_title()
    title_directors_producer()
    episodes()
    principals_extraction()
    people()
    professions()
    known_for() 
