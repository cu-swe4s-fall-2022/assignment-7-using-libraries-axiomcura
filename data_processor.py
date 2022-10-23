from pathlib import Path
from typing import List
from typing import Any
from typing import Union

import numpy as np


def get_random_matrix(num_rows: int, num_columns: int) -> np.ndarray:
    """Generates a random matrix that is sampled from a uniform range (0, 1] with

    Parameters:
    ----------
    num_rows : int
        Number of rows in your matrix
    num_columns : int
        Number of columns in your matrix

    Returns:
    -------
    np.ndarray
        Randomly generated matrix based on user provided dimensions.

    Raises:
    ------
    TypeError
        Raised if either num_rows or num_columns are not integer types
    ValueError
        Raised if either num_rows or num_columns are less than 0
    """

    # type checking
    if not isinstance(num_rows, int):
        e_msg = f"num_rows must be a integer not {type(num_rows)}"
        raise TypeError(e_msg)
    elif not isinstance(num_columns, int):
        e_msg = f"num_columns must be an integer not {type(num_rows)}"
        raise TypeError(e_msg)

    # checking num_rows and num_columns values
    if num_rows < 0:
        raise ValueError("Number of rows must be positive")
    elif num_columns < 0:
        raise ValueError("Number of columns must be positive")

    # generating matrix
    matrix = np.random.rand(num_rows, num_columns)

    return matrix


def get_file_dimensions(file_name):
    return (0, 0)


def write_matrix_to_file(
    num_rows: int, num_columns: int, file_name: str
) -> None:
    """Generates a matrix based on given number of columns and rows. The matrix
    is is then written out into your a file in your current directory.

    Parameters
    ----------
    num_rows : int
        number of rows for your matrix
    num_columns : int
        number of columns for your matrix
    file_name : str
        name of the output file containing generated matrix

    Returns
    -------
    None
        Generates a matrix file in current directory

    Raises:
    -------
    FileExistsError:
        Raised if the file name exists.

    Errors raised come from from the `get_random_matrix()` function:
    TypeError
        Raised if either num_rows or num_columns are not integer types
    ValueError
        Raised if either num_rows or num_columns are less than 0
    """

    # generate matrix
    matrix = get_random_matrix(num_rows=num_rows, num_columns=num_columns)

    # create save path object
    save_path = Path(".") / f"{file_name}.csv"

    # to prevent overwriting, we check if the file exists, if so raise error
    if save_path.is_file():
        raise FileExistsError(f"{save_path.name} already exists.")

    # writing csv file
    with open(save_path, "w") as out_file:

        # iterating each row and converting it into a string. Stringed array
        # is written into a file
        for row in matrix:

            # convert array into string type
            row_data_str = ",".join(str(i) for i in row.tolist())

            # write into file
            file_conts = f"{row_data_str}\n"
            out_file.write(file_conts)

    # printing message where the file is saved
    print(f"File saved in: {str(save_path.absolute())}")

    return None


# ------------------------------
# additional functions
# ------------------------------
def _format_types(
    data_content: List[str],
) -> List[Union[Union[float, int], str]]:
    """Converts string contents to it's appropriate format.

    Parameters
    ----------
    data_content : List[Any]
        extracted contents from iris data file

    Returns
    -------
    List[Union[Union[float, int], str]]
        list of appropriately typed data entries.
    """

    formmated_data_entries = []
    for row in data_content:

        formatted_row_entries = []
        for entry in row:

            # check if it is a integer
            if entry.isdigit():
                entry = int(entry)
                formatted_row_entries.append(entry)
                continue

            # checking if float
            try:
                entry = float(entry)
                formatted_row_entries.append(entry)

            # if value error is raised, then it is a string or bool
            except ValueError:

                # checking if it is a bool
                # -- eval checks for python attributes, functions and methods
                # -- in string format
                # eval("False") -> False #bool object from string
                try:
                    entry = eval(entry.capitalize())
                    formatted_row_entries.append(entry)

                # if NameError is caught, then it is a string
                except NameError:
                    entry = str(entry)
                    formatted_row_entries.append(entry)

        formmated_data_entries.append(formatted_row_entries)

    return formmated_data_entries


def read_data_file(path: str) -> List[str]:
    """Loads contents from iris data file as a list.

    Parameters
    ----------
    path : str
        path to datafile

    Returns
    -------
    List[str]
        contents within data file as a list

    Raises
    FileNotFoundError:
        Raised when a provided path points to a non-existing file
    PermissionError
        Raised if you do not have read permissions.
    RuntimeError
        raised if an unexpected error captured
    """

    path_obj = Path(path)
    if not path_obj.is_file():
        raise FileNotFoundError(f"{path} does not exist.")

    try:
        data_entries = []
        with open(path_obj, "r") as infile:
            iris_data = []
            for row in infile:
                entries = row.rstrip("\n").split(",")

                # remove rows with no data
                if len(entries) == 1:
                    continue

                # store data
                data_entries.append(entries)

    except PermissionError:
        raise PermissionError(
            f"You do not have permissions to read {path} file"
        )
    except Exception:
        raise RuntimeError("Unexpected error captured when loading file")

    # formatting entries to appropiate types
    data_entries = _format_types(data_entries)

    return data_entries
