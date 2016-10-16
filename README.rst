===============================
SQL to Excel converter
===============================


.. image:: https://img.shields.io/pypi/v/sqlexceller.svg
        :target: https://pypi.python.org/pypi/sqlexceller

.. image:: https://img.shields.io/pypi/pyversions/sqlexceller.svg
         :target: https://pypi.python.org/pypi/sqlexceller

.. image:: https://img.shields.io/:license-apache-blue.svg
         :target: http://www.apache.org/licenses/LICENSE-2.0

Command line program that executes SQL queries and stores results in Excel files


* Free software: Apache Software License 2.0


Features
--------

* Support for PostgreSQL, MySQL, Oracle, MSSQL, and SQLite
* Accepts multiple SQL query files
* Each SQL query will be written into a different sheet
* Parametrized queries
* Parametrized output filename

Installation
------------

To install all you need to do is run:

.. code-block:: bash

    $ pip install --upgrade sqlexceller

Usage Help
----------
::

  usage: sqlexceller [-h] [-v] [--output OUTPUT] [--db_connection_info URL]
                     [--param PARAMS]
                     file [file ...]

  sqlexceller tool
      The tool will execute SQL queries and generate an Excel file with the
      results.

  positional arguments:
    file                  SQL Query file

  optional arguments:
    -h, --help            show this help message and exit
    -v, --version         show program's version number and exit
    --output OUTPUT, -o OUTPUT
                          Output file
    --db_connection_info URL, -d URL
                          DB connection information as an URL in the form of
                            dialect[+driver]://username:password@host:port/database.
    --param PARAMS, -p PARAMS
                          Adds a parameter for the SQL queries. Parameter must
                          be specified as a key=value pair.  This argument can
                          be repeated as many times as necessary.

  Available dialects and drivers are:
    - postgresql:
      - psycopg2
      - pg8000
    - mysql:
      - mysqldb
      - mysqlconnector
      - oursql
    - oracle:
      - cx_oracle
    - mssql:
      - pyodbc
      - pymssql
    - sqlite

  There are some default parameters that will always be present:
    - NUM_QUERY
    - QUERY_NAME
    - DATE
    - DAY
    - MONTH
    - YEAR

  Usage examples:
    - Execute a simple query on a SQLite DB.
        sqlexceller query.sql -d sqlite:///example.db

    - Execute multiple queries with 2 different parameters and a custom output
      file on a PostgreSQL DB:

        Contents of query1.sql:
          SELECT *
          FROM stocks
          where transaction = :transaction;

        Contents of query2.sql:
          SELECT *
          FROM stocks
          where transaction = :transaction and product = :product;

        sqlexceller query1.sql query2.sql -p transaction=BUY -p product=HAT \
            -o "report :trans (:MONTH-:DAY).xlsx"

        Generated file will be something like: "report BUY (10-16).xlsx"

Reporting an issue
------------------

If you've found an issue with sqlexceller here's how you can report the problem:

- Preferred method is filing a bug on GitHub:

  1. Go to project's `issue tracker on GitHub`_
  2. Search for existing issues using the search field at the top of the page
  3. File a new issue with information on the problem
  4. Thanks for helping make sqlexceller better

- If you don't have a GitHub account and don't wish to create one you can just
  drop me an email.


.. _issue tracker on GitHub: https://github.com/Akrog/sqlexceller/issues
