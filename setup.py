from setuptools import find_packages, setup

setup(
    name='questiongenrator',
    version='0.0.1',
    author='Ashish Gajbhiye',
    author_email='ashish.gajbhiye@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)