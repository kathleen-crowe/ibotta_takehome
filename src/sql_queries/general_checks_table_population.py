from utils.sqlite_db import SQLiteDB

database_name = "ibotta_test2.db"
db = SQLiteDB(database_name)

offer_rewards_table_info = db.get_columns("offer_rewards")
print(offer_rewards_table_info)

query =db.execute("SELECT * FROM offer_rewards limit 1")
print(query)

count = db.execute("SELECT COUNT(*) FROM offer_rewards")
print(count)

customer_offer_rewards_table_info = db.get_columns("customer_offer_rewards")
print(customer_offer_rewards_table_info)

query =db.execute("SELECT * FROM customer_offer_rewards limit 1")
print(query)

count = db.execute("SELECT COUNT(*) FROM customer_offer_rewards")
print(count)

customer_offer_redemptions_table_info = db.get_columns("customer_offer_redemptions")
print(customer_offer_redemptions_table_info)

query =db.execute("SELECT * FROM customer_offer_redemptions limit 1")
print(query)

count = db.execute("SELECT COUNT(*) FROM customer_offer_redemptions")
print(count)

customer_offers_table_info = db.get_columns("customer_offers")
print(customer_offers_table_info)

query =db.execute("SELECT * FROM customer_offers limit 1")
print(query)

count = db.execute("SELECT COUNT(*) FROM customer_offers")
print(count)