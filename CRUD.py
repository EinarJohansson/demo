import redis

class RedisDatabase:
    def __init__(self):
        self.redis = redis.Redis(host='localhost', port=6379, db=0)

    # CRUD operations for Product table
    def create_product(self, code, quantity, price):
        product_id = self.redis.incr('product_id')
        self.redis.hmset(f'product:{product_id}', {'code': code, 'quantity': quantity, 'price': price})
        return product_id

    def read_product(self, product_id):
        return self.redis.hgetall(f'product:{product_id}')

    def update_product(self, product_id, code=None, quantity=None, price=None):
        if code:
            self.redis.hset(f'product:{product_id}', 'code', code)
        if quantity:
            self.redis.hset(f'product:{product_id}', 'quantity', quantity)
        if price:
            self.redis.hset(f'product:{product_id}', 'price', price)

    def delete_product(self, product_id):
        self.redis.delete(f'product:{product_id}')

    # CRUD operations for Supplier table
    def create_supplier(self, name, phone):
        supplier_id = self.redis.incr('supplier_id')
        self.redis.hmset(f'supplier:{supplier_id}', {'name': name, 'phone': phone})
        return supplier_id

    def read_supplier(self, supplier_id):
        return self.redis.hgetall(f'supplier:{supplier_id}')

    def update_supplier(self, supplier_id, name=None, phone=None):
        if name:
            self.redis.hset(f'supplier:{supplier_id}', 'name', name)
        if phone:
            self.redis.hset(f'supplier:{supplier_id}', 'phone', phone)

    def delete_supplier(self, supplier_id):
        self.redis.delete(f'supplier:{supplier_id}')

    # CRUD operations for ProductSupplier table
    def add_product_supplier(self, product_id, supplier_id):
        self.redis.sadd(f'product:{product_id}:suppliers', supplier_id)
        self.redis.sadd(f'supplier:{supplier_id}:products', product_id)

    def remove_product_supplier(self, product_id, supplier_id):
        self.redis.srem(f'product:{product_id}:suppliers', supplier_id)
        self.redis.srem(f'supplier:{supplier_id}:products', product_id)

    def get_product_suppliers(self, product_id):
        return self.redis.smembers(f'product:{product_id}:suppliers')

    # CRUD operations for Orders table
    def create_order(self, product_id, quantity):
        order_id = self.redis.incr('order_id')
        self.redis.hmset(f'order:{order_id}', {'product_id': product_id, 'quantity': quantity})
        return order_id

    def read_order(self, order_id):
        return self.redis.hgetall(f'order:{order_id}')

    def update_order(self, order_id, product_id=None, quantity=None):
        if product_id:
            self.redis.hset(f'order:{order_id}', 'product_id', product_id)
        if quantity:
            self.redis.hset(f'order:{order_id}', 'quantity', quantity)

    def delete_order(self, order_id):
        self.redis.delete(f'order:{order_id}')
