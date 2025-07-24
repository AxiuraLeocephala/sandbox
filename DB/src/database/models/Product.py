from src.database.models.BaseModel import BaseModel

class Product(BaseModel):
    TABLE_NAME = "pricelist"
    NAME_ID_RECORD = "ProductId"
    
    def __init__(self,
                 id: int,
                 CategoryId: int,
                 ProductName: str,
                 ProductPrice: float,
                 ProductDescription: str = "",
                 MaxQuantity: int = 2,
                 Stop: bool = False
                 ) -> None:
        self._id = id
        self.CategoryId = CategoryId
        self.ProductName = ProductName
        self.ProductDescription = ProductDescription 
        self.ProductPrice = ProductPrice
        self.MaxQuantity = MaxQuantity
        self.Stop = Stop

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self):
        raise Exception("You can`t assign an id value")