Simple Command-Line Calculator
Overview of the Project
This project is a functional, command-line interface (CLI) calculator application built using Python. It allows users to perform the four fundamental arithmetic operations: addition, subtraction, multiplication, and division. The application is designed with modularity, clear user interaction, and robust input validation to ensure reliability.
Features
•	Basic Arithmetic: Supports Addition (+), Subtraction (-), Multiplication (*), and Division (/).
•	Input Validation: Automatically handles invalid (non-numeric) input by prompting the user to re-enter a valid number.
•	Division by Zero Handling: Explicitly catches and reports a "Division by Zero" error instead of crashing.
•	Modular Design: Each arithmetic operation is encapsulated in its own function.
•	User Menu: A clear, interactive menu guides the user through operation selection.
Technologies/Tools Used
•	Programming Language: Python 3 (Tested with Python 3.8+)
•	Version Control: Git
Steps to Install & Run the Project
1.	Clone the Repository:
2.	git clone [https://github.com/VITyarthi-Students/YourRepoName.git](https://github.com/VITyarthi-Students/YourRepoName.git)
3.	cd YourRepoName
(Replace YourRepoName with your actual repository path.)
4.	Run the Calculator: Since this is a single Python script with no external dependencies, you can run it directly:
5.	python calculator.py
Instructions for Testing
The application can be tested manually by interacting with the command-line interface:
Test Case	Steps	Expected Result
Addition	Select '1', enter 10 and 5	Output: 15.0
Division	Select '4', enter 10 and 3	Output: 3.3333 (or similar float)
Invalid Input	Select '1', enter ten as the first number	Prompt: "The number is not valid; Try another one"
Divide by Zero	Select '4', enter 10 and 0	Output: Error: Zero can't be divide-Error
Exit	Select '5'	Program terminates with a farewell message.

