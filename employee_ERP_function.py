# employee program using function
emp={}

def add_employee():
	print(".......................Adding employee........................")
	emp_id = input("\tEnter the employee id")
	if emp_id not in emp.keys():
		name = input("\tEnter the name")
		age = int(input("\tEnter the age"))
		gender = input("\tEnter the gender")
		place = input("\tEnter the place")
		salary = int(input("\tEnter the salary"))
		prv_company = input("\tEnter your previous company")
		joining_date = int(input("\tEnter your joining date as (DD/MM/YYYY)"))
		temp = {
		"name":name,
		"age":age,
		"gender":gender,
		"place":place,
		"salary":salary,
		"previous_company":prv_company,
		"joining_date":joining_date
		}
		emp[emp_id] = temp
		print(emp)
	else:
		print("employee id is already taken")

def delete_employee():
	emp_id = int(input("\tEnter the employee id"))
	if emp_id not in emp.keys():
		print("\t Wrong employee id")
	else:
		del emp[emp_id]
		print(emp)

def search_employee():
	name = input("\tEnter the name")
	flag = False
	for i in emp.values():
		if i["name"] == name:
			print(f"\t{i['name']} | {i['age']} | {i['gender']}")
			flag = True
			break
		if flag == False:
			print("\tNot found")

def change_employee_details():
	change_employee_menu()
	ch1 = int(input("\t\tEnter the choice:"))
	if ch1 == 1:
		emp_id = input("\tEnter the employee id to be change:")
		print(emp_id)
		if emp_id not in emp.keys():
			print("\tWrong employee id")
		else:
			new_name = input("\tEnter the new name:")
			emp[emp_id]['name'] = new_name
			print(emp)
	elif ch1 == 2:
		emp_id = input("\tEnter the employee id to be change:")
		if emp_id not in emp.keys():
			print("\tWrong employee id")
		else:
			new_age = int(input("\tEnter the new age:"))
			emp[emp_id]['age'] = new_age
			print(emp)
	elif ch1 == 3:
		emp_id = input("\tEnter the employee id:")
		if emp_id not in emp.keys():
			print("\tWrong employee id")
		else:
			new_gender = input("\tEnter the new gender:")
			emp[emp_id]['gender'] = new_gender
			print(emp)
	elif ch1 == 4:
		emp_id = input("\tEnter the employee id to be change:")
		if emp_id not in emp.keys():
			print("\tWrong employee id")
		else:
			new_salary=int(input("\tEnter the new salary:"))
			emp[emp_id]['salary'] = new_salary
			print(emp)
def display_employee():
	for empid,employee in emp.items():
		print(f'{empid} | {employee["name"]} |{employee["age"]} |{employee["gender"]} | {employee["place"]}')
		print(emp)		

def change_employee_menu():
	print("\t1.Change employee by name:")
	print("\t2.Change employee by age:")
	print("\t3.Change employee by gender:")
	print("\t4.Change employee by salary:")



def main_menu():
	print("1.Add Employee")
	print("2.Delete Employee")
	print("3.Search Employee by name")
	print("4.Change Employee details")
	print("5.Display Details")

while True:
	main_menu()
	choice = int(input("\tEnter your choice"))
	if choice == 1:
		add_employee()
	
	elif choice == 2:
		delete_employee()
	elif choice == 3:
		search_employee()
	elif choice == 4:
		#change  employee  details
		change_employee_details()
		


	elif choice == 5:
		display_employee()
	elif choice == 6:
		break
	else:
		print("\tInvalid choice")
