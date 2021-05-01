import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

x = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
y1 = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]
y2 = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]
y3 = [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]
x4 = [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8]
y4 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]

dir=os.mkdir('Anscombes_quartet')

anscombe_df = sns.load_dataset("anscombe")

mean = anscombe_df.groupby("dataset").mean().round(2)
mean_csv = pd.DataFrame(mean)
std = anscombe_df.groupby("dataset").std(ddof=0).round(2)
std_csv = pd.DataFrame(std)
corr = anscombe_df.groupby("dataset").corr().round(2)
corr_csv = pd.DataFrame(corr)
var = anscombe_df.groupby("dataset").var().round(1)
var_csv = pd.DataFrame(var)


results=pd.concat([mean_csv, std_csv, corr_csv, var_csv])
print(results)
results.to_csv(f'Anscombes_quartet/results.csv', index=False, header=True, sep=';', float_format='%.2f')


scatter_plot_df = anscombe_df.reset_index()

fig, axs = plt.subplots(2,2, sharex=True, sharey=True, figsize=(6, 6))
fig.suptitle('Anscombes quartet', fontsize=16)

axs[0, 0].set(xlim=(0, 20), ylim=(2, 14))
axs[0, 0].set(xticks=(0, 10, 20), yticks=(0, 4, 8, 12))

axs[0, 0].scatter(x, y1)
axs[0, 1].scatter(x, y2)
axs[1, 0].scatter(x, y3)
axs[1, 1].scatter(x4, y4)

plt.savefig(f'Anscombes_quartet/plot.png')

