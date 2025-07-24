from src.database.MySQL import MySQL
from src.database.models.Product import Product

if __name__ == "__main__":
    mysql = MySQL()
    mysql.create_pool_connection()
    product1 = Product(id=1, CategoryId=1, ProductName="product_1", ProductPrice=120.0)
    product1.save()
    product1.change(ProductName="product_1.1")
    mysql.create_pool_connection()