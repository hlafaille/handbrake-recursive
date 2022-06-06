import json
import os
import subprocess
import sys

if __name__ == "__main__":
    # load config file
    with open("config.json") as file:
        config = json.loads(file.read())

    print("Iterating over files in '{0}'".format(config["path"]))

    handbrake_files = []
    handbrake_dirs = []
    handbrake_names = []

    different_extensions = []

    # walk over the directory specified in config path
    for root, dirs, files in os.walk(config["path"]):
        for name in files:
            extension = list(reversed(name.split(".")))[0]

            # test if the files extension is NOT in the blacklist
            if extension not in config["extension_blacklist"]:
                print(os.path.join(root, name))
                handbrake_files.append(os.path.join(root, name))
                handbrake_dirs.append(root)
                handbrake_names.append(name)

                # check if this extension has been recoreded
                if extension not in different_extensions:
                    different_extensions.append(extension)
    print("-----------------")
    print("Found {0} file(s) for transcoding with {1} different extension(s)".format(len(handbrake_files), len(different_extensions)))
    print("y: continue with handbrake transcode")
    print("n: exit")
    print("v: view extensions")
    confirmation = input("> ").lower()

    if "y" in confirmation:
        for element, video in enumerate(handbrake_files):
            new_output = os.path.join(handbrake_dirs[element], handbrake_names[element] + "_transcode.m4v")

            handbrake_cwd = os.path.join(os.getcwd(), "HandBrakeCLI.exe")
            print(handbrake_dirs[element])

            subprocess.call(["HandBrakeCLI.exe",
                              "--preset-import-gui",
                             "--encoder",
                             "nvenc_h264",
                              "-i", "{0}".format(handbrake_names[element]),
                              "-o", "{0}".format(handbrake_names[element] + "_transcode.m4v")], cwd=handbrake_dirs[element])
    elif "v" in confirmation:
        for elem, ext in enumerate(different_extensions):
            print("{0}) .{1}".format(elem, ext.upper()))
    else:
        sys.exit()
