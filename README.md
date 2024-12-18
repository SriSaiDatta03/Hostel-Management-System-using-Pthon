Hostel Management System 📚🏨
-
---

Overview:
-
The Hostel Management System is a Python-based application designed to efficiently allocate hostel rooms to students based on their CGPA (Cumulative Grade Point Average). This system prioritizes students with higher CGPAs for AC rooms and allocates them to the next available room type if their preferred choice is filled. If all rooms are occupied, students will be listed as unallocated.

---
Features ✨
-

Room Allocation Based on CGPA: Students with higher CGPAs are given preference for room allocation.
Dynamic Room Management: The system handles multiple room types, including AC and non-AC options.
Unallocated Students List: Easily identifies students who could not be allocated a room due to full capacity.
File Input Support: Reads student data from a specified file, making it easy to manage large datasets.

---
Getting Started 🚀
Prerequisites:
Python 3.x installed on your machine.
Basic knowledge of running Python scripts.

Installation 🧑‍💻
Clone this repository or download the script files.
Ensure you have a file containing student data in the specified format (see Data Format).
Update the file path in the script to point to your student data file.
Data Format 📄
The student data file should contain information in the following format:
text
student_roll.no: <Roll Number>
student_name: <Student Name>
CGPA: <Student CGPA>
Each student's information should be separated by a newline, and there should be no empty lines between entries.
Running the Application
Open your terminal or command prompt.
Navigate to the directory containing the script.
Run the script using the command:
```bash
python hostel_management_system.py
```
Enter the availability of each room type when prompted.

---
Code Structure 🛠️
-

Classes
Student: Represents a student with attributes such as roll number, name, and CGPA.
Hostel: Manages room allocation and keeps track of allocated and unallocated students.
Functions
allocate_rooms(students, room_availability): Allocates rooms based on student CGPAs and available rooms.
main(): The entry point of the application that handles user input and processes student data.
Example Output 🖥️
Upon successful execution, the program will display:
text
Allocated Rooms:
Roll No: 101, Student: Alice, CGPA: 9.5, Room: 1-bed room AC
Roll No: 102, Student: Bob, CGPA: 9.2, Room: 2-bed room AC

Rooms are full. The following students could not be allocated a room:
Rooms are full. Student 103 (Charlie) could not be allocated a room.

---
Contribution 🤝
-
Feel free to contribute by submitting issues or pull requests. Your feedback and suggestions are always welcome!
                                                             Happy coding! 😊
