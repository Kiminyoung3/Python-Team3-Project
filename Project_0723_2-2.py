print("=" * 50)
print("             ~ 재해 지수 계산기입니다. ~")
print("-도수율, 강도율, 연천인율, 종합재해지수를 계산할 수 있습니다.")
class SafetyMetricsCalculator:

    def 도수율_계산기(self, number_of_accidents, total_work_hours):
        # 도수율 계산하는 함수 = 재해발생건수/근로시간 * 1,000,000
        return (number_of_accidents / total_work_hours) * 1_000_000

    def 강도율_계산기(self, lost_work_days, total_work_hours):
        # 강도율 계산하는 함수 = 근로손실일수/근로시간 * 1,000
        return (lost_work_days / total_work_hours) * 1_000

    def 연천인율_계산기(self, number_of_accidents, total_workers):
        # 연천인율 계산하는 함수 = 재해발생건수/근로자 수 * 1,000
        return (number_of_accidents / total_workers) * 1_000

    def 종합재해지수_계산기1(self, number_of_accidents, total_work_hours, lost_work_days):
        # 도수율과 강도율을 모를때: 종합재해지수 계산하는 함수 = 루트(도수율 * 강도율)
        frequency_rate = self.도수율_계산기(number_of_accidents, total_work_hours)
        severity_rate = self.강도율_계산기(lost_work_days, total_work_hours)
        return (frequency_rate * severity_rate) ** 0.5

    def 종합재해지수_계산기2(self, dosu, gangdo):
        # 도수율과 강도율을 알때: 종합재해지수 계산하는 함수 = 루트(도수율 * 강도율)
        return (dosu * gangdo) ** 0.5


def get_input(prompt):

    while True:
        try:
            value = int(input(prompt))  # 값을 입력받음
            if value < 0:  # 입력받은 값이 양수일 경우,
                raise ValueError  # 예외 발생시킴(입력받은 값이 양수가 아닐 경우)
            else:
                return value
        except ValueError:  # 예외를 에러로 인식하고 처리함
            print("유효한 양의 정수를 입력해주세요.")


def main():
    print("=" * 50)
    print("*"*10, "<Safety Metrics Calculator>", "*"*10)
    print("=" * 50)

    calculator = SafetyMetricsCalculator()

    while True:
        get_choice = input("계산할 재해 지수를 입력하세요. (도수율/강도율/연천인율/종합재해지수): ").strip()
        print("-" * 30)

        if get_choice == "도수율":
            number_of_accidents = get_input("★ 재해 발생 건수를 입력하세요.: ")
            total_work_hours = get_input("★ 연간 근로시간을 입력하세요.: ")

            frequency_rate = calculator.도수율_계산기(number_of_accidents, total_work_hours)
            print("-" * 10, "계산결과", "-" * 10)
            print("♥ 도수율: ", frequency_rate, "→ 100만 근로시간당", frequency_rate, "건의 재해 발생")
            print("=" * 50)

        elif get_choice == "강도율":
            lost_work_days = get_input("★ 근로손실일수를 입력하세요.: ")
            total_work_hours = get_input("★ 연간 근로시간을 입력하세요.: ")

            severity_rate = calculator.강도율_계산기(lost_work_days, total_work_hours)
            print("-" * 10, "계산결과", "-" * 10)
            print("♥ 강도율: ", severity_rate, "→ 1000시간당", severity_rate, "일의 근로손실일수 발생")
            print("=" * 50)

        elif get_choice == "연천인율":
            number_of_accidents = get_input("★ 재해 발생 건수를 입력하세요.: ")
            total_workers = get_input("★ 연평균 근로자 수를 입력하세요.: ")

            annual_accident_rate = calculator.연천인율_계산기(number_of_accidents, total_workers)
            print("-" * 10, "계산결과", "-" * 10)
            print(f"♥ 연천인율: ", annual_accident_rate, "→ 1년에 1000명 당", annual_accident_rate, "건의 재해 발생")
            print("=" * 50)

        elif get_choice == "종합재해지수":
            while True:
                disaster = input("도수율과 강도율을 먼저 계산하시겠습니까? (네/아니오): ").strip().lower()
                print("-" * 50)
                if disaster == "네":
                    number_of_accidents = get_input("★ 재해 발생 건수를 입력하세요.: ")
                    total_work_hours = get_input("★ 연간 근로시간을 입력하세요.: ")
                    lost_work_days = get_input("★ 근로손실일수를 입력하세요.: ")

                    comprehensive_disaster_index1 = calculator.종합재해지수_계산기1(number_of_accidents, total_work_hours, lost_work_days)
                    frequency_rate1 = calculator.도수율_계산기(number_of_accidents, total_work_hours)
                    severity_rate1 = calculator.강도율_계산기(lost_work_days, total_work_hours)

                    print("-" * 10, "계산결과", "-" * 10)
                    print("♥ 도수율: ", frequency_rate1)
                    print("♥ 강도율: ", severity_rate1)
                    print("♥ 종합재해지수: ", comprehensive_disaster_index1)
                    print("=" * 50)
                    break

                elif disaster == "아니오":
                    dosu = get_input("★ 도수율을 입력하세요.: ")
                    gangdo = get_input("★ 강도율을 입력하세요.: ")

                    comprehensive_disaster_index2 = calculator.종합재해지수_계산기2(dosu, gangdo)
                    print("-" * 10, "계산결과", "-" * 10)
                    print("♥ 종합재해지수: ", comprehensive_disaster_index2)
                    print("=" * 50)
                    break

                else:
                    print("올바른 입력을 하세요. (네/아니오)")
                    print("=" * 50)

        else:
            print("위의 재해 지수 중 한 가지를 입력해주세요.")

        repeat = input("계산을 다시 하시겠습니까? (네/아니오): ").strip().lower()
        print("=" * 50)
        if repeat != '네':
            break


if __name__ == "__main__":
    main()
