# employee program using list
employee=[]
while True:
	print("1.Add Employee")
	print("2.Delete Employee")
	print("3.Search Employee")
	print("4.Display all Employee")
	print("5.Change the employee name in the list")
	print("6.exit")
	ch=int(input("Enter your choice"))
	if ch==1:
		#Add Employee
		print(".................Adding employee................")
		name=input("Enter the name")
		if name:
			employee.append(name)
			print(employee)
	elif ch==2:
		#Delete Employee
		print("..................Deleting employee....................")
		print(employee)
		name=input("Enter the name to be deleted from the list")
		employee.remove(name)
		print(employee)
	elif ch==3:
		#Search Employee
		print("............................Search employee................")
		print(employee)
		name=input("Enter the element you want to search")
		if name in employee:
			print(name + "is in the list")
		else:
			print(name + "is not in the list")
	elif ch==4:
		#Display Employee
		print(".....................Display employee..................")
		print(employee)
		for i in range(0,len(employee)):
			print(i+1,".",employee[i])
	elif ch==5:
		#Change Employee Data
		print("........................change employee..................")
		name=input("enter the name")
		index=employee.index(name)
		new_name=input("enter the new name")
		employee[index]=new_name
		print(employee)
	elif ch==6:
		break

	else:
		print("invaid choice")
