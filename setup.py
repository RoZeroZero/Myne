from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='myne',
      version='0.1',
      description='modpack loader',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
      ],
      keywords='myne',
      url='http://github.com/RoZeroZero/Myne',
      author='RoZeroZero',
      author_email='',
      license='opensource',
      packages=['myne'],
      install_requires=[
          'tkinter',
      ],
      entry_points={
          'console_scripts': ['myne=myne.modules:main'],
      },
      include_package_data=True,
      zip_safe=False)