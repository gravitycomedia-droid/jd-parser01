from typing import Any, Self

from pydantic import BaseModel, Field, field_validator, model_validator

class JobPosting(BaseModel):
    title : str = Field(Example=['Full Stack Developer'])
    company:str
    location: str
    skills: list[str] = Field(min_length =1)
    experience_years: int | None = Field(ge=0,le=40)
    remote:bool
    salary_min_lpa: float | None = None
    salary_max_lpa: float | None = None

    @field_validator("skills", mode="before")
    @classmethod
    def clean_skills(cls, v: Any) -> list[str]:
        if not isinstance(v, list):
            return v
        
        return list(dict.fromkeys(
            item.strip().lower()
            for item in v
            if isinstance(item, str) and item.strip()
        ))

    @model_validator(mode="after")
    def validate_salary_range(self) -> Self:
        if (
            self.salary_min_lpa is not None
            and self.salary_max_lpa is not None
            and self.salary_min_lpa > self.salary_max_lpa
        ):
            raise ValueError("salary_min_lpa cannot be greater than salary_max_lpa")
        return self