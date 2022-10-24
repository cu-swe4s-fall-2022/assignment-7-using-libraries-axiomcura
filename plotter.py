"""_summary_

* create_iris_boxplot - Creates a box plot
"""
import matplotlib.pyplot as plt
import pandas as pd


def create_iris_boxplot(
    iris_df: pd.DataFrame, outname: str, axis=None
) -> plt.Axes:
    """Creates a box plot of sepal width/length and petal width/length.

    Parameters
    ----------
    iris_df : pd.DataFrame
        dataframe containing iris data
    outname : str
        name of produced image

    Raises
    ------
    TypeError
        raised if iris_df is not a data frame or out name is not a string type
    ValueError
        raised if expected column values do not match from extracted data
    """

    # type checking
    if not isinstance(iris_df, pd.DataFrame):
        raise TypeError("Iris data must be a pandas dataframe")
    if not isinstance(outname, str):
        raise TypeError(f"outname must be a string, not {type(outname)}")

    # columns
    sel_cols = iris_df.columns.tolist()[:-1]
    if sel_cols != [
        "sepal_width",
        "sepal_length",
        "petal_width",
        "petal_length",
    ]:
        raise ValueError(
            "Column from dataset do not match with expected column names"
        )

    # format data into dictionary
    data = {}
    for col_name in sel_cols:
        data_array = iris_df[col_name].values
        data[col_name] = data_array

    # creating subplot
    fig, ax = plt.subplots()
    if axis is not None:
        ax = axis

    ax.boxplot(data.values())
    ax.set_xticklabels(data.keys())
    ax.set_ylabel("cm")
    ax.set_title("Iris boxplot of all species")

    # saving plot
    plt.savefig(outname)
    plt.close()

    return ax


def petal_width_v_length_scatter(
    iris_df: pd.DataFrame, outname: str, axis=None
) -> plt.Axes:
    """Creates a scatter plot that compares all sepal widths across all species
    . Returns axis object that contains all the plot data.

    Parameters
    ----------
    iris_df : pd.DataFrame
        data frame containing iris data
    outname : str
        name of generated image output

    Return
    ------
    plt.Axes
        axis object

    Raises
    ------
    TypeError
        raised if iris_df is not a data frame or out name is not a string type
    ValueError
        raised if expected column values do not match from extracted data
    """
    # type checking
    if not isinstance(iris_df, pd.DataFrame):
        raise TypeError("Iris data must be a pandas dataframe")
    if not isinstance(outname, str):
        raise TypeError(f"outname must be a string, not {type(outname)}")

    # plotting data based on species
    fig, ax = plt.subplots()
    if axis is not None:
        ax = axis

    species = iris_df["iris_species"].unique().tolist()
    for species_name in species:
        iris_subset = iris_df[iris_df["iris_species"] == species_name]
        ax.scatter(
            iris_subset["sepal_length"],
            iris_subset["sepal_width"],
            label=species_name,
        )

    # labeling axis
    ax.set_ylabel("sepal_width (cm)")
    ax.set_xlabel("sepal_length (cm)")
    ax.set_title("Sepal Length vs Sepal Width based on Species")
    ax.legend()

    # saving plot
    plt.savefig(outname)

    plt.close()
    return ax

def merged_boxplot_and_scatter(iris_df: pd.DataFrame, outname: str) -> plt.Axes:
    """plots both boxplot and scatter plot together and saves it.

    Parameters
    ----------
    iris_df : pd.DataFrame
        iris data frame
    outname : str
        outname of generated image

    Returns
    -------
    None
        Merged image with named by outname in current directory
    """
    # type checking
    if not isinstance(iris_df, pd.DataFrame):
        raise TypeError("Iris data must be a pandas dataframe")
    if not isinstance(outname, str):
        raise TypeError(f"outname must be a string, not {type(outname)}")

    fig, ax = plt.subplots(1, 2)
    fig.set_size_inches(20,10)
    create_iris_boxplot(iris_df, outname="box", axis=ax[0])
    petal_width_v_length_scatter(iris_df, outname="scatter", axis=ax[1])

    for i in range(len(ax)):
        ax[i].spines['top'].set_visible(False)
        ax[i].spines['right'].set_visible(False)
        ax[i].spines['bottom'].set_visible(True)
        ax[i].spines['left'].set_visible(True)

    plt.savefig(outname)