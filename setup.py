from setuptools import setup, find_packages

setup(
    name="antonia-cli",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["aider-chat"],
    entry_points={
        "console_scripts": [
            "antonia=antonia:main",
        ],
    },
    author="Emanuel Diaz",
    description="Antonia CLI - Agente de código IA en memoria de Doña Antonia Rodríguez",
    python_requires=">=3.8",
)