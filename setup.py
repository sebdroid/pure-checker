from setuptools import setup, Extension


def main():
    setup(
        name="pure-py",
        version="1.0.4",
        description="A static analysis file format checker.",
        author="Seb",
        author_email="me@sebjo.se",
        ext_modules=[Extension("pure_py", ["pure_py.c"])],
    )


if __name__ == "__main__":
    main()
