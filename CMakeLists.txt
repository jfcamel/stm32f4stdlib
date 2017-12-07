project(STM32F4STDLIB C)
cmake_minimum_required(VERSION 2.8)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/bin)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_RELEASE ${CMAKE_CURRENT_BINARY_DIR}/bin)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_DEBUG ${CMAKE_CURRENT_BINARY_DIR}/bin)

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/lib)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY_RELEASE ${CMAKE_ARCHIVE_OUTPUT_DIRECTORY})
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY_DEBUG ${CMAKE_ARCHIVE_OUTPUT_DIRECTORY})

include(${CMAKE_SOURCE_DIR}/cmake/toolchain.cmake)

include_directories(
  ${CMAKE_CURRENT_SOURCE_DIR}/src/CMSIS/core
  ${CMAKE_CURRENT_SOURCE_DIR}/src/CMSIS/device
  ${CMAKE_CURRENT_SOURCE_DIR}/src/StdPeriph_Driver/inc
)

set(STM32F4STDLIB_SRC
  src/StdPeriph_Driver/src/misc.c
  src/StdPeriph_Driver/src/stm32f4xx_adc.c
  src/StdPeriph_Driver/src/stm32f4xx_can.c
  src/StdPeriph_Driver/src/stm32f4xx_crc.c
  src/StdPeriph_Driver/src/stm32f4xx_cryp.c
  src/StdPeriph_Driver/src/stm32f4xx_cryp_aes.c
  src/StdPeriph_Driver/src/stm32f4xx_cryp_des.c
  src/StdPeriph_Driver/src/stm32f4xx_cryp_tdes.c
  src/StdPeriph_Driver/src/stm32f4xx_dac.c
  src/StdPeriph_Driver/src/stm32f4xx_dbgmcu.c
  src/StdPeriph_Driver/src/stm32f4xx_dcmi.c
  src/StdPeriph_Driver/src/stm32f4xx_dfsdm.c
  src/StdPeriph_Driver/src/stm32f4xx_dma.c
  src/StdPeriph_Driver/src/stm32f4xx_dma2d.c
  src/StdPeriph_Driver/src/stm32f4xx_dsi.c
  src/StdPeriph_Driver/src/stm32f4xx_exti.c
  src/StdPeriph_Driver/src/stm32f4xx_flash.c
  src/StdPeriph_Driver/src/stm32f4xx_flash_ramfunc.c
  src/StdPeriph_Driver/src/stm32f4xx_gpio.c
  src/StdPeriph_Driver/src/stm32f4xx_hash.c
  src/StdPeriph_Driver/src/stm32f4xx_hash_md5.c
  src/StdPeriph_Driver/src/stm32f4xx_hash_sha1.c
  src/StdPeriph_Driver/src/stm32f4xx_i2c.c
  src/StdPeriph_Driver/src/stm32f4xx_iwdg.c
  src/StdPeriph_Driver/src/stm32f4xx_lptim.c
  src/StdPeriph_Driver/src/stm32f4xx_ltdc.c
  src/StdPeriph_Driver/src/stm32f4xx_pwr.c
  src/StdPeriph_Driver/src/stm32f4xx_rcc.c
  src/StdPeriph_Driver/src/stm32f4xx_rng.c
  src/StdPeriph_Driver/src/stm32f4xx_rtc.c
  src/StdPeriph_Driver/src/stm32f4xx_sai.c
  src/StdPeriph_Driver/src/stm32f4xx_sdio.c
  src/StdPeriph_Driver/src/stm32f4xx_spi.c
  src/StdPeriph_Driver/src/stm32f4xx_syscfg.c
  src/StdPeriph_Driver/src/stm32f4xx_tim.c
  src/StdPeriph_Driver/src/stm32f4xx_usart.c
  src/StdPeriph_Driver/src/stm32f4xx_wwdg.c
)

add_definitions(-DSTM32F411xE
                -DUSE_STDPERIPH_DRIVER)
add_library(stm32f4stdperiph ${STM32F4STDLIB_SRC})
