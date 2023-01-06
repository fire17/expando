from setuptools import setup

setup(
    name="xo.redis",
    version="0.2.5.1",
    py_modules=["xo.redis","xo.xo"],
    install_requires=["expando","redis"],
    author="Tami",
    author_email="fire17@gmail.com",
    description="Use redis db as an object. expando like a dictionary or an object",
    long_description="Dynamically read and write to redis on the fly. Subscriptable, iterable, and more.",
    long_description_content_type="text/markdown",
    url="https://github.com/fire17/xo.redis",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "xo.redis = redis:redis",
        ]
    }
)
