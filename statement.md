Problem Statement:
  In financial markets, investors frequently buy and sell stocks but often struggle to accurately determine whether their transactions result in a profit, loss, or break-even due to
manual miscalculations, absence of proper record-keeping, and lack of transparency in cost factors such as brokerage charges. This leads to incorrect decision-making and difficulty
in tracking past transactions over time. Therefore, there is a need for a simple, user-friendly, and reliable system that can automate the calculation of total cost, total returns, 
profit or loss amount, percentage change, and break-even price while also maintaining a history of transactions for future reference. The proposed Stock Profit/Loss Calculator 
application addresses this problem by providing an interactive software solution that performs accurate calculations, validates user inputs, stores transaction records, and assists 
users in evaluating their stock performance efficiently and error-free.

Scope of the Project:
  The scope of this project includes designing and developing a menu-driven Stock Profit/Loss Calculator application that enables users to 
perform accurate financial computations for stock transactions by accepting inputs such as buy price, sell price, quantity, and optional 
brokerage charges, and generating results including total cost, total value, profit or loss amount, percentage change, and break-even price. 
The system also allows users to store each completed transaction automatically in a CSV file and retrieve the saved history for review, 
ensuring basic data persistence without requiring a database. The application is limited to single-transaction processing per calculation and 
does not support bulk uploads, real-time market integration, or multi-user authentication. The scope further covers implementation of 
validation for numeric inputs, basic logging for activity tracking, and a structured modular design using classes and utility functions.

Target users :
  The Stock Profit/Loss Calculator application is primarily designed for beginner-level investors, students, and individuals who need a simple 
and reliable tool to understand and evaluate stock transaction outcomes without using complex financial software. It is especially useful for 
academic learners studying programming or finance, as it provides a practical way to analyze profit and loss while reinforcing computational 
logic and input handling. Small-scale traders who manually track their transactions can also benefit from the system’s ability to calculate 
results quickly and store basic history for reference. 

High Level Features :
  The project provides a menu-driven stock calculation system that allows users to compute profit or loss based on buy price, sell price, 
quantity, and optional brokerage charges. It includes an automated result summary that displays total cost, total value, percentage change, 
and break-even price to help users clearly understand the outcome of their transaction. The application supports persistent storage by saving
each transaction into a CSV file, enabling users to maintain a simple historical record without requiring a database. It offers a built-in 
option to view all previously saved transactions directly from the program, making history tracking quick and accessible. The code ensures safe 
and error-free execution through input validation, preventing invalid or negative values from being entered. Additionally, logging is implemented to 
monitor important events such as successful saves and application activity, contributing to better maintainability and debugging.
