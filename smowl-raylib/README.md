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

**Option 1: Easy Build Script (Recommended)**
We have included a PowerShell script that automatically finds CMake and Ninja for you.
```powershell
cd smowl-raylib
.\build.ps1
```

**Option 2: Manual Build**
If you have CMake and Ninja in your PATH:
```powershell
cd smowl-raylib
cmake -G "Ninja" -B build -S .
cmake --build build
```

## Project Structure

*   `src/main.cpp`: Main application entry point and UI logic.
*   `CMakeLists.txt`: Build configuration (links against `C:/raylib`).

## Development Status

- [x] **UI Prototype:** Basic chat interface with input history and scrolling.
- [ ] **Llama.cpp Integration:** Pending. Currently uses a mock response.
