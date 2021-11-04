# ******************************
# Tomer Griba 325105625
# Ido Sar Shalom 212410146
# ******************************
import socket
import threading
from player import *
from question_array import *
from random import random

# Max clients in the server
MAX_CLIENTS = 3
# Create a server open socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 39212

print('Server started!')

# Bind the server to the host and port values and listen for new clients
sock.bind((host, port))
sock.listen(MAX_CLIENTS)

clients = []

# Chaser game function
def start_game(conn, address):
    # concatenate a string to the client
    string_to_client = ""
    # continue playing flag
    continuePlaying = True
    while continuePlaying:
        string_to_client += "Do you want to play the chaser game? (Answer Y/N)\n"
        # send the string_to_client
        conn.send(string_to_client.encode())

        # receive and decode message from client
        msg = conn.recv(1024)
        msg = msg.decode()

        if msg == 'Y':
            # create player and question_bank objects for the game
            question_bank = QuestionsPool()
            game_player = player()

            string_to_client = ""
            string_to_client += "Welcome to the first step of the game, where you will receive 3 questions\n"

            # loop first 3 questions for the player
            money_for_current_question = 5000
            numberOfQuestions = 3
            for i in range(numberOfQuestions):
                string_to_client += "Question " + str(i + 1) + "\n"

                # randomize a question to the player
                returned_question = question_bank.randomize_question()

                string_to_client += str(returned_question.get_question())
                conn.send(string_to_client.encode())

                # receive and decode message from client
                msg = conn.recv(1024)
                msg = msg.decode()

                # check for invalid input error
                if msg.isdigit():
                    if returned_question.is_correct_answer(int(msg)):
                        string_to_client = "The answer was right\n"
                        game_player.add_money(money_for_current_question) # raise the player's money
                    else:
                        string_to_client = "The answer was wrong\n"
                else:
                    string_to_client = "The answer was wrong\n"

            # all answers were wrong
            if game_player.get_money() == 0:
                string_to_client = "The player answered all the questions wrong, return to the beginning of the game\n"

            else:
                # second stage of the game
                is_valid_input = False

                while not is_valid_input:
                    string_to_client += "Welcome to stage 2, please choose one of the options\n" \
                            "Choose 1 in order to start from level 3 with the current amount of money\n" \
                            "Choose 2 in order to start from level 2 with and double your money\n" \
                            "Choose 3 in order to get away from the chaser and start from level 4 with half of your money\n"

                    conn.send(string_to_client.encode())

                    msg = conn.recv(1024)
                    msg = msg.decode()

                    # check for invalid input error
                    if msg.isdigit():
                        msg = int(msg)

                    # set the place of the player according to input

                    if msg == 1:
                        game_player.set_place(3)
                        is_valid_input = True

                    elif msg == 2:
                        game_player.set_money(game_player.get_money() * 2)
                        game_player.set_place(2)
                        is_valid_input = True

                    elif msg == 3:
                        game_player.set_money(game_player.get_money()/2)
                        game_player.set_place(4)
                        is_valid_input = True

                    else:
                        string_to_client = "Invalid input\n"

                # third stage of the game

                string_to_client = "************************************************************\n" + \
                       "Now let's start the game against the chaser !\n" + \
                       "Each correct answer will move the player one step forward to the bank.\n" \
                       "Answering wrong question will cause the player to stay in his current place.\n" \
                       "By pressing the tav 'h' on the keyboard the player can eliminate two wrong answers of the question.\n" + \
                       "Remember the player can only use it ones.\n" + \
                       "************************************************************\n\n"

                # Continue to the game against the chaser
                chaser_location = 0
                bank_location = 7
                while (game_player.get_place() is not chaser_location and game_player.get_place() is not bank_location):
                    # Print status
                    string_to_client += "Player's current money is " + str(
                        game_player.get_money()) + ", Player's location is " + str(
                        game_player.get_place()) + ", Chaser location is " + str(chaser_location)

                    # player's help button
                    if game_player.get_help():
                        string_to_client += ", Player can use the help button ('h')\n"
                    else:
                        string_to_client += ", Player already used the help button\n"

                    string_to_client += "Current questions is:\n"

                    returned_question = question_bank.randomize_question()

                    string_to_client += returned_question.get_question()
                    conn.send(string_to_client.encode())

                    # receive and decode message from client
                    msg = conn.recv(1024)
                    msg = msg.decode()

                    # check for player's help button
                    if msg == "h":
                        if game_player.get_help():
                            game_player.use_help()
                            string_to_client = "The player chose the help button\n" + returned_question.get_help_question()
                        else:
                            string_to_client = "Player already used the help button\n"
                        conn.send(string_to_client.encode())
                        msg = conn.recv(1024)
                        msg = msg.decode()

                    # check for invalid input error, and feedback for the player
                    if msg.isdigit():
                        if returned_question.is_correct_answer(int(msg)):
                            string_to_client = "The player answered correctly\n"
                            game_player.add_place(1) # add 1 to the player's place
                        else:
                            string_to_client = "The player was wrong\n"
                    else:
                        string_to_client = "The player was wrong\n"

                    # chaser answer the question right with 75%
                    if random() <= 0.75:
                        chaser_location += 1
                        string_to_client += "The chaser answered correctly\n"
                    else:
                        string_to_client += "The chaser was wrong\n"

                # Check for the game winner
                if chaser_location == game_player.get_place():
                    string_to_client = "chaser won\n"
                else:
                    string_to_client = "Player won\n"
        # Client chose not to play the game
        elif msg == 'N':
            continuePlaying = False
        # invalid input
        else:
            string_to_client = "Invalid input, please try again\n"
    # remove the current client from the list
    clients.remove(conn)
    # close the connection
    conn.close()

# server full funtion - no more clients can connect to the server
def server_full(client_socket, address):
    # send server full message to the client
    client_socket.send("Server is full".encode())
    # remove the current client from the list
    clients.remove(client_socket)
    # close the connection
    client_socket.close()



while True:
    conn, addr = sock.accept()
    # Add new client to the clients list
    clients.append(conn)
    # Check for space in the server
    if len(clients) > MAX_CLIENTS:
        # Create thred to the game function
        thread = threading.Thread(target=server_full, args=(conn, addr))
        thread.start()
    # Server is full
    else:
        # Create thred to the server full function
        thread = threading.Thread(target=start_game, args=(conn, addr))
        thread.start()

# Close the server
sock.close()