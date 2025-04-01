"""
🎯 문제 1: Player 클래스 만들기
아래 딕셔너리 + 함수 방식 코드를 객체지향 스타일로 바꿔보세요!

🔸 요구사항
Player 클래스를 만들고,
name, xp, team을 속성으로 가지게 하세요.

introduce()라는 메서드를 정의해서
Hello! My name is {name} and I play for {team} 라고 출력하게 하세요.

객체를 두 개 생성하고, 각각 introduce() 메서드를 실행해보세요.

👉 딕셔너리 대신 클래스로 구조화 연습!"
"""

# class Player:

#     def __init__(self, name, xp, team):
#         self.name = name
#         self.xp = xp
#         self.team = team

#     def indroudce(self):
#         print(f"Hello! My name is {self.name} and I play for {self.team}")

# member_one = Player("sola", 1000, "Blue")
# member_one.indroudce()
# member_two = Player("choonsik", 5000, "Red")
# member_two.indroudce()

"""
🎯 문제 2: Cat 클래스 상속 예제
기존의 Dog 예제를 응용해서 Cat 클래스와 상속 구조를 연습해보세요!

🔸 요구사항
Cat이라는 클래스를 만들고,
name, breed, age를 __init__()에서 받도록 하세요.

Meow()라는 메서드를 만들어 "Meow~!" 출력하게 하세요.

Kitten(Cat) 클래스를 만들어 age를 기본값 0.2로 설정하세요.

Kitten 클래스에 introduce() 메서드를 만들어
"I'm {name}, a baby {breed} cat"를 출력하고 Meow()도 불러보세요.

👉 클래스 상속, 메서드 호출, super() 활용 연습!
"""

class Cat:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    
    def Meow(self):
        print("Meow~!")

class Kitten(Cat):

    def __init__(self, name, breed):
        super().__init__(name, breed, age=0.2)

    def introdce(self):
        print(f"I'm {self.name}, a baby {self.breed} cat")
        super().Meow()

Happy = Kitten("Happy", "maltiz", 2)
Happy.introdce()