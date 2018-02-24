set -x
set -e

build_folder=build/android/x86_64/

rm -rf $build_folder
mkdir -p $build_folder
conan install . --profile android-x86_64 --install-folder $build_folder --build missing
conan build . --build-folder $build_folder
