from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.files import get

class VTKRecipe(ConanFile):
    """
        This Conan recipe is used to build and package the Visualization Toolkit (VTK),
        an open-source software system for 3D computer graphics, image processing, and visualization.
    """
    name = "vtk-desktop"
    version = "9.4.0"
    license = "BSD license"
    author = "Yaren Akin "
    url = "https://github.com/yarenakin/conan-vtk-recipe"
    description = "The Visualization Toolkit (VTK) is an open-source toolkit for 3D computer graphics, image processing, and visualization."
    topics = ("3D", "visualization", "graphics")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.cache_variables["BUILD_SHARED_LIBS"] = self.options.shared # shared=True: Build dynamic libraries. shared=False: Build static libraries.
        tc.generate()

    def source(self):
        """
        Download the VTK source code. The URL points to the official VTK
        repository on vtk.org. The source is stripped of unnecessary root folders.
        """
        get(self, url="https://www.vtk.org/files/release/9.4/VTK-9.4.0.tar.gz", strip_root=True)

    def build(self):
        """
        Configure and build VTK using CMake. The configuration files generated
        in the `generate` step are used here.
        """
        cmake = CMake(self)
        cmake.configure() #Run the CMake configuration
        cmake.build()   #Run the CMake build

    def package(self):
        """
        Package the built VTK libraries, headers, and other resources into a
        distributable Conan package.
        """
        cmake = CMake(self)
        cmake.install() # Install the build artifacts into the package folder

    def package_info(self):
        """
        Provide information about the packaged VTK library to consumers.
        This includes the location of CMake configuration files.
        """
         # Extract the major and minor version (e.g., 9.4) from the full version (e.g., 9.4.0)
        two_digit_version = self.version[:-2]
        # Specify the directory containing VTK CMake configuration files
        self.cpp_info.builddirs = [f"lib/cmake/vtk-{two_digit_version}"]
