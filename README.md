
# 🎬 IMDb Database Project

This project builds a structured, queryable database from raw IMDb `.tsv` files using Python and SQLite. It supports in-depth analysis of movie ratings, genres, creators, cast members, and relationships between TV episodes and series.

---

## 📌 Project Overview

IMDb provides massive datasets in `.tsv` format, which are hard to query directly. This project:
- Cleans and normalizes those files
- Creates CSVs and imports them into a SQLite3 database
- Defines an ERD-based schema with relationships
- Includes 20+ advanced SQL queries and views for practice

---

## 🗂️ Data Sources

Raw IMDb files used:
- `title.basics.tsv` – Title metadata
- `title.akas.tsv` – Alternate/localized titles
- `title.crew.tsv` – Directors and writers
- `title.episode.tsv` – TV episode info
- `title.principals.tsv` – Cast and crew
- `title.ratings.tsv` – User ratings
- `name.basics.tsv` – People (actors, directors, etc.)

---

## 🔧 Tech Stack

- Python (for data cleaning & CSV generation)
- SQLite3 (for structured relational DB)
- SQL (for querying, analysis, and view creation)

---

## 🧱 Schema Highlights

Normalized tables include:
- `titles`, `ratings`, `genres`, `genre_lookup`
- `alternate_titles`, `episodes`, `title_directors`, `title_writers`
- `principals`, `people`, `professions`, `known_for`

Each table is connected via primary and foreign keys to ensure relational integrity.

---

## 🧠 SQL Queries & Views

The project includes:
- `imdb_queries.sql` – core query views
- `imdb_advanced_queries.sql` – 20 advanced views
- `imdb_advanced_queries_with_selects.sql` – views + matching SELECTs

### Examples:
- Top-rated titles with > 100k votes
- Most common professions
- Titles with multiple genres
- Actors who also directed
- Genre-wise average ratings
- Ranking titles per genre

---

## 📂 Folder Structure

```
imdb-project/
├── data/                  # Raw .tsv files
├── csv/                   # Cleaned CSV outputs
├── scripts/               # Python scripts for ETL
├── sql/                   # SQL queries and views
├── docs/                  # ERD, README, visuals
└── imdb.sqlite3           # Final database
```

---

## 📈 What You’ll Learn

- Working with raw data files and cleaning them
- Normalizing and structuring relational databases
- Writing advanced SQL queries and creating views
- Designing a data project from extraction to analysis

---

## 🚀 Future Extensions

- Add a Streamlit/Flask UI to explore data
- Use PostgreSQL/MySQL for larger-scale DB
- Add full-text search for names and titles
- Build dashboards using Power BI or Tableau

---

## 🙌 Credits

IMDb data is made available under the [IMDb Datasets Terms of Use](https://www.imdb.com/interfaces/).

---

## 📬 Questions?

Reach out if you’d like help running this project or extending it!

