'''
1. Type Class
Python은 객체 지향 프로그래밍 언어이다. Python에서 기본적으로 정의되어 있는
클래스를 최소 5가지 이상 작성하시오.
'''

#답안 - int float complex list tuple range str dict set True False

'''
2. Magic Method
아래에 제시된 매직 메서드들이 각각 어떠한 역할을 하는지 간단하게 작성하시오.
__init__, __del__, __str__, __repr__
'''
# 답안
'''
python의 magic method는 특별한 method들을 통칭한다.
special method, Double UNDERscroe method라고도 부름.

1. __init__ ->(initialize method) class의 instance가 생성될 때 자동 call.
method 자체가 뭔가 동작한다는 의미. function call 할 때 처럼 __init__ 아래 코드를 읽어주는 효과가 생긴다.
class method를 __init__ 보다 위쪽에 define하고, initialize method에 call하도록 할 수도 있음.
initialize method를 정의할 때 parentheses 안에 self 이외에 들어가는 arguments를 넣어줘야함.
다른 object oriented language에서는 생성자(constructor)라고 부름.

2. __del__ -> delete라고 생각. 소멸자(destructor)
instance가 사라지기전에 특정코드들이 읽혔으면 할때 __del__넣고, 그 아래에 원하는 코드를 넣어준다.

3. __str__ -> 객체를 사용자가 이해할 수 있는 str로 return하는 함수.
repr과 다르게, 추가적인 가공이나 다른데이터와 호환될 수 있도록 '문자열화'하는데 목적이 있음.
ex) print()안에 여러 data type을 한번에 넣는것.(서로 다른 자료형간에 interface를 제공하기 위해 존재)
단적으로 A라는 class에 str(a), print(a)하면 __str__을 읽지만, 그냥 a를 실행시키면 __repr__을 읽어준다.

4. __repr__ -> representation method. object의 '본질'보다 외부에 노출되는 object의 모습을 나타냄.
 (인간이 이해할 수 있는 '표현'으로 나타내기 위함) 해당 object를 인간이 이해할 수 있는 '표현'으로 나타내기 위함.
 
 
 python에서는 모든 var들이 class이고 instance.
'''


'''
3. Instance Method
.sort()같이 str, list, dict 조작할때 사용했던것들은 class에 정의된 method들이었다. 
이처럼 str, list, dict등을 조작하는 method들을 최소 3가지 이상 그 역할과 함께 작성
list.count() => list안의 element 개수가 몇개인지 int type으로 return
list.index(value) => list안의 특정 value값의 첫번째 idx number. 같은 value가 여러번 반복되어도 첫번째 index만 return
dict.items() => dict의 data를 (key, value) tuple 형태로 한겹 싸인 list를 return

'''

'''
4. 오류의 종류
아래에 제시되어있는 오류들이 각각 어떤 경우에 발생하는지 작성

1.ZeroDivisionError -> 0으로 나눴을때 발생. 0으로 나누면 무한발산하니까 컴퓨터가 value를 return할 수 없다.
2.NameError -> 1.변수 선언안하고 사용.// 2.대소문자 틀림,오타// 3.외장함수 import안하고 사용
3.TypeError -> 연산자에서 type불일치. method가 요구하는 type과 맞지않을때 발생. function call시 arg 안넣었을 때.
4.IndexError ->iterable object의 element 추출시에 발생. 잘못된 index 입력.
5.KeyError -> dict의 해당 key가 없을 때
6.ModuleNotFoundError ->해당 이름의 모듈이 존재하지 않을때. 오타를 확인하거나, directory가 잘되어있는지 확인. 가상환경 잘못일수도.
7.ImportError -> module은 있는데 module안에 해당 class나 함수가 없을 때.

'''
