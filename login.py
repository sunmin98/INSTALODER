import instaloader

# Instaloader 객체 생성
loader = instaloader.Instaloader()

# 쿠키 파일 경로
cookie_file = "cookies.txt"

# 쿠키로 세션 로드
with open(cookie_file, 'rb') as file:
    loader.context.load_session_from_file('jiwom10', file)

print("쿠키 파일로 로그인 성공!")

# 크롤링할 계정 이름
profile_name = "aespa_official"


profile = instaloader.Profile.from_username(loader.context, profile_name)


for idx, post in enumerate(profile.get_posts()):
    if idx >= 10:
        break
    print(f"Downloading image {idx + 1} from post: {post.url}")
    loader.download_pic(
        filename=f"{profile_name}__post{idx + 1}__{post.date}",  # 저장 파일명
        url=post.url,
        mtime=post.date
    )
print("이미지 다운로드 완료!")
