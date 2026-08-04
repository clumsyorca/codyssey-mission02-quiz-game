"""퀴즈 한 문제를 표현하는 Quiz 클래스."""


class Quiz:
    """문제 1개 = Quiz 객체 1개.

    속성(attribute)
      question : str  - 문제 내용
      choices  : list - 선택지 4개
      answer   : int  - 정답 번호 (1~4)
    """

    CHOICE_COUNT = 4   # 선택지는 4개로 고정 (클래스 전체가 공유하는 값)

    def __init__(self, question, choices, answer):
        # self는 "지금 만들어지고 있는 이 객체"를 가리킨다.
        # self.question에 넣어야 객체마다 자기 값을 따로 기억한다.
        self.question = question
        self.choices = choices
        self.answer = answer

    def show(self, number=None):
        """문제와 선택지를 화면에 출력한다."""
        title = f"[문제 {number}]" if number else "[문제]"
        print(title)
        print(self.question)
        print()
        # enumerate로 인덱스를 1부터 붙여서 화면 번호와 맞춘다.
        for index, choice in enumerate(self.choices, start=1):
            print(f"  {index}. {choice}")

    def is_correct(self, user_answer):
        """사용자가 고른 번호가 정답이면 True, 아니면 False를 반환한다."""
        return user_answer == self.answer

    def answer_text(self):
        """정답 번호에 해당하는 선택지 내용을 돌려준다. (오답 안내용)

        화면 번호는 1부터지만 리스트 인덱스는 0부터라 1을 빼 준다.
        """
        return self.choices[self.answer - 1]
