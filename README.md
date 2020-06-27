# Shuttle Bus Educational Tool

## About the Shuttle Bus Educational Tool
This is a project to create a tool that teaches entry level students (Year 7 - 9) the basics of procedural programming thorugh manipulating a shuttle bus around a map by giving it directions. It uses a basic programming language to read the user's commands and intereperet them to commands for the bus. The tool teaches kids the very basics of how to use procedures and for loops.

## Installation and Dependencies
Click Clone and Download ZIP. Then extract the zipped file, write the program for the bus in "Instructions.txt" (or another allocated .txt file) and run "run.py".

The "Shuttle Bus Educational Tool" runs using Python and is heavily dependent on pygame. Users should have both python and pygame installed.

- To install python please visit https://www.python.org/, locate the latest version for your operating system and follow the installation instructions. If running on Windows make sure you add the python installation to PATH (tick box in the first screen of the installer). Also make sure pip is installed for all instillations. Adding the installation to PATH and making sure pip is installed will help make it easy to install pygame later.

- To install pygame open terminal (for windows CMD and make sure you run it as an administrator) and run `py pip install pygame`.
  >https://www.pygame.org/

## Program Syntax
Currently the "Shuttle Bus Educational Tool" uses Java-style syntax, requiring users to use braces `{` to define functions and for loops and semicolons `;` to end lines.

### Basic Shuttle Bus Commands
`forward(distance)` - Move the bus forward `distance` spaces.  
`reverse(distance)` - Move the bus backwards `distance` spaces.  
`left(angle)` - Turn the bus on the spot `angle` degrees anticlockwise (`angle` must be a multiple of 90).  
`right(angle)` - Turn the bus on the spot `angle` degrees clockwise (`angle` must be a multiple of 90).


> #### Example:
> ```
> forward(4);  
> left(90);  
> forward(2);  
> right (180);  
> reverse(1);
> ```
> This program would make the bus go forwards 4 spaces, turn left 90°, go forward 2 spaces, turn right 180° (or turn around) and reverse 1 space.

### Functions
Functions are defined using the `function` keyword. This must be followed by the name of the function, some empty parentheis and a open brace: `function exampleFunction() {`. The definition of this function will continue until there is a matching closing brace `}` found. Everytime a function is called within the program it wil run the contents of the function. The "Shuttle Bus Educational Tool" does not currently include variables so paramerters cannot currently be passed into functions. Currently the opening brace for a function must be on the same line as the `function` keyword.

> #### Example:
> ```
> function square() {
>     forward(2);
>     right(90);
>     forward(2);
>     right(90);
>     forward(2);
>     right(90);
>     forward(2);
> }
>
> square();
> right(90);
> square();
> ```
> This program would make the bus go in a sqaure around the block twice.

### Loops
Loops are defined using the `for` keyword This must be followed by parenthesis containing the number of times the code contents of the function should loop for and an open brace: `for(3) {`. The definition of this loop will continue until there is a matching closing brace `}` found. Currently the opening brace for a for loop must be on the same line as the `for` keyword.


> #### Example:
> ```
> for(3) {
>     forward(2);
>     right(90);
> }
>
> forward(2);
> ```
> This program would make the bus go in a sqaure around the block.


For a full example see the Instructions.txt file.

## Bugs and Feature Requests
If you find a bug please register it by creating an issue in the github repository (https://github.com/drlim2u/Shuttle-Bus-Educational-Tool/issues). Any bugs found and reported would be much appreciated.

If you have a feature request please also create an issue using the link above.

## Credits

David Lim - Project Creator  
Michael Allen - Programmer and Artist

## License
The included license must be included in all copies or substantial portions of the Software.
