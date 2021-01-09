""""
print("1.자료형")
print("\n\n실수형")
###실수형

#(유효숫자) e (지수) = (유효숫자) 10 (지수)
#10억의 지수표현 방식
a = 1e9
print(a)

#752.5
a = 75.25e1
print(a) 

#3.954
a = 3954e-3
print(a)

#round
a = 0.3 + .6
print(a) #정확한 0.9가 아님!
print(round(a,4)) # 5번째 자리에서 반올림 (4번째 자리까지 표현된다고 이해)

a = 123.456
print(round(a)) #소수점 첫째자리에서 반올림
print(round(a,-1)) #1의자리 반올림
"""

""""

print("\n\n리스트")
###리스트
#비어있는 리스트 만들기
a = list()
print (a)
a = []
print(a) 
#편리한 초기화 방법
a=[0]*10 #크기가 10이고 모든값이 0인 1차원리스트
print(a)


a = [i for i in range(10)]
print(a)

#음수 인덱스 사용(뒤에서 부터 n번째)
print(a[-1])

#슬라이싱
print(a[1:5]) #2번째 부터 5번째 까지 (인덱스 1부터 인덱스 4 까지)


print("\n\n리스트 컴프리헨션")
###리스트 컴프리헨션

#배열을 초기화 할때 다음과 같이 대괄화 안에서 조작이 가능!

array = [i for i in range(10) if i % 2 ==1]

print(array)

array = [i*i for i in range(1,10)]
print(array)


#2차원 리스트
n = 4
m = 3
array = [[0]*m for _ in range(n)]
print(array)

array[1][1] = 5
print(array)

  #잘못된 예
n = 4
m = 3
array = [[0]*m] *n
print(array)

array[1][1] = 5
print(array)
  # 1행, 1열의 위치만 5로 바뀌어야하는데 이 방법으로 2차원리스트를 초기화 생성 시키면 전체 리스트 안에 포함된 각 리스트가 모두 같은 객체로 인식이 되어서 모든 행에 두번째 열이 5로 바뀌에 된다.

print("\n\n리스트 관련 기타 메서드")
###리스트 관련 기타 리스트
a = [1,4,3]
print("기본리스트: ", a)

#리스트에 원소 삽입
a.append(2)
print("삽입: ",a)

#오름차순
a.sort()
print("오름차순 정렬: ",a)

#내림차순
a.sort(reverse = True)
print("내림차순 정렬",a)

#리스트 원소 뒤집기
a.reverse()
print("원소 뒤집기: ", a)

#특정 인덱스에 데이터 추가
a.insert(2,4)
print("인덱스 2에 4 추가: ",a)

#특정 값인 데이터 개수 세기
print("값이 4인 데이터 개수: ", a.count(4))

#특정 값 데이터 삭제
a.remove(1)
print("값이 1인 데이터 삭제: ",a)

#리스트에서 특정 값을 가지는 원소 모두제거
a = [1,2,3,4,5,5,5]
remove_set={3,5} #집합자료형

result = [i for i in a if i not in remove_set]
print(result)
  #리스트컴프리헨션 사용
  # for i in a : 리스트 a의 원소를 순차적으로 탐색
  # if i not in remove_set : remove_set에 존재하지 않는 원소만 반환
"""


"""
print("\n\n문자열")
###문자열

data = 'Hello World' #작은 따옴표 안에 큰따옴표도 가능
print(data)

data = "Don't you know \"Python?\"" #백슬래시(\)를 활용하여 따옴표를 더 넣는것 가능.
print(data)

#문자열 연산
a = "Hello"
b = "World"
print(a + " " + b) # 더하기 연산을 하면 두 문자열이 이어짐.

a = "String"
print(a * 3) #곱하기 연산을 하면 그 수만큼 문자열이 반복됨.

a = "ABCDEF"
print(a[2:4]) #슬라이싱, 인덱싱도 가능
print(a[3]) 
 #변경 불가능

print("\n\n튜플 자료형")
###튜플자료형
a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(a[3])
print(a[1:4])
  #변경 불가능, 컴프리헨션 불가능 

  
print("\n\n사전자료형")
###사전자료형
data = dict()
data["사과"] = "Apple"
data['바나나'] = 'Banana'
data["코코넛"] = 'Coconut'
print(data)



print(data.keys()) #키 데이터만 담은 리스트
print(data.values()) 
#값데이터만 담은 리스트
list_keys = list(data.keys()) #완벽한 리스트 형으로 바꿈.
print(list_keys)


print("\n\n집합 자료형")
###집합자료형
#집합 자료형 초기화 방법1: 리스트형을 set()함수를 통해 집합자료형으로 변경.
data = set([1,2,3,3,4,4,5,1,1])
print(data)
#방법2 : 애초에 집합자료형으로 생성
data = {5,2,-3,3,4,4,5,1,1}
print(data)
  #중복되는 숫자는 하나로만 나옴, 자동 오름차순 (음수는 양수 다음부터 오름차순)

#합집합, 교집합, 차집합
a = set([i for i in range(1,6)])
b = set([i for i in range(3,8)]) 
print(a | b) #합집합
print(a & b) #교집합
print(a - b) #차집합

data = {1,2,3}
data.add(4) #새로운 원소 추가
print(data)

data.update([5,6]) #여러개 추가
print(data)
data.update([-1,-5])
print(data)

data.remove(-5) #특정 원소 삭제
print(data)
"""

"""
print("\n\n입출력")
###입력


n = int(input()) #입력을 받은 정보를 int로 저장.

data1 = input() #공백을 포함하여 data에 그 자체로 저장됨.

data2 = input().split() # 공백을 기준으로 구분하여 입력, 문자열 리스트로 저장됨.

data3 = map(int, input().split()) #출력이 안됨

data4 = list(map(int, input().split())) #map을 이용해 정수형으로 바꿔주고 list형으로 바꿈.
print(data1)
print(data2)
print(data3)
print(data4)

data = data4

data.sort(reverse=True)
print(data)
"""
""""
a,b,c = map(int,input().split()) #다음과 같이 리스트형 말고 3개 각각에 입력값 저장가능
#packing, unpacking 오류를 피하기 위해 정해진 갯수만 입력해야함.a

#빠르게 입력 받기
import sys
data = sys.stdin.readline().rstrip() #input() 보다 빠른수행시간으로 입력받음.
print(data)
"""

#출력
a=1
b=2
print(a,b) #콤마를 이용해 띄어쓰기 간격 출력 후 자동 줄바꿈(enter)
print(7,end=" ") #출력후 띄어 쓰기만 하도록 조정
print(8, end = " ")

answer = 7
print("정답은 "+ str(answer) + "입니다.") 
  #문자열과 정수형을 더하기연산할수 없기 때문에 정수형을 문자열로 바꾸어 더하기연산후 출력.
print(f"정답은 {answer}입니다.") #f-string으로도 출력가능 굳이 정수형을 문자열로 바꿀필요 없음.