# Women's University Complaint Reporting System
# Observer Design Pattern - Multiple Students

class Student:
    def update(self, complaint_id, new_status):
        print(
            f"Notification for {self.name}: "
            f"Complaint {complaint_id} "
            f"status changed to {new_status}."
        )


class Complaint:
    def register_observer(self, student):
        self.observers.append(student)

    def notify_observers(self):
        for student in self.observers:
            student.update(self.complaint_id, self.status)

    def change_status(self, new_status):
        self.status = new_status
        print("\nComplaint status updated to:", new_status)
        self.notify_observers()


# Create three students
student1 = Student()
student1.name = "Nomsa"

student2 = Student()
student2.name = "Rufaro"

student3 = Student()
student3.name = "Lisa"


# Create the first complaint
complaint1 = Complaint()
complaint1.complaint_id = 101
complaint1.description = "Broken classroom equipment"
complaint1.status = "Pending"
complaint1.observers = []

# Register two students for complaint 101
complaint1.register_observer(student1)
complaint1.register_observer(student2)


# Create the second complaint
complaint2 = Complaint()
complaint2.complaint_id = 102
complaint2.description = "Water supply problem"
complaint2.status = "Pending"
complaint2.observers = []

# Register two students for complaint 102
complaint2.register_observer(student2)
complaint2.register_observer(student3)


# Display original statuses
print("Complaint 101 status:", complaint1.status)
print("Complaint 102 status:", complaint2.status)


# Change the status of the first complaint
print("\n--- Updating Complaint 101 ---")
complaint1.change_status("Under Review")


# Change the status of the second complaint
print("\n--- Updating Complaint 102 ---")
complaint2.change_status("Resolved")