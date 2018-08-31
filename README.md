# ChuckNorris

This repository contains a library written in `c++` that depends on `sqlite3`

It also contains:

* wrappers for the following languages:
  * `C`
  * `Java`  (with `jna`)
  * `Python3` (with `cffi`)
  * `Swift`

* an Android application
* an iOS application

* and all the scripts you need to build everything without pull your hair out :)

It's used as an example for the [Let's Build Chuck Norris](https://dmerej.info/blog/post/introducing-the-chuck-norris-project/) series on my blog.

# Build instructions

## For Android

* Download ndk
* make standalone toolchains

* Add rust targets
```
rustup target list | grep android
rustup target add ...
```

* Patch ~/.cargo/config

```
[target.armv7-linux-androideabi]
linker = "/home/dmerej/3rdpart/android-arm-api-27-toolchain/bin/arm-linux-androideabi-gcc"

[target.x86_64-linux-android]
linker = "/home/dmerej/3rdpart/android-x86_64-api-27-toolchain/bin/x86_64-linux-android-clang"
```

* Set PATH and build (required for sqlite build

```
  export PATH=$PATH:/home/dmerej/3rdpart/android-arm-api-27-toolchain/bin/
  cargo build --target armv7-linux-androideabi --release

  export PATH=$PATH:/home/dmerej/3rdpart/android-x86_64-api-27-toolchain/bin/
  cargo build --target x86_64-linux-android --release
```

* Symlinks in android are already OK :)
