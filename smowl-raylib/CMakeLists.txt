cmake_minimum_required(VERSION 3.14)

# Force Windows System
set(CMAKE_SYSTEM_NAME Windows)

project(smowl-raylib)

# --- Local Raylib Configuration ---
# User provided path: C:/raylib
set(RAYLIB_PATH "C:/raylib")

# 1. Include Headers
if(EXISTS "${RAYLIB_PATH}/include/raylib.h")
    include_directories("${RAYLIB_PATH}/include")
    message(STATUS "Found Raylib headers at: ${RAYLIB_PATH}/include")
else()
    message(FATAL_ERROR "Could not find raylib.h in ${RAYLIB_PATH}/include")
endif()

# 2. Link Libraries
link_directories("${RAYLIB_PATH}/lib")

# --- Source Files ---
set(SOURCES
    src/main.cpp
)

# --- Executable ---
add_executable(${PROJECT_NAME} ${SOURCES})

# --- Linking ---
# Link raylib and its required Windows system dependencies manually
# since we are using raw binaries, not a CMake package.
target_link_libraries(${PROJECT_NAME} PRIVATE 
    raylib      # C:/raylib/lib/libraylib.a
    opengl32 
    gdi32 
    winmm 
    shell32
)

# --- Configuration ---
if (WIN32)
    # Hide console window in release builds
    # set_target_properties(${PROJECT_NAME} PROPERTIES WIN32_EXECUTABLE ON)
endif()
