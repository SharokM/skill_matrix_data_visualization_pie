import matplotlib.pyplot as plt 


# PIE CHART 
pieSlices = [160, 80, 90, 10, 5, 20]
sliceLabels = ["Python", "React.JS", "JavaScript", "NodeJS", "Azure", "Other"]
sliceColors = ["#8B008B", "#7FFFD4", "#7FFF00", "#D2691E", "#0000FF", "#DC143C"]


plt.pie(pieSlices, labels=sliceLabels, colors=sliceColors)
plt.title("Programming Language Usage", fontsize=22)
plt.savefig("pieSlicePiechart.png")
plt.show()

# LINE CHART 
timePerWeek = [10, 5, 7, 1, 2, 1]
dateStarted = ["Python", "JavaScript", "GIT", "NodeJS", "YAML", "JEST"]
plt.plot(dateStarted, timePerWeek, color="#F16059")
plt.xlabel("Year Started", fontsize=16)
plt.ylabel("time per week (hours)", fontsize=16)
plt.title("Programming Skill Usage")
plt.savefig("lineGraph.png")
plt.show()



# BAR CHART 
towns = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia"]
average_income = [75000, 65000, 55000, 50000, 45000, 40000]
plt.bar(towns, average_income, color="#F16059")
plt.xlabel("Towns", fontsize=16) 
plt.ylabel("Average Income ($)", fontsize=16) 
plt.title("Average Income by Town") 
plt.savefig("barChart.png")
plt.show()

# HISTOGRAM
LanguagesByYear = [2025, 2026, 2027] 
bins = 6
plt.hist(LanguagesByYear, bins, histtype="bar", color="#F16059") 
plt.xlabel("Year", fontsize=16) 
plt.ylabel("Number of Programming Languages Learned", fontsize=16) 
plt.xticks(range(2025,2029,1))
plt.yticks(range(0,5,1))
plt.title("Programming Languages Learned Over Time") 
plt.savefig("histogram.png") 
plt.show()           

# Trending Temps Line Chart
month = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
temp = [28,32,31,40,45,55,60,65,54,43,34,30]
plt.plot(month, temp, color="purple")
plt.xlabel("Month", fontsize=18)
plt.ylabel("Temp (f)", fontsize=18)
plt.title("Alaska Ave Temp for 2018 in Alaska(F)")
plt.savefig("noth_pole_temp.png")
plt.show()

# Movie by year Histo 
movie_year = [2019,2019,2018,2018,2017,2016,2016,2016,2015,2015,2014,2014,2014,2013,2012,2012,2011,2010,2010,2009,2009,2008,2008,2007,2007,2007,2007,2006,2006,2006,2006,2005,2004,2004,2003,2003,2003,2002,2002,2001,1999,1999,1998,1998,1997,1996,1996,1995,1994,1993,1992,1991,1990,1989,1988,1987,1986,1985,1985,1984,1983,1982,1982,1982,1981,1979,1979,1979,1978,1978,1977,1977]
bins =[1976,1985, 1986,1997, 1998,2007, 2008,2019]
plt.hist(movie_year, bins, histtype="bar", color="#F16059")
plt.xlabel("Year")
plt.ylabel("Number of Movies")
plt.title("Movie Career of Brad Pitt")
plt.savefig("movie_histogram.png") 
plt.show()