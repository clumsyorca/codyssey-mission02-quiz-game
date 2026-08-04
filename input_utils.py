"""사용자 입력을 받고 검사하는 공통 함수 모음.

메뉴 선택, 정답 입력, 퀴즈 등록 등 숫자를 받는 곳이 여러 군데라
같은 검사 코드를 반복해서 쓰지 않도록 함수로 분리했다.
"""


def ask_number(prompt, min_value, max_value):
    """min_value~max_value 범위의 정수를 받을 때까지 계속 물어본다.

    처리하는 잘못된 입력:
      - 빈 입력(그냥 Enter)
      - 숫자가 아닌 값(예: abc)
      - 범위 밖의 숫자(예: 메뉴에서 9)
    앞뒤 공백은 제거하고 판단하므로 " 1 "도 1로 인정된다.
    """
    while True:
        text = input(prompt).strip()   # 앞뒤 공백 제거

        if text == "":
            print(f"⚠️  입력이 비어 있습니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
            continue

        try:
            number = int(text)
        except ValueError:
            # int()로 바꿀 수 없는 값이면 ValueError가 발생한다.
            print(f"⚠️  숫자만 입력할 수 있습니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
            continue

        if number < min_value or number > max_value:
            print(f"⚠️  {min_value}-{max_value} 범위를 벗어났습니다. 다시 입력하세요.")
            continue

        return number


def ask_text(prompt):
    """비어 있지 않은 문자열을 받을 때까지 계속 물어본다."""
    while True:
        text = input(prompt).strip()
        if text == "":
            print("⚠️  내용을 입력해 주세요. (빈 값은 저장할 수 없습니다)")
            continue
        return text
