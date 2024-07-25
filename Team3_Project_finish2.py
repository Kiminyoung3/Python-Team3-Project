import pandas as pd
from datetime import datetime
import os

class SafetyMetricsCalculator:

    def __init__(self):
        pass

    def 도수율_계산기(self, number_of_accidents, total_work_hours):
        return (number_of_accidents / total_work_hours) * 1_000_000

    def 강도율_계산기(self, lost_work_days, total_work_hours):
        return (lost_work_days / total_work_hours) * 1_000

    def 연천인율_계산기(self, number_of_accidents, total_workers):
        return (number_of_accidents / total_workers) * 1_000

    def 종합재해지수_계산기1(self, number_of_accidents, total_work_hours, lost_work_days):
        frequency_rate = self.도수율_계산기(number_of_accidents, total_work_hours)
        severity_rate = self.강도율_계산기(lost_work_days, total_work_hours)
        return (frequency_rate * severity_rate) ** 0.5

    def 종합재해지수_계산기2(self, dosu, gangdo):
        return (dosu * gangdo) ** 0.5

def get_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError
            else:
                return value
        except ValueError:
            print("유효한 양의 정수를 입력해주세요.")

def save_to_excel(file_name, results):
    if os.path.exists(file_name):
        df = pd.read_excel(file_name)
    else:
        df = pd.DataFrame()

    new_data = pd.DataFrame(results)
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_excel(file_name, index=False)
    print(f'데이터가 {file_name} 파일에 저장되었습니다.')

def main():
    print("=" * 60)
    print("          ~~~~~~~ 재해 지수 계산기입니다. ~~~~~~~")
    print("   ~도수율, 강도율, 연천인율, 종합재해지수를 계산할 수 있습니다.~")
    print("=" * 60)

    calculator = SafetyMetricsCalculator()
    results = []

    while True:
        get_choice = input("              ~계산할 재해 지수를 입력하세요.~ \n1. 도수율 \n2. 강도율 \n3. 연천인율 \n4. 종합재해지수 "
                           "\n\n→ 재해 지수 선택: ").strip()

        if get_choice == "도수율":
            number_of_accidents = get_input("\n★ 재해 발생 건수를 입력하세요.: ")
            total_work_hours = get_input("★ 연간 근로시간을 입력하세요.: ")

            frequency_rate = calculator.도수율_계산기(number_of_accidents, total_work_hours)
            results.append({
                '재해 지수 종류': '도수율',
                '입력값': f"재해 발생 건수: {number_of_accidents}, 연간 근로시간: {total_work_hours}",
                '결과값': frequency_rate
            })

            print("." * 60)
            print("               ", "-" * 10, "계산결과", "-" * 10)
            print("." * 60)
            print("♥ 도수율: ", frequency_rate, "→ 100만 근로시간당", frequency_rate, "건의 재해 발생")
            print("=" * 60)

        elif get_choice == "강도율":
            lost_work_days = get_input("★ 근로손실일수를 입력하세요.: ")
            total_work_hours = get_input("★ 연간 근로시간을 입력하세요.: ")

            severity_rate = calculator.강도율_계산기(lost_work_days, total_work_hours)
            results.append({
                '재해 지수 종류': '강도율',
                '입력값': f"근로손실일수: {lost_work_days}, 연간 근로시간: {total_work_hours}",
                '결과값': severity_rate
            })

            print("." * 60)
            print("               ", "-" * 10, "계산결과", "-" * 10)
            print("." * 60)
            print("♥ 강도율: ", severity_rate, "→ 1000시간당", severity_rate, "일의 근로손실일수 발생")
            print("=" * 60)

        elif get_choice == "연천인율":
            number_of_accidents = get_input("★ 재해 발생 건수를 입력하세요.: ")
            total_workers = get_input("★ 연평균 근로자 수를 입력하세요.: ")

            annual_accident_rate = calculator.연천인율_계산기(number_of_accidents, total_workers)
            results.append({
                '재해 지수 종류': '연천인율',
                '입력값': f"재해 발생 건수: {number_of_accidents}, 연평균 근로자 수: {total_workers}",
                '결과값': annual_accident_rate
            })

            print("." * 60)
            print("               ", "-" * 10, "계산결과", "-" * 10)
            print("." * 60)
            print(f"♥ 연천인율: ", annual_accident_rate, "→ 1년에 1000명 당", annual_accident_rate, "건의 재해 발생")
            print("=" * 60)

        elif get_choice == "종합재해지수":
            while True:
                disaster = input("도수율과 강도율을 먼저 계산하시겠습니까? (네/아니오): ").strip().lower()

                if disaster == "네":
                    number_of_accidents = get_input("★ 재해 발생 건수를 입력하세요.: ")
                    total_work_hours = get_input("★ 연간 근로시간을 입력하세요.: ")
                    lost_work_days = get_input("★ 근로손실일수를 입력하세요.: ")

                    comprehensive_disaster_index1 = calculator.종합재해지수_계산기1(number_of_accidents, total_work_hours, lost_work_days)
                    frequency_rate1 = calculator.도수율_계산기(number_of_accidents, total_work_hours)
                    severity_rate1 = calculator.강도율_계산기(lost_work_days, total_work_hours)

                    results.append({
                        '재해 지수 종류': '종합재해지수',
                        '입력값': f"도수율: {frequency_rate1}, 강도율: {severity_rate1}",
                        '결과값': comprehensive_disaster_index1
                    })

                    print("." * 60)
                    print("               ", "-" * 10, "계산결과", "-" * 10)
                    print("." * 60)
                    print("♥ 도수율: ", frequency_rate1)
                    print("♥ 강도율: ", severity_rate1)
                    print("♥ 종합재해지수: ", comprehensive_disaster_index1)
                    print("=" * 60)

                    break

                elif disaster == "아니오":
                    dosu = get_input("★ 도수율을 입력하세요.: ")
                    gangdo = get_input("★ 강도율을 입력하세요.: ")

                    comprehensive_disaster_index2 = calculator.종합재해지수_계산기2(dosu, gangdo)

                    results.append({
                        '재해 지수 종류': '종합재해지수',
                        '입력값': f"도수율: {dosu}, 강도율: {gangdo}",
                        '결과값': comprehensive_disaster_index2
                    })

                    print("." * 60)
                    print("               ", "-" * 10, "계산결과", "-" * 10)
                    print("." * 60)
                    print("♥ 종합재해지수: ", comprehensive_disaster_index2)
                    print("=" * 0)

                    break

                else:
                    print("올바른 입력을 하세요. (네/아니오)")

        else:
            print("위의 재해 지수 중 한 가지를 입력해주세요.")

        repeat = input("계산을 다시 하시겠습니까? (네/아니오): ").strip().lower()

        if repeat != '네':
            break

    if results:
        save_to_excel("results.xlsx", results)

if __name__ == "__main__":
    main()
