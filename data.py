from dataclasses import dataclass


@dataclass
class ProductSale:
    product: str
    quantity: int
    price: float
    revenue: float