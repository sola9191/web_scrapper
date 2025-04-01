"""
아래와 같은 유저 정보가 있는 딕셔너리가 있습니다.
이 유저가 "Python"을 좋아한다고 추가해주고, 이름은 "Sola"로 변경해주세요.
그리고 "age"는 삭제하고, "level"이라는 키에 99를 추가하세요.
[요구사항]
"Python"을 fav_languages에 추가
"name"을 "Sola"로 변경
"age"를 삭제
"level"을 99로 추가
최종 user 딕셔너리를 출력
"""
# user = {
#     "name": "nico",
#     "age": 22,
#     "fav_languages": ["JavaScript", "C++"]
# }

# user['name'] = 'sola'
# user['fav_languages'].append('Python')
# del user['age']
# user['level'] = 99

# print(user)

"""
 문제 2: 요일 리스트 조작하기 (리스트)
요일 리스트가 아래와 같이 주어졌습니다.
✅ 요구사항
"Thur"과 "Fri"를 한 줄에 추가 (append() 또는 extend() 활용)
"Mon"을 리스트에서 삭제
리스트를 거꾸로 뒤집기 (reverse())
"Sun"이 리스트 안에 있는지 여부를 True 또는 False로 출력
"""
week = ["Mon", "Tue", "Wed"]
week.append("Thur")
week.append("Fri")
week.remove("Mon")
week.reverse()
print("Sun" in week)
print(week) 