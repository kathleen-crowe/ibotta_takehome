from utils.sqlite_db import SQLiteDB

database_name = "ibotta.db"
db = SQLiteDB(database_name)

# 4) What is the total amount of redemption for each customer?
# customer_offer_redemptions - customer_id, verified_redemption_count, amount
# using the verified redemption count assuming that represents what customers have already redeemed
# for each customer offer, multiply the redemption count by amount to find redemption amount
# join to customer_offers using the customer_offer_id to get the customer_id
# sum the total redemption amount across all offers that customer has redeemed

query =db.execute(
    """
    SELECT DISTINCT
        co.customer_id,
        SUM(cor.verified_redemption_count * cor.offer_amount) OVER (PARTITION BY co.customer_id) AS total_redemption_amount
    FROM customer_offer_redemptions cor
    INNER JOIN customer_offers co 
        on cor.customer_offer_id = co.id
    -- WHERE co.customer_id = 40416955
    ORDER BY co.customer_id;
    """
)

print(query)
print(len(query))
print(query[0]) 
# for customer 40416955
# [(40416955, 1, 0.5, 19956443086, 0.5), 
# (40416955, 1, 0.25, 19956449536, 0.25), 
# (40416955, 1, 1.0, 19956490122, 1.0), 
# (40416955, 1, 1.5, 19956453807, 1.5), 
# (40416955, 1, 0.65, 19956450447, 0.65), 
# (40416955, 1, 0.5, 19956503714, 0.5), 
# (40416955, 1, 1.99, 19956446328, 1.99), 
# (40416955, 2, 1.5, 19956448836, 3.0), 
# (40416955, 3, 0.25, 19956445741, 0.75), 
# (40416955, 1, 1.75, 19956450992, 1.75), 
# (40416955, 1, 3.98, 19956502026, 3.98), 
# (40416955, 1, 2.68, 19956476722, 2.68), 
# (40416955, 1, 2.5, 19956454249, 2.5), 
# (40416955, 1, 1.5, 19956489444, 1.5), 
# (40416955, 1, 2.0, 19956458411, 2.0), 
# (40416955, 1, 1.88, 19956446618, 1.88), 
# (40416955, 1, 2.0, 19956447627, 2.0), 
# (40416955, 1, 1.5, 19956479411, 1.5)]

# so total redemption amount for this customer is [(40416955, 29.93)]