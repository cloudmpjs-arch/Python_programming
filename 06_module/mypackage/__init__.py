# __init__.py파일 (패키지 초기화 파일)
# 패키지가 로드할 때 실행되는 최기화 파일

# 1. 패키지를 import 할 때 실행되어야하는 초기화 코드 (환경 확인, 설정값 )
print("__init__")

# 2. 패키지 메타데이터 작성 (버전, 작성자)
VERSION = "1.0.0"

# 3. 패키지 re-export (패키지 안 세부 구조를 몰라도 import할 수 있게)
# from mypackage.mymath import add    # 절대 임포트
from .mymath import add               # 상대 임포트
