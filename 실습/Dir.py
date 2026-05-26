import hashlib
import os

base1 = input("첫 번째 디렉토리 입력: ")
base2 = input("두 번째 디렉토리 입력: ")


# [추가] 파일 내용을 비교하기 위한 초간단 함수
def get_hash(path):
    hasher = hashlib.md5()
    try:
        with open(path, "rb") as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
    except:
        return None


def listAll(path, base_path, result_dict):
    dirfiles = os.listdir(path)
    subdirs = [path + "/" + x for x in dirfiles if os.path.isdir(path + "/" + x)]
    print(path)

    with os.scandir(path) as entries:
        D = {}
        for entry in entries:
            print(f"이름: {entry.name}")
            if entry.is_file():
                file_size_bytes = entry.stat().st_size
                print(f"크기: {file_size_bytes}")

                file_hash = get_hash(entry.path)
                D[entry.name] = (file_size_bytes, file_hash)

        for name, info in D.items():
            rel_path = os.path.relpath(path + "/" + name, base_path)
            result_dict[rel_path] = info

    for subdir in subdirs:
        listAll(subdir, base_path, result_dict)

    print(D)


dir1_result = {}
dir2_result = {}

print(f"\n=== {base1} 탐색 시작 ===")
listAll(base1, base1, dir1_result)

print(f"\n=== {base2} 탐색 시작 ===")
listAll(base2, base2, dir2_result)


if len(dir1_result) != len(dir2_result):
    print("두 디렉토리의 파일 개수가 다릅니다!")
    print(f"   - {base1}: {len(dir1_result)}개 / {base2}: {len(dir2_result)}개")
else:
    print(f"파일 개수 동일 ({len(dir1_result)}개)")

all_match = True
for rel_path, info1 in dir1_result.items():
    if rel_path not in dir2_result:
        print(f"[{rel_path}] 파일이 한쪽에만 존재합니다.")
        all_match = False
        continue

    info2 = dir2_result[rel_path]

    if info1[0] != info2[0] or info1[1] != info2[1]:
        print(f"[{rel_path}] 파일의 크기나 내용이 다릅니다.")
        all_match = False

if all_match:
    print("모든 파일의 이름, 크기, 내용이 일치합니다!")
