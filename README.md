# portf-lio-

# Web Scraping & Data Analysis with Python

A collection of small projects where I practice web scraping and data
manipulation. Everything here was built on Termux (Android), using just
a phone and a lot of curiosity.

## Projects

### JSON Quote Scraper
File: `Pandas_preview`

A scraper that talks directly to a public JSON API
(quotes.toscrape.com) instead of parsing HTML. It fetches the raw data,
deserializes it into Python dictionaries and loads everything into a
pandas DataFrame, flattening nested fields like author names with
`.apply()` and `lambda`.

What I learned here:
- Consuming REST endpoints with `requests`
- Deserializing JSON into native Python structures
- Normalizing nested data into clean DataFrame columns

### Exploratory Analysis with Pandas
File: `Basic_scraper.py`

Takes the raw data collected by the scraper and turns it into something
actually analyzable: cleaning columns, creating derived fields and
running simple aggregations to explore the dataset.

What I learned here:
- Building DataFrames from lists of dictionaries
- Column transformation with `.apply()`
- Basic data cleaning and aggregation

## Environment

Everything in this repo was developed on Termux (Android) with
Python 3.12+, which proves you don't need a fancy machine to start
learning data engineering.

## How to run

```bash
pip install requests pandas
python Basic_scraper.py
```

## Roadmap

- Add pagination to the JSON scraper
- Export results to CSV
- More APIs, more datasets
