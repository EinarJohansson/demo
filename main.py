from CRUD import *

if __name__ == '__main__':
  # Create a RedisDatabase instance
  db = RedisDatabase()

  # Create a product
  product_id = db.create_product('P001', 10, 100)

  # Create a supplier
  supplier_id = db.create_supplier('ABC Supplies', '123-456-7890')

  # Associate the product with the supplier
  db.add_product_supplier(product_id, supplier_id)

  # Create an order for the product
  order_id = db.create_order(product_id, 5)

  # Read the product, supplier, and order
  product = db.read_product(product_id)
  supplier = db.read_supplier(supplier_id)
  order = db.read_order(order_id)

  print('Product:', product)
  print('Supplier:', supplier)
  print('Order:', order)

  # Update the product and order
  db.update_product(product_id, quantity=20)
  db.update_order(order_id, quantity=10)

  # Read the updated product and order
  product = db.read_product(product_id)
  order = db.read_order(order_id)

  print('Updated Product:', product)
  print('Updated Order:', order)

  # Delete the product and order
  db.delete_product(product_id)
  db.delete_order(order_id)

  # Check if the product and order still exist
  product = db.read_product(product_id)
  order = db.read_order(order_id)

  print('Product after deletion:', product)
  print('Order after deletion:', order)


  
