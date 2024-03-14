<h2>기능</h2><p>CJUAuto_internet_lectures는 다음과 같은 작업을 자동화합니다:</p><ul><li>사용자가 제공한 자격 증명을 사용하여 CJU 사이버 강의 포털에 로그인합니다.</li><li>등록된 강의 목록과 강의 상태를 검색합니다.</li><li>현재 날짜와 강의 일정을 기반으로 아직 완료되지 않은 강의에 자동으로 참석합니다.</li><li>지정된 Slack 채널로 자세한 보고서를 보냅니다. 실행 중 완료된 강의와 전체 참석 상태가 포함됩니다.</li></ul><h2>전제 조건</h2><p>스크립트를 실행하기 전에 다음 사항이 필요합니다:</p><ul><li>시스템에 Python 3.6 이상이 설치되어 있어야 합니다.</li><li>Chrome WebDriver가 설치되어 시스템의 PATH에 추가되어 있어야 합니다. 설치된 Chrome 버전과 일치하는지 확인하세요.</li><li><code>.env</code> 파일이 스크립트와 동일한 디렉토리에 있어야 하며 필요한 환경 변수가 포함되어 있어야 합니다(아래 자세한 내용 참조).</li><li>Python 환경에 <code>selenium</code>, <code>slack_sdk</code>, <code>python-dotenv</code>가 설치되어 있어야 합니다.</li></ul><h2>환경 설정</h2><p>다음 변수를 포함하는 <code>.env</code> 파일을 스크립트의 디렉토리에 생성하세요:</p><pre><div class="dark bg-gray-950 rounded-md"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>plaintext</span><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 3.5C10.8954 3.5 10 4.39543 10 5.5H14C14 4.39543 13.1046 3.5 12 3.5ZM8.53513 3.5C9.22675 2.3044 10.5194 1.5 12 1.5C13.4806 1.5 14.7733 2.3044 15.4649 3.5H17.25C18.9069 3.5 20.25 4.84315 20.25 6.5V18.5C20.25 20.1569 19.1569 21.5 17.25 21.5H6.75C5.09315 21.5 3.75 20.1569 3.75 18.5V6.5C3.75 4.84315 5.09315 3.5 6.75 3.5H8.53513ZM8 5.5H6.75C6.19772 5.5 5.75 5.94772 5.75 6.5V18.5C5.75 19.0523 6.19772 19.5 6.75 19.5H17.25C18.0523 19.5 18.25 19.0523 18.25 18.5V6.5C18.25 5.94772 17.8023 5.5 17.25 5.5H16C16 6.60457 15.1046 7.5 14 7.5H10C8.89543 7.5 8 6.60457 8 5.5Z" fill="currentColor"></path></svg>Copy code</button></span></div><div class="p-4 overflow-y-auto"><sider-code-explain id="sider-code-explain" data-gpts-theme="light"></sider-code-explain><code class="!whitespace-pre hljs language-plaintext">ID=당신의_CJU_아이디
PW=당신의_CJU_비밀번호
SLACK_TOKEN=당신의_Slack_봇_토큰
SLACK_CHANNEL=당신의_Slack_채널_이름
SKIP_CODE=강의_내용을_건너뛰는_자바스크립트_코드
</code></div></div></pre><ul><li><code>ID</code> 및 <code>PW</code>는 CJU 포털 로그인 자격 증명입니다.</li><li><code>SLACK_TOKEN</code>은 Slack 앱에서 가져온 Bot User OAuth Access Token입니다. Slack 앱을 만들고 알림을 받을 채널에 그것을 초대하세요.</li><li><code>SLACK_CHANNEL</code>은 알림을 받기 원하는 Slack 채널입니다(예: <code>#사이버-강의</code>).</li><li><code>SKIP_CODE</code>는 강의 콘텐츠를 건너뛰는 데 사용되는 JavaScript 코드입니다. 이는 웹 애플리케이션의 작동 방식에 대한 특정 지식이 필요할 수 있습니다.</li></ul><h2>실행 방법</h2><ol><li>터미널이나 명령 프롬프트를 엽니다.</li><li><code>CJUAuto_internet_lectures</code> 스크립트가 있는 디렉토리로 이동합니다.</li><li><code>selenium</code>, <code>slack_sdk</code>, <code>python-dotenv</code>가 설치된 Python 환경에 있는지 확인합니다.</li><li>다음 명령을 실행하여 스크립트를 실행합니다:</li></ol><pre><div class="dark bg-gray-950 rounded-md"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 3.5C10.8954 3.5 10 4.39543 10 5.5H14C14 4.39543 13.1046 3.5 12 3.5ZM8.53513 3.5C9.22675 2.3044 10.5194 1.5 12 1.5C13.4806 1.5 14.7733 2.3044 15.4649 3.5H17.25C18.9069 3.5 20.25 4.84315 20.25 6.5V18.5C20.25 20.1569 19.1569 21.5 17.25 21.5H6.75C5.09315 21.5 3.75 20.1569 3.75 18.5V6.5C3.75 4.84315 5.09315 3.5 6.75 3.5H8.53513ZM8 5.5H6.75C6.19772 5.5 5.75 5.94772 5.75 6.5V18.5C5.75 19.0523 6.19772 19.5 6.75 19.5H17.25C18.0523 19.5 18.25 19.0523 18.25 18.5V6.5C18.25 5.94772 17.8023 5.5 17.25 5.5H16C16 6.60457 15.1046 7.5 14 7.5H10C8.89543 7.5 8 6.60457 8 5.5Z" fill="currentColor"></path></svg>Copy code</button></span></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">python CJUAuto_internet_lectures.py
</code></div></div></pre><ol start="5"><li>스크립트는 작업을 수행하고 완료되면 지정된 Slack 채널로 보고서를 보냅니다.</li></ol><h2>중요 사항</h2><ul><li><strong>개인 정보 및 보안</strong>: 스크립트는 CJU 포털 자격 증명이 필요합니다. <code>.env</code> 파일의 보안을 유지하고 자격 증명을 공유하지 않도록 주의하세요.</li><li><strong>실행 시간</strong>: 스크립트의 실행 시간은 강의 수와 강의의 개수에 따라 달라집니다. 부하를 최소화하고 실행이 원활하도록 하기 위해 오프 피크 시간에 실행하는 것이 좋습니다.</li><li><strong>컴플라이언스</strong>: 이 스크립트를 책임 있게 사용하고 CJU의 서비스 약관 및 허용되는 사용 정책을 준수하는지 확인하세요. 학업 의무를 충족시키면서 바쁜 일정을 관리하는 등의 합법적인 목적으로 참석 프로세스를 자동화하기 위해 제공됩니다.</li></ul><p>추가 도움이 필요하거나 문제를 신고해야 하는 경우 리포지토리 관리자에게 문의하세요.</p><hr><p><code>requirements.txt</code> 파일을 사용할 수 있다면 해당 파일도 함께 포함하여 설치 및 의존성 관리를 더욱 간편하게 할 수 있습니다.</p>
