"""state.json 파일을 읽고 쓰는 Storage 클래스.

'게임 진행'과 '파일 다루기'는 성격이 다른 일이라 클래스를 나눴다.
QuizGame은 저장 방식(JSON인지 DB인지)을 몰라도 되고,
Storage는 게임 규칙을 몰라도 된다.
"""

import json
import os

from quiz import Quiz
from default_quizzes import make_default_quizzes

# 파일 이름을 여기 한 곳에서만 정해 두면 나중에 바꾸기 쉽다.
FILE_NAME = "state.json"

# 이 파일(storage.py)이 있는 폴더 = 프로젝트 루트.
# 이렇게 절대 경로로 만들어 두면 어느 위치에서 python3 main.py를 실행해도
# 항상 같은 state.json을 쓰게 된다.
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_PATH = os.path.join(ROOT_DIR, FILE_NAME)


class Storage:
    """퀴즈 목록과 최고 점수를 JSON 파일로 저장/복원한다."""

    def __init__(self, path=DEFAULT_PATH):
        self.path = path

    def load(self):
        """저장된 데이터를 읽어 (퀴즈 목록, 최고 점수)를 돌려준다.

        아래 세 경우 모두 프로그램이 죽지 않고 기본 퀴즈로 시작한다.
          1) 파일이 아예 없을 때 (첫 실행)
          2) 파일 내용이 JSON 형식이 아닐 때 (손상)
          3) JSON이긴 한데 필요한 키/형식이 어긋날 때
        """
        if not os.path.exists(self.path):
            print(f"📂 저장된 데이터가 없어 기본 퀴즈로 시작합니다. ({FILE_NAME} 없음)")
            return make_default_quizzes(), 0

        try:
            with open(self.path, "r", encoding="utf-8") as f:
                data = json.load(f)

            quizzes = [Quiz.from_dict(item) for item in data["quizzes"]]
            best_score = int(data["best_score"])

        except (json.JSONDecodeError, KeyError, TypeError, ValueError) as e:
            # 형식이 깨진 경우
            print(f"⚠️  데이터 파일이 손상되어 기본 퀴즈로 복구합니다. (원인: {e})")
            return make_default_quizzes(), 0
        except OSError as e:
            # 권한 문제 등 파일을 못 여는 경우
            print(f"⚠️  데이터 파일을 읽을 수 없어 기본 퀴즈로 시작합니다. (원인: {e})")
            return make_default_quizzes(), 0

        print(f"📂 저장된 데이터를 불러왔습니다. (퀴즈 {len(quizzes)}개, 최고점수 {best_score}점)")
        return quizzes, best_score

    def save(self, quizzes, best_score):
        """퀴즈 목록과 최고 점수를 state.json에 저장한다. 성공하면 True."""
        data = {
            "quizzes": [quiz.to_dict() for quiz in quizzes],
            "best_score": best_score,
        }
        try:
            with open(self.path, "w", encoding="utf-8") as f:
                # ensure_ascii=False : 한글이 \uXXXX로 깨지지 않고 그대로 저장됨
                # indent=2           : 사람이 읽기 좋게 줄바꿈/들여쓰기
                json.dump(data, f, ensure_ascii=False, indent=2)
            return True
        except OSError as e:
            print(f"⚠️  저장에 실패했습니다. (원인: {e})")
            return False
