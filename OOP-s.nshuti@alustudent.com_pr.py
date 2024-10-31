# Define the Patient class
class Patient:
    def __init__(self, id, name, age, gender, admission_date, condition):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.admission_date = admission_date
        self.condition = condition

    # Method to display patient details
    def get_details(self):
        return (f"ID: {self.id}\n"
                f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Gender: {self.gender}\n"
                f"Admission Date: {self.admission_date}\n"
                f"Condition: {self.condition}\n")

# Function to count total number of patients
def count_patients(patient_list):
    return len(patient_list)

# Function to list all patient names
def list_patient_names(patient_list):
    return [patient.name for patient in patient_list]

#Function to find and display a patient by ID
def print_patient_by_id(patient_list):
    patient_id = int(input("Enter patient ID to search: "))
    for patient in patient_list:
        if patient.id == patient_id:
            print("Patient details found:")
            print(patient.get_details())
            return
    print("Patient not found.")

# Create instances of the Patient class
patient1 = Patient(1, "Paul Muanguzi", 30, "Male", "2024-10-01", "Recovering")
patient2 = Patient(2, "Alain Ngabo", 20, "Male", "2024-10-12", "Critical")
patient3 = Patient(3, "Shalom Silver", 22, "Male", "2024-10-20", "Stable")
patient4 = Patient(4, "Norette Atete", 19, "Female", "2024-10-28", "Under Observation")
patient5 = Patient(5, "Joella Teta", 21, "Female", "2024-11-03", "Recovering")
patient6 = Patient(6, "Gaju Keane", 20, "Female", "2024-11-04", "Stable")

# Store the patients in a list
patient_list = [patient1, patient2, patient3, patient4, patient5, patient6]

# Display total number of patients
print("Total Patients:", count_patients(patient_list))

# Display list of all patient names
print("Patient Names:", list_patient_names(patient_list))

#Search and print a patient by ID
print_patient_by_id(patient_list)
