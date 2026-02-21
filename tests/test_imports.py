import importlib

modules = [
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
    "dotenv",
    "yaml",
    "pydantic",
]


def test_import_core_modules():
    missing = []
    for m in modules:
        try:
            importlib.import_module(m)
        except Exception as e:
            missing.append((m, str(e)))
    assert not missing, f"Missing or failing imports: {missing}"
