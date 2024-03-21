from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os 
import slack_sdk
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService





class Auto_internet_lectures:
    def __init__(self):
        ##환경변수 로드
        load_dotenv()
        self.id = os.getenv("ID")
        self.pw = os.getenv("PW")
        self.SLACK_TOKEN = os.environ.get("SLACK_TOKEN")
        self.SLACK_CHANNEL = "#university"
        
        ##저장 변수
        self.courses_dict = {} ##수강 과목 list
        self.all_lct_dict = {} ##모든 강의 list
        
        ##구분 변수
        self.year = "2024"
        
        ##수강 스킵 코드
        self.js_skip_code='iframe = document.getElementById("sub-frame-contents");iframe.contentWindow.startTime -= 3000000;iframe.contentWindow.pre_study_time = 3000000;iframe.contentWindow.loadDurationTime = 3000000;iframe.contentWindow.CmiSetValue("cmi.session_time",3000000);iframe.contentWindow.cmi_session_time;iframe.contentWindow.CmiSetValue("cmi.saved_session_time",3000000);iframe.contentWindow.CmiSetValue("cmi.study_time",3000000);iframe.contentWindow.CmiSetValue("cmi.duration_time",3000000);iframe.contentWindow.CmiSetValue("cmi.check_time1",1500000);iframe.contentWindow.CmiSetValue("cmi.check_time2",3000000);iframe.contentWindow.cmi_progress_measure = 1;iframe.contentWindow.cmiCheckProgress(0.5);iframe.contentWindow.cmiCheckProgress(1);MAIN.doClose();'

        ##main page url
        self.main_page_url ="https://hive.cju.ac.kr/usr/member/stu/dash/detail.do"
        
        ##driver loading
        self.options = webdriver.ChromeOptions()  # Chrome 브라우저 설정 옵션 객체 생성

        # 다양한 설정 옵션 추가
        self.options.add_argument('--disable-extensions')  # 확장 프로그램 사용 안함
        self.options.add_argument('--start-maximized')  # 창 최대화
        self.options.add_argument('--incognito')  # 시크릿 모드로 실행
        self.options.add_argument('--disable-gpu')  # GPU 가속 사용 안함 (★★★★★ 많이 사용)
        self.options.add_argument('--disable-dev-shm-usage')  # /dev/shm 사용 안함
        self.options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"')  # User-Agent 설정
        self.options.add_argument('--disable-notifications')  # 알림 사용 안함
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        
        self.service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.driver.get(self.main_page_url)

    ##현재 날짜를 이용해 가치있는 날짜 범위있지 확인
    def is_today_in_date_range(self, start_date, end_date):
        # 현재 날짜 가져오기
        today = datetime.today()

        # 시작일과 종료일을 datetime 객체로 변환
        start_date = datetime.strptime(start_date, "%Y.%m.%d")
        end_date = datetime.strptime(end_date, "%Y.%m.%d")

        # 오늘의 날짜가 범위 내에 있는지 확인
        return start_date <= today <= end_date
    
    def slack_message_with_time(self,msg):
        datetime_format = datetime.today().strftime("%Y-%m-%d %H:%M")
        client = slack_sdk.WebClient(token = self.SLACK_TOKEN)
        client.chat_postMessage(
            channel=self.SLACK_CHANNEL,
            text="["+datetime_format+"] "+msg
            )
    
    def formatting_slack(self, is_listening_courses):
        formatted_message = "\n"
        for course, details in self.all_lct_dict.items():
            formatted_message += f"*{course}*\n"
            for week, info in details.items():
                formatted_message += f"• {week}: "
                if isinstance(info, dict) and info.get('progress_rate') is not None:
                    if info['progress_rate']:
                        formatted_message += "Completed "
                    else:
                        formatted_message += "Not completed "
                    formatted_message += f" ({info['start_date']} ~ {info['end_date']})\n"
                    for period, status in info['periods'].items():
                        formatted_message += f"  - {period}: "
                        if status[0]:
                            formatted_message += "O"
                        else:
                            formatted_message += "X"
                    formatted_message += "\n"
                else:
                    formatted_message += "Information not available\n"
            formatted_message += "\n"

        if is_listening_courses:
            formatted_message += "이번 실행 때 수강한 강의 목록:\n"
            for course in is_listening_courses:
                formatted_message += f"- {course}\n"

        return formatted_message.strip()
    
    def login(self):
        self.driver.find_element(By.ID,"j_username_login").send_keys(self.id)
        sleep(1)
        self.driver.find_element(By.ID,"j_password_login").send_keys(self.pw)
        sleep(1)
        self.driver.find_element(By.CLASS_NAME,"c_btn.enter").click()
        sleep(1)
    
    def close_popup(self):
        main = self.driver.window_handles

        for i in main:
            if i != main[0]:
                self.driver.switch_to.window(i)
                self.driver.close()

        self.driver.switch_to.window(main[0])
        sleep(0.3)
        
    def get_courses_list(self):
        ##수강과목 list elem
        #{"과목명":"과목이동url(js code)"}
        #'인공지능캡스톤디자인1': "doClassroom({'courseActiveSeq':'86759','courseApplySeq':'5122201','ltType':'B67001','chkAuthCju':'N'});"

        ##과목 목록
        courses_table = self.driver.find_element(By.CLASS_NAME,"tbl_col3.prof_cs").find_elements(By.TAG_NAME,"tbody")[1]
        courses = courses_table.find_elements(By.CLASS_NAME,"al")

        for elem in courses:
            ##강의 명
            name = elem.text.strip()
            ##강의 이동 js(-> "doClassroom({'courseActiveSeq':'86779','courseApplySeq':'5122427','ltType':'B67001','chkAuthCju':'N'});")
            onclick_code = elem.find_element(By.TAG_NAME,"a").get_attribute("onclick")
            onclick_code = onclick_code.replace("\t","").replace("\n","")
            
            self.courses_dict[name] = onclick_code
        return self.courses_dict
    
    def get_lct_status(self):
        weeks = self.driver.find_elements(By.CLASS_NAME,"lct_view")
    
        content = {}
        for week in weeks:
            title = week.find_element(By.CLASS_NAME,"title").text
            ##몇 주차인지 저장
            week_name = title.split()[0]
        
            ##수강 기간 찾기
            start_date = None
            end_date = None
            split_title = title.split()
            for word in split_title:
                if word.find(self.year) != -1:
                    start_date,end_date = word.strip("(").strip(")").split("~")
                    break
        
            ##교시 내용
            periods_dict = {}
            periods_rates = []
            periods_url = []
            
            periods = week.find_elements(By.CLASS_NAME,"result")
            ##시험 주차인 경우 || 사이버강의가 아닌 경우
            if len(periods) == 1:
                continue
            
            for period in periods:
                rate = period.find_element(By.CLASS_NAME,"rate").text
                ##수강이 안되어 있는 경우
                if rate.find("100") == -1 :
                    periods_rates.append(False)
                else:
                    periods_rates.append(True)
            
            lct_btns = week.find_elements(By.CLASS_NAME,"group")
            for lct_btn in lct_btns:
                ##학습 버튼 onclick js code로 되어 있음
                periods_url.append(lct_btn.find_element(By.TAG_NAME,"button").get_attribute("onclick"))
        
            ##진도율 구하기
            progress_rate = True
            for periods_rate in periods_rates:
                if periods_rate == False:
                    progress_rate = False
                    break
            
            content[week_name] = {"progress_rate":progress_rate,"start_date":start_date,"end_date":end_date}
            for i in range(len(periods_rates)):
                periods_dict[str(i+1)+"교시"] = [periods_rates[i],periods_url[i]]
            ##한 교과의 dict 완성 
            ##ex->{'1주차': {'progress_rate': False, 'start_date': '2024.03.04', 'end_date': '2024.03.18', 'periods': {'1교시': [False, "MAIN.doStudyPopupCdn('445431')"], '2교시': [False, "MAIN.doStudyPopupCdn('446599')"]}}}
            content[week_name]["periods"] = periods_dict
            
        return content
    
    def listen_lectures(self,content):
        is_listening = False
        ##수강
        for key in content.keys():
            ## progress_rate(진도율)이 False인 것만 date 체크
            pointer = content[key]
            if pointer["progress_rate"] == False:
                ##오늘 날짜 기준 수강 가능한 것만 체크
               if self.is_today_in_date_range(pointer["start_date"],pointer["end_date"]):
                    is_listening = True
                    for k in pointer["periods"].keys():
                        self.driver.execute_script(pointer["periods"][k][1])
                        sleep(2)
                            
                        main = self.driver.window_handles
                        self.driver.switch_to.window(main[-1])
                        sleep(2.5)
                        self.driver.execute_script(self.js_skip_code)
                        sleep(2)
                        ##alert 확인
                        self.driver.switch_to.alert.accept()
                        sleep(1.5)
                        self.driver.switch_to.alert.accept()
                        sleep(1.5)
                        self.driver.switch_to.alert.accept()

                        self.driver.switch_to.window(main[0])
        return is_listening
    
    # Slack 메시지 전송을 위한 수정된 main 메서드
    def main(self):
        self.login()
        sleep(2)
        self.close_popup()
        sleep(1)
        self.get_courses_list()
        sleep(1)
        is_listening_courses = []
        for key in self.courses_dict.keys():
            self.driver.execute_script(self.courses_dict[key])
            sleep(1)
            self.all_lct_dict[key] = self.get_lct_status()
            sleep(1)
            is_listening = self.listen_lectures(self.all_lct_dict[key])
            if is_listening:
                is_listening_courses.append(key)
                self.driver.refresh()
                self.all_lct_dict[key] = self.get_lct_status()
                self.all_lct_dict[key]["is_listening"] = True
            sleep(1)
        self.driver.quit()
        slack_message = self.formatting_slack(is_listening_courses)
        self.slack_message_with_time(slack_message)
        return self.all_lct_dict
        
ail = Auto_internet_lectures()
ail.main()