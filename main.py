import matplotlib.pyplot as plt 

pieSlices = [160, 80, 90, 10, 5, 20]

sliceLabels = ["Python", "React.JS", "JavaScript", "NodeJS", "Azure", "Other"]

sliceColors = ["#8B008B", "#7FFFD4", "#7FFF00", "#D2691E", "#0000FF", "#DC143C"]

plt.pie(pieSlices, labels=sliceLabels, colors=sliceColors)
plt.title("Programming Language Usage", fontsize=22)
plt.savefig("pieSlicePiechart.png")
plt.show()

