import json

def display_menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v1.0")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")
    print("********************************")

def print_authorized_vehicles(allowed_vehicles_list):
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in allowed_vehicles_list:
        print(vehicle)
    print()

def search_vehicle(allowed_vehicles_list, vehicle_name):
    if vehicle_name in allowed_vehicles_list:
        print(f"\n{vehicle_name} is an authorized vehicle\n")
    else:
        print(f"\n{vehicle_name} is not an authorized vehicle. If you received this in error, please check the spelling and try again.\n")

def add_authorized_vehicle(allowed_vehicles_list, vehicle_name):
    if vehicle_name not in allowed_vehicles_list:
        allowed_vehicles_list.append(vehicle_name)
        print(f'\nYou have added "{vehicle_name}" as an authorized vehicle\n')
        save_vehicles('authorized_vehicles.json', allowed_vehicles_list)
    else:
        print(f'\n"{vehicle_name}" is already an authorized vehicle\n')

def delete_authorized_vehicle(allowed_vehicles_list, vehicle_name):
    if vehicle_name in allowed_vehicles_list:
        confirmation = input(f'\nAre you sure you want to remove "{vehicle_name}" from the Authorized Vehicles List? ').strip().lower()
        if confirmation == 'yes':
            allowed_vehicles_list.remove(vehicle_name)
            print(f'\nYou have REMOVED "{vehicle_name}" as an authorized vehicle\n')
            save_vehicles('authorized_vehicles.json', allowed_vehicles_list)
    else:
        print(f'\n"{vehicle_name}" is not in the Authorized Vehicles List\n')

def load_vehicles(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Rivian R1T', 'Ram 1500']

def save_vehicles(file_path, allowed_vehicles_list):
    with open(file_path, 'w') as file:
        json.dump(allowed_vehicles_list, file)

def main():
    file_path = 'authorized_vehicles.json'
    allowed_vehicles_list = load_vehicles(file_path)
    
    while True:
        display_menu()
        user_input = input().strip()

        if user_input == '1':
            print_authorized_vehicles(allowed_vehicles_list)
        elif user_input == '2':
            vehicle_name = input("Please enter the full Vehicle name: ").strip()
            search_vehicle(allowed_vehicles_list, vehicle_name)
        elif user_input == '3':
            vehicle_name = input("Please enter the full Vehicle name you would like to add: ").strip()
            add_authorized_vehicle(allowed_vehicles_list, vehicle_name)
        elif user_input == '4':
            vehicle_name = input("Please enter the full Vehicle name you would like to REMOVE: ").strip()
            delete_authorized_vehicle(allowed_vehicles_list, vehicle_name)
        elif user_input == '5':
            save_vehicles(file_path, allowed_vehicles_list)
            print("Thank you for using the AutoCountry Vehicle Finder. Goodbye!")
            break
        else:
            print("Invalid input, please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
