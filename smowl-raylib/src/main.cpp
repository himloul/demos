#include "raylib.h"
#include <string>
#include <vector>
#include <iostream>

// Configuration
const int SCREEN_WIDTH = 800;
const int SCREEN_HEIGHT = 600;
const int FONT_SIZE = 20;
const int MARGIN = 10;
const int INPUT_BOX_HEIGHT = 50;
const Color BG_COLOR = { 24, 24, 24, 255 };       // Dark Gray
const Color INPUT_BG_COLOR = { 40, 40, 40, 255 }; // Slightly Lighter Gray
const Color TEXT_COLOR = RAYWHITE;
const Color ACCENT_COLOR = { 0, 121, 241, 255 };  // Blue

struct Message {
    std::string text;
    bool isUser;
};

int main() {
    // Initialization
    SetConfigFlags(FLAG_WINDOW_RESIZABLE);
    InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, "Smowl - Raylib Chat Client");
    SetTargetFPS(60);

    // State
    std::vector<Message> history;
    history.push_back({"Welcome to Smowl! I am a local AI assistant.", false});
    
    // Input Buffer
    char inputBuffer[256] = { 0 };
    int letterCount = 0;
    
    // Main game loop
    while (!WindowShouldClose()) {
        
        int screenWidth = GetScreenWidth();
        int screenHeight = GetScreenHeight();

        // Update
        // ----------------------------------------------------------------------------------
        // Capture keyboard input
        int key = GetCharPressed();
        while (key > 0) {
            if ((key >= 32) && (key <= 125) && (letterCount < 255)) {
                inputBuffer[letterCount] = (char)key;
                inputBuffer[letterCount+1] = '\0'; // Add null terminator
                letterCount++;
            }
            key = GetCharPressed();
        }

        if (IsKeyPressed(KEY_BACKSPACE)) {
            letterCount--;
            if (letterCount < 0) letterCount = 0;
            inputBuffer[letterCount] = '\0';
        }

        if (IsKeyPressed(KEY_ENTER) && letterCount > 0) {
            // Add user message
            history.push_back({std::string(inputBuffer), true});
            
            // Mock AI Response (Placeholder for Llama.cpp)
            history.push_back({"I heard you say: " + std::string(inputBuffer), false});

            // Clear buffer
            letterCount = 0;
            inputBuffer[0] = '\0';
        }
        // ----------------------------------------------------------------------------------

        // Draw
        // ----------------------------------------------------------------------------------
        BeginDrawing();
            ClearBackground(BG_COLOR);

            // 1. Draw Message History Area
            int historyAreaHeight = screenHeight - INPUT_BOX_HEIGHT - (MARGIN * 2);
            int yOffset = MARGIN;
            
            // Simple rendering starting from the bottom of the history area
            // Ideally, we would calculate total height and handle scrolling
            int currentY = historyAreaHeight; 
            
            for (auto it = history.rbegin(); it != history.rend(); ++it) {
                const char* text = it->text.c_str();
                int textWidth = MeasureText(text, FONT_SIZE);
                
                currentY -= (FONT_SIZE + MARGIN);
                
                // Stop drawing if we go off the top of the screen
                if (currentY < MARGIN) break;

                Color msgColor = it->isUser ? ACCENT_COLOR : TEXT_COLOR;
                const char* prefix = it->isUser ? "You: " : "Bot: ";
                
                DrawText(prefix, MARGIN, currentY, FONT_SIZE, LIGHTGRAY);
                DrawText(text, MARGIN + 60, currentY, FONT_SIZE, msgColor);
            }

            // 2. Draw Input Box
            Rectangle inputBox = { 
                (float)MARGIN, 
                (float)(screenHeight - INPUT_BOX_HEIGHT - MARGIN), 
                (float)(screenWidth - (MARGIN * 2)), 
                (float)INPUT_BOX_HEIGHT 
            };
            
            DrawRectangleRec(inputBox, INPUT_BG_COLOR);
            DrawRectangleLinesEx(inputBox, 1, DARKGRAY);

            // Draw Input Text
            DrawText(inputBuffer, inputBox.x + 10, inputBox.y + 15, FONT_SIZE, TEXT_COLOR);

            // Blinking cursor
            if (((int)GetTime() * 2) % 2 == 0) {
                DrawText("_", inputBox.x + 10 + MeasureText(inputBuffer, FONT_SIZE), inputBox.y + 15, FONT_SIZE, ACCENT_COLOR);
            }

        EndDrawing();
        // ----------------------------------------------------------------------------------
    }

    // De-Initialization
    CloseWindow();

    return 0;
}
