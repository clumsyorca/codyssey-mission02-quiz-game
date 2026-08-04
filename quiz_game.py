"""게임 전체 흐름을 관리하는 QuizGame 클래스."""

MENU_TEXT = """
========================================
        🐍 파이썬 문법 퀴즈 게임 🐍
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================"""


class QuizGame:
    """퀴즈 목록과 최고 점수를 들고 메뉴 루프를 돌리는 클래스."""

    def __init__(self):
        self.quizzes = []      # Quiz 객체들이 들어갈 리스트
        self.best_score = 0    # 지금까지의 최고 점수

    def show_menu(self):
        """메뉴 화면을 출력한다."""
        print(MENU_TEXT)

    def run(self):
        """사용자가 종료를 고를 때까지 메뉴를 반복해서 보여준다."""
        while True:
            self.show_menu()
            choice = input("선택: ")

            if choice == "1":
                print("\n(아직 준비 중인 기능입니다: 퀴즈 풀기)")
            elif choice == "2":
                print("\n(아직 준비 중인 기능입니다: 퀴즈 추가)")
            elif choice == "3":
                print("\n(아직 준비 중인 기능입니다: 퀴즈 목록)")
            elif choice == "4":
                print("\n(아직 준비 중인 기능입니다: 점수 확인)")
            elif choice == "5":
                print("\n👋 게임을 종료합니다. 수고하셨습니다!")
                break
            else:
                print("\n⚠️  잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
