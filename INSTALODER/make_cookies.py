### 쿠키파일 갱신 함수 ###
### 쿠키 예상 기한 90일 ###

import instaloader

def update_cookie(username: str, password: str, cookie_file: str = "cookies.txt"):
    """
    Instaloader를 사용하여 Instagram 쿠키 파일을 갱신하는 함수.

    Args:
        username (str): Instagram 사용자 이름.
        password (str): Instagram 비밀번호.
        cookie_file (str): 저장할 쿠키 파일 경로 (기본값: 'cookies.txt').

    Returns:
        None
    """
    # Instaloader 객체 생성
    loader = instaloader.Instaloader()

    # 계정 로그인
    loader.login(username, password)

    # 쿠키 파일로 세션 저장
    with open(cookie_file, 'wb') as file:
        loader.context.save_session_to_file(file)

    print("쿠키 파일 갱신 완료!")

# 사용자 이름과 비밀번호 입력
username = ""
password = ""

# 쿠키 갱신 함수 호출
update_cookie(username, password)