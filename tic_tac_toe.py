def play_turn(board, x,y,piece):
    if x>=3 or y >=3 or x<0 or y<0:
        return False
    
    if board[y][x] == "":
        board[y][x] = piece
        return True
    else:
        return False

if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 3, 0, "X"))
    print(game_board)