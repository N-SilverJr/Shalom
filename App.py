#!/usr/bin/python3

# Function to display available treatment services
def list_services():
    services = {
        1: "General Consultation",
        2: "Pediatric Care",
        3: "Dental Services",
        4: "Cardiology",
        5: "Dermatology",
        6: "Psychiatry",
    }
    print("\nAvailable Treatment Services:")
    for key, value in services.items():
        print(f"{key}. {value}")
    return services


# Function to book an appointment
def book_appointment(services):
    try:
        service_id = int(input("\nEnter the service number to book an appointment: "))
        if service_id in services:
            name = input("Enter your name: ")
            date = input("Enter the date for your appointment (YYYY-MM-DD): ")
            print(f"\nAppointment booked for {name} on {date} for {services[service_id]}.")
        else:
            print("\nInvalid service selection. Please try again.")
    except ValueError:
        print("\nInvalid input. Please enter a valid number.")


# Main function to display the menu
def main_menu():
    while True:
        print("\n--- Accessing Healthcare Services Program ---")
        print("1. List Available Treatment Services")
        print("2. Book an Appointment")
        print("3. Exit")

        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                services = list_services()
            elif choice == 2:
                if 'services' in locals():
                    book_appointment(services)
                else:
                    print("\nPlease list the services first.")
            elif choice == 3:
                print("\nThank you for using the program. Goodbye!")
                break
            else:
                print("\nInvalid option. Please choose a valid number.")
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")


if __name__ == "__main__":
    main_menu()
