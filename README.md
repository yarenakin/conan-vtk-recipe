# VTK Conan Recipe

This repository contains a Conan recipe for building and packaging the Visualization Toolkit (VTK), a widely used open-source library for 3D computer graphics, image processing, and visualization.

## Features
- Supports both **static** and **shared** builds.
- Fully compatible with Conan's dependency management system.
- Tested with VTK version **9.4.0**.
- Supports Windows (Visual Studio).

## Prerequisites
- [Conan](https://conan.io/) (version 2.0+ recommended)
- [CMake](https://cmake.org/) (version 3.15 or higher)
- A compatible C++ compiler (e.g., MSVC for Windows)
## My default conan profile:
[settings]
arch=x86_64
build_type=Release
compiler=msvc
compiler.cppstd=17
compiler.runtime=dynamic
compiler.version=194
os=Windows

## Building the Package
To build the VTK package, run this command:
```bash
conan create . --build=missing -s build_type=Release

## Note: Automatic Test Execution with `test_package`

During the `conan create` command, Conan automatically detects and executes the test located in the `test_package` directory after building the package. This mechanism ensures that the package is working as expected.
