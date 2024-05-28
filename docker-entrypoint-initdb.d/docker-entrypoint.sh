#!/bin/bash

# Create database
psql -U postgres -d postgres -c 'CREATE EXTENSION IF NOT EXISTS "pgcrypto";'
#psql -U postgres -d postgres -c "CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, mail VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL);"
psql -U postgres -d postgres -c "CREATE TABLE IF NOT EXISTS person (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    first_name TEXT NOT NULL CHECK (first_name ~ '^[a-zA-Z\xC0-\uFFFF]+([ \-'']{0,1}[a-zA-Z\xC0-\uFFFF]+){0,2}[.]{0,1}$'),
    middle_name TEXT CHECK (middle_name ~ '^[a-zA-Z\xC0-\uFFFF]+([ \-'']{0,1}[a-zA-Z\xC0-\uFFFF]+){0,2}[.]{0,1}$'),
    last_name TEXT CHECK (last_name ~ '^[a-zA-Z\xC0-\uFFFF]+([ \-'']{0,1}[a-zA-Z\xC0-\uFFFF]+){0,2}[.]{0,1}$'),
    email TEXT NOT NULL
);"

#r"^(?:[!#-\[\]-\u{10FFFF}]|\\[\t -\u{10FFFF}])*\"|[!#-'*+\-/-9=?A-Z\^-\u{10FFFF}](?:\.?[!#-'*+\-/-9=?A-Z\^-\u{10FFFF}])*)@([!#-'*+\-/-9=?A-Z\^-\u{10FFFF}](?:\.?[!#-'*+\-/-9=?A-Z\^-\u{10FFFF}])*|\[[!-Z\^-\u{10FFFF}]*\])$"

# Populate users table
#psql -U postgres -d postgres -c "INSERT INTO users (name, mail, password) VALUES ('John Doe', 'john@example.com', 'mysecretpassword');"
psql -U postgres -d postgres -c "INSERT INTO person (first_name, middle_name, email) VALUES ('John', 'Doe', 'john@example.com');"

# Create projects table
psql -U postgres -d postgres -c "CREATE TABLE IF NOT EXISTS projects (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL);"

# Populate projects table
psql -U postgres -d postgres -c "INSERT INTO projects (name) VALUES ('My Project');"

# Create timelogs table
psql -U postgres -d postgres -c "CREATE TABLE IF NOT EXISTS timelogs (id SERIAL PRIMARY KEY, content TEXT NOT NULL, project_id INTEGER NOT NULL, user_id INTEGER NOT NULL);"

# Populate timelogs table
psql -U postgres -d postgres -c "INSERT INTO timelogs (content, project_id, user_id) VALUES ('Logged some time', 1, 1);"