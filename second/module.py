import sys

from decouple import config

sys.path.insert(0, config("BASE_PATH"))

from second.algorithm import check_win


class BoardStatus:
    board = list(range(1, 10))

    @classmethod
    def draw_board(cls, board):
        print("_" * 13)
        for i in range(3):
            print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
            print("_" * 13)

    @classmethod
    def main(cls, board):
        counter = 0
        win = False
        while not win:
            cls.draw_board(board)
            if counter % 2 == 0:
                cls.players_input("X")
            else:
                cls.players_input("O")
            counter += 1
            if counter > 4:
                tmp = check_win(board)
                if tmp:
                    print(tmp, "win!")
                    win = True
                    break
            if counter == 9:
                print("draw!")
                break
        cls.draw_board(board)

    @classmethod
    def players_input(cls, player_taken):
        valid = False
        while not valid:
            player_answer = input("Куда поставим " + player_taken + "? ")
            try:
                player_answer = int(player_answer)
            except Exception as ex:
                print("Некорректный ввод. Вы уверены, что ввели число?")
                continue
            if 1 <= player_answer <= 9:
                if str(cls.board[player_answer - 1]) not in "XO":
                    cls.board[player_answer - 1] = player_taken
                    valid = True
                else:
                    print("Эта клетка уже занята!")
            else:
                print("Введите число от 1 до 9.")


s = BoardStatus
s.main(board=(range(1, 10)))

