###Using user-defined functions example
##myfamily = {1: {'Name': 'Josh', 'Age': '47', 'Birthday': 'November 11', 'Favorite Food': 'Probably Yao Hua', 'Role': 'Dad'}, 2: {'Name': 'Janet', 'Age': '49', 'Birthday': 'October 2', 'Favorite Food': 'Who knows?', 'Role': 'Mom'}, 3: {'Name': 'Joyce', 'Age': '17', 'Birthday': 'July 15', 'Favorite Food': 'Again, who knows?', 'Role': 'Sister'}, 4: {'Name': 'Serena', 'Age': '14', 'Birthday': 'October 17', 'Favorite Food': 'Chicken', 'Role': 'Sister'}, 5: {'Name': 'Justin', 'Age': '11', 'Birthday': 'October 12', 'Favorite Food': 'Fries', 'Role': 'Brother'}}
##def family(person):
##        print("\nName: ", myfamily[str.capitalize(person)]['Name'])
##        print("Age: ", myfamily[str.capitalize(person)]['Age'])
##        print("Birthday: ", myfamily[str.capitalize(person)]['Birthday'])
##        print("Favorite Food: ", myfamily[str.capitalize(person)]['Favorite Food'])
##        print("Role: ", myfamily[str.capitalize(person)]['Role'])
##
##for i in myfamily:
##    family(i)



#OR:
myfamily = {'Josh': {'Name': 'Josh', 'Age': '47', 'Birthday': 'November 11', 'Favorite Food': 'Probably Yao Hua', 'Role': 'Dad'}, 'Janet': {'Name': 'Janet', 'Age': '49', 'Birthday': 'October 2', 'Favorite Food': 'Who knows?', 'Role': 'Mom'}, 'Joyce': {'Name': 'Joyce', 'Age': '17', 'Birthday': 'July 15', 'Favorite Food': 'Again, who knows?', 'Role': 'Sister'}, 'Serena': {'Name': 'Serena', 'Age': '14', 'Birthday': 'October 17', 'Favorite Food': 'Chicken', 'Role': 'Sister'}, 'Justin': {'Name': 'Justin', 'Age': '11', 'Birthday': 'October 12', 'Favorite Food': 'Fries', 'Role': 'Brother'}}
def family(person):
	if str.capitalize(person) not in myfamily:
		print(str.capitalize(person), "is not part of my family")
	else:
		print("\nName: ", myfamily[str.capitalize(person)]['Name'])
		print("Age: ", myfamily[str.capitalize(person)]['Age'])
		print("Birthday: ", myfamily[str.capitalize(person)]['Birthday'])
		print("Favorite Food: ", myfamily[str.capitalize(person)]['Favorite Food'])
		print("Role: ", myfamily[str.capitalize(person)]['Role'])

family('joe mama')
family('sErEnA')


##Easier but same concept
##def employee(empname, emprole):
##    print("Employee Name: ", empname)
##    print("Employee Role: ", emprole)
##
##employee('Serena','Manager')
    
