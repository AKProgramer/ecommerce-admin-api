import os
import shutil

def clear_pycache():
    for root, dirs, files in os.walk('.', topdown=False):
        for name in dirs:
            if name == '__pycache__':
                shutil.rmtree(os.path.join(root, name))

if __name__ == "__main__":
    clear_pycache()
    print("__pycache__ directories cleared.")
