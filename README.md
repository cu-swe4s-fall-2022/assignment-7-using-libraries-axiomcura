# DataProc

`DataProc` is a simple program that takes in data from the iris dataset.

It generates 3 plots:
- **iris box plots**: compares sepal width and length across all flower species.
- **petal_width_v_length_scatter**: Creates a scatter plot that compares sepal width across all flower species.
- **merged_boxplot_and_scatter**: Creates a plot that merges the first two plots

## Release v0.1

We are happy to annouce the first release of `DataProc`! 🙌.
- Contains a `plotter.py` function that takes in iris.data files and generates High res plots
- Contains a rigorous testing module that checks for data structures and types
- Arguments required to use this program is simple!

## Installation

### Installation

`DataProc` is installed by using conda package manager system.

If you do not have `conda` installed, please follow these instructions on how to install `conda`:

- [Windows](https://conda.io/projects/conda/en/latest/user-guide/install/windows.html)
- [Linux](https://conda.io/projects/conda/en/latest/user-guide/install/linux.html)
- [MacOs](https://conda.io/projects/conda/en/latest/user-guide/install/macos.html)

Once you have `conda` installed, you can now install by follow these simple steps:

Clone the repository into your working directory:

```text
git clone https://github.com/cu-swe4s-fall-2022/assignment-7-using-libraries-axiomcura.git
```

Once the repo is downloaded, go into the directory.

```text
cd assignment-7-using-libraries-axiomcura/
```

Inside the directory, the next step is to downloaded the required dependencies and setup `DataProc` into your `conda` environment.

```text
conda env create -f environment.yaml && conda activate DataProc && pip install -e .
```

After runing the code above, `DataProc` is ready to use!

## Usage

### Documentation

One can access the `DataProc`'s `plotter` documentation by typing:

```text
plotter.py --help
```

And it will return:

```text
usage: plotter.py [-h] -i IRIS_DATA -o OUTNAME

options:
  -h, --help            show this help message and exit
  -i IRIS_DATA, --iris_data IRIS_DATA
                        iris dataset
  -o OUTNAME, --outname OUTNAME
                        outname of the generated files
```

- `iris_data` is the input iris data file

- `outname` is the name of the generated images. For example, if the outname is `pretty_flowres` then the generated outputs will be `pretty_flower`_{plot_type}.png

### Usage Example

Using `DataProc`'s `plotter` script is very simple. The script only requires a user to provide the `iris.data` file and an outname. In the repo directory, type:

```text
plotter.py -i iris.data -o pretty_flowers
```

The output message when complete:

```text
Plotter complete!
```

The generated image files are:

```text
pretty_flowers_boxplot.png
pretty_flowers_merged_box_and_scatter.png
pretty_flowers_scatterplot.png
```

Below are the generated images:

**pretty_flowers_boxplot.png**

![pretty_flowers_boxplot](https://user-images.githubusercontent.com/31600622/197667643-8a32a289-65b7-4c74-a723-9df185156ce3.png)


**pretty_flowers_scatterplot.png**

![pretty_flowers_scatterplot](https://user-images.githubusercontent.com/31600622/197667974-fd710d94-2b63-4a42-8262-789f7e2113c7.png)


**pretty_flowers_merged_box_and_scatter.png**

![pretty_flowers_merged_box_and_scatter](https://user-images.githubusercontent.com/31600622/197667588-8a9c973c-01b8-4415-ab1a-bf4be8f60939.png)
