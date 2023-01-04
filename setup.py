from setuptools import setup

setup(
    name="expando",
    version="0.5.5",
    py_modules=["expando","xo"],
    install_requires=[],
    author="Tami",
    author_email="fire17@gmail.com",
    description="Use expando like a dictionary or an object",
    long_description="Dynamically create attributes on the fly. Use expando like a dictionary or an object.",
    long_description_content_type="text/markdown",
    url="https://github.com/fire17/expando",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "xo = xo:main",
            "expando = xo:main"
        ]
    }
)
