def main():
	try:
		studentList = {} #empty dictionary
		fileInput = open("students.txt", "r")
		students = fileInput.readlines()
		fileInput.close()

		for studentInfo in students:
			parts = studentInfo.split(',')
			studentList[parts[0]] = parts[1:]

	except Exception as fileNotFoundError:
		print("File not found")
		return

	while True:
		print("Please make a selection ")
		userChoice = input("1. Search by last name\n2. Search by major\n3. Quit\n ")
		if userChoice == "1":
			lastName = input("Enter the last name: ")
			found = False
			for studentID, parts in studentList.items():
				if parts[0] == lastName:
					print(f"ID: {studentID}, Name: {parts[1]} {parts[0]}, Major: {parts[2]}, GPA: [{parts[3]}] ")
					found = True
			if not found:
				print("Student not found")

		if userChoice == "2":
			major = input("Enter the major: ")
			found = False
			for studentID, parts in studentList.items():
				if parts[2] == major:
					print(f"ID: {studentID}, Name: {parts[1]} {parts[0]}, Major: {parts[2]}, GPA: [{parts[3]}] ")
					found = True
			if not found:
				print("Student not found")

		elif userChoice == "3":
			print("Operation has quit")
			break


main()
