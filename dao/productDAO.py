from models.Product import Product

class productDAO:
    # hard-coded products (1 of each type with 3 distinct attributes each)
    # each product is only initialized with attributes for its own product type, all others = None
    def __init__(self):
        self.products = [Product(productID=1, productName="Next Gen Phaser",
                                 price="80",
                                 type="replica",
                                 gender=None,
                                 movable=None,
                                 isMirror=None,
                                 character=None,
                                 hasColour=None,
                                 dimensions=None,
                                 material="aluminum",
                                 scale="1/1",
                                 isLimited=True,
                                 description="Replica of the phaser blaster used on the set of Star Trek the Next Generation",
                                 image_url="/static/images/NextGenPhaser.jpg"),

                         Product(productID=2,
                                 productName="Original Series Sulu Model",
                                 price="30",
                                 type="Figurine",
                                 gender="Male",
                                 movable="No moving pieces",
                                 isMirror="not from Mirror-verse",
                                 character=None,
                                 hasColour=None,
                                 dimensions=None,
                                 material=None,
                                 scale=None,
                                 isLimited=None,
                                 description="1/6 scale figurine of Lt.Sulu from Star Trek the original series",
                                 image_url="/static/images/OriginalSeriesSuluFigurine.jpg"),
                         Product(productID=3,
                                 productName="Live Long and Prosper tv series Spock Poster",
                                 price="20",
                                 type="Poster",
                                 gender=None,
                                 movable=None,
                                 isMirror=None,
                                 character="Spock",
                                 hasColour=True,
                                 dimensions='18x24-inch',
                                 material=None,
                                 scale=None,
                                 isLimited=None,
                                 description="18x24-inch Poster of widely beloved StarTrek character Spock ",
                                 image_url="/static/images/Spock_Poster.png")]


# returns all products
    def getAllProducts(self):
        return self.products

# loops through products and returns product that matches the ID arg
    def getProductById(self, productID):
        for product in self.products:
            if product.productID == productID:
                return product
        return None  # If no product is found

