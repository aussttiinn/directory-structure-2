import setuptools

with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()

setuptools.setup(
    name='directory-structure-cli',
    version='1.0',
    description='A fork to print a directory tree structure in your Python code.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/aussttiinn/directory-structure-cli',
    author='Gabriel Stork, aussttiinn',
    author_email='storkdeveloper@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords='directory structure tree emoji folder file',
    packages=setuptools.find_packages(),
    install_requires=['emoji', 'click', 'pyperclip'], 
    python_requires='>=3',
    entry_points={
        'console_scripts': [
            'dstree=directory_structure_cli.tree:cli',
        ],
    },
)
