from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        return max(int(job['max_salary'])
                   for job in self.jobs_list if job['max_salary'].isdigit())

    def get_min_salary(self) -> int:
        return min(int(job['min_salary'])
                   for job in self.jobs_list if job['min_salary'].isdigit())

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        min_salary = job.get("min_salary")
        max_salary = job.get("max_salary")

        if min_salary is None or max_salary is None:
            raise ValueError("Both salaries must be present")

        if not (str(min_salary).isdigit() and str(max_salary).isdigit()):
            raise ValueError("salary values need to be numeric")

        if float(min_salary) > float(max_salary):
            raise ValueError("the minimum salary is greater than the maximum")

        if not (str(salary).isdigit() or isinstance(salary, (int, float))):
            raise ValueError("Salary must be a number")

        return float(min_salary) <= float(salary) <= float(max_salary)

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
