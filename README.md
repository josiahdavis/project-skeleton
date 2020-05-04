# Project Skeleton
Minimalistic project structure.

## Usage

```
# Clone
git clone https://github.com/josiahdavis/project-skeleton.git
cd project-skeleton

# Set up local python environment
conda create -n py37 python=3.7

# Activate environment
source activate py37

# Install the relevant packages
pip install -r requirements.txt

# Install
pip install -e .

# ....
# Make some changes
# ....

# Run tox
tox -e pydocstyle
tox -e flake8
tox -e docs

# Deactivate environment
source deactivate
```

## References

- [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/)
