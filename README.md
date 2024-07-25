'재해지수 계산기: 안전 강.도'는 다양한 재해 지수를 계산할 수 있는 프로그램입니다. 이 계산기를 사용해서 도수율, 강도율, 연천인율, 종합재해지수를 쉽게 계산할 수 있습니다.

#기능소개
 1. 도수율 계산기
    - 재해 발생 건수와 연간 근로시간을 입력하여 도수율을 계산합니다.
    - 도수율 공식: '도수율 = (재해발생건수 / 근로시간) * 1,000.000'
 2. 강도율 계산기
    - 근로손실일수와 연간 근로시간을 입력하여 강도율을 계산합니다.
    - 강도율 공식: '강도율 = (근로손실일수 / 근로시간) * 1,000'
 3. 연천인율 계산기
    - 재해 발생 건수와 연평균 근로자 수를 입력하여 연천인율을 계산합니다.
    - 연천인율 공식: '연천인율 = (재해발생건수 / 근로자 수) * 1,000'
 4. 종합재해지수 계산기
    - 도수율과 강도율을 모르는 경우: 재해 발생 건수, 연간 근로시간, 근로손실일수를 입력하여 종합재해지수를 계산합니다.
    - 도수율과 강도율을 알고있는 경우: 직접 도수율을 입력하여 종합재해지수를 계산합니다.
    - 종합재해지수 공식: '종합재해지수 = 루트(도수율 * 강도율)'

#사용 방법
 1. 도수율 계산하기
    - 재해 발생 건수와 연간 근로시간을 입력합니다.
    - 예시 입력
      - 재해 발생 건수 : 5
      - 연간 근로시간: 200,000
    - 출력
      -도수율: 25.0 → 100만 근로시간당 25.0건의 재해 발생
 2. 강도율 계산하기
    - 근로손실일수와 연간 근로시간을 입력합니다.
    - 예시 입력
      -근로손실일수: 50
      -연간 근로시간: 200,000
    - 출력
      -강도율: 0.25 → 1000시간당 25.0일의 근로손실일수 발생
 3. 연천인율 계산하기
    - 재해 발생 건수와 연평균 근로자 수를 입력합니다.
    - 예시 입력
      -재해 발생 건수: 5
      -연평균 근로자 수: 1000
    - 출력
      -연천인율: 5.0 → 1년에 1000명 당 5.0건의 재해 발생
 4. 종합재해지수 계산하기
    - 도수율과 강도율을 먼저 계산한 후 입력하거나, 이미 알고 있는 도수율과 강도율을 입력합니다.
    - 예시 입력
      -재해 발생 건수: 5
      -연간 근로시간: 200,000
      -근로손실일수: 50
    - 출력
      -도수율: 25.0
      -강도율: 0.25
      -종합재해지수: 2.5

#사용성 개선
 1. 재해 지수에 필요한 변수를 입력할 때 양수 정수가 아닌 값을 입력할 경우
    - -500, 사과 등 입력
      : 오류메세지 "올바른 값을 입력하세요. (네/아니요)"를 출력
 2. 계산 완료 후 재시작 여부 확인
    - 재해 지수 결과 값 출력 후
      :"계산을 다시 하시겠습니까? (네/아니요)" 를 출력
