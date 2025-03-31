# QLIB: An AI-Oriented Quantitative Investment

## Initialization

### Conda Environment

The environment should be built before run the program

```bash
# the name of environment
ENV_NAME="Example"

if conda info --envs | grep -q $ENV_NAME; then
    echo "$ENV_NAME is existing, skipping this process..."
else
    # Creating new conda environment
    echo "Creating new conda environment $ENV_NAME..."
    conda create -n $ENV_NAME python=3.12
fi
```

```bash
# activate
eval "$(conda shell.bash hook)"
conda activate $ENV_NAME
```

```bash
# check if the current env. isn't $ENV_NAME
if [[ $CONDA_DEFAULT_ENV != $ENV_NAME ]]; then
    echo "The current env. isn't $ENV_NAME, $ENV_NAME is now activating..."
    conda activate $ENV_NAME
fi
```

```bash
# check the path of pip
HOME_PATH=$(echo ~)
EXPECTED_PIP_PATH="$HOME_PATH/.conda/envs/$ENV_NAME/bin/pip"
CURRENT_PIP_PATH=$(which pip)

if [[ $CURRENT_PIP_PATH != $EXPECTED_PIP_PATH ]]; then
    echo "Setting correct PATH..."
    export PATH="$HOME_PATH/.conda/envs/$ENV_NAME/bin:$PATH"
fi
```

### Python Environment

```bash
pip install pyqlib
pip install numpy
pip install --upgrade cython
```

```bash
# Check if the qlib directory exists
if [ -d ~/qlib ]; then
    echo "The qlib directory already exists. Entering the directory..." && cd ~/qlib
else
    echo "The qlib directory does not exist. Cloning the qlib repository..."
    cd ~ && git clone https://github.com/microsoft/qlib.git && cd qlib
    python setup.py install
fi
```
More Guidance in http://qlib.readthedocs.io/en/latest/start/integration.html