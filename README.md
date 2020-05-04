# Project Skeleton
Minimalistic project structure.

## Usage

```
# Clone
git clone https://github.com/josiahdavis/project-skeleton.git
cd project-skeleton

# Set up local python environment
conda create -n py36 python=3.6

# Activate environment
source activate py36

# Install the relevant packages
pip install -r requirements.txt

# Install
pip install -e .


# Run tox
tox -e pydocstyle
tox -e flake8
tox -e docs
```

## References

- [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/)
