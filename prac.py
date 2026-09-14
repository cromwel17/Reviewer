#Scenario: A school has equipment that students can borrow. An Equipment has a name, equipment_id, and is_rented flag. A Student can rent(equipment) and return_equipment(equipment).
#A student cannot rent equipment that is already rented. Attempting to do so should raise a custom EquipmentUnavailableError that includes the equipment's name in its message.
#Task:

#Implement:

#Equipment
#Student
#Custom EquipmentUnavailableError
#Equipment.__str__()

#The __str__ method should show the equipment name and whether it is available or rented.


class EquipmentUnavcvailableError(Exception):

    pass


class Equipment:
  def __init__(self, name, equipment_id, is_rented=False):
    self.name = name
    self.equipment_id = equipment_id
    self.is_rented = is_rented

  def __str__(self):
     status = "Rented" if self.is_rented else "Available"
     return f"Equipment ID: {self.equipment_id}, Name: {self.name}, Status: {status}"
  

class Student:
   def __init__(self, name, student_id):
      self.name = name
   
   def rent (self, equipment):
      if equipment.is_rented:
         raise EquipmentUnavcvailableError(f"{equipment.name} is currently unavailable for rent.")
      else:
         equipment.is_rented = True

         print(f"{self.name} has rented {equipment.name}.")

   def return_equipment(self, equipment):
       equipment.is_rented = False
       print(f"{self.name} has returned {equipment.name}.")


laptop = Equipment("Laptop", 1)
student = Student("Francis", 10)

print(laptop)  # Output: Equipment ID: 1, Name: Laptop, Status: Available

student.rent(laptop)  # Output: Francis has rented Laptop.
print(laptop)  # Output: Equipment ID: 1, Name: Laptop, Status

try:
   student.rent(laptop)
except EquipmentUnavcvailableError as error:
   print("Rental failed", error)

student.return_equipment(laptop)  # Output: Francis has returned Laptop.
print(laptop)  # Output: Equipment ID: 1, Name: Laptop, Status






