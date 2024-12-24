from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id: Optional[int]
    name: str
    description: Optional[str]
    price: float
    category_id: int
