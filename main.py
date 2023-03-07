from CRUD import *
import sys
if __name__ == '__main__':
  # Create a RedisDatabase instance
  db = RedisDatabase()

  print("\nCreate a product!")

  product_name = input("Enter the productname: ")
  product_code = input("Enter the product code: ")
  product_quantity = input("Enter the quantity of the product: ")
  product_price = input("Enter the price of the product (SEK): ")

  # Create a product
  db.create_product(product_name, product_code, product_quantity, product_price)

  print("\nCreate a supplier!")
  supplier_name = input("Enter the suppliername: ")
  supplier_phone = input("Enter the phonenumber for the supplier: ")

  # Create a supplier
  db.create_supplier(supplier_name, supplier_phone)

  print("\nCreate a product supplier!")
  
  print("Here is all the products!")
  for (product, key) in db.show_all_products():
    print('Product ID:')
    print(key)
    print('Value:')
    print(product)
    print()
  
  chosen_product_id = input("Choose a product_id that the supplier should stock: ")

  print("\nHere are all the suppliers!")
  for (supplier, key) in db.show_all_suppliers():
    print('Supplier ID:')
    print(key)
    print('Value:')
    print(supplier)
    print()

  chosen_supplier_id = input("Choose what supplier that should stock the product: ")

  # Associate the product with the supplier
  db.create_product_supplier(chosen_product_id, chosen_supplier_id)

  print('\nCreate an order!')
  for (product, key) in db.show_all_products():
    print('Product ID:')
    print(key)
    print('Value:')
    print(product)
    print()

  order_product_id = input("Which product do you want to order?: ")

  for (supplier, key) in db.show_all_product_suppliers(order_product_id):
    print('Supplier ID:')
    print(key)
    print('Value:')
    print(supplier)
    print()

  order_supplier_id = input("Which supplier do you want to order from?: ")

  # Create an order for the product
  quantity = input("How much of the product do you want to order?: ")
  order_id = db.create_order(order_product_id, quantity)

  print('\nDin beställning är klar!')

  # Read the updated product and order
  product = db.read_product(order_product_id)
  order = db.read_order(order_id)

  print('Uppdaterade produkten:', product)
  print('Din order:', order)

  # Delete the product and order
  db.delete_product(chosen_product_id)
  db.delete_order(order_id)
  db.delete_product_supplier(chosen_product_id, chosen_supplier_id)
  db.delete_supplier(chosen_supplier_id)

  # Check if the product and order still exist
  product = db.read_product(chosen_product_id)
  order = db.read_order(order_id)
  supplier = db.read_supplier(chosen_supplier_id)
  product_supplier = db.read_product_suppliers(chosen_supplier_id)

  print('Product after deletion:', product)
  print('Order after deletion:', order)
  print('Supplier after deletion:', supplier)
  print('Product supplier after deletion:', product_supplier)


