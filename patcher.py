from argparse import ArgumentParser
from os import chdir as cd
from os import system as exec, listdir
from os.path import exists, isfile, join
from shutil import rmtree
from sys import exit

ignored_dirs = [
    "SlivaCore-API",
    "SlivaCore-Server",
    "Bukkit",
    "CraftBukkit"
]


def apply_patches(what: str, target: str, branch: str):
    exec(f"git clone {what} {target}")

    cd(target)

    print(f"Resetting {target} to {what}")

    exec("git config commit.gpgSign false")
    exec("git remote rm origin")
    exec(f"git remote add origin ../{what}")
    exec("git checkout master")
    exec("git fetch origin")
    exec(f"git reset --hard {branch}")

    print(f"Applying patches to {target}")

    exec("git am --abort")

    patches_dir = f"../{what}-Patches"

    patches = [f for f in listdir(patches_dir) if isfile(join(patches_dir, f))]

    for patch in patches:
        exec(f"git am --3way {patches_dir}/{patch}")

    cd("..")


parser = ArgumentParser(prog="SlivaCore build system",
                        description="Patcher for SlivaCore bukkit fork",
                        usage="patcher <applyPatches/rebuildPatches/clean/build>")

parser.add_argument('action', help="Action to work with")

args = parser.parse_args()

action: str = args.action.lower()

match action:
    case "applypatches":
        if not exists("Bukkit") or not exists("CraftBukkit"):
            print("Downloading Bukkit and CraftBukkit submodules...")
            exec("git submodule add -f https://hub.spigotmc.org/stash/scm/spigot/bukkit.git Bukkit")
            exec("git submodule add -f https://hub.spigotmc.org/stash/scm/spigot/craftbukkit.git CraftBukkit")
            exec("git submodule update --init")
            apply_patches("Bukkit", "SlivaCore-API", "origin/master")
            apply_patches("CraftBukkit", "SlivaCore-Server", "origin/master")
        else:
            print(f"There is already a project")
            print(f"Use clean to remove directories")

    case "rebuildpatches":
        exec("./rebuildPatches.sh")
    case "clean":
        for i in ignored_dirs:
            if exists(i):
                rmtree(i)
    case "build":
        if exists("Spigot-API") and exists("Spigot-Server"):
            exec("mvn clean package")
        else:
            print("Firstly you should applyPatches")
            exit(1)
