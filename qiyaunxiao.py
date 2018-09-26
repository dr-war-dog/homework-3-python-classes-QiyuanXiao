import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.DataFrame.from_csv("F:\\UIUC\\590DV\\homework4\\us-marriages-divorces-1867-2014.csv")

# build class
class Dataset:
    selectdate1 = data[(data.index >= "1867") & (data.index <= "1880")]

    selectdate2 = data[(data.index >= "1875") & (data.index <= "1881")]

    def __init__(self, data):
        self.data = data


# load data
df = Dataset(data)

# question 1 plot
plt.yticks(np.linspace(0, 15, 8))
plt.xticks(np.linspace(1867, 1880, 14))
plt.title("Marriages and Divorces between 1867-1880", fontsize=12)
plt.ylabel("Marriages and Divorces per 1000 capita", fontsize=10)
plt.xlabel("Year", fontsize=10)
df.selectdate1["Marriages_per_1000"].plot()
df.selectdate1["Divorces_per_1000"].plot()
plt.legend(["Marriages", "Divorces"])
plt.savefig("F:\\UIUC\\590DV\\homework4\\question_1.png")
plt.show()


# question 2 plot
plt.yticks(np.linspace(0, 15, 8))
plt.xticks(np.linspace(1875, 1881, 7))
plt.title("Marriages and Divorces between 1875-1881", fontsize=12)
plt.ylabel("Marriages and Divorces per 1000 capita", fontsize=10)
plt.xlabel("Year", fontsize=10)
df.selectdate2["Marriages_per_1000"].plot()
df.selectdate2["Divorces_per_1000"].plot()
plt.legend(["Marriages", "Divorces"])
plt.savefig("F:\\UIUC\\590DV\\homework4\\question_2.png")
plt.show()
