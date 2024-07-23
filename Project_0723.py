def calculate_frequency_rate(number_of_accidents, total_work_hours):
    """
    Calculate Frequency Rate (도수율).
    :param number_of_accidents: Total number of accidents (건수)
    :param total_work_hours: Total work hours (시간)
    :return: Frequency Rate (per million hours)
    """
    return (number_of_accidents / total_work_hours) * 1_000_000


def calculate_severity_rate(lost_work_days, total_work_hours):
    """
    Calculate Severity Rate (강도율).
    :param lost_work_days: Total lost work days due to accidents (일수)
    :param total_work_hours: Total work hours (시간)
    :return: Severity Rate (per thousand hours)
    """
    return (lost_work_days / total_work_hours) * 1_000


def calculate_annual_accident_rate(number_of_accidents, total_workers):
    """
    Calculate Annual Accident Rate (연천인율).
    :param number_of_accidents: Total number of accidents (건수)
    :param total_workers: Total number of workers (근로자 수)
    :return: Annual Accident Rate (per thousand workers)
    """
    return (number_of_accidents / total_workers) * 1_000


def calculate_comprehensive_disaster_index(frequency_rate, severity_rate):
    """
    Calculate Comprehensive Disaster Index (종합재해지수).
    :param frequency_rate: Frequency Rate (도수율)
    :param severity_rate: Severity Rate (강도율)
    :return: Comprehensive Disaster Index
    """
    return (frequency_rate * severity_rate) ** 0.5


# Example usage
number_of_accidents = 5
total_work_hours = 200_000
lost_work_days = 150
total_workers = 100

frequency_rate = calculate_frequency_rate(number_of_accidents, total_work_hours)
severity_rate = calculate_severity_rate(lost_work_days, total_work_hours)
annual_accident_rate = calculate_annual_accident_rate(number_of_accidents, total_workers)
comprehensive_disaster_index = calculate_comprehensive_disaster_index(frequency_rate, severity_rate)

print(f"Frequency Rate (도수율): {frequency_rate:.2f} per million hours")
print(f"Severity Rate (강도율): {severity_rate:.2f} per thousand hours")
print(f"Annual Accident Rate (연천인율): {annual_accident_rate:.2f} per thousand workers")
print(f"Comprehensive Disaster Index (종합재해지수): {comprehensive_disaster_index:.2f}")
