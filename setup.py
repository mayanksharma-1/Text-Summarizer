import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

version = "0.0.1"
REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "mayanksharma-1"
AUTHOR_EMAIL = "as.mayanksharma@gmail.com"
srcRepo = "text_summarizer"

setuptools.setup(
    name=srcRepo,
    version=version,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for text summarization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
