def check_equations(equations):
    results = []  # 결과를 저장할 리스트
    for equation in equations:
        # 등호 기준으로 좌항과 우항 분리
        expression, answer = equation.split('=')
        # 좌항 평가 및 우항 값 변환
        calculated = eval(expression.strip())  # 좌항 계산
        given_answer = int(answer.strip())  # 우항 값
        # 비교 결과 추가
        if calculated == given_answer:
            results.append('O')  # 맞으면 'O'
        else:
            results.append('X')  # 틀리면 'X'
    return results

if __name__ == "__main__":
    # 테스트
    equations = ["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]
    print(check_equations(equations))