"""게임 전체 흐름을 관리하는 QuizGame 클래스."""

from input_utils import ask_number
from storage import Storage

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

    def __init__(self, storage=None):
        # storage를 밖에서 받을 수 있게 해 두면 테스트할 때 다른 파일 경로를 넣기 쉽다.
        self.storage = storage if storage else Storage()
        # 프로그램이 켜질 때 저장된 데이터를 먼저 불러온다.
        self.quizzes, self.best_score = self.storage.load()

    def save(self):
        """현재 퀴즈 목록과 최고 점수를 파일에 저장한다."""
        return self.storage.save(self.quizzes, self.best_score)

    def show_menu(self):
        """메뉴 화면을 출력한다."""
        print(MENU_TEXT)

    def run(self):
        """사용자가 종료를 고를 때까지 메뉴를 반복해서 보여준다."""
        while True:
            self.show_menu()
            # 검사는 ask_number가 담당하므로 여기서는 1~5만 신경 쓰면 된다.
            choice = ask_number("선택: ", 1, 5)

            # match/case는 파이썬 3.10에서 추가된 문법. if/elif와 같은 역할이지만
            # "하나의 값을 여러 경우로 나눈다"는 의도가 더 잘 드러난다.
            match choice:
                case 1:
                    print("\n(아직 준비 중인 기능입니다: 퀴즈 풀기)")
                case 2:
                    print("\n(아직 준비 중인 기능입니다: 퀴즈 추가)")
                case 3:
                    print("\n(아직 준비 중인 기능입니다: 퀴즈 목록)")
                case 4:
                    print("\n(아직 준비 중인 기능입니다: 점수 확인)")
                case 5:
                    self.save()   # 종료 전에 저장
                    print("\n👋 게임을 종료합니다. 수고하셨습니다!")
                    break
