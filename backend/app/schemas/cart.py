from pydantic import baseModel, Field
from typing import Optional

class CartItemBase(BaseModel):
    product_id: int = Field(..., description="ID of the product")
    quantity: int = Field(..., gt=0, description="Quantity of the product in the cart")

class CartItemCreate(CartItemBase):
    pass

class CartItemUpdate(BaseModel):
    product_id: Optional[int] = Field(None, description="ID of the product")
    quantity: Optional[int] = Field(None, gt=0, description="Quantity of the product in the cart")

class CartItem(CartItemBase):
    product_id: int
    name: str = Field(..., description="Name of the product")
    price: float = Field(..., gt=0, description="Price of the product")
    quantity: int = Field(..., gt=0, description="Quantity of the product in the cart")
    subtotal: float = Field(..., gt=0, description="Total price for this item (price * quantity)")
    image_url: Optional[str] = Field(None, description="URL of the product image")

class CartResponse(BaseModel):
    items: list[CartItem] = Field(..., description="List of items in the cart")
    total: float = Field(..., description="Total price")
    items_count: float = Field(..., gt=0, description="Total number of items in the cart")
    