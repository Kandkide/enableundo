from setuptools import setup, find_packages

setup(
    name='mpon',
    version='1.00',
    packages=find_packages(include=['mptkone', 'mptkone.*', 'functions', 'functions.*']),
    install_requires=[
        # 'pickle',
        # 'openpyxl',
        # 'pandas>=0.23.3',
        # 'numpy>=1.14.5',
        # 'matplotlib>=2.2.0',
        # 'seaborn'
    ],
    # extras_require={
    #     'mswin': ['pywin32'],
    # }#,
    entry_points={
        'console_scripts': ['mpon=mptkone.mptkgui:tkbuilder']
    }
)
# https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/
# Boilerplate:
#   pip install -e .
#   pip uninstall mpon
#   pip install git+https://github.com/Kandkide/mpon.git
#       Need to set Path to git before hand.
#       (in my environment) "C:\Program Files\Git\bin"
#       In this case,
#       set PATH=%PATH%;C:\Program Files\Git\bin
#       (FYI, to show path variable)
#       echo %path%