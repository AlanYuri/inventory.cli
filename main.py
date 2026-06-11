inventory = []

def show_menu():
  print("\n" + "="*30)
  print(" CLI Inventory System ")
  print("="*30)
  print("1 - Register new equipment")
  print("2 - List equipments")
  print("3 - Logoff")
  print("="*30)

def register_equipment():
  print("\n--- Register Equipment ---")
  name = input("Name of device: ")
  ip = input("IP Adress: ")
  status = input("Status (Active/Unactive): ")

  new_id = len(inventory) + 1

  equipment = {
    "id": new_id,
    "name": name,
    "ip": ip,
    "status": status
  }

  inventory.append(equipment)

  print(f"\n[Success] '{name} succesfully registered!")

def listing_equipments():
  print("\n--- Registered equipments ---")

  if not inventory:
    print("No equipment registered yet.")
    return
  
  for eq in inventory:
    print(f"Id: {eq['id']} | Name: {eq['name']} | Ip: {eq['ip']} | Status: {eq['status']}")

while True:
  show_menu()
  option = input("Choose an option: ")

  if option == "1":
    register_equipment()
  
  elif option == "2":
    listing_equipments()
  
  elif option == "3":
    print("\nLogging off... See ya soon!")
    break

  else:
    print("\n[Error] Invalid option! Type 1, 2 or 3.")
