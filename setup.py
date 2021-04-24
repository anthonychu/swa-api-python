from setuptools import setup

setup(name='swa_api',
      version='0.1',
      description='SWA API',
      url='http://github.com/anthonychu/swa-api-python',
      author='Anthony',
      author_email='antchu@microsoft.com',
      license='MIT',
      install_requires='azure-cosmos',
      packages=['swa_api'],
      zip_safe=False)