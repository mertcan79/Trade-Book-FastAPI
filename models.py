from pydantic import BaseModel


class ClientOrder(BaseModel):
    instrument_id: str
    traded_price: float
    quantity: int
    hedge: bool
