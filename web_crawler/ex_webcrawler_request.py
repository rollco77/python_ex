import requests                # requests 패키지 가져오기
url = 'https://www.naver.com'  # 가져올 url 문자열로 입력
response = requests.get(url)   # requests의 get함수를 이용해 해당 url로 부터 html이 담긴 자료를 받아옴
print(response.status_code)    # 정상적으로 받아졌다면 200이라는 상태코드를 반환
html_text = response.text      # 우리가 얻고자 하는 html 문서가 여기에 담기게 됨

print(html_text)