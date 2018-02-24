set -x
set -e
conan install . --profile android-x86_64 --install-folder build/android/x86_64/
conan build . --build-folder build/android/x86_64
