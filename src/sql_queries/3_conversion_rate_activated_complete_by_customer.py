from utils.sqlite_db import SQLiteDB

database_name = "ibotta_test2.db"
db = SQLiteDB(database_name)

# 3) What is the conversion rate of activated to complete for each customer?
# conversion rate = number of completed offers / number of activated offers for each customer

# tables to use:
# customer_offers - customer_id, offer_id, activated
# offer_rewards - offer_reward_id, offer_id
# customer_offer_rewards - customer_id, finished, offer_reward_id

# Find the number of activated offers for each customer
# join to offer_rewards to get the id to use as offer_reward_id in customer_offer_rewards 
# Find the number of completed customer offer rewards (finished is not null))
# For each customer, from their set of activated offers, check is those offers were completed
# Divide the counts of the customers completed activated offers by the total activated offers to find conversion rate

query =db.execute(
    """
    WITH activated_offer_reward_ids AS(
    SELECT DISTINCT
        co.customer_id,
        orw.id AS offer_reward_id
    FROM offer_rewards orw
    INNER JOIN customer_offers co ON orw.offer_id = co.offer_id
    WHERE co.activated IS NOT NULL
    ),
    completed_offer_reward_ids AS (
    SELECT DISTINCT
        customer_id,
        offer_reward_id
    FROM customer_offer_rewards
    WHERE finished IS NOT NULL
    )

    SELECT DISTINCT
        aor.customer_id,
        COUNT(cor.offer_reward_id) AS completed,
        COUNT(aor.offer_reward_id) AS activated,
        (COUNT(distinct cor.offer_reward_id) * 1.0 / COUNT(distinct aor.offer_reward_id)) AS conversion_rate
    FROM activated_offer_reward_ids aor
    LEFT JOIN completed_offer_reward_ids cor ON aor.offer_reward_id = cor.offer_reward_id AND aor.customer_id = cor.customer_id
    GROUP BY aor.customer_id
    """
)

print(query)
print(query[0])
# for customer_id 40390000 the 2 active offers are 685652 and 747457
#  offer_reward_id for offer_id 685652 is 722086, completed
#  offer_reward_id for offer_id 747457 is 784210, completed
# customer has 2 other offer rewards that were not completed but also not activated so rate is 1.0 or 100%