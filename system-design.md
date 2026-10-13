Women's University Complaint Reporting System

 1. Introduction
The Women's University Complaint Reporting System is designed to help students submit complaints and track their progress online.

 2. Problem Statement
Students may experience difficulties reporting complaints and following up on them. The proposed system will provide a centralized platform for submitting, managing, and tracking complaints.

 3. System Users

 Students
- Register and log in.
- Submit complaints.
- Track complaint status.
- View complaint history.

 Staff Members
- View assigned complaints.
- Investigate complaints.
- Update complaint status.

 Administrators
- Manage user accounts.
- Assign complaints to staff.
- Generate complaint reports.

 4. Main System Screens
- Login Screen
- Registration Screen
- Student Dashboard
- Submit Complaint Screen
- Complaint History Screen
- Staff Dashboard
- Administrator Dashboard

5. Database Design

Users Table
Stores user information, including UserID, FullName, Email, PasswordHash, and Role.

 Complaints Table
Stores complaint information, including ComplaintID, UserID, Category, Description, DateSubmitted, and Status.

Assignments Table
Stores assignment information, including AssignmentID, ComplaintID, StaffID, and DateAssigned.

 ComplaintUpdates Table
Stores complaint progress information, including UpdateID, ComplaintID, UpdatedBy, UpdateDescription, and UpdateDate.

 6. Security Requirements
- Passwords must be stored securely as password hashes.
- Only authorized users should access the system.
- Students should only access complaints they are permitted to view.
- Sensitive complaint information must be protected.

 7. Expected Outcome
The system will make complaint submission, management, and tracking easier for students and university staff.
