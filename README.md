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
├── pyproject.toml   ← REQUIRED
├── src/
│   ├── models/
│   ├── db/
│   ├── utils/
├── tests/
├── main.py

src/
  models/        # Pydantic data models
  db/            # SQLite wrapper
  utils/         # CSV loader + helpers

tests/
  models/        # unit tests for models

data/
  csv/           # raw input files

main.py          # pipeline entry point