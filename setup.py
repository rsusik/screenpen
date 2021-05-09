import io
from setuptools import setup, find_packages

version = {}
exec(open("screenpen/version.py").read(), version)  # pylint: disable=exec-used
print(version)

def get_requirements():
    with open("requirements.txt") as fp:
        return [req for req in (line.strip() for line in fp) if req and not req.startswith("#")]


setup(
    name="screenpen",
    version=version["__version__"],
    author="Robert Susik",
    author_email="robert.susik@gmail.com",
    options={"bdist_wheel": {"universal": True}},    
    license="GPLv3",
    description=(
        "Screen annotation software which allows drawing directly on the screen."
    ),
    long_description=io.open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    install_requires=get_requirements(),
    python_requires=">=3.7",
    entry_points={
        "gui_scripts": [
            "screenpen=screenpen:main",
        ],
    },
    package_dir={"": "."},
    packages = find_packages("."),
    #include_package_data=True, # read from manifest.in
    package_data={
        '': ['utils/*'], 
    },
    url="https://rsusik.github.io/screenpen/",
    classifiers=[
        #"Development Status :: 3 - Alpha ",
        "Environment :: X11 Applications :: Qt",
        "Framework :: Matplotlib",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Topic :: Communications :: Conferencing",
        "Topic :: Education",
        "Topic :: Multimedia :: Graphics :: Capture :: Screen Capture",
        "Topic :: Multimedia :: Graphics :: Presentation",
    ],
)