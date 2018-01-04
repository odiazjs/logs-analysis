# logs-analysis
A python program that analyzes logs from a postgresql database.

# Setup the database

1. Download the database zip file from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
2. To load the data, cd into the vagrant directory and use the command ``psql -d news -f newsdata.sql.``

### Here's what this command does: ###
`psql` — the PostgreSQL command line program
``-d news`` — connect to the database named news which has been set up for you
``-f newsdata.sql`` — run the SQL statements in the file newsdata.sql
  Running this command will connect to your installed database server and execute the SQL commands in the downloaded file,       creating tables and populating them with data.

# Run the project

1. Execute the following command at project root
- ` ~/usr/project-root/ python3 run.py `
