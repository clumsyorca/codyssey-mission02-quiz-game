"""프로그램 진입점. 실행: python3 main.py"""

from quiz_game import QuizGame


def main():
    game = QuizGame()
    game.run()


# 이 파일을 직접 실행했을 때만 main()이 돌아간다.
# (다른 파일에서 import 할 때는 실행되지 않음)
if __name__ == "__main__":
    main()
