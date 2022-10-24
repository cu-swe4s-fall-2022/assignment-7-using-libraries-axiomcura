import hashlib
import os
import pickle
import random
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

import data_processor as dp
import plotter as pl


class TestMatrixGeneration(unittest.TestCase):
    def test_make_matrix_1(self) -> None:
        """makes matrix with integer"""

        # setting input parameters
        n_rows = 10
        n_cols = 10

        # loading true matrix
        with open("single_mat.pickle", "rb") as f:
            true_mat = pickle.load(f)

        # generating test matrix
        test_mat = dp.get_random_matrix(n_rows, n_cols)

        # checking shape, and data type
        self.assertEqual(type(true_mat), type(test_mat))
        self.assertEqual(true_mat.shape, test_mat.shape)

    def test_make_matrix_2(self) -> None:
        """Make matrix with 1 non integer types"""

        # setting input parameters
        n_rows = 10.0
        n_cols = 10

        # test
        self.assertRaises(TypeError, dp.get_random_matrix, n_rows, n_cols)

    def test_make_matrix_3(self) -> None:
        """Make matrix with 2 non integer types"""

        # setting input parameters
        n_rows = 10.0
        n_cols = 10.0

        # test
        self.assertRaises(TypeError, dp.get_random_matrix, n_rows, n_cols)

    def test_make_matrix_4(self) -> None:
        """Make matrix with string number types"""

        # setting input parameters
        n_rows = "10"
        n_cols = "10"

        # test
        self.assertRaises(TypeError, dp.get_random_matrix, n_rows, n_cols)

    def test_make_matrix_5(self) -> None:
        """Make matrix with row numbers lower than 0"""

        # setting input parameters
        n_rows = -1
        n_cols = 10

        # test
        self.assertRaises(ValueError, dp.get_random_matrix, n_rows, n_cols)

    def test_make_matrix_5(self) -> None:
        """Make matrix with column numbers lower than 0"""

        # setting input parameters
        n_rows = 10
        n_cols = -1

        self.assertRaises(ValueError, dp.get_random_matrix, n_rows, n_cols)

    def test_making_multiple_matrix(self) -> None:
        """Generates 100 matrices and checks for type and shape. There is a
        10% probability where one of the inputs will be a float"""

        # simulating 100 matrices generation
        for _ in range(100):

            # setting float probability
            floats_exists = False
            float_proba_threshold = 0.10
            n_rows_float_proba = round(np.random.random(), 3)
            n_cols_float_proba = round(np.random.random(), 3)

            # setting parameters
            n_rows = np.random.randint(1, 100)
            n_cols = np.random.randint(1, 100)

            # change parameters to float based on probability
            if n_rows_float_proba < 0.10:
                n_rows = np.random.random() * 100
                floats_exists = True
            if n_cols_float_proba < float_proba_threshold:
                n_cols = np.random.random() * 100
                floats_exists = True

            # if the a float type is present, check for exception raises
            if floats_exists is True:
                print("Float type found, testing exception handling")

                # reset float exist state
                floats_exists = False

                # create matrix with float types
                self.assertRaises(
                    TypeError, dp.get_random_matrix, n_rows, n_cols
                )

            else:
                # setting truths
                true_shape = (n_rows, n_cols)
                true_type_str = "<class 'numpy.ndarray'>"

                matrix = dp.get_random_matrix(n_rows, n_cols)
                test_type_str = str(type(matrix))
                test_shape = matrix.shape

                # testing
                self.assertEqual(true_shape, test_shape)
                self.assertEqual(true_type_str, test_type_str)

    @classmethod
    def setUp(cls) -> None:

        # generating file names
        cls.single_mat = "single_mat.pickle"
        cls.file_exists = "file_exists.csv"

        # generating datasets
        with open(cls.single_mat, "wb") as mat_file:
            mat = np.random.rand(10, 10)
            pickle.dump(mat, mat_file)

        # generates an empty file
        with open(cls.file_exists, "w") as f:
            f.write("file exists")

    @classmethod
    def tearDown(cls) -> None:
        os.remove(cls.single_mat)
        os.remove(cls.file_exists)


# TODO: Finish loader function
class TestIO(unittest.TestCase):
    """Test class focuses on reading and writing files"""

    def test_type_converts_1(self) -> None:
        """Converts all entries within rows to it's appropriate types"""

        unformated_conts = [
            ["6.4", "8.4", "2.2", "6.8", "Iris-setosa"],
            ["5.9", "1.3", "2.3", "8.6", "Iris-setosa"],
            ["4.2", "8.1", "8.6", "9.0", "Iris-versicolor"],
            ["3.8", "11.6", "4.0", "3.0", "Iris-versicolor"],
            ["6.0", "7.3", "12.7", "2.8", "Iris-virginica"],
            ["10.3", "5.8", "1.5", "7.7", "Iris-virginica"],
        ]

        expected_formatted_conts = [
            [6.4, 8.4, 2.2, 6.8, "Iris-setosa"],
            [5.9, 1.3, 2.3, 8.6, "Iris-setosa"],
            [4.2, 8.1, 8.6, 9.0, "Iris-versicolor"],
            [3.8, 11.6, 4.0, 3.0, "Iris-versicolor"],
            [6.0, 7.3, 12.7, 2.8, "Iris-virginica"],
            [10.3, 5.8, 1.5, 7.7, "Iris-virginica"],
        ]

        test_conts = dp._format_types(unformated_conts)

        self.assertEqual(expected_formatted_conts, test_conts)

    def test_type_converts_2(self) -> None:
        """Converts all entries within rows to it's appropriate types. Contains
        bools and integers"""

        unformated_conts = [
            ["6.4", "8.4", "2.2", "6", "Iris-setosa"],
            ["5.9", "1.3", "2.3", "8", "Iris-setosa"],
            ["4.2", "8.1", "8.6", "9", "Iris-versicolor"],
            ["3.8", "11.6", "true", "3.0", "Iris-versicolor"],
            ["6.0", "7.3", "False", "2.8", "Iris-virginica"],
            ["10.3", "5.8", "True", "7.7", "Iris-virginica"],
        ]

        expected_formatted_conts = [
            [6.4, 8.4, 2.2, 6, "Iris-setosa"],
            [5.9, 1.3, 2.3, 8, "Iris-setosa"],
            [4.2, 8.1, 8.6, 9, "Iris-versicolor"],
            [3.8, 11.6, True, 3.0, "Iris-versicolor"],
            [6.0, 7.3, False, 2.8, "Iris-virginica"],
            [10.3, 5.8, True, 7.7, "Iris-virginica"],
        ]

        test_conts = dp._format_types(unformated_conts)

        self.assertEqual(expected_formatted_conts, test_conts)

    def test_loading_datafile(self) -> None:
        """Tests loading in datafile, and checks if the loaded contents is
        the same as the expected contents. Check data structure and integrity
        """
        data_file_path = "datafile.data"

        cols = [
            "sepal_width",
            "sepal_length",
            "petal_width",
            "petal_length",
            "iris_species",
        ]

        expected_conts = [
            [6.4, 8.4, 2.2, 6.8, "Iris-setosa"],
            [5.9, 1.3, 2.3, 8.6, "Iris-setosa"],
            [4.2, 8.1, 8.6, 9.0, "Iris-versicolor"],
            [3.8, 11.6, 4.0, 3.0, "Iris-versicolor"],
            [6.0, 7.3, 12.7, 2.8, "Iris-virginica"],
            [10.3, 5.8, 1.5, 7.7, "Iris-virginica"],
        ]

        expected_df = pd.DataFrame(data=expected_conts, columns=cols)
        expected_types = expected_df.dtypes.values.tolist()

        #
        loaded_conts = dp.read_data_file(data_file_path)
        test_types = loaded_conts.dtypes.values.tolist()

        # checking contents, types, and column names
        self.assertEqual(
            expected_df.values.tolist(), loaded_conts.values.tolist()
        )
        self.assertEqual(expected_types, test_types)
        self.assertEqual(cols, loaded_conts.columns.tolist())

    def test_load_datafile_not_exists(self) -> None:
        """Checks for exceptions if the file does not exists"""
        file_not_exist = "notafile.data"
        self.assertRaises(FileNotFoundError, dp.read_data_file, file_not_exist)

    def test_load_datafile_no_permission(self) -> None:
        """Checks for exceptions if datafile has no permission"""
        no_perm_file = "datafile_no_perm.data"
        self.assertRaises(PermissionError, dp.read_data_file, no_perm_file)

    def test_writing_random_matrix(self) -> None:
        """Writing a matrix into file"""

        # setting input parameters
        n_rows = 10
        n_cols = 10

        # create file
        fname = "test_mat"
        test_path = Path() / f"{fname}.csv"

        # write out matrix
        dp.write_matrix_to_file(n_rows, n_cols, fname)

        # checking if the file exists
        check_file = test_path.is_file()
        self.assertTrue(check_file)

        # removing generated file
        os.remove(str(test_path))

    def test_writing_random_matrix_2(self) -> None:
        """Writing 100 matrices"""

        for idx in range(100):

            # setting input parameters
            n_rows = np.random.randint(1, 100)
            n_cols = np.random.randint(1, 100)

            # create file
            fname = f"test_mat_{idx}"

            test_path = Path() / f"{fname}.csv"

            # write out matrix
            dp.write_matrix_to_file(n_rows, n_cols, fname)

            # checking if the file exists
            check_file = test_path.is_file()
            self.assertTrue(check_file)

            # removing generated file
            os.remove(str(test_path))

    def test_file_exists(self) -> None:
        """Test whether a file exists"""

        # setting input parameters
        n_rows = 10
        n_cols = 10

        # create file
        fname = "file_exists"

        self.assertRaises(
            FileExistsError, dp.write_matrix_to_file, n_rows, n_cols, fname
        )

    @classmethod
    def setUp(cls) -> None:

        # generating file names
        cls.file_exists = "file_exists.csv"
        cls.file_no_permission = "datafile_no_perm.data"
        cls.datafile = "datafile.data"

        # generates an empty file
        with open(cls.file_exists, "w") as f:
            f.write("file exists")

        # generate subset of iris datafile
        with open(cls.datafile, "w") as f:

            # settings seed for controlled randomization
            random.seed(42)

            # generating random data
            species = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
            for species_name in species:

                # generating two random entries
                for _ in range(2):

                    # create random entry array
                    rand_entries = [
                        round(random.random() * 10 + random.randint(0, 3), 1)
                        for _ in range(4)
                    ]

                    # stringify entry array
                    entries_str = ",".join(
                        [str(rand_entry) for rand_entry in rand_entries]
                    )

                    # add species name
                    complete_entry_str = f"{entries_str},{species_name}\n"

                    # store stringified entries
                    f.write(complete_entry_str)

        # create a file with no write permission
        with open(cls.file_no_permission, "w") as f:
            f.write("data")
            os.chmod(cls.file_no_permission, 111)

    @classmethod
    def tearDown(cls) -> None:
        os.remove(cls.file_exists)
        os.remove(cls.datafile)
        os.remove(cls.file_no_permission)


class TestPlotter(unittest.TestCase):
    def test_barplot(self) -> None:
        """Creates a plot and generates a md5 hash. Compares md5 hashes for
        data integrity
        """
        data_file_path = "datafile.data"

        cols = [
            "sepal_width",
            "sepal_length",
            "petal_width",
            "petal_length",
            "iris_species",
        ]

        conts = [
            [6.4, 8.4, 2.2, 6.8, "Iris-setosa"],
            [5.9, 1.3, 2.3, 8.6, "Iris-setosa"],
            [4.2, 8.1, 8.6, 9.0, "Iris-versicolor"],
            [3.8, 11.6, 4.0, 3.0, "Iris-versicolor"],
            [6.0, 7.3, 12.7, 2.8, "Iris-virginica"],
            [10.3, 5.8, 1.5, 7.7, "Iris-virginica"],
        ]

        iris_df = pd.DataFrame(data=conts, columns=cols)

        ax = pl.create_iris_boxplot(iris_df, outname="testplot")
        test_type = str(type(ax))
        expected_type = "<class 'matplotlib.axes._subplots.AxesSubplot'>"

        # hashing generated plot (check for data integrity)
        expected_hash = "1f611fe69e7df7b0c9f2846362ed7e4b"
        test_hash = hashlib.md5("testplot.png".encode("UTF-8")).hexdigest()
        os.remove("testplot.png")

        self.assertEqual(expected_hash, test_hash)
        self.assertEqual(test_type, expected_type)

    def test_non_string_outname(self) -> None:
        """Checks for exceptions if a non-string outname was provided"""
        data_file_path = "datafile.data"

        cols = [
            "sepal_width",
            "sepal_length",
            "petal_width",
            "petal_length",
            "iris_species",
        ]

        conts = [
            [6.4, 8.4, 2.2, 6.8, "Iris-setosa"],
            [5.9, 1.3, 2.3, 8.6, "Iris-setosa"],
            [4.2, 8.1, 8.6, 9.0, "Iris-versicolor"],
            [3.8, 11.6, 4.0, 3.0, "Iris-versicolor"],
            [6.0, 7.3, 12.7, 2.8, "Iris-virginica"],
            [10.3, 5.8, 1.5, 7.7, "Iris-virginica"],
        ]

        iris_df = pd.DataFrame(data=conts, columns=cols)

        self.assertRaises(TypeError, pl.create_iris_boxplot, iris_df, 1)

    def test_non_df_boxplot(self) -> None:
        """Checks for exceptions if a non dataframe is passed"""

        conts = [
            [6.4, 8.4, 2.2, 6.8, "Iris-setosa"],
            [5.9, 1.3, 2.3, 8.6, "Iris-setosa"],
            [4.2, 8.1, 8.6, 9.0, "Iris-versicolor"],
            [3.8, 11.6, 4.0, 3.0, "Iris-versicolor"],
            [6.0, 7.3, 12.7, 2.8, "Iris-virginica"],
            [10.3, 5.8, 1.5, 7.7, "Iris-virginica"],
        ]

        self.assertRaises(TypeError, pl.create_iris_boxplot, conts, "testplot")

    def test_scatter(self) -> None:
        """Creates a plot and generates a md5 hash. Compares md5 hashes for
        data integrity
        """
        data_file_path = "datafile.data"

        cols = [
            "sepal_width",
            "sepal_length",
            "petal_width",
            "petal_length",
            "iris_species",
        ]

        conts = [
            [6.4, 8.4, 2.2, 6.8, "Iris-setosa"],
            [5.9, 1.3, 2.3, 8.6, "Iris-setosa"],
            [4.2, 8.1, 8.6, 9.0, "Iris-versicolor"],
            [3.8, 11.6, 4.0, 3.0, "Iris-versicolor"],
            [6.0, 7.3, 12.7, 2.8, "Iris-virginica"],
            [10.3, 5.8, 1.5, 7.7, "Iris-virginica"],
        ]

        iris_df = pd.DataFrame(data=conts, columns=cols)

        ax = pl.petal_width_v_length_scatter(iris_df, outname="testscatter")
        test_type = str(type(ax))
        expected_type = "<class 'matplotlib.axes._subplots.AxesSubplot'>"

        # hashing generated plot (check for data integrity)
        expected_hash = "a405e5fdced63a0ebec851dfd5a66532"
        test_hash = hashlib.md5("testscatter.png".encode("UTF-8")).hexdigest()
        os.remove("testscatter.png")

        self.assertEqual(expected_hash, test_hash)
        self.assertEqual(expected_type, test_type)

    def test_non_string_name_scatter(self) -> None:
        """Checks for exceptions if a non-string outname was provided"""
        data_file_path = "datafile.data"

        cols = [
            "sepal_width",
            "sepal_length",
            "petal_width",
            "petal_length",
            "iris_species",
        ]

        conts = [
            [6.4, 8.4, 2.2, 6.8, "Iris-setosa"],
            [5.9, 1.3, 2.3, 8.6, "Iris-setosa"],
            [4.2, 8.1, 8.6, 9.0, "Iris-versicolor"],
            [3.8, 11.6, 4.0, 3.0, "Iris-versicolor"],
            [6.0, 7.3, 12.7, 2.8, "Iris-virginica"],
            [10.3, 5.8, 1.5, 7.7, "Iris-virginica"],
        ]

        iris_df = pd.DataFrame(data=conts, columns=cols)

        self.assertRaises(
            TypeError, pl.petal_width_v_length_scatter, iris_df, 1
        )

    def test_non_df_scatter(self) -> None:
        """Checks for exceptions if a non dataframe is passed"""

        conts = [
            [6.4, 8.4, 2.2, 6.8, "Iris-setosa"],
            [5.9, 1.3, 2.3, 8.6, "Iris-setosa"],
            [4.2, 8.1, 8.6, 9.0, "Iris-versicolor"],
            [3.8, 11.6, 4.0, 3.0, "Iris-versicolor"],
            [6.0, 7.3, 12.7, 2.8, "Iris-virginica"],
            [10.3, 5.8, 1.5, 7.7, "Iris-virginica"],
        ]

        self.assertRaises(
            TypeError, pl.petal_width_v_length_scatter, conts, "testscatter"
        )

    def test_merge_plot(self) -> None:
        """Test production of merge plot"""

        cols = [
            "sepal_width",
            "sepal_length",
            "petal_width",
            "petal_length",
            "iris_species",
        ]

        conts = [
            [6.4, 8.4, 2.2, 6.8, "Iris-setosa"],
            [5.9, 1.3, 2.3, 8.6, "Iris-setosa"],
            [4.2, 8.1, 8.6, 9.0, "Iris-versicolor"],
            [3.8, 11.6, 4.0, 3.0, "Iris-versicolor"],
            [6.0, 7.3, 12.7, 2.8, "Iris-virginica"],
            [10.3, 5.8, 1.5, 7.7, "Iris-virginica"],
        ]

        iris_df = pd.DataFrame(data=conts, columns=cols)

        ax = pl.merged_boxplot_and_scatter(iris_df, outname="merged_scatter_and_boxplot")

        # hashing generated plot (check for data integrity)
        expected_hash = "93b4e84d9124109fbf7f5604f6bb9d82"
        test_hash = hashlib.md5("merged_scatter_and_boxplot.png".encode("UTF-8")).hexdigest()
        os.remove("merged_scatter_and_boxplot.png")

        self.assertEqual(expected_hash, test_hash)
