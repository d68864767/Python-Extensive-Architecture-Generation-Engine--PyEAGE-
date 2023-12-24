# config.py

# Import necessary libraries
from pathlib import Path

# Define the base directory for the project
BASE_DIR = Path(__file__).resolve().parent

# Define the directory for the templates
TEMPLATE_DIR = BASE_DIR / 'templates'

# Define the default template file
DEFAULT_TEMPLATE = TEMPLATE_DIR / 'default_template.py'

# Define the output directory for the generated project structure
OUTPUT_DIR = BASE_DIR / 'output'

# Define the AI model parameters
AI_MODEL_PARAMS = {
    'tensorflow_version': '2.4.1',
    'scikit_learn_version': '0.24.1'
}

# Define the file and directory handling parameters
FILE_DIR_PARAMS = {
    'pathlib_version': '1.0.1'
}

# Define the command line interface parameters
CLI_PARAMS = {
    'click_version': '7.1.2'
}

# Define the version control parameters
VC_PARAMS = {
    'GitPython_version': '3.1.14'
}

# Define the documentation parameters
DOC_PARAMS = {
    'sphinx_version': '3.5.3'
}

# Define the testing parameters
TEST_PARAMS = {
    'pytest_version': '6.2.2'
}
