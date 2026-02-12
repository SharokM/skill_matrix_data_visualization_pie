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