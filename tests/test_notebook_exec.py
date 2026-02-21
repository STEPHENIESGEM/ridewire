import os
import nbformat
from nbclient import NotebookClient


def test_execute_main_notebook(tmp_path):
    nb_path = os.path.join("notebooks", "[FINAL]_RideWire-Business-Dashboard.ipynb")
    assert os.path.exists(nb_path), f"Notebook not found: {nb_path}"
    nb = nbformat.read(nb_path, as_version=4)
    client = NotebookClient(nb, timeout=300, kernel_name="python3")
    client.execute()
    out = tmp_path / "executed.ipynb"
    nbformat.write(nb, out)
    assert out.exists()
