"""
문제 1: 숫자 맞히기 (횟수 제한 추가)
사용자에게 1부터 20 사이의 숫자를 맞히게 하되, 기회는 5번만 주세요.

요구사항
randint()으로 1~20 사이 난수 생성
사용자는 숫자 입력
기회는 총 5번 → 틀릴 때마다 남은 기회 안내
정답 맞추면 "You win!", 못 맞추면 "You lose... 정답은 XX" 출력
"""
# from random import randint

# ran_number = randint(1,20)
# opp = 5

# for x in range(opp):
#     user_number = int(input("1~20 사이의 숫자를 입력하세요: "))
#     opp -= 1
#     if ran_number == user_number :
#         print("You Win!")
#         break
#     else :
#         if opp == 0 :
#             print(f"You lose... 정답은 {ran_number}")
#             break
#     print(f"남은 기회 : {opp}")

"""
컴퓨터는 random 모듈로 "rock", "paper", "scissors" 중 하나를 선택합니다.
사용자는 input()으로 세 가지 중 하나를 입력합니다.
승패 판정 로직:
rock > scissors
scissors > paper
paper > rock
결과 출력:
"You win!", "You lose!", "It's a draw!" 중 하나를 출력합니다.
(선택) 소문자 입력이 아니어도 처리하도록 lower()를 써도 좋아요 😊
"""
import random

com = random.choice(["rock", "paper", "scissors"])
user = input("가위, 바위, 보 중 하나를 입력하세요: ").lower()

if (user == "rock" and com =="scissors") or (user == "scissors" and com =="paper") or (user == "paper" and com =="rock"):
    print("You win!")
elif com == user :
    print("It's a drow!")
else :
    print("You lose!")