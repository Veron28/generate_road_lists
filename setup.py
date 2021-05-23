import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["os"],
    'include_files': ['excel_generation.py',
                       'from_number_to_address.py',
                      'generateRoads.py',
                      'graph.py',
                      'List_day_generate.py',
                      'probability_distribution.py',
                      'rast.py', 'transaction1.py',
                      ],  # (2)
    'includes': [],
    'zip_include_packages': ['pandas', 'random', 'datetime', 'openpyxl', 'xlrd', 'os',
                             'numpy', 'networkx', 'matplotlib', 'calendar', 'geopy'],  # (1)
    'excludes': [],  # (3)
    "include_msvcr": True,
    "optimize": 2,
}  # зависимости

base = None
if sys.platform == "win32":
    base = "Console"


setup(
        name='Генератор маршрутов',
        version='1.0',
        description="",
        author='<AUTHOR>',
        author_email='<EMAIL>',
        options={"build_exe": build_exe_options},
        executables=[Executable("main.py", base=base,
                     targetName="Генератор маршрутов.exe")]
)