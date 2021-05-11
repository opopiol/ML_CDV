import pandas as pd
import os
import seaborn as sns


def get_anscombe_data():
    """This function loads Anscombe's quartet data from seaborn's library
    :return: anscombe_df: Data frame with Anscombe's quartet values
    """

    anscombe_df = sns.load_dataset("anscombe")

    return anscombe_df


def get_anscombe_results(anscombe_df):
    """This function calculates mean, standard deviation, variance and correlation
    :param anscombe_df: File name of input data
    :return: results: dataframe's calculations
    """

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
    """This function creates plot for each dataset
    :param anscombe_df: File name of input data
    :return: ansc_plot: Show the results of a linear regression within each dataset
    """

    ansc_plot = sns.lmplot(x="x", y="y", col="dataset", hue="dataset",
               data=anscombe_df, col_wrap=2, ci=None, palette="muted",
               height=4, scatter_kws={"s": 50, "alpha": 1})

    return ansc_plot


def main():
    """This function creates directory and saves results in csv and plot"""

    anscombe_dir = os.mkdir('anscombes_quartet')

    anscombe_df = get_anscombe_data()
    results = get_anscombe_results(anscombe_df)
    ansc_plot = get_anscombe_plot(anscombe_df)

    results.to_csv(os.path.join('anscombes_quartet', 'results.csv'))
    ansc_plot.savefig(os.path.join('anscombes_quartet', 'plot.png'))


if __name__ == "__main__":
    main()
