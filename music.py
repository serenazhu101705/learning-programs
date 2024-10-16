import module
singers = ['singer1','singer2','singer3','singer4','singer5']
Band = {}
def year(year,concerts,record,music,tour,tour_name,*ends):
    "Annual Earnings of each member of the band"
    global band
    band = {}
    for i in singers:
        band[i] = {}
    band['Total'] = {}
    for i in band:
        band[i]['Concerts'] = round(concerts/5)
        band[i]['Record Deal'] = round(record/5)
        band[i]['Music'] = round(music/5)
        band[i][tour_name] = round(tour/5)
    for i in band['Total']:
        band['Total'][i] = round(band['Total'][i] * 5)
            
    def ads(singer,value):
        for i in band:
            if singer == i:
                band[i]['Endorsements'] = round(value)
    ends = [i for i in list(ends)]
    list(map(ads,singers,ends))
    ads('Total',sum(ends))
    for i in band:
        total = round(sum(band[i].values()))
        ads = band[i]['Endorsements']
        net_worth = round((((total - ads) * 2/5 ) + ads)* 3/4)
        band[i]['Total Earnings'] = total
        band[i]['Net Worth'] = net_worth
    for el in band:
        k = []
        k.append(band[el]['Net Worth'])
        for i in Band:
            k.append(Band[i][el]['Net Worth'])
        if year != '2020':
            band[el]['Total Net Worth'] = sum(k)
        else:
            band[el]['Total Net Worth'] = band[el]['Net Worth']
    Band[year] = band
year('2020',62600000,62400000,102700000,0,"Tour",61200000,52800000,41700000,40900000,29760000)
year('2021',18700000,62400000,177100000,608400000,'Blessings Staduim Tour',97700000,86900000,72500000,70600000,38900000)
years = list(Band)
def Print(year, singer):
    print("\n" + year + ":\n")
    for i in Band[year][singer]:
        print(i + ":", "${}".format("{:,}".format(Band[year][singer][i])))
singers.append('Total')
print("Press ENTER to see the statistics.")
for i in singers:
    module.enter()
    print("\n" + str.title(i) + "\n")
    for el in Band:
        Print(el,i)
print("\n\nThis band has been together for",len(Band),"years, since",years[0])
print("Would you like to see some statistics?")
stats = module.yesorno()
if stats == "no":
    print("Ok, goodbye!")
    
else:
    singers.remove('Total')
    for last_year in Band:
        pass
    def equals(singer,value):
        k.append(Band[last_year][singer][value])
    def l(value):
        for singer in singers:
            equals(singer,value)
        for ok in Band[last_year]:
                 if Band[last_year][ok][value] == max(k):
                     global e_singer
                     e_singer = ok
        e = []
        for i in Band:
            e.append(Band[i][e_singer][value])
        global e_value
        e_value = sum(e)

    def kl(valu):
        global k
        k = []
        l(valu)
        print("The singer with the most earnings in the",valu,"category is",str.title(e_singer) + ", with about","${}".format("{:,}".format(e_value)),"in total",str.lower(valu),"income as of",last_year)
    List = ["Endorsements","Total Earnings","Net Worth"]
    print("As of",str(last_year) + ":\n")
    print("(Press ENTER to see the next statistic)")
    for i in List:
        module.Next(kl,i)
    totals = []
    for i in Band:
        totals.append(Band[i]['Total']['Total Earnings'])
    module.Next(print,("All in all, the Band made a total of " + "${}".format("{:,}".format(sum(totals))) + " in pretax income, and has a total net worth of around " + "${}".format("{:,}".format(Band[last_year]['Total']['Total Net Worth']))))
    tours = set()
    tour_years = set()
    for i in Band:
        for el in singers:
            for iel in Band[i][el]:
                if "Tour" in iel and iel != "Tour" and Band[i][el][iel] != 0:
                    tours.add(iel)
                    tour_years.add(i)
    tour_money = []
    for i in range(0,len(tour_years)):
        for el in range(0,len(tours)):
            h = list(tour_years)[i]
            g = list(tours)[el]
            tour_money.append(Band[h]['Total'][g])
    if len(tours) > 1 or len(tours) == 0:
        times = " times."
    else:
        times = " time."
    module.Next(print,("Since " + str(years[0]) + ", they have been on tour " + str(len(tours)) + str(times)))
    if len(tours) != 0: 
        module.Next(print,("Here are the tours that they have been on since their beginning:"))
        for i in tours:
            print(i)
        module.Next(print,"The Band has been on tour in the following years:")
        for i in tour_years:
            print(i)
        module.enter()
        for i in range(0,len(tour_money)):
            print("In",str(list(tour_years)[i]) + ", they tallied a gross income of","${}".format("{:,}".format(tour_money[i])),"from touring.")
            print("Each singer ended up with","${}".format("{:,}".format(round(tour_money[i]/5))),"in gross income.")
            module.enter()
    def li(value):
        e = []
        for i in Band:
            e.append(Band[i]['Total'][value])
        return sum(e)
    concerts = li('Concerts')
    record = li('Record Deal')
    music = li('Music')
    tour = sum(tour_money)
    total = concerts + record + music + tour
    def percentage(value):
        value = round((value/total)*100,1)
        return value    
    concerts = percentage(concerts)
    record = percentage(record)
    music = percentage(music)
    tour = percentage(tour)
    equals = {"Concerts":concerts,"Record Deal":record,"Music":music,"Tour":tour}
    for i,el in equals.items():
        module.Next(print,"The " + str(i) + " portion make up "+"%"+str(el) + " of the total income.")
