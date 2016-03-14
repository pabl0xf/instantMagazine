from setuptools import setup

setup(name='instantmagazine',
      version='0.1.0',
      packages=['instantmagazine'],
      entry_points={
          'console_scripts': [
              'instantmagazine = instantmagazine.__main__:main'
          ]
      },
      )