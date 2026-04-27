import sqlite3

from utils import SQLiteDB, CSVLoader
from models import OfferReward, CustomerOffer, CustomerOfferReward, CustomerOfferRedemption

data_to_populate = {
    "offer_rewards": {
        "model": OfferReward,
        "csv_path": "src/csv_data/offer_rewards_168083.csv",
    },
    "customer_offers": {
        "model": CustomerOffer,
        "csv_path": "src/csv_data/customer_offers_296332.csv",
    },
    "customer_offer_rewards": {
        "model": CustomerOfferReward,
        "csv_path": "src/csv_data/customer_offer_rewards_144392.csv",
    },
    "customer_offer_redemptions": {
            "model": CustomerOfferRedemption,
            "csv_path": "src/csv_data/customer_offer_redemptions_31025.csv"
    },
}

database_name = "ibotta_test2.db"
db = SQLiteDB(database_name)
loader = CSVLoader()

for table_name, dataset in data_to_populate.items():
    model = dataset["model"]
    csv_path = dataset["csv_path"]

    # create table from Pydantic model
    db.create_table(model, table_name)

    # load CSV
    csv_data =loader.load(
        csv_path,
        model
    )

    print(f"Records to load for {table_name}: {len(csv_data)}")
    print(f"First record: {csv_data[0]}")

    print(f"Inserting data into {table_name}...")
    db.insert_data(model, table_name, csv_data)

db.close()