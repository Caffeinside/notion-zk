from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='notion-zk',
    version='0.1.0',
    description='Notion helper for my Zettelkasten',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='BASA',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(),
    install_requires=['inquirer==2.9.1',
                      'md2notion==2.4.1',
                      'python-dotenv==0.19.2'],
    # Also need to pip install git+https://github.com/jamalex/notion-py.git@refs/pull/294/merge (master broken)
    entry_points={'console_scripts': ['nzk=notion_zk.__main__:main']},
)
