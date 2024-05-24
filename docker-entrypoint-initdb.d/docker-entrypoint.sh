#!/bin/bash

# Create database
psql -U postgres -d postgres -c "CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, mail VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL);"

# Populate users table
psql -U postgres -d postgres -c "INSERT INTO users (name, mail, password) VALUES ('John Doe', 'john@example.com', 'mysecretpassword');"

# Create projects table
psql -U postgres -d postgres -c "CREATE TABLE IF NOT EXISTS projects (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL);"

# Populate projects table
psql -U postgres -d postgres -c "INSERT INTO projects (name) VALUES ('My Project');"

# Create timelogs table
psql -U postgres -d postgres -c "CREATE TABLE IF NOT EXISTS timelogs (id SERIAL PRIMARY KEY, content TEXT NOT NULL, project_id INTEGER NOT NULL, user_id INTEGER NOT NULL);"

# Populate timelogs table
psql -U postgres -d postgres -c "INSERT INTO timelogs (content, project_id, user_id) VALUES ('Logged some time', 1, 1);"