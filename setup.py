import re
import os.path
from setuptools import setup, find_packages

_here = os.path.abspath(os.path.dirname(__file__))
requirements_path = os.path.join(_here, 'requirements', 'requirements.txt')
dev_requirements_path = os.path.join(_here, 'requirements', 'dev_requirements.txt')


def get_requirments(path):
    with open(path, 'rt') as f:
        data = f.read()
    return re.findall(r"[A-Za-z][A-Za-z0-9\-\.]+==[0-9\.\-A-Za-z]*", data)


requirements = get_requirments(requirements_path)
dev_requirements = get_requirments(requirements_path)

setup(
    name="plan_your_travel",
    version="0.1",
    install_requires=requirements,
    zip_safe=False,
    packages=find_packages(),
    extras_require={"dev": dev_requirements},
)
