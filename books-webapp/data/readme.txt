Setting up the books/authors database
CS257 Software Design
Fall 2020
Jeff Ondich

How to set up my books/authors data so you can run my sample web application.

1. Creating the database and using psql

- If you're on your own computer, you know how to set up a database and use psql to populate it and access it. You know your username, you know which database you're using (e.g. "books" or "postgres" or whatever you've been doing your work on), and you know whether you require a password to launch psql.

- If you're logged in to perlman.mathcs.carleton.edu using your Carleton user name (see books-webapp/readme.txt, item 2), then:

  * your database name is your Carleton user name, and you are barred
    from creating new databases (you can try, but it won't work).
    So your books/authors tables will be in the YOURUSERNAME database,
    not in a database named "books" or something like that.
        
  * your user name is your Carleton user name, too

  * you don't need to enter a password

So to connect to your database with psql while logged in to perlman? Just do this:

    psql

NOTE: To do step 2 conveniently, you should cd into books-webapp/data before running psql.


2. The file books.sql is a file I created by setting up my "books" database and then running

    pg_dump --no-owner --no-privileges -U MY_PG_USER_NAME books > books.sql

So you should do this:

- Launch psql and execute this SQL statement: CREATE DATABASE books
- Quit psql
- Run: psql -U YOUR_USER_NAME books < books.sql

This will create and populate the books, authors, and books_authors tables.

This process is faster and easier than manually executing a bunch of CREATE TABLE statements and then \copy for a bunch of .csv files.

