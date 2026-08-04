"""프로그램 진입점. 실행: python3 main.py"""

from quiz_game import QuizGame


def main():
    game = QuizGame()
    try:
        game.run()
    except (KeyboardInterrupt, EOFError):
        # KeyboardInterrupt : 사용자가 Ctrl+C를 누른 경우
        # EOFError          : 입력이 더 이상 들어오지 않는 경우 (Ctrl+D 등)
        # 그냥 두면 빨간 오류 메시지와 함께 비정상 종료되므로 여기서 받아서
        # 안내 문구를 띄우고 지금까지의 내용을 저장한 뒤 정상적으로 끝낸다.
        print("\n\n⚠️  입력이 중단되었습니다. 저장 후 종료합니다.")
        game.save()
        print("👋 안전하게 종료되었습니다.")


# 이 파일을 직접 실행했을 때만 main()이 돌아간다.
# (다른 파일에서 import 할 때는 실행되지 않음)
if __name__ == "__main__":
    main()
