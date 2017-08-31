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

include(${CMAKE_SOURCE_DIR}/../cmake/toolchain.cmake)

include_directories(
  ${CMAKE_CURRENT_SOURCE_DIR}/CMSIS/core
  ${CMAKE_CURRENT_SOURCE_DIR}/CMSIS/device
  ${CMAKE_CURRENT_SOURCE_DIR}/StdPeriph_Driver/inc
)

set(STM32F4STDLIB_SRC
  StdPeriph_Driver/src/misc.c
  StdPeriph_Driver/src/stm32f4xx_adc.c
  StdPeriph_Driver/src/stm32f4xx_can.c
  StdPeriph_Driver/src/stm32f4xx_crc.c
  StdPeriph_Driver/src/stm32f4xx_cryp.c
  StdPeriph_Driver/src/stm32f4xx_cryp_aes.c
  StdPeriph_Driver/src/stm32f4xx_cryp_des.c
  StdPeriph_Driver/src/stm32f4xx_cryp_tdes.c
  StdPeriph_Driver/src/stm32f4xx_dac.c
  StdPeriph_Driver/src/stm32f4xx_dbgmcu.c
  StdPeriph_Driver/src/stm32f4xx_dcmi.c
  StdPeriph_Driver/src/stm32f4xx_dfsdm.c
  StdPeriph_Driver/src/stm32f4xx_dma.c
  StdPeriph_Driver/src/stm32f4xx_dma2d.c
  StdPeriph_Driver/src/stm32f4xx_dsi.c
  StdPeriph_Driver/src/stm32f4xx_exti.c
  StdPeriph_Driver/src/stm32f4xx_flash.c
  StdPeriph_Driver/src/stm32f4xx_flash_ramfunc.c
  StdPeriph_Driver/src/stm32f4xx_gpio.c
  StdPeriph_Driver/src/stm32f4xx_hash.c
  StdPeriph_Driver/src/stm32f4xx_hash_md5.c
  StdPeriph_Driver/src/stm32f4xx_hash_sha1.c
  StdPeriph_Driver/src/stm32f4xx_i2c.c
  StdPeriph_Driver/src/stm32f4xx_iwdg.c
  StdPeriph_Driver/src/stm32f4xx_lptim.c
  StdPeriph_Driver/src/stm32f4xx_ltdc.c
  StdPeriph_Driver/src/stm32f4xx_pwr.c
  StdPeriph_Driver/src/stm32f4xx_rcc.c
  StdPeriph_Driver/src/stm32f4xx_rng.c
  StdPeriph_Driver/src/stm32f4xx_rtc.c
  StdPeriph_Driver/src/stm32f4xx_sai.c
  StdPeriph_Driver/src/stm32f4xx_sdio.c
  StdPeriph_Driver/src/stm32f4xx_spi.c
  StdPeriph_Driver/src/stm32f4xx_syscfg.c
  StdPeriph_Driver/src/stm32f4xx_tim.c
  StdPeriph_Driver/src/stm32f4xx_usart.c
  StdPeriph_Driver/src/stm32f4xx_wwdg.c
)

add_definitions(-DSTM32F411xE
                -DUSE_STDPERIPH_DRIVER)
add_library(stm32f4stdlib ${STM32F4STDLIB_SRC})
target_include_directories(stm32f4stdlib PRIVATE
  $<BUILD_INTERFACE:${CMAKE_SOURCE_DIR}>
)

