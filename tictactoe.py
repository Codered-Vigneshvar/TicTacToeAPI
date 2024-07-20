from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import uuid

app = Flask(__name__)
CORS(app)

# Database connection details
DB_HOST = "yt-demo.c7s8gqgmm3ln.us-east-2.rds.amazonaws.com"
DB_NAME = "TicTacToe"
DB_USER = "postgres"
DB_PASSWORD = "G7m!X9t#qK2f5B&z4L"
DB_PORT = 5432

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )
    return conn

def initialize_board():
    return [" "] * 9

def check_winner(board):
    winning_combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    
    for combo in winning_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != " ":
            return board[combo[0]]
    
    if " " not in board:
        return "Draw"
    
    return None

@app.route("/")
def home():
    return "home2"

@app.route("/register", methods=["POST"])
def register():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"message": "Request body must be JSON"}), 400

        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({"message": "Missing required fields!"}), 400

        conn = get_db_connection()
        cur = conn.cursor()
        
        insert_query = """
            INSERT INTO users (username, password, wins)
            VALUES (%s, %s, %s)
        """
        cur.execute(insert_query, (username, password, 0))
        conn.commit()
        cur.close()
        conn.close()
        
        return jsonify({"message": "User registered successfully!"}), 201
    
    except psycopg2.IntegrityError:
        conn.rollback()
        cur.close()
        conn.close()
        return jsonify({"message": "Username already exists!"}), 400
    except Exception as e:
        conn.rollback()
        cur.close()
        conn.close()
        return jsonify({"message": "An error occurred: " + str(e)}), 500

@app.route("/get-user-details", methods=["POST"])
def get_user_detail():
    data = request.get_json()
    if not data:
        return jsonify({"message": "Request body must be JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    conn = get_db_connection()
    cur = conn.cursor()

    try:
        select_query = """
            SELECT * FROM users WHERE username = %s AND password = %s
        """
        cur.execute(select_query, (username, password))
        user = cur.fetchone()
        
        if user:
            return jsonify({"status": "success"}), 200
        else:
            return jsonify({"status": "failed"}), 401
    
    except Exception as e:
        return jsonify({"message": "An error occurred: " + str(e)}), 500
    
    finally:
        cur.close()
        conn.close()

@app.route('/create_game', methods=['POST'])
def create_game():
    data = request.get_json()
    username = data.get('username')
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    if not user:
        cur.close()
        conn.close()
        return jsonify({'message': 'Invalid username'}), 400
    
    game_id = str(uuid.uuid4())
    board = ''.join(initialize_board())
    cur.execute(
        "INSERT INTO games (game_id, player1, player2, board, current_turn, winner) VALUES (%s, %s, %s, %s, %s, %s)",
        (game_id, username, None, board, username, None))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'game_id': game_id})

@app.route('/join_game', methods=['POST'])
def join_game():
    data = request.get_json()
    username = data.get('username')
    game_id = data.get('game_id')
    
    if not username or not game_id:
        return jsonify({'message': 'Username and game ID are required'}), 400
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cur.fetchone()
        if not user:
            return jsonify({'message': 'Invalid username'}), 400

        cur.execute("SELECT * FROM games WHERE game_id = %s", (game_id,))
        game = cur.fetchone()
        if not game:
            return jsonify({'message': 'Invalid game ID'}), 400

        if game[1] == username or game[2] == username:
            return jsonify({'message': 'Already in the game'}), 400

        if game[2]:
            return jsonify({'message': 'Game is already full'}), 400

        cur.execute("UPDATE games SET player2 = %s WHERE game_id = %s", (username, game_id))
        conn.commit()
        return jsonify({'message': 'Joined game', 'game_id': game_id})
    
    except Exception as e:
        return jsonify({'message': 'An error occurred: ' + str(e)}), 500
    
    finally:
        cur.close()
        conn.close()

@app.route('/make_move', methods=['POST'])
def make_move():
    data = request.get_json()
    username = data.get('username')
    game_id = data.get('game_id')
    move = data.get('move')

    if not username or not game_id or move is None:
        return jsonify({'message': 'Username, game ID, and move are required'}), 400

    conn = get_db_connection()
    cur = conn.cursor()

    try:
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_SERIALIZABLE)

        cur.execute("SELECT * FROM games WHERE game_id = %s FOR UPDATE", (game_id,))
        game = cur.fetchone()
        if not game:
            return jsonify({'message': 'Invalid game ID'}), 400

        board = list(game[3])
        current_turn = game[4]
        winner = game[5]

        if winner:
            return jsonify({'message': 'Game already has a winner', 'board': ''.join(board), 'winner': winner})

        if username != current_turn:
            return jsonify({'message': 'It\'s not your turn'}), 400

        if board[move] != " ":
            return jsonify({'message': 'Invalid move'}), 400

        board[move] = 'X' if current_turn == game[1] else 'O'
        winner = check_winner(board)
        next_turn = game[2] if current_turn == game[1] else game[1]

        if winner and winner != "Draw":
            update_wins_query = "UPDATE users SET wins = wins + 1 WHERE username = %s"
            winner_username = game[1] if winner == 'X' else game[2]
            cur.execute(update_wins_query, (winner_username,))

        update_query = "UPDATE games SET board = %s, current_turn = %s, winner = %s WHERE game_id = %s"
        cur.execute(update_query, (''.join(board), None if winner else next_turn, winner, game_id))
        conn.commit()

        return jsonify({
            'message': 'Move made',
            'board': ''.join(board),
            'current_player': next_turn if not winner else None,
            'winner': winner
        })
    
    except Exception as e:
        return jsonify({'message': 'An error occurred: ' + str(e)}), 500
    
    finally:
        cur.close()
        conn.close()


@app.route('/get_game_state', methods=['POST'])
def get_game_state():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'Request body must be JSON'}), 400

    game_id = data.get('game_id')
    if not game_id:
        return jsonify({'message': 'Game ID is required'}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        cur.execute("SELECT * FROM games WHERE game_id = %s", (game_id,))
        game = cur.fetchone()
        
        if not game:
            return jsonify({'message': 'Invalid game ID'}), 400
        
        board = list(game[3])  # 4th column for board (9-character string)
        current_turn = game[4]  # 5th column for current_turn
        winner = game[5]  # 6th column for winner

        # Determine the message based on the game state
        if winner:
            message = "Game ended"
            current_player = "None"
        else:
            message = "Game ongoing"
            current_player = current_turn

        # Fetch player names
        cur.execute("SELECT player1, player2 FROM games WHERE game_id = %s", (game_id,))
        players = cur.fetchone()
        if not players:
            return jsonify({'message': 'Players not found for the game'}), 400

        player1, player2 = players

        # Determine winner's name
        if winner == 'X':
            winner_name = player1
        elif winner == 'O':
            winner_name = player2
        else:
            winner_name = "None"

        return jsonify({
            'game_id': game_id,
            'board': ''.join(board),
            'current_player': current_player,
            'message': message,
            'winner': winner_name
        })
    
    except Exception as e:
        return jsonify({'message': 'An error occurred: ' + str(e)}), 500
    
    finally:
        cur.close()
        conn.close()




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
