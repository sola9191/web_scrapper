"""
🧁 예제 1: 쉬운 문제 — 책장과 책 (구성 관계)
📌 문제 설명
Book 클래스와 Bookshelf 클래스를 만들고,
Bookshelf에 여러 Book 객체를 추가해서 전체 목록을 출력해보세요.

🔸 요구사항
[Book 클래스]
속성: title, author
메서드: info() → "책 제목: {title}, 저자: {author}" 출력
[Bookshelf 클래스]
속성: books 리스트
메서드:add_book(book): 책 추가, show_books(): 모든 책 info 출력

[출력 예제]
책 제목: 파이썬 입문, 저자: 솔아
책 제목: 데이터 분석, 저자: 민지

"""
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#     def info(self):
#         print(f"책 제목: {self.title}, 저자: {self.author}")

# class Bookshelf:
#     def __init__(self):
#         self.book_list = []

#     def add_book(self, title, autor):
#         new_book = Book(title, autor)       
#         self.book_list.append(new_book)

#     def show_books(self):
#         for book in self.book_list:
#             book.info()

# new_bookshelf = Bookshelf()
# new_bookshelf.add_book("파이썬 입문", "솔아")
# new_bookshelf.add_book("데이터 분석", "민지")
# new_bookshelf.show_books()
"""
⚔️ 예제 2: 중간 난이도 — 수강생과 강의 (구성 관계 + 동작 포함)
📌 문제 설명
Student 클래스와 Course 클래스를 만들고,
강의에 여러 학생을 등록하고, 출석부를 출력해보세요.

🔸 요구사항
[Student 클래스]
속성: name, grade
메서드: introduce() → "안녕하세요, 저는 {grade}학년 {name}입니다."
[Course 클래스]
속성: title, students 리스트
메서드:
add_student(student): 수강생 추가
remove_student(name): 이름으로 수강생 제거
list_students(): 모든 수강생 소개

[출력결과]
수강생: 지우, 2학년 등록됨
수강생: 현수, 3학년 등록됨

출석부:
안녕하세요, 저는 2학년 지우입니다.
안녕하세요, 저는 3학년 현수입니다.
"""
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def introduce(self):
        print(f"안녕하세요. 저는 {self.grade}학년 {self.name}입니다.")

class Course:
    def __init__(self, title):
        self.students = []
        self.title = title
    def add_student(self, name, grade):
        new_student = Student(name, grade)
        self.students.append(new_student)
        print(f"수강생: {name}, {grade}학년 등록됨")
    def remove_student(self, name):
        self.students = [s for s in self.students if s.name != name]
    def list_student(self):
        for student in self.students:
            student.introduce()

math_course = Course("수학")
math_course.add_student("지우", 2)
math_course.add_student("현수", 3)
math_course.list_student()
math_course.remove_student("지우")
math_course.list_student()