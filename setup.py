from setuptools import setup, find_packages


VERSION = '1.26'


setup(name='thefuck',
      version=VERSION,
      description="Magnificent app which corrects your previous console command",
      author='Vladimir Iakovlev',
      author_email='nvbn.rm@gmail.com',
      url='https://github.com/nvbn/thefuck',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples',
                                      'tests', 'release']),
      include_package_data=True,
      zip_safe=False,
      install_requires=['pathlib', 'psutil', 'colorama'],
      entry_points={'console_scripts': [
          'thefuck = thefuck.main:main']})
