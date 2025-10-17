# Coding Assignment Tic Tac Toe Challenge


## Functional Specification

### Overview
* Two players take turns placing X’s and O’s on a 3x3 grid.
* The win condition is the first player to get three across a column, down a row, or on either diagonal.

## User Stories
- As a user, I want to see a welcome message.
- As a user, I want to be offered a chance to learn how to play.
- As a user, I want to input my X/O choices based on number placement.
- As a user, I want to know when I win.

### Functional Requirements:
| Feature ID | Feature Name | Description |
|------------|--------------|-------------|
| **FR-001** | **User Instructions Prompt** | Game asks user if they would like instructions before starting |
| **FR-002** | **Game Board Display** | Creates and displays a 3x3 game grid with comma-separated numbers |
| **FR-003** | **Current Player Move Input** | Gets and validates player moves with auto-start for Player X |
| **FR-004** | **Board Update Mechanism** | Updates game board with player moves in real-time |
| **FR-005** | **Win Condition Detection** | Checks for winning patterns across rows, columns, and diagonals |
| **FR-006** | **Game Exit Functionality** | Allows user to quit game at any time during gameplay | 


## TO DO Features :
* Check for tie game
* Format player inputs, add colors, Red = X Blue = O
* Interactive:  Players can pay against one another online
* Validate Input so cannot make illegal moves
* When player wins, provide a gif
* Play again functionality
* Render to production
* Build database to maintain records
* Create user login

## Run App

`python3 app.py`
