from utils.sqlite_db import SQLiteDB

database_name = "ibotta.db"
db = SQLiteDB(database_name)

# 1) What is the total counts of offer activations for each customer?
# customer_offers - customer_id, activated
# Find each distinct customer_id and count the activations (activated is not null) for each customer_id, order by customer_id
# Filter out all offers that are not activated (activated is null)
# Can also use a group by customer_id and count(*) I just like window functions

query =db.execute(
    """
    SELECT DISTINCT
        customer_id,
        COUNT(activated) OVER (PARTITION BY customer_id) AS offer_activation_count
    FROM customer_offers
    WHERE activated is NOT NULL
    ORDER BY customer_id;
    """
    )

print(query)
print(len(query))
print(query[0]) #(40390000, 2) - customer_id 40390000 has activated 2 offers, 4 total offers, none verified