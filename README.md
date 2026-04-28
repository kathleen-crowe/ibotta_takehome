# ibotta_takehome
Take home project for Ibotta Interview

# Setup
Clone Repo
git clone ...
cd ibotta_takehome

Install uv (if not installed)
curl -Ls https://astral.sh/uv/install.sh | sh

Create virtual ENV
uv venv

Install project dependencies
uv pip install -e .

to check package installation: uv pip list

# Testing
uv run pytest

# Run the pipeline
uv run python src/pipeline.py 

# General Checks that data was populated to each table
uv run src/sql_queries/general_checks_table_population.py

# SQL Queries
uv run src/sql_queries/1_count_offer_activation_by_customer.py
uv run src/sql_queries/2_customers_not_active_2_months_back.py
uv run src/sql_queries/3_conversion_rate_activated_complete_by_customer.py
uv run src/sql_queries/4_total_redemption_by_customer.py


# Project structure 
ibotta_takehome/
├── pyproject.toml
├── src/
│   ├── csv_data/ # raw input files
│   ├── models/ # Pydantic data models
│   ├── sql_queries/ # Sql queries for part II (and some provided for db population checks)
│   ├── utils/
├── tests/ # unit tests for models, pipeline utils and db functions
├── pipeline.py # pipeline entry point

I decided to build out a streamline data pipeline to insert into a sql lite database.

I took the utility functions provided and built out a SQLiteDB class.  This class is used throughout the pipeline to create tables in the database, insert records, and also in the part II when accessing data from the database, these generalized DB functions can be used as an ORM type of layer to run SQL queries.

I also build out other utility functions to use the Pydantic data models and translate those to be usable in a SQL lite DB, to make sure model types are handled in a way that is compatible with the database but still uses all the base functionality of Pydantic models to validate and enforce data structures.  Lastly, I turned the csv read function provided into it's own CSV reader class.  This is called in the pipeline to grab data from the raw csv files, I think having a built out class keeps the pipeline code super clean and readable, and also offers future flexibility for how we want to interact with raw data.  In this class, functions can be added to clean and transform the data, or the class can be expanded upon to include the reading of other types of data files that may be used in the future.

The core of this data pipeline is the models.  I chose to use pydantic models because it provides a single source of truth between the raw data and the database.  By building out pydantic models for the data, this ensures the raw data will match what goes into the database and creates an easy to manage tie between the two for ongoing updates to the tables.  The models also allow easy testing on the data and validation enforcement around data types and what data needs to be present in the raw data.

I ran all of these commands and inserted into ibotta_test2.db but updated all the code so you can run the pipeline from scratch into a the ibotta.db and see how the process works.