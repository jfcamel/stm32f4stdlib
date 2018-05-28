from conans import ConanFile, CMake, tools


# need to resolve this var as PREFIX in .pc flle
VARNAME_STM32STDPERIPH = "${package_root_path_lib_stm32stdperiph}"


class Stm32f4StdPeriphLibConan(ConanFile):
    name = "stm32f4stdperiph"
    version = "0.6"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "Description of libsm32f4stdperiph"
    settings = { "os": ["Linux", ],
                 "compiler": ["gcc", ],
                 "build_type": ['Debug', 'None', 'Release'],
                 "arch": ["armv7", "armv7hf"]
    }
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = [ "src/*", "cmake/*", "CMakeLists.txt", "*.pc" ]
    #build_policy = "always"

    def build(self):
        tools.replace_prefix_in_pc_file("stm32f4stdperiph.pc", VARNAME_STM32STDPERIPH)

    def package(self):
        self.copy("*.h", dst="include", src="src/CMSIS/core")
        self.copy("*.h", dst="include", src="src/CMSIS/device")
        self.copy("*.h", dst="include", src="src/StdPeriph_Driver/inc")
        self.copy("*.c", dst="src", src="src/CMSIS/core")
        self.copy("*.c", dst="src", src="src/CMSIS/device")
        self.copy("*.c", dst="src", src="src/StdPeriph_Driver/src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*.pc", dst="", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["libstm32f4stdperiph"]
