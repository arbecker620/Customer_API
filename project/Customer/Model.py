from pydantic import BaseModel
import uuid
from typing import Optional

class Customer(BaseModel):
    name: str
    address: Optional[str]
    Date_of_Birth: Optional[str]

