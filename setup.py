import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="juniperSNMPv3crypt",
    version="0.0.5",
    author="Zach Bray",
    author_email="zachbray123@gmail.com",
    description="Encrypt/decrypts juniper $9$ secrets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zach-bray/junipercrypt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_require='>=2.7'
)
