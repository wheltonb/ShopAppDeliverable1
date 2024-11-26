class ProductService:
    def __init__(self, dao):
        self.dao = dao

    def get_all_products(self):
        return self.dao.getAllProducts()

    def get_product_by_id(self, product_id):
        return self.dao.getProductById(product_id)
