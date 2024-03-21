import os
import shutil


def remove_pycache(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for dir_name in dirs:
            if dir_name == "__pycache__":
                full_path = os.path.join(root, dir_name)
                print(f"Deleting: {full_path}")
                shutil.rmtree(full_path)


if __name__ == "__main__":
    project_dir = "."  # 현재 디렉토리에서 시작. 필요에 따라
    remove_pycache(project_dir)
