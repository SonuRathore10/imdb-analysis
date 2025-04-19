import sqlite3
import csv

def create_tables(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS titles (
            tconst TEXT PRIMARY KEY,
            title_type TEXT,
            primary_title TEXT,
            original_title TEXT,
            is_adult INTEGER,
            start_year INTEGER,
            end_year INTEGER,
            runtime_minutes INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS genre_lookup (
            genre_id INTEGER PRIMARY KEY,
            genre TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS genres (
            tconst TEXT,
            genre_id INTEGER,
            FOREIGN KEY (tconst) REFERENCES titles(tconst),
            FOREIGN KEY (genre_id) REFERENCES genre_lookup(genre_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alternate_titles (
            tconst TEXT,
            ordering INTEGER,
            title TEXT,
            region TEXT,
            language TEXT,
            is_original INTEGER,
            FOREIGN KEY (tconst) REFERENCES titles(tconst)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ratings (
            tconst TEXT PRIMARY KEY,
            average_rating REAL,
            num_votes INTEGER,
            FOREIGN KEY (tconst) REFERENCES titles(tconst)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS title_directors (
            tconst TEXT,
            nconst TEXT,
            FOREIGN KEY (tconst) REFERENCES titles(tconst),
            FOREIGN KEY (nconst) REFERENCES people(nconst)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS title_writers (
            tconst TEXT,
            nconst TEXT,
            FOREIGN KEY (tconst) REFERENCES titles(tconst),
            FOREIGN KEY (nconst) REFERENCES people(nconst)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS episodes (
            tconst TEXT PRIMARY KEY,
            parent_tconst TEXT,
            season_number INTEGER,
            episode_number INTEGER,
            FOREIGN KEY (tconst) REFERENCES titles(tconst),
            FOREIGN KEY (parent_tconst) REFERENCES titles(tconst)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS principals (
            tconst TEXT,
            nconst TEXT,
            ordering INTEGER,
            category TEXT,
            job TEXT,
            character_name TEXT,
            FOREIGN KEY (tconst) REFERENCES titles(tconst),
            FOREIGN KEY (nconst) REFERENCES people(nconst)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS people (
            nconst TEXT PRIMARY KEY,
            primary_name TEXT,
            birth_year INTEGER,
            death_year INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS professions (
            nconst TEXT,
            profession TEXT,
            FOREIGN KEY (nconst) REFERENCES people(nconst)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS known_for (
            nconst TEXT,
            tconst TEXT,
            FOREIGN KEY (nconst) REFERENCES people(nconst),
            FOREIGN KEY (tconst) REFERENCES titles(tconst)
        )
    ''')

def insert_csv_data(cursor, table_name, columns, filename):
    with open(filename, newline='', encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader) 
        placeholders = ",".join(["?" for _ in columns])
        query = f"INSERT INTO {table_name} ({','.join(columns)}) VALUES ({placeholders})"
        for row in reader:
            cursor.execute(query, row)

def main():
    conn = sqlite3.connect("imdb.sqlite3")
    cursor = conn.cursor()

    create_tables(cursor)

    insert_csv_data(cursor, "titles", ['tconst','title_type','primary_title','original_title','is_adult','start_year','end_year','runtime_minutes'], "titles.csv")
    insert_csv_data(cursor, "genre_lookup", ['genre_id', 'genre'], "genre_lookup.csv")
    insert_csv_data(cursor, "genres", ['tconst', 'genre_id'], "genres.csv")
    insert_csv_data(cursor, "alternate_titles", ['tconst', 'ordering', 'title', 'region', 'language', 'is_original'], "alternate_titles.csv")
    insert_csv_data(cursor, "ratings", ['tconst', 'average_rating', 'num_votes'], "ratings.csv")
    insert_csv_data(cursor, "title_directors", ['tconst', 'nconst'], "title_directors.csv")
    insert_csv_data(cursor, "title_writers", ['tconst', 'nconst'], "title_writers.csv")
    insert_csv_data(cursor, "episodes", ['tconst', 'parent_tconst', 'season_number', 'episode_number'], "episodes.csv")
    insert_csv_data(cursor, "principals", ['tconst', 'nconst', 'ordering', 'category', 'job', 'character_name'], "principals.csv")
    insert_csv_data(cursor, "people", ['nconst', 'primary_name', 'birth_year', 'death_year'], "people.csv")
    insert_csv_data(cursor, "professions", ['nconst', 'profession'], "professions.csv")
    insert_csv_data(cursor, "known_for", ['nconst', 'tconst'], "known_for.csv")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
