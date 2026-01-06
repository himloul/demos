# Smowl - Native Raylib Client

A lightweight, native UI for the Smowl chatbot, built with C++ and Raylib.
This version uses a **local installation** of Raylib for faster builds and full offline support.

## Prerequisites

1.  **Raylib**: Installed at `C:/raylib` (or update `CMakeLists.txt` with your path).
2.  **C++ Compiler**: MinGW (via MSYS2) or MSVC.
3.  **Build Tools**:
    *   **CMake**: Windows version (Kitware).
    *   **Ninja**: Recommended for fast builds (via `winget install Ninja-build.Ninja`).

## How to Build (Windows)

We use **Ninja** and **CMake** for the most robust build process on Windows.

1.  **Navigate to the project directory:**
    ```powershell
    cd smowl-raylib
    ```

2.  **Configure the project:**
    *   *Using Ninja (Recommended):*
        ```powershell
        cmake -G "Ninja" -B build -S .
        ```
    *   *Note:* If Ninja is not in your PATH, you may need to provide the full path to it.

3.  **Build the executable:**
    ```powershell
    cmake --build build
    ```

4.  **Run the application:**
    ```powershell
    .\build\smowl-raylib.exe
    ```

## Project Structure

*   `src/main.cpp`: Main application entry point and UI logic.
*   `CMakeLists.txt`: Build configuration (links against `C:/raylib`).

## Development Status

- [x] **UI Prototype:** Basic chat interface with input history and scrolling.
- [ ] **Llama.cpp Integration:** Pending. Currently uses a mock response.
