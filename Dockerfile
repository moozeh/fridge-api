# 1. 베이스 이미지 선택 (slim 버전으로 가볍게 시작)
FROM python:3.13-slim

# 3. 작업 디렉토리 설정
WORKDIR /app

# 4. 의존성 파일 복사
COPY requirements.txt .

# 5. uv를 사용하여 의존성 설치
# --system 옵션은 Docker 컨테이너의 전역 파이썬 환경에 패키지를 설치하도록 합니다.
# Docker 환경에서는 가상환경을 따로 만들 필요가 없으므로 이 방식이 효율적입니다.
RUN pip install -r requirements.txt

# 6. 애플리케이션 소스 코드 복사
COPY . .

# 7. 서버 실행
# uvicorn을 실행하여 FastAPI 앱을 서비스합니다.
# --host 0.0.0.0는 컨테이너 외부에서 접근할 수 있도록 모든 네트워크 인터페이스에서 수신 대기하라는 의미입니다.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]