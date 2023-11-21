def save(score: int, image_file: str) -> None: # return x
        with open("info.txt", "w") as file: # info.txt 파일을 "w"(쓰기모드)로 열기
            file.write(f"Score: {score}, Image: {image_file}") # 문자열을 file에 쓰기

def load() -> tuple[int, str]: # return int, str # 방광이슈
    try: # 이미지가 없을 때 (예외의 상황) 를 위한 코드
        with open("info.txt", "r") as file: # info.txt 파일을 "r"(읽기모드)로 열기
            data = file.read() # 파일의 내용을 문자열로 읽어 변수에 지정
            score_part, image_part = data.split(", ") # ", " 를 기준으로 데이터 나누기
            score = int(score_part.split(": ")[1]) # 두번째 요소를 정수로 반환하여 변수에 지정
            image_file = image_part.split(": ")[1] # 두번째 요소를 반환하여 변수에 지정
            return score, image_file # score, image_flie 반환
    except FileNotFoundError: # 예외 상황시
        return 0, '2R/images/1.png' # score = 0, image_file = 기본 이미지 로 변경