from setuptools import setup, find_packages

setup(
    name='my_clients',
    version='0.0.8',
    author='ChatGPT and Denis Ustinov',
    author_email='revers-06-checkup@icloud.com',
    description='A Python package for working with APIs',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/DenisUstinov/my-clients',
    license='MIT',
    packages=find_packages(),
    install_requires=['websockets', 'backoff', 'aiohttp'],
    python_requires='>=3.11',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: MIT License',
        'Programming Language :: Python :: 3.11'
    ],
)
