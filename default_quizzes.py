"""기본으로 제공되는 파이썬 문법 퀴즈 데이터.

state.json이 없는 첫 실행이거나 파일이 손상됐을 때 이 데이터로 시작한다.
주제를 '파이썬 문법'으로 잡았기 때문에, 이번 미션의 학습 목표
(자료형 / 조건문 / 반복문 / 함수 / 클래스 / 파일 입출력 / 예외 처리)를
한 문제씩 훑도록 문제를 골랐다.

퀴즈 하나의 모양은 state.json에 저장되는 형태와 똑같이 dict로 적어 두었다.
  {"question": 문제, "choices": [선택지 4개], "answer": 정답 번호(1~4)}
"""

from quiz import Quiz

DEFAULT_QUIZZES = [
    {
        "question": "참(True)과 거짓(False) 두 가지 값만 가질 수 있는 자료형은?",
        "choices": ["int", "str", "bool", "list"],
        "answer": 3,
    },
    {
        "question": "키(key)와 값(value)을 짝지어 저장하는 자료형은?",
        "choices": ["list", "dict", "tuple", "set"],
        "answer": 2,
    },
    {
        "question": "앞의 조건이 거짓일 때, 또 다른 조건을 이어서 검사하는 키워드는?",
        "choices": ["else", "elif", "switch", "case"],
        "answer": 2,
    },
    {
        "question": "반복 횟수를 미리 알 수 없고, 조건이 참인 동안 계속 반복할 때 쓰는 것은?",
        "choices": ["for", "while", "if", "def"],
        "answer": 2,
    },
    {
        "question": "함수를 정의할 때 사용하는 키워드는?",
        "choices": ["func", "define", "def", "function"],
        "answer": 3,
    },
    {
        "question": "함수에서 결과 값을 돌려주면서 함수를 끝내는 키워드는?",
        "choices": ["print", "return", "break", "pass"],
        "answer": 2,
    },
    {
        "question": "객체가 만들어질 때 자동으로 호출되어 속성을 초기화하는 메서드는?",
        "choices": ["__init__", "__main__", "__str__", "__name__"],
        "answer": 1,
    },
    {
        "question": "클래스 메서드의 첫 번째 매개변수 self가 가리키는 것은?",
        "choices": ["클래스 그 자체", "메서드를 호출한 객체 자신", "부모 클래스", "전역 변수"],
        "answer": 2,
    },
    {
        "question": "open() 함수에서 모드 'w'의 의미는?",
        "choices": ["읽기 전용", "이어쓰기", "쓰기(기존 내용은 지워짐)", "바이너리 읽기"],
        "answer": 3,
    },
    {
        "question": "오류가 발생해도 프로그램이 멈추지 않도록 감싸 주는 문법은?",
        "choices": ["if / else", "try / except", "for / in", "def / return"],
        "answer": 2,
    },
]


def make_default_quizzes():
    """위의 dict 목록을 Quiz 객체 리스트로 만들어 돌려준다."""
    return [
        Quiz(item["question"], item["choices"], item["answer"])
        for item in DEFAULT_QUIZZES
    ]
