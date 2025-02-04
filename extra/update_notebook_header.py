"""A Script to update notebook for colab compatibility.

This extensions adds a first cell to the notebook with the necessary
dependencies to run the notebook.
"""

import os
import json
from pathlib import Path
from copy import deepcopy
import argparse
import glob
from typing import Any

import nbformat as nbf
from nbformat import NotebookNode


def _arg2path(p:str) -> Path:
    return Path(p).absolute()

if __name__ == "__main__":
    # Get all the notebooks in the src directory
    parser = argparse.ArgumentParser()
    parser.add_argument("header_notebook", type=_arg2path, default=Path(__file__).parent() / "header_colab.ipynb")
    parser.add_argument("notebook_dir", type=_arg2path, default=Path(__file__).parent() / 'src')

    args = parser.parse_args()
    os.chdir(args.notebook_dir)


    header_nbk = nbf.read(args.header_notebook, as_version=4)
    for notebook_file in glob.glob("*.ipynb"):
        nbk = nbf.read(notebook_file)
        nbk.cells = [nbk.cells[0], *header_nbk.cells, *nbk.cells[1:]]

        nbf.write(nbk, notebook_file)

    # in the CI pipeline, these new notebook will be uploaded to a new branch
