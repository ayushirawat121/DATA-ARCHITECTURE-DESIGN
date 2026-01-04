from pymongo import MongoClient
import json
import os

# ----------------------------
# MongoDB Connection
# ----------------------------
client = MongoClient("mongodb://localhost:27017/")
db = client["fleximart_nosql"]
collection = db["products"]

# ----------------------------
# Load JSON file
# ----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(BASE_DIR, "products_catalog.json")

with open(json_path, "r", encoding="utf-8") as file:
    products_data = json.load(file)

# ----------------------------
# Operation 1: Insert data into MongoDB
# ----------------------------
if isinstance(products_data, list):
    collection.insert_many(products_data)
else:
    collection.insert_one(products_data)

print("Product catalog data loaded successfully")


# ----------------------------
# Operation 2: Basic Query
# ----------------------------
query = {
    "category": "Electronics",
    "price": {"$lt": 50000}
}

projection = {
    "_id": 0,
    "name": 1,
    "price": 1,
    "stock": 1
}

results = collection.find(query, projection)

print("Electronics products with price < 50000:")
for product in results:
    print(product)


# ----------------------------
# Operation 3: Review Analysis
# ----------------------------
pipeline = [
    {
        "$addFields": {
            "average_rating": {
                "$avg": "$reviews.rating"
            }
        }
    },
    {
        "$match": {
            "average_rating": {"$gte": 4.0}
        }
    },
    {
        "$project": {
            "_id": 0,
            "name": 1,
            "category": 1,
            "average_rating": 1
        }
    }
]

results = collection.aggregate(pipeline)

print("Products with average rating >= 4.0:")
for product in results:
    print(product)

# ----------------------------
# Operation 4: Update Operation
# ----------------------------
from datetime import datetime

collection.update_one(
    {"product_id": "ELEC001"},
    {
        "$push": {
            "reviews": {
                "user": "U999",
                "rating": 4,
                "comment": "Good value",
                "date": datetime.utcnow()
            }
        }
    }
)

print("New review added successfully to product ELEC001")


# ----------------------------
# Operation 5: Complex Aggregation
# ----------------------------
pipeline = [
    {
        "$group": {
            "_id": "$category",
            "avg_price": {"$avg": "$price"},
            "product_count": {"$sum": 1}
        }
    },
    {
        "$project": {
            "_id": 0,
            "category": "$_id",
            "avg_price": {"$round": ["$avg_price", 2]},
            "product_count": 1
        }
    },
    {
        "$sort": {"avg_price": -1}
    }
]

results = collection.aggregate(pipeline)

print("Average Price by Category:")
for doc in results:
    print(doc)



