from models.Product import Product

class productDAO:
    def __init__(self):
        self.products = [Product(productID=1, productName="Next Gen Phaser", price="80", type="replica", gender=None,
                                 movable=None, isMirror=None, character=None, hasColour=None, dimensions=None, material="aluminum",
                                 scale="1/1", isLimited=True, description="Replica of the phaser blaster used on the set of Star Trek the Next Generation", image_url="static/images/NextGenPhaser.jpg"),

                         Product(productID=1, productName="Original Series Sulu Model", price="30", type="Figurine", gender=None,
                                 movable=None, isMirror=None, character=None, hasColour=None, dimensions=None,
                                 material=None, scale=None, isLimited=None,
                                 description="1/6 scale figurine of Lt.Sulu from Star Trek the original series", image_url="static/images/OriginalSeriesSuluFigurine.jpg")]



    def getAllProducts(self):
        return self.products

    def getProductById(self, productID):
        for product in self.products:
            if product.productID == productID:
                return product
        return None  # If no product is found

