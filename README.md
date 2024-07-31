# Multiplayer Tic-Tac-Toe Game

This is a multiplayer Tic-Tac-Toe game built using Flask for the backend, PostgreSQL for the database, and React for the frontend. The game allows users to register, log in, create games, join games, and play Tic-Tac-Toe.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Frontend](#frontend)


## Features

- User Registration and Authentication
- Create and Join Games
- Real-time Gameplay
- Track Wins and Game History

## Tech Stack

- **Backend:** Flask
- **Database:** PostgreSQL
- **Frontend:** React, React Native
- **Hosting:** AWS EC2

## Installation

### Prerequisites

- Python 3.8+
- PostgreSQL
- AWS EC2
- AWS RDS

### Backend Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/tictactoe-game.git](https://github.com/Codered-Vigneshvar/TicTacToeAPI.git
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Set up the environment variables. Create a `.env` file in the `backend` directory:
    ```env
    DB_HOST=your_db_host
    DB_NAME=TicTacToe
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_PORT=5432
    ```
## Database Setup

1. Create the database:
    ```sql
    CREATE DATABASE TicTacToe;
    ```

2. Create the tables:
    ```sql
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(255) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL,
        wins INT DEFAULT 0
    );

    CREATE TABLE games (
        game_id UUID PRIMARY KEY,
        player1 VARCHAR(255) REFERENCES users(username),
        player2 VARCHAR(255) REFERENCES users(username),
        board CHAR(9) NOT NULL,
        current_turn VARCHAR(255),
        winner VARCHAR(255)
    );
    ```

## Running the Application

### Backend

1. Start the Flask server:
    ```bash
    python final.py
    ```

### Frontend

1. Start the React development server:
    ```bash
    npm start
    ```

## API Endpoints

### User Registration

- **URL:** `/register`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "username": "your_username",
        "password": "your_password"
    }
    ```
- **Response:**
    - `201 Created` on success
    - `400 Bad Request` if username already exists or fields are missing

### User Login

- **URL:** `/get-user-details`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "username": "your_username",
        "password": "your_password"
    }
    ```
- **Response:**
    - `200 OK` on success
    - `401 Unauthorized` if credentials are incorrect

### Create Game

- **URL:** `/create_game`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "username": "your_username"
    }
    ```
- **Response:**
    - `200 OK` with `game_id`

### Join Game

- **URL:** `/join_game`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "username": "your_username",
        "game_id": "game_id"
    }
    ```
- **Response:**
    - `200 OK` on success
    - `400 Bad Request` if the game is full or doesn't exist

### Make Move

- **URL:** `/make_move`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "username": "your_username",
        "game_id": "game_id",
        "move": move_index
    }
    ```
- **Response:**
    - `200 OK` on success
    - `400 Bad Request` if the move is invalid or it's not the user's turn

### Get Game State

- **URL:** `/get_game_state`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "game_id": "game_id"
    }
    ```
- **Response:**
    - `200 OK` with current game state

## Frontend

The frontend is built using React for the web and React Native for mobile. To run the web frontend, use:

npm start

## Blog
For a detailed explanation of how the backend of this Tic-Tac-Toe game was created, please refer to my blog post:
<a href="https://medium.com/@vigneshvars2001/building-a-multiplayer-tic-tac-toe-game-backend-with-flask-f56abd293193" target="_blank">click here</a>.



