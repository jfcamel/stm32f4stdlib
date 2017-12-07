STM32F4StdPeriph
================

A StandardPeriph library that is provided with conan build tool.


How to build
============


prepare work directory
```
$ mkdir build && cd build
```

prepare depedencies
```
$ conan install ..
or 
$ conan install -s arch='armv7' ..
```

build
```
$ conan build ..
```

if you need to cache to your local conan cache,
```
at project root
$ conan export ${user}/${channel}
```

```
conan install stm32f4stdperiph/0.4@jfcamel/canary -s arch='armv7' --build stm32f4stdperiph
```