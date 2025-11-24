Project Statement: Command-Line Arithmetic Utility
 

Problem Statement
Modern computing environments often rely on complex tools and graphical interfaces for calculation, which can be inefficient or inaccessible in minimalist contexts like remote terminal sessions, embedded systems, or automated scripting workflows. The fundamental problem addressed is the lack of a lightweight, highly reliable, and quick-to-use command-line utility specifically engineered to perform the four basic arithmetic operations with maximum efficiency, robust input validation, and clear, non-ambiguous error reporting. This project fills the gap between full-featured calculator applications and the quick, simple mathematical needs of technical users.


Scope of the Project
The scope is rigorously confined to developing a standalone Python script that provides a command-line interface (CLI) offering:
1.	User Interaction: A loop able, menu-driven experience for operation selection.
2.	Core Functionality: Accurate execution of addition, subtraction, multiplication, and division.
3.	Robustness: Essential error handling for non-numeric input and the specific mathematical singularity of division by zero. The solution will not include advanced functions (e.g., exponents, trigonometry, graphing) or persistent storage/memory features.

Target Users
•	Developers & System Administrators: Who require rapid calculations directly within the terminal during coding or system monitoring.
•	Computer Science Students: Learning fundamental modular programming, input validation, and exception handling principles.
•	Minimalist Users: Individuals who prefer fast, text-based tools over graphical interfaces for basic mathematics.

High-Level Features
1.	Operation Selector: An interactive, numbered menu allowing the user to choose one of the four arithmetic functions or exit.
2.	Input Integrity: A dedicated input module that continuously prompts the user until a valid numeric value is provided.
3.	Arithmetic Engine: Functions dedicated to precise calculation of two float-type operands.
4.	Zero-Division Guard: A specific check within the division function to prevent runtime crashes and return a user-friendly error message.

