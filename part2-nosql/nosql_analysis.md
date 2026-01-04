------------------------------Section A: Limitations of RDBMS --------------------------------

Relational databases work best when data has a fixed structure, but they face problems when data keeps changing. In this project, products are stored in tables with fixed columns. This becomes difficult when different products have different attributes. For example, laptops need RAM, processor, and storage details, while shoes need size and color. In an RDBMS, we would need to add many extra columns or create separate tables, which makes the database complex and hard to manage.

Another limitation is frequent schema changes. Whenever a new type of product is added, the table structure must be changed using ALTER statements. This is risky and time-consuming, especially in large databases.

Storing customer reviews is also difficult in relational databases. Reviews often contain nested data like replies and ratings. Representing this in tables requires many joins, which makes queries slow and complicated


--------------------------------Section B: NoSQL Benefits --------------------------------

MongoDB solves many problems faced by relational databases by using a flexible and document-based data model. Unlike RDBMS, MongoDB does not require a fixed schema. This means different products can store different attributes in the same collection. For example, a laptop document can include RAM and processor details, while a shoe document can include size and color without changing the database structure.

MongoDB also supports embedded documents, which makes it easy to store customer reviews directly inside product documents. Reviews, ratings, and comments can be stored together in a nested format. This reduces the need for multiple tables and complex joins, making data retrieval faster and simpler.

Another major advantage of MongoDB is horizontal scalability. MongoDB can distribute data across multiple servers using sharding. This allows the database to handle large volumes of data and high traffic efficiently, making it suitable for applications that grow over time.


-------------------------------- Section C: Trade-offs  --------------------------------

While MongoDB offers flexibility, it also has some disadvantages compared to MySQL. One major drawback is the lack of strong relational integrity. MongoDB does not enforce foreign key constraints, so maintaining relationships between products, orders, and customers must be handled by the application logic, increasing the chance of inconsistent data.

Another disadvantage is complex transaction handling. Although MongoDB supports transactions, they are more limited and can be less efficient than MySQL for multi-table operations such as financial reporting. For applications that require strict consistency and complex joins, MySQL is often more reliable and easier to manage.



