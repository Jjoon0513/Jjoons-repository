#만일 랜덤 수를 지정하고 싶으면 Python 기본 내장 모듈인
#random 모듈을 사용하면 됩니다 먼저 random 모듈을 사용하려면
#(import random) 을 사용하여 파일에 random 모듈을 임포트 하시면 됩니다.
#예를 보여드리겠습니다.

import random

#이렇게 입력하시면 임포트 됩니다.
#seed값을 바꾸어야 random값이 변경되던 C언어와는 다르게
#파이썬에서는 seed를 쓸필요가 없습니다.

random.random()
#1과 0사이중 아무숫자나 지정해줍니다.(소수점 15자리)

#예를들어 70% 확률로 코드가 실행되도록 하고싶을때

if random.random() <= 0.7:
  print("HelloWorld!")
  #70%확률로 HelloWorld!를 출력합니다

#두번째로 random.randint()를 사용한다면 더욱 쉬운 사용이 가능합니다.
#random.randint()는 괄호안에 두 수를 지정하면 첫번째수 이상 두번째수 이하의 랜덤한 수 중 하나를 지정해줍니다.
#마찬가지로 예를 보여드리겠습니다.

if random.randint(1,10) == 4:
  #1이상 10이하 수 중 숫자 하나를 지정합니다.
  print("HelloWorld")
  #만일 숫자가 4와 같을시 HelloWorld！를 출력합니다.

if random.randint(1,10) <= 6:
  #1이상 10이하 수 중 숫자 하나를 지정합니다.
  print("HelloWorld")
  #만일 숫자가 6보다 낮을시 HelloWorld！를 출력합니다.
  #또한 이는 60%의 확률로 HelloWorld!를 출력합니다.

#마지막으로 random.choice()를 사용하면 리스트중에 하나를 선택해줍니다
a = [a, b, c, d]
#리스트를 저장한다면

random.choice(a)
#a리스트안에서 랜덤한 값 하나를 지정합니다.
#a 일수도 있고 b,c또는 d 일수도 있습니다.

x = [apple, orange, bird, cow]
print(random.choice(x))
#x리스트안에서 랜덤한 값 하나를 지정하여 출력합니다.
#apple 일수도 있고 orange, bird 또는 cow일수도 있습니다.
