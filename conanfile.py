from conans import ConanFile, CMake


class Stm32f4stdlibConan(ConanFile):
    name = "stm32f4stdlib"
    version = "0.2"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "Description of Stm32f4stdlib"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = [ "src/*", "cmake/*" ]
    #build_policy = "always"

    def build(self):
        cmake = CMake(self)
        self.run('cmake %s/src %s' % (self.source_folder, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="src/CMSIS/core")
        self.copy("*.h", dst="include", src="src/CMSIS/device")
        self.copy("*.h", dst="include", src="src/StdPeriph_Driver/inc")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["stm32f4stdlib"]
