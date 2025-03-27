class PersonDataManager:
    def __init__(self):
        self.persons = []

    def collect_person_data(self):
        first_name = input("Ingrese el nombre: ")
        last_name = input("Ingrese el apellido: ")
        dni = input("Ingrese el DNI: ")

        phone_numbers = []
        while True:
            phone_number = input("Ingrese un número de teléfono (o presione Enter para finalizar): ")
            if phone_number == "":
                break
            phone_numbers.append(phone_number)

        person_entry = [
            first_name,
            last_name,
            dni,
            phone_numbers
        ]

        self.persons.append(person_entry)
        return person_entry

    def display_persons(self):
        print("Personas registradas:")
        for index, person in enumerate(self.persons, 1):
            print(f"""
Persona {index}:
- Nombre: {person[0]}
- Apellido: {person[1]}
- DNI: {person[2]}
- Teléfonos: {', '.join(person[3])}
            """)

def main():
    manager = PersonDataManager()
    manager.collect_person_data()
    manager.display_persons()

if __name__ == "__main__":
    main()