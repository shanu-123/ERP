emp={}
teams={}
organization={}
def add_employee():
	print("................Adding employee.....................")
	emp_id = input("\tEnter the employee id")
	if emp_id not in emp.keys():
		name = input("\tEnter the name")
		age = int(input("\tEnter the age"))
		gender = input("\tEnter the gender")
		place = input("\tEnter the place")
		salary = int(input("\tEnter the salary"))
		prv_company = input("\tEnter your previous company")
		joining_date = int(input("\tEnter your joining date (DD/MM/YYYY)"))
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

def manage_organization():
	print("....................Manage organization.....................")
	print("\t1.Add organization")
	print("\t2.Edit organization")
	print("\t3.Display organization")
	print("\t4.Exit")

def manage_all_organization():
	manage_organization()
	while True:
		ch = int(input("\tEnter your choice"))
		if ch == 1:
			emp_id = input("\tEnter the employee id")
			if emp_id in emp.keys():
				org_name = input("\tEnter the name of organization")
				org_email = input("\tEnter the organization mail id")
				temp = {
					"org_name":org_name,
					"org_email":org_email
				}
				organization[emp_id] = temp
			else:
				print("\tWrong employee id")
		elif ch == 2:
			print("...................Editing organization..................")
			emp_id = input("\tEnter the employee id")
			if emp_id not in emp.keys():
				print("\tWrong employee id")
			else:
				organization[emp_id]['org_name'] = input("\tEnter the new organization")
				display_organization()
		elif ch == 3:
			display_organization()
		elif ch == 4:
			break
		else:
			print("\tInvalid choice")

def display_organization():
	for emp_id,org_details in organization.items():
		print(f"\t{emp_id} | {org_details['org_name']} | {org_details['org_email']}")

def delete_employee():
	print("..................Deleting employee.......................")
	emp_id = input("\tEnter the employee id")
	if emp_id not in emp.keys():
		print("\t Wrong employee id")
	else:
		del emp[emp_id]
		print(emp)
def search_employee():
	print("..................Searching employee...................")
	name = input("\tEnter the name")
	flag = False
	for i in emp.values():
		if i["name"] == name:
			print(f'\t{i["name"]} | {i["age"]} | {i["gender"]}')
			flag = True
			break
	if flag == False:
		print("\tNot found")

def change_employee_details():
	print("...................Changing employee details.....................")
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
	print("...........................Displaying employee details.........................................")
	for empid,employee in emp.items():
		print(f"{empid} | {employee['name']} |{employee['age']} | {employee['gender']} | {employee['place']} | {employee['salary']} | {employee['previous_company']} | {employee['joining_date']} ")
		print(emp)

def change_employee_menu():
	print("......................Change employee menu.....................")
	print("\t1.Change employee by name:")
	print("\t2.Change employee by age:")
	print("\t3.Change employee by gender:")
	print("\t4.Change employee by salary:")



def main_menu():
	print("...........................Main menu..............................")
	print("1.Add Employee")
	print("2.Delete Employee")
	print("3.Search Employee by name")
	print("4.Change Employee details")
	print("5.Display Details")
	print("6.Manage all teams")
	print("7.Manage all organization")
	print("8.Exit")
def manage_all_team_menu():
	print("......................Manage team menu...........................")
	print("\t1.Create Team")
	print("\t2.Display Team")
	print("\t3.Manage Team(Particular)")
	print("\t4.Delete Team")
	print("\t5.Exit")
def manage_all_teams():
	while True:
		manage_all_team_menu()
		ch = int(input("\tEnter your choice"))
		if ch == 1:
			#create team
			create_team()
		elif ch == 2:
			#Display teams
			display_team()
		elif ch == 3:
			#Manage team(particular)
			manage_team()
		elif ch == 4:
			delete_team()
		elif ch == 5:
			break
		else:
			print("\nInvalid choice")

def create_team():
	print("......................Create team..........................")
	team_name = input("\tEnter the team name")
	teams[team_name] = []

def delete_team():
	print("...........................Delete team...........................")
	team_name = input("\tEnter the team name ")
	if team_name in teams.keys():
		del teams[team_name]
		print("\tDeleted the team")
	else:
		print("\tWrong team name")


def display_team():
	print("...................................Display Team................................")
	for key,values in teams.items():
		name_string = ""
		for i in values:
			name_string = name_string +"|"+emp[i]["name"]
		print(f"{key} => {name_string} ")

def manage_team_menu():
	print("......................Manage team manu......................")
	print("\t\t1.Add Member")
	print("\t\t2.Delete Member")
	print("\t\t3.List Members")

def manage_team():
	team_name = input("\t\tEnter the team name")
	manage_team_menu()
	cho = int(input("\t\tEnter the choice"))
	if cho == 1:
		add_member(team_name)
	elif cho == 2:
		delete_member(team_name)
	elif cho == 3:
		list_member(team_name)
	else:
		print("\tInvalid choice")

def add_member(team_name):
	print("..........................Adding team.................")
	display_employee()
	emp_id = input("\t\tEnter the employee id")
	if emp_id in emp.keys():
		teams[team_name].append(emp_id)
	else:
		print("\t\tWrong employee id")
		print("\tAdded the member into the team")

def list_member(team_name):
	print(".........................Listing out the team...................")
	name_string = ""
	for i in teams[team_name]:
		name_string = name_string +"|"+i+"." + emp[i]["name"]
	print(f"{name_string}")

def delete_member(team_name):
	print("...........................delete team......................")
	list_member(team_name)
	emp_id = input("\t\tEnter the employee id")
	if emp_id in teams[team_name]:
		teams[team_name].remove(emp_id)
	else:
		print("\t\tWrong employee id")

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
		change_employee_details()
	elif choice == 5:
		display_employee()
	elif choice == 6:
		manage_all_teams()
	elif choice == 7:
		manage_all_organization()
	elif choice == 8:
		break
	else:
		print("\tInvalid choice manage_group")

