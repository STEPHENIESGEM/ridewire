import sys
import nbformat
from nbclient import NotebookClient, CellExecutionError


def run_notebook(path: str) -> int:
    print(f"Executing notebook: {path}")
    nb = nbformat.read(path, as_version=4)
    client = NotebookClient(nb, timeout=300, kernel_name='python3')
    try:
        client.execute()
    except CellExecutionError as e:
        print("Notebook execution failed:", e)
        return 2
    # write executed notebook output next to original for inspection
    out_path = path.replace('.ipynb', '.executed.ipynb')
    nbformat.write(nb, out_path)
    print(f"Notebook executed successfully, output written to {out_path}")
    return 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python ci/run_notebook.py <notebook.ipynb>")
        sys.exit(1)
    nb_path = sys.argv[1]
    sys.exit(run_notebook(nb_path))
