import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns


def get_anscombe_data():
    anscombe_df = sns.load_dataset("anscombe")

    return anscombe_df


def get_anscombe_results(anscombe_df):

    mean = anscombe_df.groupby("dataset").mean().round(2)
    mean_csv = pd.DataFrame(mean)
    std = anscombe_df.groupby("dataset").std(ddof=0).round(2)
    std_csv = pd.DataFrame(std)
    corr = anscombe_df.groupby("dataset").corr().round(2)
    corr_csv = pd.DataFrame(corr)
    var = anscombe_df.groupby("dataset").var().round(1)
    var_csv = pd.DataFrame(var)

    results = pd.concat([mean_csv, std_csv, corr_csv, var_csv])

    return results


def get_anscombe_plot(anscombe_df):
    ansc_plot = sns.lmplot(x="x", y="y", col="dataset", hue="dataset",
               data=anscombe_df, col_wrap=2, ci=None, palette="muted",
               height=4, scatter_kws={"s": 50, "alpha": 1})

    return ansc_plot


def main():
    anscombe_dir = os.mkdir('anscombes_quartet')

    anscombe_df = get_anscombe_data()
    results = get_anscombe_results(anscombe_df)
    ansc_plot = get_anscombe_plot(anscombe_df)

    results.to_csv(os.path.join('anscombes_quartet', 'results.csv'))
    ansc_plot.savefig(os.path.join('anscombes_quartet', 'plot.png'))

if __name__ == "__main__":
    main()


