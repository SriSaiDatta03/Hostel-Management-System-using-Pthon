import heapq

class Student:
    def __init__(self, roll_no, name, cgpa):
        self.roll_no = roll_no
        self.name = name
        self.cgpa = float(cgpa)

    def __lt__(self, other):
        return self.cgpa > other.cgpa

class Hostel:
    def __init__(self, room_availability):
        self.rooms = {
            '3-bed room AC': room_availability['3-bed room AC'] * 3,
            '2-bed room AC': room_availability['2-bed room AC'] * 2,
            '1-bed room AC': room_availability['1-bed room AC'],
            '3-bed room non-AC': room_availability['3-bed room non-AC'] * 3,
            '2-bed room non-AC': room_availability['2-bed room non-AC'] * 2,
            '1-bed room non-AC': room_availability['1-bed room non-AC']
        }
        self.room_priority = [
            '3-bed room AC',
            '2-bed room AC',
            '1-bed room AC',
            '3-bed room non-AC',
            '2-bed room non-AC',
            '1-bed room non-AC'
        ]
        self.allocated_rooms = []
        self.unallocated_students = []

    def allocate_room(self, student):
        for room_type in self.room_priority:
            if self.rooms[room_type] > 0:
                self.rooms[room_type] -= 1
                self.allocated_rooms.append((student.roll_no, student.name, student.cgpa, room_type))
                return
        self.unallocated_students.append((student.roll_no, student.name))

    def print_allocations(self):
        print("\nAllocated Rooms:")
        for roll_no, name, cgpa, room in self.allocated_rooms:
            print(f"Roll No: {roll_no}, Student: {name}, CGPA: {cgpa}, Room: {room}")

        print("\nRooms are full. The following students could not be allocated a room:")
        for roll_no, name in self.unallocated_students:
            print(f"Rooms are full. Student {roll_no} ({name}) could not be allocated a room.")

def allocate_rooms(students, room_availability):
    hostel = Hostel(room_availability)
    sorted_students = sorted(students, key=lambda x: x.cgpa, reverse=True)

    for student in sorted_students:
        hostel.allocate_room(student)

    hostel.print_allocations()

def main():
    Hostel_rooms = {
        '3-bed room AC': 0,
        '2-bed room AC': 0,
        '1-bed room AC': 0,
        '3-bed room non-AC': 0,
        '2-bed room non-AC': 0,
        '1-bed room non-AC': 0
    }

    for key in Hostel_rooms:
        value = int(input(f"Enter the value for '{key}': "))
        Hostel_rooms[key] = value

    students_heap = [Student(roll_no, student['student_name'], student['CGPA']) for roll_no, student in students_dict.items()]
    heapq.heapify(students_heap)

    hostel = Hostel(Hostel_rooms)

    while students_heap:
        student = heapq.heappop(students_heap)
        hostel.allocate_room(student)

    hostel.print_allocations()

if __name__ == '__main__':
    with open(r'C:\Users\Bh.Sri Sai Datta\OneDrive\Desktop\students.pdf', 'r') as file: #Change the file path
        students_dict = {}
        student = {}
        for line in file:
            line = line.strip()
            if line:
                key, value = line.split(': ')
                if key == "student_roll.no":
                    roll_no = value
                    student = {'student_name': '', 'CGPA': ''}
                else:
                    student[key.replace(' ', '_')] = value
                    if key == "CGPA":
                        students_dict[roll_no] = student
                        student = {}
        if student:
            students_dict[roll_no] = student

    main()
