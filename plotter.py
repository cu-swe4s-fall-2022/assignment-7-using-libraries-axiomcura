"""_summary_

* create_iris_boxplot - Creates a box plot
"""
import matplotlib.pyplot as plt
import pandas as pd


def create_iris_boxplot(iris_df: pd.DataFrame, outname: str) -> None:
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
    ax.boxplot(data.values())
    ax.set_xticklabels(data.keys())
    ax.set_ylabel("cm")
    ax.set_title("Iris boxplot of all species")

    # saving plot
    plt.savefig(outname)


def petal_width_v_length_scatter(iris_df: pd.DataFrame, outname: str) -> None:
    """_summary_

    Parameters
    ----------
    iris_df : pd.DataFrame
        _description_
    outname : str
        _description_

    Return
    ------
    None
        Generates an image file

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

    # setting up subplots
    fig, ax = plt.subplots()

    # plotting data based on species
    species = iris_df["iris_species"].unique().tolist()
    for species_name in species:
        iris_subset = iris_df[iris_df["iris_species"] == species_name]
        plt.scatter(
            iris_subset["sepal_length"],
            iris_subset["sepal_width"],
            label=species_name,
        )

    # labeling axis
    ax.set_ylabel("sepal_width (cm)")
    ax.set_xlabel("sepal_length (cm)")
    ax.set_title("Sepal Length vs Sepal Width based on Species")
    plt.legend()

    # saving plot
    plt.savefig(outname)
