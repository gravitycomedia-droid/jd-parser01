from pydantic import ValidationError

from models import JobPosting

test_cases = [
	{
		"title": "Senior Python Developer",
		"company": "Example Tech",
		"location": "Remote",
		"skills": ["Python ", "python", "SQL"],
		"experience_years": 5,
		"remote": True,
		"salary_min_lpa": 12,
		"salary_max_lpa": 18,
	},
	{
		"company": "Example Tech",
		"location": "Bengaluru",
		"skills": ["Python", "SQL"],
		"experience_years": 3,
		"remote": False,
		"salary_min_lpa": 8,
		"salary_max_lpa": 12,
	},
	{
		"title": "Data Analyst",
		"company": "Example Analytics",
		"location": "Hyderabad",
		"skills": ["SQL", "Python"],
		"experience_years": 4,
		"remote": False,
		"salary_min_lpa": 12,
		"salary_max_lpa": 6,
	},
]

for case_number, jd_data in enumerate(test_cases, start=1):
	print(f"Test case {case_number}:")
	try:
		job_posting = JobPosting(**jd_data)
		print(job_posting.model_dump_json(indent=2))
	except ValidationError as error:
		print(error)
	print()

print(JobPosting.model_json_schema())
