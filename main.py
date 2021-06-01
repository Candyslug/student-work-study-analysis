import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import matplotlib.patches as mpatches

xls = pd.ExcelFile (r'./data_sheet.xlsx') #file
df1 = pd.read_excel(xls, 'data_page') #page on the excel sheet

x = np.array(pd.DataFrame(df1, columns=['Attendance']).values)
y = np.array(pd.DataFrame(df1, columns=['Grade']).values)

def make_list(l):
    res = list()
    for i in range(l.shape[0]):
        res.append(float(l[i]))
    return res

ages = np.array(pd.DataFrame(df1, columns=['Age']).values)
res = np.array(make_list(ages))
print(np.average(res))

x = make_list(x)
y = make_list(y)

plt.scatter(x, y)

slope, intercept, r, p, std_err = stats.linregress(x, y)
print('slope: ', slope)
print('intercept: ', intercept)
print('r: ', r)
print('p: ', p)
def myfunc(x):
    return slope * x + intercept
mymodel = list(map(myfunc, x))
plt.plot(x, mymodel, color='red')

blue_patch = mpatches.Patch(label='Grade')
red_patch = mpatches.Patch(color='red', label='Trend Line')

plt.legend(handles=[blue_patch, red_patch])

plt.title("results")

plt.grid()

plt.xlabel('Attendace (%)')
plt.ylabel('Final Grade (%)')
plt.show()

