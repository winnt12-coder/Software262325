K,L = map(int, input().split())
student = {}

for i in range(L):
    s = input()
    if s in student:
        del student[s]
    student[s] = ""
group = list(student.keys())[:K]
for x in group:
    print(x)
