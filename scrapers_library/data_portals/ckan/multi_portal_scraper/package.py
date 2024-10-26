from dataclasses import dataclass

@dataclass
class Package:
    url: str = ""
    title: str = ""
    agency_name: str = ""
    description: str = ""