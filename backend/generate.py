# generate.py 스크립트를 작성합니다. 이 스크립트는 지정된 앱 구조에 따라 Django 앱 폴더와 기본 파일들을 생성합니다.

import os
app_structure = {
    "users": ["__init__.py", "models.py", "views.py", "serializers.py", "urls.py", "tests.py"],
    "stores": ["__init__.py", "models.py", "views.py", "serializers.py", "urls.py", "tests.py"],
    "attendance": ["__init__.py", "models.py", "views.py", "serializers.py", "urls.py", "tests.py"],
    "orders": ["__init__.py", "models.py", "views.py", "serializers.py", "urls.py", "tests.py"],
    "room_assignments": ["__init__.py", "models.py", "views.py", "serializers.py", "urls.py", "tests.py"],
    "reports": ["__init__.py", "views.py", "urls.py", "tests.py"],
    "core": ["__init__.py", "models.py", "utils.py", "tests.py"]
}
# 파일 생성 스크립트


def create_files(app_name, files):
    os.makedirs(app_name, exist_ok=True)
    for file in files:
        with open(os.path.join(app_name, file), 'w') as f:
            if file == "models.py":
                f.write(
                    "from django.db import models\n\n# Create your models here.\n")
            else:
                f.write("# Create your " + file + " here.\n")


# 앱과 파일 생성

for app, files in app_structure.items():
    create_files(app, files)

"프로젝트 구조가 생성되었습니다."
