#도수율, 강도율, 연천인율, 종합재해지수를 계산하는 코드
#반복문, 함수, 클래스, 조건문 활용하여 구성

# get_input 함수: 사용자로부터 양의 정수를 입력받기 위한 함수입니다. 사용자가 잘못된 입력을 할 경우 오류 메시지를 표시하고 다시 입력을 받습니다.

# main 함수: 프로그램의 주요 실행 흐름을 관리합니다.
#             사용자가 입력한 데이터를 바탕으로 SafetyMetricsCalculator 객체를 생성하고 각 지표를 계산하여 출력합니다.
#             또한 반복하여 계산할 수 있도록 반복문을 사용합니다.

#클래스 생성
class SafetyMetricsCalculator:
    def __init__(self, number_of_accidents, total_work_hours, lost_work_days, total_workers, dosu, gangdo):
        self.number_of_accidents = number_of_accidents     #요소1: 재해발생건수
        self.total_work_hours = total_work_hours     #요소2: 근로시간
        self.lost_work_days = lost_work_days     #요소3: 근로손실일수
        self.total_workers = total_workers     #요소4: 근로자 수
        self.dosu = dosu
        self.gangdo = gangdo

    def 도수율_계산기(self):
    # 도수율 계산하는 함수 = 재해발생건수/근로시간 * 1,000,000
        return (self.number_of_accidents / self.total_work_hours) * 1_000_000

    def 강도율_계산기(self):
    # 강도율 계산하는 함수 = 근로손실일수/근로시간 * 1,000
        return (self.lost_work_days / self.total_work_hours) * 1_000

    def 연천인율_계산기(self):
    # 연천인율 계산하는 함수 = 재해발생건수/근로자 수 * 1,000
        return (self.number_of_accidents / self.total_workers) * 1_000

    def 종합재해지수_계산기1(self):
    # 도수율과 강도율을 모를때: 종합재해지수 계산하는 함수 = 루트(도수율 * 강도율)
        frequency_rate = self.도수율_계산기()
        severity_rate = self.강도율_계산기()
        return (frequency_rate * severity_rate) ** 0.5

    def 종합재해지수_계산기2(self):
    # 도수율과 강도율을 알때: 종합재해지수 계산하는 함수 = 루트(도수율 * 강도율)
        return (self.dosu * self.gangdo) ** 0.5


def get_input(prompt):
#사용자로부터 양의 정수를 입력받기 위한 함수. 잘못된 입력을 할 경우 오류메세지 표시 후 다시 입력받는다.
    while True:
        try:
            value = int(input(prompt)) #값을 입력받음
            if value < 0: #입력받은 값이 양수일 경우,
                raise ValueError #예외 발생시킴(입력받은 값이 양수가 아닐 경우)
            else:
                return value
        except ValueError: #예외를 에러로 인식하고 처리함
            print("유효한 양의 정수를 입력해주세요.")


def main():
    print("=" * 30)
    print("*<Safety Metrics Calculator>*")
    print("=" * 30)

    while True:
        get_choice = input("계산할 재해 지수를 입력하세요. (도수율/강도율/연천인율/종합재해지수): ")

        if get_choice == "도수율":
            number_of_accidents = get_input("★ 재해 발생 건수를 입력하세요.: ")
            total_work_hours = get_input("★ 연간 근로시간을 입력하세요.: ")

            calculator = SafetyMetricsCalculator(number_of_accidents, total_work_hours)
            frequency_rate = calculator.도수율_계산기()

            print("♥ 도수율: ", frequency_rate, "→ 100만 근로시간당", frequency_rate, "건의 재해 발생")

        elif get_choice == "강도율":
            lost_work_days = get_input("★ 근로손실일수를 입력하세요.: ")
            total_work_hours = get_input("★ 연간 근로시간을 입력하세요.: ")

            calculator = SafetyMetricsCalculator(lost_work_days, total_work_hours)
            severity_rate = calculator.강도율_계산기()

            print("♥ 강도율: ", severity_rate, "→ 1000시간당", severity_rate, "일의 근로손실일수 발생")

        elif get_choice == "연천인율":
            number_of_accidents = get_input("★ 재해 발생 건수를 입력하세요.: ")
            total_workers = get_input("★ 연평균 근로자 수를 입력하세요.: ")

            calculator = SafetyMetricsCalculator(number_of_accidents, total_workers)
            annual_accident_rate = calculator.연천인율_계산기()

            print(f"♥ 연천인율: ", annual_accident_rate, "→ 1년에 1000명 당", annual_accident_rate, "건의 재해 발생")

        elif get_choice == "종합재해지수":
            while True:
                disaster = input("도수율과 강도율을 먼저 계산하시겠습니까? (네/아니오): ")
                if disaster == "네":
                    number_of_accidents = get_input("★ 재해 발생 건수를 입력하세요.: ")
                    total_work_hours = get_input("★ 연간 근로시간을 입력하세요.: ")
                    lost_work_days = get_input("★ 근로손실일수를 입력하세요.: ")

                    calculator = SafetyMetricsCalculator(number_of_accidents, total_work_hours, lost_work_days)
                    comprehensive_disaster_index1 = calculator.종합재해지수_계산기1()

                    print("♥ 종합재해지수: ", comprehensive_disaster_index1)

                if disaster == "아니오":
                    get_disaster1 = get_input("★ 도수율을 입력하세요.: ")
                    get_disaster2 = get_input("★ 강도율을 입력하세요.: ")
                    comprehensive_disaster_index2 = calculator.종합재해지수_계산기2()
                    print("♥ 종합재해지수: ", comprehensive_disaster_index2)


        else:
            print("위의 재해 지수 중 한 가지를 입력해주세요.")

        repeat = input("계산을 다시 하시겠습니까? (네/아니오): ").strip().lower()
        if repeat != '네':
            break


if __name__ == "__main__":
    main()
