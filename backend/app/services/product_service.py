from sqlalchemy.orm import Sesion
from typing import List
from ..repositories.category_repository import ProductRepository
from ..schemas.category import ProductCreate, ProductResponse, ProductListResponse
from fastapi import HTTPException, status

class ProductService:
    def __init__(self, db: Session):
        self.repository = ProductRepository(db)
        self.category_repository = CategoryRepository(db)
    
    def get_all_products(self) -> ProductListResponse:
        products = self.repository.get_all()
        product_responses = [ProductResponse.model_validate(product) for product in products]
        return ProductListResponse(
            products=[ProductResponse.model_validate(product) for product in products],
            total=len(products)
        )
    
    def get_product_by_id(self, product_id: int) -> ProductResponse:
        product = self.product_repository.get_by_id(product_id)
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
        return ProductResponse.model_validate(product)
    
    def get_products_by_category(self, category_id: int) -> ProductListResponse:
        category = self.category_repository.get_by_id(category_id)
        if not category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
        products = self.product_repository.get_by_category(category_id)
        return ProductListResponse(
            products=[ProductResponse.model_validate(product) for product in products],
            total=len(products)
        )
    
    def create_product(self, product_data: ProductCreate) -> ProductResponse:
        category = self.category_repository.get_by_id(product_data.category_id)
        if not category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
        product = self.product_repository.create(product_data)
        return ProductResponse.model_validate(product)
    