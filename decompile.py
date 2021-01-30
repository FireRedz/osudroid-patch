import subprocess, os
from pathlib import Path
from patches import ip


def decompile_apk(apk: str):
    if not os.path.isfile(apk) or not apk.endswith('.apk'):
        raise Exception("Not an APK file.")

    apkDir = Path(Path(apk).stem)

    if apkDir.exists():
        return print("Already decompiled")


    p = subprocess.Popen(f'java -jar tools/apktool.jar d {apk}', stderr=subprocess.STDOUT)
    p.wait()

def build_apk(directory: str):
    # build and sign
    t = subprocess.Popen(f'java -jar tools/apktool.jar b {directory} --output build.apk')
    t.wait()
    t = subprocess.Popen(f'java -jar tools/signer.jar -a build.apk --out build')
    t.wait()

    # delete unsigned build.apk
    os.remove('build.apk')



if __name__ == '__main__':
    decompile_apk('droid.apk')
    ip.patch('droid', "YOURDOMAINHERE.fuck") # must have http at the front