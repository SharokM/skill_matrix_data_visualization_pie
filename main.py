import matplotlib.pyplot as plt 

pieSlices = [160, 80, 90, 10, 5, 20]

sliceLabels = ["Python", "React.JS", "JavaScript", "NodeJS", "Azure", "Other"]

sliceColors = ["purple", "teal", "yellow", "brown", "blue", "red"]

plt.pie(pieSlices, labels=sliceLabels, colors=sliceColors)
plt.title("Programming Language Usage")
plt.savefig("pieSlicePiechart.png")
plt.show()