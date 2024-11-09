import math

def question1(inNum):
   print("input : ", inNum)
   sum = 0
   while (inNum > 0):
      sum = sum + (inNum % 10)
      inNum = inNum // 10
   print(sum)
   return sum # 30

def question2(inNum):
   print("input : ", inNum)
   for i in range(2, inNum):
      if ((inNum % i) == 0):
         return "소수 아님"
   return "소수"

def question3(list1, list2):
   print("input : ", list1, list2)
   cnt = 0
   for i in range(0, len(list1)):
      for j in range(0, len(list2)):
         if (list1[i] == list2[j]):
            cnt += 1
   return cnt

def question4(inStr):
   print("input : ", inStr)
   sum = 0
   outStr = ""
   for i in range(0, len(inStr)):
      if str(inStr[i]).isalpha(): # 새로운 문자열에 붙여주는 느낌
         outStr += " " # 만약 알파벳이면 공백으로 추가함
      else :
         outStr += inStr[i] # 알파벳이 아니면 그냥 그 값 그대로 추가
   aList = outStr.split()
   for i in range(0, len(aList)):
      sum += int(aList[i])
   return sum # 27
  
def question5(inStr, inList):
   print("input : ", inStr, inList)
   a = list(inStr)
   for i in inList:
      a[i] = ""
   a = "".join(a) # join에 구분자가 없는 경우 그냥 모든 요소를 붙임
   return a # "programmers"

def question6(inNum):
   print("input : ", inNum)
   
   return int(math.lcm(6, inNum)/6) # inNum과 6의 최소공배수를 피자 조각 수인 6으로 다시 나눠줌

def question7(inStr1, inStr2):
   print("input : ", inStr1, inStr2)
   #입력으로 주어지는 날짜를 정수로 변환하고 시간도 초단위 정수로
      # 날짜 정수 * 86400 + 초단위 정수 -> 특정 숫자(초단위)
      # 뒷값에서 앞값빼면 몇초동안 주차했는지 나옴
      # -> 주차 요금 계산하는 로직으로 하기
   inStr1 = str(inStr1)
   inStr2 = str(inStr2)

   date1, time1 = inStr1.split()
   date2, time2 = inStr2.split()

   date1List = date1.split(".")
   date1List.pop(-1)
   date2List = date2.split(".")
   date2List.pop(-1)

   for i in range(0, len(date1List)):
      date1List[i] = int(date1List[i])
      date2List[i] = int(date2List[i])

   time1List = time1.split(":")
   time2List = time2.split(":")

   for i in range(0, len(time1List)):
      time1List[i] = int(time1List[i])
      time2List[i] = int(time2List[i])

   print(date1List, time1List)
   print(date2List, time2List)

   valueD1 = (date1List[0] * 365 * 86400) + (date1List[1] * 30 * 86400) + (date1List[2] * 86400) + (time1List[0] * 3600) + (time1List[1] * 60) + (time1List[2])
   valueD2 = (date2List[0] * 365 * 86400) + (date2List[1] * 30 * 86400) + (date2List[2] * 86400) + (time2List[0] * 3600) + (time2List[1] * 60) + (time2List[2])
   
   # 윤년, 월별 날짜를 고려해야함

   # parking_charge = ((pay + 599) // 600) * 500  # 10분 단위로 올림 계산
   # print("주차 요금:", parking_charge)
   
   # return parking_charge # 5138000


if __name__ == "__main__":
   # if question1(698142) == 30:
   #    print("1번. 정답입니다.")
   # else:
   #    print("1번. 정답이 아닙니다.")
   
   # if question2(5) == "소수":
   #    print("2번. 정답입니다.")
   # else:
   #    print("2번. 정답이 아닙니다.")
   
   # if question2(9) == "소수 아님":
   #    print("2번. 정답입니다.")
   # else:
   #    print("2번. 정답이 아닙니다.")

   # if question3([15, 4, 9, 3, 5], [2, 8, 1, 0, 32, 9, 3]) == 2:
   #    print("3번. 정답입니다.")
   # else:
   #    print("3번. 정답이 아닙니다.")

   # if question4("ab12c5d1e9") == 27:
   #    print("4번. 정답입니다.")
   # else:
   #    print("4번. 정답이 아닙니다.")

   if question5("apporoograpemmemprs", [1, 16, 6, 15, 0, 10, 11, 3]) == "programmers":
      print("5번. 정답입니다.")
   else:
      print("5번. 정답이 아닙니다.")

   # if question6(7) == 7:
   #    print("6번. 정답입니다.")
   # else:
   #    print("6번. 정답이 아닙니다.")

   # if question6(4) == 2:
   #    print("6번. 정답입니다.")
   # else:
   #    print("6번. 정답이 아닙니다.")

   # if question7("2023.12.27. 10:20:30", "2024.3.7. 19:00:05") == 5138000: # 날짜구하는 달력
      
   #    print("7번. 정답입니다.")
   # else:
   #    print("7번. 정답이 아닙니다.")