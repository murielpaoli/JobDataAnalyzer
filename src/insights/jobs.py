import csv
from typing import List, Dict


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path: str) -> List[Dict]:
        with open(path, 'r') as file:
            reader = csv.DictReader(file)
            self.jobs_list = list(reader)
        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        return list(set(job['job_type']
                        for job in self.jobs_list if job['job_type']))

    def filter_by_multiple_criteria(self, jobs: List[Dict],
                                    filter_criteria: Dict) -> List[dict]:
        if not isinstance(filter_criteria, dict):
            raise TypeError("filter_criteria must be a dictionary")
        return [job for job in jobs if all(job[key] == value for key,
                                           value in filter_criteria.items())]
