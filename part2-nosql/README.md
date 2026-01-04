This part of the project demonstrates the use of MongoDB, a NoSQL document-oriented database, to store and analyze a flexible product catalog for the FlexiMart system.

Unlike relational databases, MongoDB allows schema-less documents, making it suitable for handling products with different attributes and embedded data such as customer reviews.

-------------Technologies Used->
   a. MongoDB Community Server
   b. MongoDB Compass
   c. Python  
   d. PyMongo

--------------Data Used ->
    The product data is stored in a JSON file: products_catalog.json

--------------Database Setup -> 
    Database Name: fleximart_nosql
    Collection Name: products
The database and collection were created using MongoDB Compass.

---------------How to run MongoDB operations
    a. Install dependency - pip install pymongo
    b. mongodb://localhost:27017
    c. python part2-nosql/mongodb_operations.py

Files in this folder -> 
    a. mongodb_operations.py - python script containing MongoDB operations
    b. products_catalog.json - product catalog data
    c. nosql_analysis.md - conceptual analysis of NoSql vs RDBMS 
    d. README.md - documentation for part2