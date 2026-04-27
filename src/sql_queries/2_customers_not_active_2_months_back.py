from utils.sqlite_db import SQLiteDB

database_name = "ibotta_test2.db"
db = SQLiteDB(database_name)

# 2) Provide a list of customers that who haven't activated an offer in the last couple months?
# customer_offers - customer_id, activated
# Find customers who's last activated date is more than 2 months ago or customers who have never activated an offer (activated is null for all offers for that customer_id)
# MAX activated date - if null for each customer offer then None will return as the max, if there are activated dates then the max will return for comparison.

query =db.execute(
    """
    SELECT DISTINCT
        customer_id,
        MAX(datetime(activated)) AS last_activated_date
    FROM customer_offers
    GROUP BY customer_id
    HAVING last_activated_date IS NULL OR last_activated_date >= datetime('now', '-2 months')
    ORDER BY customer_id;
    """
    )

print(query)
print(len(query)) #239 customers have not activated an offer in the last 2 months or have never activated an offer
print(query[0]) #(40390054, None) - customer_id 40390054 has 2 offers but has never activated an offer

# Data is from 2021 so only things that are being returned here are customers who have never activated an offer.