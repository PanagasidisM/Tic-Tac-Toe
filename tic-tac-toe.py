def print_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])


def check_win(player, board):
    wins = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]
    for win in wins:
        if board[win[0]] == board[win[1]] == board[win[2]] == player:
            return True
    return False


def tictactoe():
    board = [" "," "," "," "," "," "," "," "," "]
    player = "X"
    turn = 0

    while turn < 9:
        print_board(board)

        spot = int(input("Player " + player + ", pick a spot (0-8): "))
        if spot < 0 or spot > 8:
            print("Ivalid spot. Must be 0 - 8")
            continue
        if board[spot] != " ":
            print("Spot taken")
            continue

        board[spot] = player
        turn += 1
        if check_win(player, board):
            print_board(board)
            print("Player " + player + " wins")
            return

        if player == "X":
            player = "O" 
        else:
            player = "X"

    print_board(board)
    print("Tie")


def main():
    while True:
        tictactoe()
        replay = input("Do you want to play again? (yes/no): ")
        if replay == "no":
            print("Thank you for playing")
            break


if __name__ == "__main__":
    main()
