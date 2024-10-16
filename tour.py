f = open("/home/serena/note.txt")
l = f.readlines()
f.close()
cities = []
states = set()
international = []
countries = set()
countries.add("United States of America")
def ooo(start,end,ci,st):
	for i in range(start,end):
		c = l[i].replace("\n","")
		k = c.split()
		for i in range(len(k)):
			if "," in k[i]:
				k[i] = k[i].replace(",","")
				Break = i
		city = ""
		state = ""
		for i in range(Break + 1):
			city = city + " " + k[i]
		for i in range(Break + 1,len(k)):
			state = state + " " + k[i]
		city = city[1 : :]
		state = state[1 : :]
		ci.append(city)
		st.add(state)
	ci.sort()
ooo(0,55,cities,states)
ooo(55,len(l),international,countries)
states = sorted(states)
countries = sorted(countries)

