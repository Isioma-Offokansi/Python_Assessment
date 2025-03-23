# Python_Assessment
My summative assessment written in Python with tests for each question.
## Questions Overview

### Question 1: Basic Programming Structure (20 Marks)
- **File**: `question_1.py`
- **Description**: Computes the center of mass of a set of spheres. Each sphere is defined by its center coordinates, radius, and unit mass.
- **Function**: `centreOfMass(spheres)`
- **Tests**: `test_question_1.py`

### Question 2: List Built-in Data Structure (15 Marks)
- **File**: `question_2.py`
- **Description**: Detects collisions between two sets of spheres. A collision occurs if any sphere from one set intersects with a sphere from the other set.
- **Function**: `collide(objectA, objectB)`
- **Tests**: `test_question_2.py`

### Question 3: Recursion (15 Marks)
- **File**: `question_3.py`
- **Description**: Implements a recursive function to generate all possible combinations of letters from a T9 keypad input.
- **Function**: `t9Words(keysPressed)`
- **Tests**: `test_question_3.py`

### Question 4: Python I/O (10 Marks)
- **File**: `question_4.py`
- **Description**: Reads an adjacency matrix of an unweighted digraph from a CSV file and validates its format.
- **Function**: `readAdjacency(filename)`
- **Exception**: `InvalidFileFormatException` (defined in `invalidfileformatexception.py`)
- **Tests**: `test_question_4.py`

### Question 5: User Defined Data Structure (30 Marks)
- **File**: `question_5.py`
- **Description**: Implements a class `Encoding` to encode and decode text using a bespoke binary tree encoding.
  - **Method 1**: `__init__(binary_tree)` - Initializes the encoding tree.
  - **Method 2**: `decodeText(binary_code)` - Decodes a binary string into plain text.
  - **Method 3**: `encodeText(plain_text)` - Encodes plain text into a binary string.
- **Tests**:
  - `test_question_5_i.py`: Tests the constructor.
  - `test_question_5_ii.py`: Tests the `decodeText` method.
  - `test_question_5_iii.py`: Tests the `encodeText` method.

## Data Files
The `data/` folder contains CSV files used for testing `question_4.py`. These files represent adjacency matrices with various formats:
- `validmatrix.csv` and `validmatrix2.csv`: Valid adjacency matrices.
- `blankspace.csv`, `missingvalue.csv`, `invalidvalue.csv`, `toofewrows.csv`, `toomanyrows.csv`: Invalid matrices for testing error handling.

## Development Environment
- **Python Version**: 3.8+
- **IDE**: Visual Studio Code
- **Unit Testing Framework**: `unittest`

### VS Code Configuration
- **Launch Configuration**: `.vscode/launch.json`
- **Testing Configuration**: `.vscode/settings.json`

## How to Run
1. Clone the repository.
2. Navigate to the `ClosedExamination` folder.
3. Run the unit tests for each question where X is the test number:
   ```bash
   python -m unittest test_question_X.py
