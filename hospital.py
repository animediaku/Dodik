class Patient:
    def __init__(self, first_name, middle_name, last_name, address, city, state, postal_code, contact_number, emergency_contact_name, emergency_contact_number):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.contact_number = contact_number
        self.emergency_contact_name = emergency_contact_name
        self.emergency_contact_number = emergency_contact_number

    def get_full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    def get_address(self):
        return f"{self.address}, {self.city}, {self.state}, {self.postal_code}"

    def get_contact_info(self):
        return self.contact_number

    def get_emergency_contact_info(self):
        return f"{self.emergency_contact_name} - {self.emergency_contact_number}"

    def set_address(self, new_address, new_city, new_state, new_postal_code):
        self.address = new_address
        self.city = new_city
        self.state = new_state
        self.postal_code = new_postal_code

    def set_contact_info(self, new_contact_number):
        self.contact_number = new_contact_number

    def set_emergency_contact_info(self, new_emergency_contact_name, new_emergency_contact_number):
        self.emergency_contact_name = new_emergency_contact_name
        self.emergency_contact_number = new_emergency_contact_number

class Procedure:
    def __init__(self, name, date, practitioner, charges):
        self.name = name
        self.date = date
        self.practitioner = practitioner
        self.charges = charges

    def get_procedure_details(self):
        return f"Procedure: {self.name}\nDate: {self.date}\nPractitioner: {self.practitioner}\nCharges: ${self.charges:.2f}"

def save_patient_to_file(patient, filename):
    try:
        with open(filename, 'w') as f:
            f.write(f"{patient.first_name}\n")
            f.write(f"{patient.middle_name}\n")
            f.write(f"{patient.last_name}\n")
            f.write(f"{patient.address}\n")
            f.write(f"{patient.city}\n")
            f.write(f"{patient.state}\n")
            f.write(f"{patient.postal_code}\n")
            f.write(f"{patient.contact_number}\n")
            f.write(f"{patient.emergency_contact_name}\n")
            f.write(f"{patient.emergency_contact_number}\n")
        print(f"Patient data saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving patient data: {e}")

def load_patient_from_file(filename):
    try:
        with open(filename, 'r') as f:
            first_name = f.readline().strip()
            middle_name = f.readline().strip()
            last_name = f.readline().strip()
            address = f.readline().strip()
            city = f.readline().strip()
            state = f.readline().strip()
            postal_code = f.readline().strip()
            contact_number = f.readline().strip()
            emergency_contact_name = f.readline().strip()
            emergency_contact_number = f.readline().strip()
        return Patient(first_name, middle_name, last_name, address, city, state, postal_code, contact_number, emergency_contact_name, emergency_contact_number)
    except Exception as e:
        print(f"An error occurred while loading patient data: {e}")
        return None

def save_procedure_to_file(procedure, filename):
    try:
        with open(filename, 'w') as f:
            f.write(f"{procedure.name}\n")
            f.write(f"{procedure.date}\n")
            f.write(f"{procedure.practitioner}\n")
            f.write(f"{procedure.charges}\n")
        print(f"Procedure data saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving procedure data: {e}")

def load_procedure_from_file(filename):
    try:
        with open(filename, 'r') as f:
            name = f.readline().strip()
            date = f.readline().strip()
            practitioner = f.readline().strip()
            charges = float(f.readline().strip())
        return Procedure(name, date, practitioner, charges)
    except Exception as e:
        print(f"An error occurred while loading procedure data: {e}")
        return None

# --- Main program ---
if __name__ == "__main__":
    # Get patient details from user input
    first_name = input("Enter patient's first name: ")
    middle_name = input("Enter patient's middle name: ")
    last_name = input("Enter patient's last name: ")
    address = input("Enter patient's address: ")
    city = input("Enter patient's city: ")
    state = input("Enter patient's state: ")
    postal_code = input("Enter patient's postal code: ")
    contact_number = input("Enter patient's contact number: ")
    emergency_contact_name = input("Enter patient's emergency contact name: ")
    emergency_contact_number = input("Enter patient's emergency contact number: ")

    patient = Patient(first_name, middle_name, last_name, address, city, state, postal_code, contact_number, emergency_contact_name, emergency_contact_number)

    # Save patient data to file
    save_patient_to_file(patient, 'patient_data.txt')

    # Load patient data from file
    loaded_patient = load_patient_from_file('patient_data.txt')
    if loaded_patient:
        print("\nLoaded Patient Details:")
        print(f"Name: {loaded_patient.get_full_name()}")
        print(f"Address: {loaded_patient.get_address()}")
        print(f"Contact: {loaded_patient.get_contact_info()}")
        print(f"Emergency Contact: {loaded_patient.get_emergency_contact_info()}")

    # Get procedure details from user input
    num_procedures = int(input("\nHow many procedures were performed? "))
    procedures = []
    for i in range(num_procedures):
        print(f"\nProcedure {i+1}:")
        name = input("Enter procedure name: ")
        date = input("Enter procedure date (YYYY-MM-DD): ")
        practitioner = input("Enter practitioner name: ")
        charges = float(input("Enter procedure charges: "))
        procedure = Procedure(name, date, practitioner, charges)
        procedures.append(procedure)

        # Save procedure data to file
        save_procedure_to_file(procedure, f'procedure_{i+1}_data.txt')

    # Load procedure data from files
    loaded_procedures = []
    for i in range(num_procedures):
        loaded_procedure = load_procedure_from_file(f'procedure_{i+1}_data.txt')
        if loaded_procedure:
            loaded_procedures.append(loaded_procedure)

    # Display procedure details and calculate total charges
    if loaded_procedures:
        print("\nLoaded Procedure Details:")
        total_charges = 0
        for procedure in loaded_procedures:
            print(procedure.get_procedure_details())
            print("---")
            total_charges += procedure.charges
        print(f"Total Charges: ${total_charges:.2f}")