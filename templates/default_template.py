```python
# templates/default_template.py

# This is a default template for the PyEAGE project. 
# It provides a basic structure for a Python project, which can be customized as per the user's requirements.

project_structure = {
    "root": {
        "name": "project_name",
        "type": "directory",
        "children": [
            {
                "name": "src",
                "type": "directory",
                "children": [
                    {
                        "name": "main.py",
                        "type": "file",
                        "content": "# main.py\n\n# This is the main entry point of your application."
                    },
                    {
                        "name": "utils.py",
                        "type": "file",
                        "content": "# utils.py\n\n# This file contains utility functions for your application."
                    }
                ]
            },
            {
                "name": "tests",
                "type": "directory",
                "children": [
                    {
                        "name": "test_main.py",
                        "type": "file",
                        "content": "# test_main.py\n\n# This file contains tests for your main application."
                    }
                ]
            },
            {
                "name": "docs",
                "type": "directory",
                "children": []
            },
            {
                "name": "README.md",
                "type": "file",
                "content": "# README.md\n\n# This is the README for your project."
            },
            {
                "name": ".gitignore",
                "type": "file",
                "content": "# .gitignore\n\n# This file specifies intentionally untracked files that Git should ignore."
            },
            {
                "name": "requirements.txt",
                "type": "file",
                "content": "# requirements.txt\n\n# This file lists all of the Python packages that your project depends on."
            },
            {
                "name": "setup.py",
                "type": "file",
                "content": "# setup.py\n\n# This file describes your project and the files that it includes."
            }
        ]
    }
}
```
