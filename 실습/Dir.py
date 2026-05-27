import os

def get_files(d):
    res = {}
    try:
        with os.scandir(d) as entries:
            for e in entries:
                if e.is_file():
                    # os.stat()을 활용해 파일 크기 구하기
                    sz = os.stat(e.path).st_size
                    # 파일 내용 읽기
                    with open(e.path, 'rb') as f:
                        content = f.read()
                    res[e.name] = (sz, content)
    except FileNotFoundError:
        print(f"오류: '{d}' 디렉토리를 찾을 수 없습니다.")
        return None
    return res

def compare_dirs():
    d1 = input("첫 번째 디렉토리 이름: ").strip()
    d2 = input("두 번째 디렉토리 이름: ").strip()
    
    # 각 디렉토리의 파일 정보 가져오기
    i1 = get_files(d1)
    i2 = get_files(d2)
    
    if i1 is None or i2 is None:
        return

    # 파일명 집합
    f1, f2 = set(i1.keys()), set(i2.keys())
    
    print("\n--- 비교 결과 ---")
    
    # 1. 파일 개수 비교
    if len(f1) != len(f2):
        print(f"파일 개수: 다름 (파일 개수가 일치하지 않음: {len(f1)}개 vs {len(f2)}개)")
    else:
        print(f"파일 개수: 같음")

    # 2. 파일명 비교
    for name in f1:
        if name in f2:
            print(f"두 폴더 모두 이름이 {name}인 파일이 있습니다.")

    s1 = [val[0] for val in i1.values()]
    s2 = [val[0] for val in i2.values()]

    # 3. 각 파일의 크기 비교
    for s in s1:
        if s in s2:
            print(f"두 폴더에 크기가 {s}인 파일이 있습니다.")
            s2.remove(s)

    c1 = [val[1] for val in i1.values()]
    c2 = [val[1] for val in i2.values()]
    # 4. 각 파일의 내용 비교
    for c in c1:
        if c in c2:
            print(f"두 폴더에 내용 {c}인 파일이 있습니다.")
            c2.remove(c)

if __name__ == "__main__":
    compare_dirs()

