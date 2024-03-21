## CJU 자동 인터넷 강의 수강 스크립트

### 기능
* 사용자 제공 ID/PW를 사용하여 CJU 사이버 강의 포털에 로그인
* 등록된 강의 목록 및 강의 상태 검색
* 현재 날짜와 강의 일정 기반 아직 완료되지 않은 강의 자동 수강
* 지정된 Slack 채널로 수강 내역 요약 전송 (이번 실행 강의, 전체 강의 포함)

### 전제 조건
* 시스템에 Python 3.6 이상 설치
* Chrome WebDriver 설치 및 PATH 추가 (Chrome 버전 일치 확인)
* 스크립트와 동일한 디렉토리에 .env 파일 생성 및 환경 변수 설정
* Python 환경에 selenium, slack_sdk, python-dotenv 설치

### 환경 설정
* 스크립트 디렉토리에 .env 파일 생성 및 다음 변수 설정
```
ID=당신의_CJU_아이디
PW=당신의_CJU_비밀번호
SLACK_TOKEN=당신의_Slack_봇_토큰
SKIP_CODE=강의_내용을_건너뛰는_자바스크립트_코드
```
* ID 및 PW: CJU 포털 로그인 ID/PW
* SLACK_TOKEN: Slack 앱 Bot User OAuth Access Token (Slack 앱 생성 및 알림 채널 초대 필요)
* SKIP_CODE: 강의 콘텐츠 건너뛰기 JavaScript 코드 (웹 애플리케이션 작동 방식에 대한 특정 지식 필요)

### 실행 방법
1. 터미널 또는 명령 프롬프트 열기
2. 스크립트 디렉토리로 이동
3. 다음 명령 실행하여 필요 패키지 설치
```
pip install -r requirements.txt
```
4. 다음 명령 실행하여 스크립트 실행
```
python CJUAuto_internet_lectures.py
```
5. 스크립트 작업 완료 후 지정된 Slack 채널로 보고서 전송

### 중요 사항
* 개인 정보 및 보안: 스크립트에 CJU 포털 자격 증명 필요, .env 파일 보안 유지 및 자격 증명 공유 금지
* 실행 시간: 강의 수 및 길이에 따라 달라짐, 부하 최소화 및 원활한 실행 위해 오프 피크 시간 실행 권장

### 버전관리
**ver1.0**
* 전반적인 기능 제작

**ver1.1**
* 백그라운드 실행 및 기타 서버용 셀레니움 옵션 추가

**ver1.1.1**
* service객체 추가

**ver1.1.2**
* Chrome으로 변경

**ver1.1.3**
* --no-sandbox 옵션 추가

**ver1.1.4**
* webdriver_manager 도입