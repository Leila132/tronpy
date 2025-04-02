from pydantic import BaseModel


class AddressBase(BaseModel):
    address: str


class Address(AddressBase):
    class Config:
        from_attributes = True
