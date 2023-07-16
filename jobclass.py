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
        """
        Returns a string representation of the object.
        
        Parameters:
            None

        Returns:
            str: A formatted string containing the title, salary, type, city,
                 description, responded, and response attributes of the object.
        """
        return f"Title: {self.title}\nSalary: {self.salary} \ntype: {self.type}\nCity: {self.city}\nDescription: {self.description}\nResponded: {self.responded}\nResponse: {self.response}"
    
    def to_dict(self):
        """
        Converts the object to a dictionary representation.

        :return: The dictionary representation of the object.
        :rtype: dict
        """
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data):
        """
        A class method that creates an instance of the class from a dictionary.

        Parameters:
            cls (type): The class itself.
            data (dict): A dictionary containing the data to initialize the instance.

        Returns:
            The instance of the class created from the dictionary.
        """
        return cls(**data)