import os
import sys

print("Walking uic_files Directory, looking for .ui files to compile...")
print("---------------------------")

try:
    os.mkdir("ui")
except FileExistsError:
    pass

if os.name == "nt":
    uic = os.path.join("pyside6-uic")
else:
    print("Must add support for Linux venv structure")
    sys.exit(1)

# first walk over the main directories, create their folders in the build folder
for root, dirs, files in os.walk("uic_files", topdown=False):
    for name in dirs:
        try:
            os.mkdir(os.path.join("ui", name))
        except FileExistsError:
            pass
        print(os.path.join(root, name))


# now walk over the actual files, compile them
for root, dirs, files in os.walk("uic_files", topdown=False):
    for name in files:
        new_root = root.replace("uic_files", "ui")
        print(os.path.join(new_root, name))
        os.system("{0} -o {1} -g python {2}".format(uic,
                                                           os.path.join(os.getcwd(), new_root, "{0}".format(name.replace(".ui", ".py"))),
                                                           os.path.join(os.getcwd(), root, name)))