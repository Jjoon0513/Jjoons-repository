#if문 입니다

#일단 처음으로 if문의 기초는

#if 참,거짓:
#    //실행문//

#이며 추가로
#else, elif를 추가적으로 입력할 수 있습니다

#else는 if문이 거짓이 나오면 작동하며
#elif는 if문이 거짓이 나왔으며 elif문에 조건이 맞을시 작동합니다
#else 혹은 elif 를 추가적으로 입력한다면

#if 참,거짓:
#  //실행문//
#elif 참,거짓:
#  //실행문//
#else 참,거짓:
#  //실행문//

if x:
  print("HelloWorld!")
 
  #x가 참이라면 HelloWorld!를출력합니다

if x == 5:
  print("HelloWorld!")
 
  #x가 5와 같다면 HelloWorld!를 출력합니다
  
if x == 7:
  print("HelloWorld!")
else:
  print("HelloPython!")
 
  #x가 5와 같다면 HelloWorld!를 출력합니다
  #아니라면 HelloPython!을 출력합니다
  
if x == 10
  print("HelloWorld!")
elif x == 4
  print("HelloPython!")
else:
  print("HelloJjoon!")

  #x가 10과 같다면 HelloWorld!를 출력합니다
  #아니고 x가 4과 같다면 HelloPython!를 출력합니다
  #다 아니면 HelloJjoon!을 출력합니다
