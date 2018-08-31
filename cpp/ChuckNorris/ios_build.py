import subprocess
from path import Path

def main():
    for arch in ["armv7", "armv7s","armv8", "x86", "x86_64"]:
        build_sqlite(arch)
        build_chucknorris(arch)


def build_sqlite(arch):
    with Path("../conan/sqlite3/"):
        conan_create(ref="dmerej/test", arch=arch, profile="ios")

def build_chucknorris(arch):
    build_folder = Path("build") / "ios" / arch
    conan_install(profile="ios", arch=arch, install_folder=build_folder)
    conan_build(build_folder=build_folder)
    package_folder = Path("../../ios/bindings/nativelibs/") / arch
    conan_package(build_folder=build_folder, package_folder=package_folder)


def conan_create(*, ref, profile, arch):
    run_conan("create", ".", ref,
        "--profile", profile,
        "--settings", f"arch={arch}"
    )

def conan_install(*, profile, arch, install_folder):
    run_conan("install", ".",
        "--profile", profile,
        "--settings", f"arch={arch}",
        "--install-folder", install_folder
      )

def conan_build(*, build_folder):
    run_conan("build", ".",
        "--build-folder", build_folder)

def conan_package(*, build_folder, package_folder):
    run_conan("package", ".",
        "--build-folder", build_folder,
        "--package-folder", package_folder)

def run_conan(*cmd):
    print("conan", *cmd)
    subprocess.run(["conan"] + list(cmd), check=True)


if __name__ == "__main__":
    main()
