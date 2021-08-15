#Employee ERP using dictionary
emp={}
while True:
	print("....................Menu................")
	print("1.Add Employee")
	print("2.Delete Employee")
	print("3.Search Employee by name")
	print("4.Change Employee Details")
	print("5.Display Details")
	choice = int(input("\tEnter the choice"))
	if choice == 1:
		print(".....................Adding employee.................")
		emp_id = input("\tEnter the employee id")
		if emp_id not in emp.keys():
			name = input("\tEnter the name")
			age = int(input("\tEnter the age"))
			gender = input("\tEnter the gender")
			place = input("\tEnter the place")
			salary = int(input("\tEnter the salary"))
			prv_company = input("\tEnter your previous company")
			joining_date = int(input("\tEnter your joining date as (DD/MM/YYYY)")
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
	elif choice == 2:
		print(".....................Delete employee.................")
		emp_id = int(input("\tEnter the employee id"))
		if emp_id not in emp.keys():
			print("\t Wrong employee id")
		else:
			del emp[emp_id]
			print(emp)
	elif choice == 3:
		print("....................................Search employee.........................")
		name = input("\tEnter the name")
		flag = False
		for i in emp.values():
			if i["name"] == name:
				print(f"\t{i['name']} | {i['age']} | {i['gender']}")
				flag = True
				break
		if flag == False:
			print("\tNot found")
	elif choice == 4:
		print(".................................change employee details......................")
		#change  employee  details
		print("\t1.Change employee by name:")
		print("\t2.Change employee by age:")
		print("\t3.Change employee by gender:")
		print("\t4.Change employee by salary:")
		ch1 = int(input("\t\tEnter the choice:"))
		if ch1 == 1:
			print(".............................change employee name..................")
			emp_id = input("\tEnter the employee id to be change:")
			print(emp_id)
			if emp_id not in emp.keys():
				print("\tWrong employee id")
			else:
				new_name = input("\tEnter the new name:")
				emp[emp_id]['name'] = new_name
				print(emp)
		elif ch1 == 2:
			print(".........................change employee age.........................")
			emp_id = input("\tEnter the employee id to be change:")
			if emp_id not in emp.keys():
				print("\tWrong employee id")
			else:
				new_age = int(input("\tEnter the new age:"))
				emp[emp_id]['age'] = new_age
				print(emp)
		elif ch1 == 3:
			print("........................change employee gender.....................")
			emp_id = input("\tEnter the employee id:")
			if emp_id not in emp.keys():
				print("\tWrong employee id")
			else:
				new_gender = input("\tEnter the new gender:")
				emp[emp_id]['gender'] = new_gender
				print(emp)
		elif ch1 == 4:
			print("...........................change employee salary..................")
			emp_id = input("\tEnter the employee id to be change:")
			if emp_id not in emp.keys():
				print("\tWrong employee id")
			else:
				new_salary=int(input("\tEnter the new salary:"))
				emp[emp_id]['salary'] = new_salary
				print(emp)


	elif choice == 5:
		print("...................................display employees........................")
		for empid,emp in emp.items():
			print(f'{empid} | {emp["name"]} |{emp["age"]} |{emp["gender"]}')
			print(emp)		
	else:
		print("invalid choice")
