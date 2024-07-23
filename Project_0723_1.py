class SafetyMetricsCalculator:
    """Class to calculate safety metrics including Frequency Rate, Severity Rate, Annual Accident Rate, and Comprehensive Disaster Index."""

    def __init__(self, number_of_accidents, total_work_hours, lost_work_days, total_workers):
        self.number_of_accidents = number_of_accidents
        self.total_work_hours = total_work_hours
        self.lost_work_days = lost_work_days
        self.total_workers = total_workers

    def calculate_frequency_rate(self):
        """Calculate Frequency Rate (도수율)."""
        return (self.number_of_accidents / self.total_work_hours) * 1_000_000

    def calculate_severity_rate(self):
        """Calculate Severity Rate (강도율)."""
        return (self.lost_work_days / self.total_work_hours) * 1_000

    def calculate_annual_accident_rate(self):
        """Calculate Annual Accident Rate (연천인율)."""
        return (self.number_of_accidents / self.total_workers) * 1_000

    def calculate_comprehensive_disaster_index(self):
        """Calculate Comprehensive Disaster Index (종합재해지수)."""
        frequency_rate = self.calculate_frequency_rate()
        severity_rate = self.calculate_severity_rate()
        return (frequency_rate * severity_rate) ** 0.5


def get_input(prompt):
    """Get a positive integer input from the user with validation."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Please enter a valid positive integer.")


def main():
    print("Safety Metrics Calculator")

    while True:
        number_of_accidents = get_input("Enter the total number of accidents: ")
        total_work_hours = get_input("Enter the total work hours: ")
        lost_work_days = get_input("Enter the total lost work days: ")
        total_workers = get_input("Enter the total number of workers: ")

        calculator = SafetyMetricsCalculator(number_of_accidents, total_work_hours, lost_work_days, total_workers)

        frequency_rate = calculator.calculate_frequency_rate()
        severity_rate = calculator.calculate_severity_rate()
        annual_accident_rate = calculator.calculate_annual_accident_rate()
        comprehensive_disaster_index = calculator.calculate_comprehensive_disaster_index()

        print("\nCalculated Safety Metrics:")
        print(f"Frequency Rate (도수율): {frequency_rate:.2f} per million hours")
        print(f"Severity Rate (강도율): {severity_rate:.2f} per thousand hours")
        print(f"Annual Accident Rate (연천인율): {annual_accident_rate:.2f} per thousand workers")
        print(f"Comprehensive Disaster Index (종합재해지수): {comprehensive_disaster_index:.2f}\n")

        repeat = input("Would you like to calculate again? (yes/no): ").strip().lower()
        if repeat != 'yes':
            break


if __name__ == "__main__":
    main()
