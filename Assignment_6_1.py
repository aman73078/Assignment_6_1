# Q1. What is a database? Differentiate between SQL and NoSQL databases.

# Ans- Database is the collection of organized data that is structured or unstructured. The database's primary goal
#      is to store a huge amount of data. Many dynamic websites on the Internet today are stored in databases.
#      Examples of some databases: MySQL, Oracle, MongoDB, PostgreSQL, SQL Server, etc.

#      Difference between SQL and NoSQL databases:-
#              1. SQL databases are relational, and NoSQL databases are non-relational.
#              2. SQL databases use structured query language (SQL) and have a predefined schema. NoSQL databases 
#                 have dynamic schemas for unstructured data.
#              3. SQL databases are vertically scalable, while NoSQL databases are horizontally scalable.
#              4. SQL databases are table-based, while NoSQL databases are document, key-value, graph, or wide-
#                 column stores.
#              5. SQL databases are better for multi-row transactions, while NoSQL is better for unstructured data 
#                 like documents or JSON.


# Q2. What is DDL? Explain why CREATE, DROP, ALTER, and TRUNCATE are used with an example.

# Ans- SQL(Structured Query Language) commands are used to create and maintain Databases. Data Definition 
#      Language(DDL) is a type of SQL command used to define the components of databases using Database 
#      Management Systems.
#      Data Definition Language(DDL) commands in DBMS are used to define the database objects. We can 
#      create, delete and alter tables using DDL commands. Since a database structure is designed by DDL 
#      commands, they are called Data Definition Languages (DDLs). They consist of commands such as CREATE,
#      ALTER, TRUNCATE, and DROP.
#      
#  CREATE :- CREATE is a data definition language(DDL) command that is used for creating database objects such as 
#                database and database table.

    # Syntax to Create a Database:
    #    CREATE DATABASE Database_name;
    # Here is an example to illustrate database creation in SQL
    #    CREATE DATABASE Student_details;
# 
#  ALTER :- ALTER command in SQL is used to add, rename or modify, drop/delete columns in an existing database 
#          table. It can further be used to add and remove various constraints on an existing database table.
    # The syntax used for renaming a table is as follows:
    #   ALTER TABLE table_name_1
    #   RENAME TO table_new_name;

    # Here is an example to rename an existing database table.
    #   ALTER TABLE customer_details
    #   RENAME TO customer_may;
# 
#  TRUNCATE :- TRUNCATE TABLE command is used to remove all the data records from the database table. It deletes 
#             all the rows permanently. Ergo, we cannot perform a rollback operation to undo a TRUNCATE command.
    # The generic syntax used for writing TRUNCATE command is as follows :
    #     TRUNCATE TABLE table_name;

    # Now let us have a look at an example illustrating TRUNCATE command.
    #     TRUNCATE TABLE customer_may;
# 
#  DROP :- DROP TABLE SQL command is used to delete a database object from the database. We can even delete the 
#         database using the DROP command. We cannot perform a rollback operation to undo a DROP database/table 
#         command.
    # The basic syntax for writing DROP command to delete a database in SQL is as follows :
    #     DROP DATABASE database_name;

    # The syntax for writing DROP command to delete a database in SQL is as follows :
    #     DROP TABLE table_name;

    # Here are a few examples to illustrate the use of the DROP command in SQL.
    #     DROP TABLE customer_may;


# Q3. What is DML? Explain INSERT, UPDATE, and DELETE with an example.

# Ans- Data Manipulation Language (DML) commands in SQL manage data records stored within the database tables. It 
#      does not deal with changes to database objects and their structure. The commonly known DML commands are 
#      INSERT, UPDATE, and DELETE.
# 
#  INSERT :- INSERT commands in SQL are used to insert data records or rows in a database table. In an INSERT 
#           statement, we specify both the column_names for which the entry has to be made along with the data 
#           value that has to be inserted.
    # The basic syntax for writing INSERT statements in SQL is as follows :
    #       INSERT INTO table_name (column_name_1, column_name_2, column_name_3, ...)
    #       VALUES (value1, value2, value3, ...)

    # By VALUES, we mean the value of the corresponding columns.

    # Here are a few examples to further illustrate the INSERT statement.
    #     INSERT INTO public.customers(
    #     customer_id, sale_date, sale_amount, salesperson, store_state, order_id)
    #     VALUES (1005,'2019-12-12',4200,'R K Rakesh','MH','1007');
# 
#  UPDATE :- UPDATE command or statement is used to modify the value of an existing column in a database table.

    # The syntax for writing an UPDATE statement is as follows :
    #     UPDATE table_name
    #     SET column_name_1 = value1, column_name_2 = value2, ...
    #     WHERE condition;

    # Having learned the syntax, let us now try an example based on the UPDATE statement in SQL.
    #     UPDATE customers
    #     SET store_state = 'DL'
    #     WHERE store_state = 'NY';
# 
#  DELETE :- DELETE statement in SQL is used to remove one or more rows from the database table. It does not delete
#           the data records permanently. We can always perform a rollback operation to undo a DELETE command. 
#           With DELETE statements, we can use the WHERE clause for filtering specific rows.
    # The syntax for writing a DELETE statement is as follows :
    #      DELETE FROM table_name WHERE condition;

    # Having learned the syntax, we are all set to try an example based on the DELETE command in SQL.
    #      DELETE FROM customers
    #      WHERE store_state = 'MH'
    #      AND customer_id = '1001';


# Q4. What is DQL? Explain SELECT with an example.

# Ans- DQL statements are used for performing queries on the data within schema objects. The purpose of the DQL 
#      Command is to get some schema relation based on the query passed to it. We can define DQL as follows it is a
#      component of SQL statement that allows getting data from the database and imposing order upon it. It 
#      includes the SELECT statement. This command allows getting the data out of the database to perform 
#      operations with it.

#  SELECT :- The SELECT command is used to query or retrieve data from a table in the database. It is used 
#           to retrieve a subset of records from one or more tables.

    # The syntax for the SELECT statement is:
    #    SELECT column1 as c1
    #    column2 as c2
    #    ...
    #    from table_name;

    # Example:-
    #    select age as myAge
    #    from my_table;

    #    select * from my_table;

# Q5. Explain Primary Key and Foreign Key.

# Ans- Primary Key:- In SQL, a Primary Key is a special relational database table field or a combination of fields
#                    that uniquely identifies a record in the table of multiple records. The main feature of the 
#                    primary key is it holds a unique value for each row of table data in the database.
#                    In the DBMS table, there should be only one primary key, and none of those fields with a 
#                    primary field can contain NULL A table with only one Primary Key Constraint with single or 
#                    multiple columns. But when we use more than one field as a Primary Key, it is known as a 
#                    Composite Key. Suppose we have defined a column as a Primary Key; then there should not be 
#                    any two records with the same value as that of the column.
# ​
#      Foreign Key:- A Foreign Key in SQL refers to a column or a group of columns used to connect two tables from 
#                    the same database to perform any operations on the contents of the tables. One table’s Foreign
#                    key is connected to the primary key (has unique values and is a uniquely identified column in 
#                    that table) of another table, which is used to allow a relationship between both the tables.
# ​
#                    So, if you have 1-to-many or many-to-many relations in the database, foreign keys will be very
#                    useful. It acts as a cross-reference between two tables (parent_table and child_table) because
#                    it references the primary key of another table. So it establishes a link between parent_table 
#                    and child_table.


# Q6. Write a python code to connect MySQL to python. Explain the cursor() and execute() method.
# Ans-

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)

# .cursor() :- Cursors are created by the connection. cursor() method: they are bound to the connection for the 
#              entire lifetime and all the commands are executed in the context of the database session wrapped by
#              the connection.

# .execute() :- The Execute method executes the query, SQL statement or procedure specified in the CommandText 
#               property of the Command object. The results are stored in a new Recordset object if it is a 
#               row-returning query. A closed Recordset object will be returned if it is not a row-returning query.

# Q7. Give the order of execution of SQL clauses in an SQL query.

# Ans- The order of execution of SQL clauses in an SQL query :- 
    #      1    FROM     - 	Tables are joined to get the base data.
    #      2	WHERE	 -  The base data is filtered.
    #      3	GROUP BY -  The filtered base data is grouped.
    #      4	HAVING	 -  The grouped base data is filtered.
    #      5	SELECT	 -  The final data is returned.
    #      6	ORDER BY -	The final data is sorted.
    #      7	LIMIT	 -  The returned data is limited to row count.
