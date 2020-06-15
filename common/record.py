from typing import Optional, Sequence

from enforce_typing import enforce_types
from dataclass_builder import dataclass_builder
from dataclasses import dataclass
from common.pii import Pii


@enforce_types
@dataclass()
class Charge:
    count: Optional[int] = None
    statute: Optional[str] = None
    description: Optional[str] = None
    level: Optional[str] = None
    degree: Optional[str] = None
    disposition: Optional[str] = None
    disposition_date: Optional[str] = None
    offense_date: Optional[str] = None
    citation_number: Optional[str] = None
    plea: Optional[str] = None
    plea_date: Optional[str] = None


ChargeBuilder = dataclass_builder(Charge)


@enforce_types
@dataclass(frozen=True)
class Record:
    id: str
    state: str
    county: str
    case_num: Optional[str] = None
    first_name: Optional[Pii.String] = None
    middle_name: Optional[Pii.String] = None
    last_name: Optional[Pii.String] = None
    suffix: Optional[Pii.String] = None
    dob: Optional[Pii.String] = None
    race: Optional[str] = None
    sex: Optional[str] = None
    arrest_date: Optional[str] = None
    filing_date: Optional[str] = None
    offense_date: Optional[str] = None
    division_name: Optional[str] = None
    case_status: Optional[str] = None
    defense_attorney: Optional[Pii.StringSequence] = None
    public_defender: Optional[Pii.StringSequence] = None
    judge: Optional[Pii.String] = None
    charges: Sequence[Charge] = tuple()
    arresting_officer: Optional[Pii.String] = None
    arresting_officer_badge_number: Optional[Pii.String] = None


RecordBuilder = dataclass_builder(Record)
