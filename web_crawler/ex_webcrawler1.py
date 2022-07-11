#import requests                # requests 패키지 가져오기
#url = 'https://www.naver.com'  # 가져올 url 문자열로 입력
#response = requests.get(url)   # requests의 get함수를 이용해 해당 url로 부터 html이 담긴 자료를 받아옴
#print(response.status_code)    # 정상적으로 받아졌다면 200이라는 상태코드를 반환
#html_text = response.text      # 우리가 얻고자 하는 html 문서가 여기에 담기게 됨

# selenium의 webdriver를 사용하기 위한 import
from selenium import webdriver

# selenium으로 무엇인가 입력하기 위한 import
from selenium.webdriver.common.keys import Keys

# 페이지 로딩을 기다리는데에 사용할 time 모듈 import
import time

# 크롬드라이버 실행  (경로 예: '/Users/Roy/Downloads/chromedriver')
driver = webdriver.Chrome('/Users/suhwan/work/pythonwork/chromedriver') 

#크롬 드라이버에 url 주소 넣고 실행
driver.get('https://www.google.co.kr/')

# 페이지가 완전히 로딩되도록 3초동안 기다림
time.sleep(3)

#검색어 창을 찾아 search 변수에 저장
#search = driver.find_element_by_xpath('//*[@id="google_search"]')
search = driver.find_element_by_xpath('//*[@name="q"]')

#search 변수에 저장된 곳에 값을 전송
search.send_keys('코딩유치원 파이썬')
time.sleep(1)

#search 변수에 저장된 곳에 엔터를 입력
search.send_keys(Keys.ENTER)

time.sleep(10)
