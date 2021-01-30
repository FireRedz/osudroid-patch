import os, re

link_regex = re.compile('".*?"')
patch_1 = 'smali/ru/nsu/ccfit/zuev/osu/online/OnlineManager.smali'
patch_1_lines = [129, 778, 1042, 1271, 1466, 1671, 1757, 1833]

patch_2 = 'smali/ru/nsu/ccfit/zuev/osu/menu/e.smali'


def patch(directory: 'Path', ip: str):
    realdir = directory
    directory = os.path.join(directory, patch_1)
    with open(directory) as f:
        lines = f.readlines()

    for line in patch_1_lines:
        link = link_regex.findall(lines[line-1])
        curLine = lines[line-1].replace(link[0], f'"http://{ip}"')

        lines[line-1] = curLine


    with open(directory, 'w') as f:
        f.write(''.join(lines))

    patch_avatar(realdir, ip)


def patch_avatar(directory: 'Path', ip: str):
    directory = os.path.join(directory, patch_2)

    with open(directory, 'r') as f:
        lines = f.readlines()
        link = link_regex.findall(lines[28])
        lines[28] = lines[28].replace(link[0], f'"https://{ip}/a/"')

    with open(directory, 'w') as f:
        f.write(''.join(lines))


