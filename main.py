from browser import document

def run_python(event):
    document["output"].text = "Hello! Your Python script is running from GitHub."

document["run-btn"].bind("click", run_python)