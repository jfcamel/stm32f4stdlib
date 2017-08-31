SET(CMAKE_SYSTEM_NAME Linux)
SET(CMAKE_SYSTEM_VERSION 1)

SET(CMAKE_C_FLAGS
  "-mcpu=cortex-m4 -mthumb -mfloat-abi=soft -fmessage-length=0 -Os -fsigned-char -fno-move-loop-invariants -g3 -gstrict-dwarf -flto")


SET(CMAKE_C_COMPILER /usr/bin/arm-none-eabi-gcc)
SET(CMAKE_CXX_COMPILER /usr/bin/arm-none-eabi-g++)
SET(CMAKE_FIND_ROOT_PATH /usr/arm-none-eabi/lib/)

# search for programs in the build host directories
SET(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)

# for libraries and headers in the target directories
SET(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
SET(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
