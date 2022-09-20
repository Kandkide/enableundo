from setuptools import setup, find_packages

setup(
    name='enableundo',
    version='1.1.0',
    packages=find_packages(include=['enableundo', 'enableundo.*', 'example', 'example.*']),
    install_requires=[
    ],
    # extras_require={
    #     'mswin': ['pywin32'],
    # }#,
    entry_points={
        'console_scripts': ['undo_example=example.undoredo_example3:main']
    }
)
# https://github.com/Kandkide/enableundo.git
# Boilerplate:
#   pip install git+https://github.com/Kandkide/enableundo.git
#       Need to set Path to git before hand.
#       (in my environment) "C:\Program Files\Git\bin"
#       In this case,
#       set PATH=%PATH%;C:\Program Files\Git\bin
#       (FYI, to show path variable)
#       echo %path%