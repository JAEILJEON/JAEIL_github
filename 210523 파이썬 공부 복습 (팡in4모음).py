
scores = [80, 65, 43, 78, 88, 100, 44, 55, 75]
student_index = 0

for score in scores:

  student_index += 1

  if score < 70 :
    print(f'{student_index}번 학생 아쉽지만 다음 기수에 다시 지원해 주시길 바랍니다.')
  
  else:
    print(f'{student_index}번 학생 축하합니다!! 광주 인공지능사관학교에 최종 합격하셨습니다.')
