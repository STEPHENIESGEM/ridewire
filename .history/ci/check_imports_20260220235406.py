import sys

packages = [
    "pandas",
    "numpy",
    "scipy",
    "sklearn",
    "matplotlib",
    "seaborn",
    "plotly",
    "jupyter",
    "requests",
    "aiohttp",
    "sqlalchemy",
    "python_dotenv",
    "yaml",
    "pydantic",
]

failed = []
for pkg in packages:
    try:
        __import__(pkg)
    except Exception as e:
        failed.append((pkg, str(e)))

if failed:
    print("Import check failed for the following packages:")
    for pkg, err in failed:
        print(f" - {pkg}: {err}")
    sys.exit(2)

print("All required packages imported successfully.")
