"""게임 전체 흐름을 관리하는 QuizGame 클래스."""

from input_utils import ask_number, ask_text
from quiz import Quiz
from storage import Storage

SINGLE_LINE = "-" * 40   # 문제 사이 구분선
DOUBLE_LINE = "=" * 40   # 결과/제목 강조선

MENU_TEXT = f"""
{DOUBLE_LINE}
        🐍 파이썬 문법 퀴즈 게임 🐍
{DOUBLE_LINE}
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
{DOUBLE_LINE}"""


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

    def play_quiz(self):
        """저장된 퀴즈를 순서대로 출제하고 채점한다."""
        # 퀴즈가 하나도 없으면 진행할 수 없다.
        if not self.quizzes:
            print("\n⚠️  등록된 퀴즈가 없습니다. 먼저 [2] 퀴즈 추가로 문제를 만들어 주세요.")
            return

        total = len(self.quizzes)
        print(f"\n📝 퀴즈를 시작합니다! (총 {total}문제)")

        correct_count = 0   # 맞힌 개수를 세는 변수

        # 문제 개수가 정해져 있으므로 for로 순회한다.
        for number, quiz in enumerate(self.quizzes, start=1):
            print("\n" + SINGLE_LINE)
            quiz.show(number)
            print()

            user_answer = ask_number("정답 입력: ", 1, Quiz.CHOICE_COUNT)

            if quiz.is_correct(user_answer):
                correct_count += 1
                print("✅ 정답입니다!")
            else:
                print(f"❌ 오답입니다. 정답은 {quiz.answer}번 ({quiz.answer_text()}) 입니다.")

        self.show_result(correct_count, total)

    def show_quiz_list(self):
        """등록된 퀴즈의 문제만 번호를 붙여 나열한다. (정답은 보여주지 않음)"""
        if not self.quizzes:
            print("\n⚠️  등록된 퀴즈가 없습니다. [2] 퀴즈 추가로 문제를 만들어 주세요.")
            return

        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)\n")
        print(SINGLE_LINE)
        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"[{number}] {quiz.question}")
        print(SINGLE_LINE)

    def add_quiz(self):
        """사용자에게 문제/선택지/정답을 입력받아 새 퀴즈를 등록한다."""
        print("\n📌 새로운 퀴즈를 추가합니다.\n")

        question = ask_text("문제를 입력하세요: ")

        # 선택지 4개를 순서대로 입력받는다.
        choices = []
        for number in range(1, Quiz.CHOICE_COUNT + 1):
            choice = ask_text(f"선택지 {number}: ")
            choices.append(choice)

        answer = ask_number(f"정답 번호 (1-{Quiz.CHOICE_COUNT}): ", 1, Quiz.CHOICE_COUNT)

        # 입력값이 모두 검사를 통과했으므로 Quiz 객체를 만들어 목록에 넣는다.
        self.quizzes.append(Quiz(question, choices, answer))

        # 추가하자마자 파일에 저장해야 프로그램이 갑자기 꺼져도 남는다.
        if self.save():
            print(f"\n✅ 퀴즈가 추가되었습니다! (현재 총 {len(self.quizzes)}개)")

    def show_result(self, correct_count, total):
        """채점 결과를 100점 만점 점수로 환산해서 보여준다."""
        # 정수 나눗셈이 아니라 실수 나눗셈(/)을 써야 소수점이 살아난다.
        score = round(correct_count / total * 100)

        print("\n" + DOUBLE_LINE)
        print(f"🏆 결과: {total}문제 중 {correct_count}문제 정답! ({score}점)")

        if self.update_best_score(score):
            print("🎉 새로운 최고 점수입니다!")
        else:
            print(f"   (현재 최고 점수: {self.best_score}점)")
        print(DOUBLE_LINE)

    def update_best_score(self, score):
        """이번 점수가 최고 기록이면 갱신·저장하고 True를 돌려준다.

        '화면에 보여주는 일'(show_result)과 '기록을 판단·저장하는 일'을
        분리해 두면, 나중에 점수 규칙이 바뀌어도 이 메서드만 고치면 된다.
        """
        if score <= self.best_score:
            return False

        self.best_score = score
        self.save()
        return True

    def show_score(self):
        """저장된 최고 점수를 보여준다."""
        if self.best_score == 0:
            print("\n📊 아직 기록이 없습니다. [1] 퀴즈 풀기로 첫 점수를 만들어 보세요!")
            return

        print(f"\n🏆 최고 점수: {self.best_score}점")

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
                    self.play_quiz()
                case 2:
                    self.add_quiz()
                case 3:
                    self.show_quiz_list()
                case 4:
                    self.show_score()
                case 5:
                    self.save()   # 종료 전에 저장
                    print("\n👋 게임을 종료합니다. 수고하셨습니다!")
                    break
