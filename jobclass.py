from dataclasses import dataclass, asdict

@dataclass
class JobListing:
    title: str
    salary: str
    type: str
    city: str
    publicationdate: str
    description: str
    responded: bool
    response: str
    
    def __str__(self):
        return f"Title: {self.title}\nSalary: {self.salary} \ntype: {self.type}\nCity: {self.city}\nDescription: {self.description}\nResponded: {self.responded}\nResponse: {self.response}"
    
    def to_dict(self):
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data):
        return cls(**data)