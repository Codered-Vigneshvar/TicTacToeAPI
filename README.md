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

<a name="root"></a><br/><br/><br/>
[⬜](#1) [⬜](#2) [⬜](#3)<br/>[⬜](#4) [⬜](#5) [⬜](#6)<br/>[⬜](#7) [⬜](#8) [⬜](#9)<br/><br/><br/><br/>
<a name="1"></a><br/><br/><br/>
✖️ [⬜](#10) [⬜](#11)<br/>[⬜](#12) ⭕ [⬜](#13)<br/>[⬜](#14) [⬜](#15) [⬜](#16)<br/><br/><br/><br/>
<a name="2"></a><br/><br/><br/>
⭕ ✖️ [⬜](#17)<br/>[⬜](#18) [⬜](#19) [⬜](#20)<br/>[⬜](#21) [⬜](#22) [⬜](#23)<br/><br/><br/><br/>
<a name="3"></a><br/><br/><br/>
[⬜](#24) [⬜](#25) ✖️<br/>[⬜](#26) ⭕ [⬜](#27)<br/>[⬜](#28) [⬜](#29) [⬜](#30)<br/><br/><br/><br/>
<a name="4"></a><br/><br/><br/>
⭕ [⬜](#31) [⬜](#32)<br/>✖️ [⬜](#33) [⬜](#34)<br/>[⬜](#35) [⬜](#36) [⬜](#37)<br/><br/><br/><br/>
<a name="5"></a><br/><br/><br/>
⭕ [⬜](#38) [⬜](#39)<br/>[⬜](#40) ✖️ [⬜](#41)<br/>[⬜](#42) [⬜](#43) [⬜](#44)<br/><br/><br/><br/>
<a name="6"></a><br/><br/><br/>
[⬜](#45) [⬜](#46) ⭕<br/>[⬜](#47) [⬜](#48) ✖️<br/>[⬜](#49) [⬜](#50) [⬜](#51)<br/><br/><br/><br/>
<a name="7"></a><br/><br/><br/>
[⬜](#52) [⬜](#53) [⬜](#54)<br/>[⬜](#55) ⭕ [⬜](#56)<br/>✖️ [⬜](#57) [⬜](#58)<br/><br/><br/><br/>
<a name="8"></a><br/><br/><br/>
[⬜](#59) ⭕ [⬜](#60)<br/>[⬜](#61) [⬜](#62) [⬜](#63)<br/>[⬜](#64) ✖️ [⬜](#65)<br/><br/><br/><br/>
<a name="9"></a><br/><br/><br/>
[⬜](#66) [⬜](#67) [⬜](#68)<br/>[⬜](#69) ⭕ [⬜](#70)<br/>[⬜](#71) [⬜](#72) ✖️<br/><br/><br/><br/>
<a name="10"></a><br/><br/><br/>
✖️ ✖️ ⭕<br/>[⬜](#73) ⭕ [⬜](#74)<br/>[⬜](#75) [⬜](#76) [⬜](#77)<br/><br/><br/><br/>
<a name="11"></a><br/><br/><br/>
✖️ ⭕ ✖️<br/>[⬜](#78) ⭕ [⬜](#79)<br/>[⬜](#80) [⬜](#81) [⬜](#82)<br/><br/><br/><br/>
<a name="12"></a><br/><br/><br/>
✖️ [⬜](#83) [⬜](#84)<br/>✖️ ⭕ [⬜](#85)<br/>⭕ [⬜](#86) [⬜](#87)<br/><br/><br/><br/>
<a name="13"></a><br/><br/><br/>
✖️ ⭕ [⬜](#88)<br/>[⬜](#89) ⭕ ✖️<br/>[⬜](#90) [⬜](#91) [⬜](#92)<br/><br/><br/><br/>
<a name="14"></a><br/><br/><br/>
✖️ [⬜](#93) [⬜](#94)<br/>⭕ ⭕ [⬜](#95)<br/>✖️ [⬜](#96) [⬜](#97)<br/><br/><br/><br/>
<a name="15"></a><br/><br/><br/>
✖️ [⬜](#98) [⬜](#99)<br/>⭕ ⭕ [⬜](#100)<br/>[⬜](#101) ✖️ [⬜](#102)<br/><br/><br/><br/>
<a name="16"></a><br/><br/><br/>
✖️ ⭕ [⬜](#103)<br/>[⬜](#104) ⭕ [⬜](#105)<br/>[⬜](#106) [⬜](#107) ✖️<br/><br/><br/><br/>
<a name="17"></a><br/><br/><br/>
⭕ ✖️ ✖️<br/>⭕ [⬜](#108) [⬜](#109)<br/>[⬜](#110) [⬜](#111) [⬜](#112)<br/><br/><br/><br/>
<a name="18"></a><br/><br/><br/>
⭕ ✖️ [⬜](#113)<br/>✖️ ⭕ [⬜](#114)<br/>[⬜](#115) [⬜](#116) [⬜](#117)<br/><br/><br/><br/>
<a name="19"></a><br/><br/><br/>
⭕ ✖️ [⬜](#118)<br/>[⬜](#119) ✖️ [⬜](#120)<br/>[⬜](#121) ⭕ [⬜](#122)<br/><br/><br/><br/>
<a name="20"></a><br/><br/><br/>
⭕ ✖️ [⬜](#123)<br/>[⬜](#124) [⬜](#125) ✖️<br/>⭕ [⬜](#126) [⬜](#127)<br/><br/><br/><br/>
<a name="21"></a><br/><br/><br/>
⭕ ✖️ [⬜](#128)<br/>[⬜](#129) ⭕ [⬜](#130)<br/>✖️ [⬜](#131) [⬜](#132)<br/><br/><br/><br/>
<a name="22"></a><br/><br/><br/>
⭕ ✖️ [⬜](#133)<br/>[⬜](#134) ⭕ [⬜](#135)<br/>[⬜](#136) ✖️ [⬜](#137)<br/><br/><br/><br/>
<a name="23"></a><br/><br/><br/>
⭕ ✖️ [⬜](#138)<br/>[⬜](#139) ⭕ [⬜](#140)<br/>[⬜](#141) [⬜](#142) ✖️<br/><br/><br/><br/>
<a name="24"></a><br/><br/><br/>
✖️ ⭕ ✖️<br/>[⬜](#143) ⭕ [⬜](#144)<br/>[⬜](#145) [⬜](#146) [⬜](#147)<br/><br/><br/><br/>
<a name="25"></a><br/><br/><br/>
⭕ ✖️ ✖️<br/>[⬜](#148) ⭕ [⬜](#149)<br/>[⬜](#150) [⬜](#151) [⬜](#152)<br/><br/><br/><br/>
<a name="26"></a><br/><br/><br/>
⭕ [⬜](#153) ✖️<br/>✖️ ⭕ [⬜](#154)<br/>[⬜](#155) [⬜](#156) [⬜](#157)<br/><br/><br/><br/>
<a name="27"></a><br/><br/><br/>
[⬜](#158) [⬜](#159) ✖️<br/>[⬜](#160) ⭕ ✖️<br/>[⬜](#161) [⬜](#162) ⭕<br/><br/><br/><br/>
<a name="28"></a><br/><br/><br/>
[⬜](#163) ⭕ ✖️<br/>[⬜](#164) ⭕ [⬜](#165)<br/>✖️ [⬜](#166) [⬜](#167)<br/><br/><br/><br/>
<a name="29"></a><br/><br/><br/>
[⬜](#168) [⬜](#169) ✖️<br/>⭕ ⭕ [⬜](#170)<br/>[⬜](#171) ✖️ [⬜](#172)<br/><br/><br/><br/>
<a name="30"></a><br/><br/><br/>
[⬜](#173) [⬜](#174) ✖️<br/>[⬜](#175) ⭕ ⭕<br/>[⬜](#176) [⬜](#177) ✖️<br/><br/><br/><br/>
<a name="31"></a><br/><br/><br/>
⭕ ✖️ [⬜](#178)<br/>✖️ ⭕ [⬜](#179)<br/>[⬜](#180) [⬜](#181) [⬜](#182)<br/><br/><br/><br/>
<a name="32"></a><br/><br/><br/>
⭕ [⬜](#183) ✖️<br/>✖️ ⭕ [⬜](#184)<br/>[⬜](#185) [⬜](#186) [⬜](#187)<br/><br/><br/><br/>
<a name="33"></a><br/><br/><br/>
⭕ [⬜](#188) [⬜](#189)<br/>✖️ ✖️ ⭕<br/>[⬜](#190) [⬜](#191) [⬜](#192)<br/><br/><br/><br/>
<a name="34"></a><br/><br/><br/>
⭕ [⬜](#193) [⬜](#194)<br/>✖️ ⭕ ✖️<br/>[⬜](#195) [⬜](#196) [⬜](#197)<br/><br/><br/><br/>
<a name="35"></a><br/><br/><br/>
⭕ ⭕ [⬜](#198)<br/>✖️ [⬜](#199) [⬜](#200)<br/>✖️ [⬜](#201) [⬜](#202)<br/><br/><br/><br/>
<a name="36"></a><br/><br/><br/>
⭕ [⬜](#203) ⭕<br/>✖️ [⬜](#204) [⬜](#205)<br/>[⬜](#206) ✖️ [⬜](#207)<br/><br/><br/><br/>
<a name="37"></a><br/><br/><br/>
⭕ [⬜](#208) ⭕<br/>✖️ [⬜](#209) [⬜](#210)<br/>[⬜](#211) [⬜](#212) ✖️<br/><br/><br/><br/>
<a name="38"></a><br/><br/><br/>
⭕ ✖️ [⬜](#213)<br/>[⬜](#214) ✖️ [⬜](#215)<br/>[⬜](#216) ⭕ [⬜](#217)<br/><br/><br/><br/>
<a name="39"></a><br/><br/><br/>
⭕ [⬜](#218) ✖️<br/>[⬜](#219) ✖️ [⬜](#220)<br/>⭕ [⬜](#221) [⬜](#222)<br/><br/><br/><br/>
<a name="40"></a><br/><br/><br/>
⭕ [⬜](#223) [⬜](#224)<br/>✖️ ✖️ ⭕<br/>[⬜](#225) [⬜](#226) [⬜](#227)<br/><br/><br/><br/>
<a name="41"></a><br/><br/><br/>
⭕ [⬜](#228) [⬜](#229)<br/>⭕ ✖️ ✖️<br/>[⬜](#230) [⬜](#231) [⬜](#232)<br/><br/><br/><br/>
<a name="42"></a><br/><br/><br/>
⭕ [⬜](#233) ⭕<br/>[⬜](#234) ✖️ [⬜](#235)<br/>✖️ [⬜](#236) [⬜](#237)<br/><br/><br/><br/>
<a name="43"></a><br/><br/><br/>
⭕ ⭕ [⬜](#238)<br/>[⬜](#239) ✖️ [⬜](#240)<br/>[⬜](#241) ✖️ [⬜](#242)<br/><br/><br/><br/>
<a name="44"></a><br/><br/><br/>
⭕ [⬜](#243) ⭕<br/>[⬜](#244) ✖️ [⬜](#245)<br/>[⬜](#246) [⬜](#247) ✖️<br/><br/><br/><br/>
<a name="45"></a><br/><br/><br/>
✖️ [⬜](#248) ⭕<br/>⭕ [⬜](#249) ✖️<br/>[⬜](#250) [⬜](#251) [⬜](#252)<br/><br/><br/><br/>
<a name="46"></a><br/><br/><br/>
[⬜](#253) ✖️ ⭕<br/>⭕ [⬜](#254) ✖️<br/>[⬜](#255) [⬜](#256) [⬜](#257)<br/><br/><br/><br/>
<a name="47"></a><br/><br/><br/>
[⬜](#258) [⬜](#259) ⭕<br/>✖️ ⭕ ✖️<br/>[⬜](#260) [⬜](#261) [⬜](#262)<br/><br/><br/><br/>
<a name="48"></a><br/><br/><br/>
[⬜](#263) [⬜](#264) ⭕<br/>⭕ ✖️ ✖️<br/>[⬜](#265) [⬜](#266) [⬜](#267)<br/><br/><br/><br/>
<a name="49"></a><br/><br/><br/>
⭕ [⬜](#268) ⭕<br/>[⬜](#269) [⬜](#270) ✖️<br/>✖️ [⬜](#271) [⬜](#272)<br/><br/><br/><br/>
<a name="50"></a><br/><br/><br/>
⭕ [⬜](#273) ⭕<br/>[⬜](#274) [⬜](#275) ✖️<br/>[⬜](#276) ✖️ [⬜](#277)<br/><br/><br/><br/>
<a name="51"></a><br/><br/><br/>
⭕ [⬜](#278) ⭕<br/>[⬜](#279) [⬜](#280) ✖️<br/>[⬜](#281) [⬜](#282) ✖️<br/><br/><br/><br/>
<a name="52"></a><br/><br/><br/>
✖️ [⬜](#283) [⬜](#284)<br/>⭕ ⭕ [⬜](#285)<br/>✖️ [⬜](#286) [⬜](#287)<br/><br/><br/><br/>
<a name="53"></a><br/><br/><br/>
⭕ ✖️ [⬜](#288)<br/>[⬜](#289) ⭕ [⬜](#290)<br/>✖️ [⬜](#291) [⬜](#292)<br/><br/><br/><br/>
<a name="54"></a><br/><br/><br/>
[⬜](#293) ⭕ ✖️<br/>[⬜](#294) ⭕ [⬜](#295)<br/>✖️ [⬜](#296) [⬜](#297)<br/><br/><br/><br/>
<a name="55"></a><br/><br/><br/>
⭕ [⬜](#298) [⬜](#299)<br/>✖️ ⭕ [⬜](#300)<br/>✖️ [⬜](#301) [⬜](#302)<br/><br/><br/><br/>
<a name="56"></a><br/><br/><br/>
[⬜](#303) ⭕ [⬜](#304)<br/>[⬜](#305) ⭕ ✖️<br/>✖️ [⬜](#306) [⬜](#307)<br/><br/><br/><br/>
<a name="57"></a><br/><br/><br/>
[⬜](#308) [⬜](#309) [⬜](#310)<br/>[⬜](#311) ⭕ [⬜](#312)<br/>✖️ ✖️ ⭕<br/><br/><br/><br/>
<a name="58"></a><br/><br/><br/>
[⬜](#313) [⬜](#314) [⬜](#315)<br/>[⬜](#316) ⭕ [⬜](#317)<br/>✖️ ⭕ ✖️<br/><br/><br/><br/>
<a name="59"></a><br/><br/><br/>
✖️ ⭕ [⬜](#318)<br/>[⬜](#319) [⬜](#320) [⬜](#321)<br/>⭕ ✖️ [⬜](#322)<br/><br/><br/><br/>
<a name="60"></a><br/><br/><br/>
[⬜](#323) ⭕ ✖️<br/>[⬜](#324) [⬜](#325) [⬜](#326)<br/>⭕ ✖️ [⬜](#327)<br/><br/><br/><br/>
<a name="61"></a><br/><br/><br/>
[⬜](#328) ⭕ [⬜](#329)<br/>✖️ [⬜](#330) [⬜](#331)<br/>⭕ ✖️ [⬜](#332)<br/><br/><br/><br/>
<a name="62"></a><br/><br/><br/>
⭕ ⭕ [⬜](#333)<br/>[⬜](#334) ✖️ [⬜](#335)<br/>[⬜](#336) ✖️ [⬜](#337)<br/><br/><br/><br/>
<a name="63"></a><br/><br/><br/>
[⬜](#338) ⭕ [⬜](#339)<br/>[⬜](#340) [⬜](#341) ✖️<br/>⭕ ✖️ [⬜](#342)<br/><br/><br/><br/>
<a name="64"></a><br/><br/><br/>
[⬜](#343) ⭕ [⬜](#344)<br/>[⬜](#345) [⬜](#346) [⬜](#347)<br/>✖️ ✖️ ⭕<br/><br/><br/><br/>
<a name="65"></a><br/><br/><br/>
[⬜](#348) ⭕ [⬜](#349)<br/>[⬜](#350) [⬜](#351) [⬜](#352)<br/>⭕ ✖️ ✖️<br/><br/><br/><br/>
<a name="66"></a><br/><br/><br/>
✖️ ⭕ [⬜](#353)<br/>[⬜](#354) ⭕ [⬜](#355)<br/>[⬜](#356) [⬜](#357) ✖️<br/><br/><br/><br/>
<a name="67"></a><br/><br/><br/>
⭕ ✖️ [⬜](#358)<br/>[⬜](#359) ⭕ [⬜](#360)<br/>[⬜](#361) [⬜](#362) ✖️<br/><br/><br/><br/>
<a name="68"></a><br/><br/><br/>
[⬜](#363) [⬜](#364) ✖️<br/>[⬜](#365) ⭕ ⭕<br/>[⬜](#366) [⬜](#367) ✖️<br/><br/><br/><br/>
<a name="69"></a><br/><br/><br/>
⭕ [⬜](#368) [⬜](#369)<br/>✖️ ⭕ [⬜](#370)<br/>[⬜](#371) [⬜](#372) ✖️<br/><br/><br/><br/>
<a name="70"></a><br/><br/><br/>
[⬜](#373) [⬜](#374) ⭕<br/>[⬜](#375) ⭕ ✖️<br/>[⬜](#376) [⬜](#377) ✖️<br/><br/><br/><br/>
<a name="71"></a><br/><br/><br/>
[⬜](#378) [⬜](#379) [⬜](#380)<br/>[⬜](#381) ⭕ [⬜](#382)<br/>✖️ ⭕ ✖️<br/><br/><br/><br/>
<a name="72"></a><br/><br/><br/>
[⬜](#383) [⬜](#384) [⬜](#385)<br/>[⬜](#386) ⭕ [⬜](#387)<br/>⭕ ✖️ ✖️<br/><br/><br/><br/>
<a name="73"></a><br/><br/><br/>
✖️ ✖️ ⭕<br/>✖️ ⭕ ⬜<br/>⭕ ⬜ ⬜<br/>O wins!!!<br/>[Care to play again?](#root)<br/><br/><br/>
<a name="74"></a><br/><br/><br/>
✖️ ✖️ ⭕<br/>⬜ ⭕ ✖️<br/>⭕ ⬜ ⬜<br/>O wins!!!<br/>[Care to play again?](#root)<br/><br/><br/>
<a name="75"></a><br/><br/><br/>
✖️ ✖️ ⭕<br/>⭕ ⭕ [⬜](#388)<br/>✖️ [⬜](#389) [⬜](#390)<br/><br/><br/><br/>
<a name="76"></a><br/><br/><br/>
✖️ ✖️ ⭕<br/>⬜ ⭕ ⬜<br/>⭕ ✖️ ⬜<br/>O wins!!!<br/>[Care to play again?](#root)<br/><br/><br/>
<a name="77"></a><br/><br/><br/>
✖️ ✖️ ⭕<br/>⬜ ⭕ ⬜<br/>⭕ ⬜ ✖️<br/>O wins!!!<br/>[Care to play again?](#root)<br/><br/><br/>
<a name="78"></a><br/><br/><br/>
✖️ ⭕ ✖️<br/>✖️ ⭕ ⬜<br/>⬜ ⭕ ⬜<br/>O wins!!!<br/>[Care to play again?](#root)<br/><br/><br/>
<a name="79"></a><br/><br/><br/>
✖️ ⭕ ✖️<br/>⬜ ⭕ ✖️<br/>⬜ ⭕ ⬜<br/>O wins!!!<br/>[Care to play again?](#root)<br/><br/><br/>
<a name="80"></a><br/><br/><br/>
✖️ ⭕ ✖️<br/>⬜ ⭕ ⬜<br/>✖️ ⭕ ⬜<br/>O wins!!!<br/>[Care to play again?](#root)<br/><br/><br/>
<a name="81"></a><br/><br/><br/>
✖️ ⭕ ✖️<br/>⭕ ⭕ [⬜](#391)<br/>[⬜](#392) ✖️ [⬜](#393)<br/><br/><br/><br/>
<a name="82"></a><br/><br/><br/>
✖️ ⭕ ✖️<br/>⬜ ⭕ ⬜<br/>⬜ ⭕ ✖️<br/>O wins!!!<br/>[Care to play again?](#root)<br/><br/><br/>
<a name="83"></a><br/><br/><br/>
✖️ ✖️ ⭕<br/>✖️ ⭕ ⬜<br/>⭕ ⬜ ⬜<br/>O wins!!!<br/>[Care to play again?](#root)<br/><br/><br/>
<a name="84"></a><br/><br/><br/>
✖️ ⭕ ✖️<br/>✖️ ⭕ [⬜](#394)<br/>⭕ [⬜](#395) [⬜](#396)<br/><br/><br/><br/>
<a name="85"></a><br/><br/><br/>
✖️ ⬜ ⭕<br/>✖️ ⭕ ✖️<br/>⭕ ⬜ ⬜<br/>O wins!!!<br/>[Care to play again?](#root)<br/><br/><br/>
<a name="86"></a><br/><br/><br/>
✖️ ⬜ ⭕<br/>✖️ ⭕ ⬜<br/>⭕ ✖️ ⬜<br/>O wins!!!<br/>[Care to play again?](#root)<br/><br/><br/>
<a name="87"></a><br/><br/><br/>
✖️ ⬜ ⭕<br/>✖️ ⭕ ⬜<br/>⭕ ⬜ ✖️<br/>O wins!!!<br/>[Care to play again?](#root)<br/><br/><br/>
<a name="88"></a><br/><br/><br/>
✖️ ⭕ ✖️<br/>⬜ ⭕ ✖️<br/>⬜ ⭕ ⬜<br/>O wins!!!<br/>[Care to play again?](#root)<br/><br/><br/>
<a name="89"></a><br/><br/><br/>
✖️ ⭕ ⬜<br/>✖️ ⭕ ✖️<br/>⬜ ⭕ ⬜<br/>O wins!!!<br/>[Care to play again?](#root)<br/><br/><br/>
<a name="90"></a><br/><br/><br/>
✖️ ⭕ ⬜<br/>⬜ ⭕ ✖️<br/>✖️ ⭕ ⬜<br/>O wins!!!<br/>[Care to play again?](#root)<br/><br/><br/>
<a name="91"></a><br/><br/><br/>
✖️ ⭕ [⬜](#397)<br/>[⬜](#398) ⭕ ✖️<br/>⭕ ✖️ [⬜](#399)<br/><br/><br/><br/>
<a name="92"></a><br/><br/><br/>
✖️ ⭕ ⬜<br/>⬜ ⭕ ✖️<br/>⬜ ⭕ ✖️<br/>O wins!!!<br/>[Care to play again?](#root)<br/><br/><br/>
<a name="93"></a><br/><br/><br/>
✖️ ✖️ ⬜<br/>⭕ ⭕ ⭕<br/>✖️ ⬜ ⬜<br/>O wins!!!<br/>[Care to play again?](#root)<br/><br/><br/>
<a name="94"></a><br/><br/><br/>
✖️ ⬜ ✖️<br/>⭕ ⭕ ⭕<br/>✖️ ⬜ ⬜<br/>O wins!!!<br/>[Care to play again?](#root)<br/><br/><br/>
<a name="95"></a><br/><br/><br/>
✖️ ⭕ [⬜](#400)<br/>⭕ ⭕ ✖️<br/>✖️ [⬜](#401) [⬜](#402)<br/><br/><br/><br/>
<a name="96"></a><br/><br/><br/>
✖️ ⬜ ⬜<br/>⭕ ⭕ ⭕<br/>✖️ ✖️ ⬜<br/>O wins!!!<br/>[Care to play again?](#root)<br/><br/><br/>
<a name="97"></a><br/><br/><br/>
✖️ ⬜ ⬜<br/>⭕ ⭕ ⭕<br/>✖️ ⬜ ✖️<br/>O wins!!!<br/>[Care to play again?](#root)<br/><br/><br/>
<a name="98"></a><br/><br/><br/>
✖️ ✖️ ⬜<br/>⭕ ⭕ ⭕<br/>⬜ ✖️ ⬜<br/>O wins!!!<br/>[Care to play again?](#root)<br/><br/><br/>
<a name="99"></a><br/><br/><br/>
✖️ ⬜ ✖️<br/>⭕ ⭕ ⭕<br/>⬜ ✖️ ⬜<br/>O wins!!!<br/>[Care to play again?](#root)<br/><br/><br/>
<a name="100"></a><br/><br/><br/>
✖️ [⬜](#403) ⭕<br/>⭕ ⭕ ✖️<br/>[⬜](#404) ✖️ [⬜](#405)<br/><br/><br/><br/>
<a name="101"></a><br/><br/><br/>
✖️ ⬜ ⬜<br/>⭕ ⭕ ⭕<br/>✖️ ✖️ ⬜<br/>O wins!!!<br/>[Care to play again?](#root)<br/><br/><br/>
<a name="102"></a><br/><br/><br/>
✖️ ⬜ ⬜<br/>⭕ ⭕ ⭕<br/>⬜ ✖️ ✖️<br/>O wins!!!<br/>[Care to play again?](#root)<br/><br/><br/>
<a name="103"></a><br/><br/><br/>
✖️ ⭕ ✖️<br/>⬜ ⭕ ⬜<br/>⬜ ⭕ ✖️<br/>O wins!!!<br/>[Care to play again?](#root)<br/><br/><br/>
<a name="104"></a><br/><br/><br/>
✖️ ⭕ ⬜<br/>✖️ ⭕ ⬜<br/>⬜ ⭕ ✖️<br/>O wins!!!<br/>[Care to play again?](#root)<br/><br/><br/>
<a name="105"></a><br/><br/><br/>
✖️ ⭕ ⬜<br/>⬜ ⭕ ✖️<br/>⬜ ⭕ ✖️<br/>O wins!!!<br/>[Care to play again?](#root)<br/><br/><br/>
<a name="106"></a><br/><br/><br/>
✖️ ⭕ ⬜<br/>⬜ ⭕ ⬜<br/>✖️ ⭕ ✖️<br/>O wins!!!<br/>[Care to play again?](#root)<br/><br/><br/>
<a name="107"></a><br/><br/><br/>
✖️ ⭕ [⬜](#406)<br/>[⬜](#407) ⭕ [⬜](#408)<br/>⭕ ✖️ ✖️<br/><br/><br/><br/>
<a name="108"></a><br/><br/><br/>
⭕ ✖️ ✖️<br/>⭕ ✖️ ⬜<br/>⭕ ⬜ ⬜<br/>O wins!!!<br/>[Care to play again?](#root)<br/><br/><br/>
<a name="109"></a><br/><br/><br/>

