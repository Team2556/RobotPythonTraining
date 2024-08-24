
### **1. Structuring the Shared GitHub Repository**

#### **Repository Layout:**

1. **Root Directory:**
   - **README.md:**  
     - A comprehensive overview of the project, including a brief introduction, instructions on how to get started, and links to key resources (like Python tutorials or RobotPy documentation).
   - **CONTRIBUTING.md:**  
     - Guidelines for contributing to the repository, including coding standards, commit message conventions, and pull request processes.
   - **.gitignore:**  
     - Specify files and directories to be ignored by Git (e.g., build artifacts, virtual environments).

2. **Directory Structure:**

   - **`/docs/`:**  
     - Documentation files (e.g., installation guides, how-to documents, explanation of the code architecture).
     - Consider adding subfolders for `training_materials`, `API_docs`, and `design_docs`.

   - **`/training/`:**
     - **`/basics/`:** Python basics (syntax, loops, functions, etc.)
     - **`/robot_basics/`:** Simple Python examples related to robot control (e.g., motor control, sensor integration).
     - **`/advanced/`:** More complex examples (e.g., autonomous mode routines, vision processing).
     - **`/challenges/`:** Coding challenges and exercises for team members to practice.
     - **`/solutions/`:** Example solutions to the challenges.

   - **`/sandbox/`:**  
     - The main source code directory for the robot's Python code, organized by function. 
     - **Top-Level Directories:**
       - **`commands/`**: Houses command logic that directs subsystems.
       - **`components/`**: Stores smaller, reusable pieces of code that don't belong to a specific subsystem but are used across multiple areas (e.g., custom sensors, utility functions).
       - **`subsystems/`**: Contains the code for each major subsystem of the robot, such as drivetrain, shooter, intake, etc.
       - **`autonomous/`**: Dedicated to autonomous routines and strategies.
       - **`pathplanner/`**: Contains path planning logic, trajectory generation, and related code.
       - **Example Layout:**
         ```
         /sandbox/
         ├── commands/
         │   ├── drive_command.py
         │   ├── shoot_command.py
         │   └── tests/
         ├── components/
         │   ├── custom_sensor.py
         │   └── utils.py
         ├── subsystems/
         │   ├── drivetrain.py
         │   ├── intake.py
         │   ├── shooter.py
         │   └── tests/
         ├── autonomous/
         │   ├── auto_routines.py
         │   └── tests/
         ├── pathplanner/
         │   ├── trajectory_generator.py
         │   └── path_follower.py
         └── main.py
         ```
     - **`/tests/`:** Unit tests for each component and subsystem. Encourage test-driven development (TDD) where feasible.

   - **`/scripts/`:**
     - Utility scripts for common tasks (e.g., deploying code to the robot, running simulations).

   - **`/resources/`:**
     - Diagrams, flowcharts, and other non-code assets that are useful for understanding the robot's design and function.

#### **Version Control Practices:**

- **Branches:**
  - **`main` Branch:**  
    - The stable branch that contains tested and competition-ready code.
  - **`dev` Branch:**  
    - The branch where active development happens. All features and changes are merged here first.
  - **Feature Branches:**  
    - Create separate branches for new features, e.g., `feature/drivetrain-improvements`. Once a feature is complete, it should be merged into `dev` after code review.

- **Pull Requests (PRs):**
  - Require team members to create PRs when merging code from feature branches to `dev` or `dev` to `main`. 
  - Use PRs for code reviews, where other team members can comment and suggest improvements.

- **Issues and Tasks:**
  - Use GitHub Issues to track bugs, feature requests, and tasks. Label them accordingly (e.g., `bug`, `enhancement`, `documentation`).
  - Assign team members to issues based on their skills and areas they want to develop.

### **2. Organizing Training for the Transition**

#### **Training Schedule:**

1. **Week 1-2: Python Basics**

   **Objective:**  
   Ensure every team member understands the basic syntax and structure of Python, laying a foundation for more complex robot code development.

   **Topics:**
   - **Syntax:**  
     - Variables, data types, and operators.
     - Control structures: `if`, `else`, `for`, `while` loops.
     - Functions: Defining and calling functions, using arguments and return values.
     - Lists, dictionaries, and sets: Basic data structures in Python.
   - **Key Differences from Java:**
     - Emphasize Python’s use of indentation instead of braces `{}`.
     - Dynamic typing versus Java’s static typing.

   **Resources:**
   - Online courses such as Codecademy’s Python track or Coursera’s Python for Everybody.
   - Live coding sessions where you walk through simple Python scripts and explain how they work.
   - Use the `/training/basics/` directory to store example scripts and exercises.

   **Exercises:**
   - Basic calculations and string manipulations.
   - Creating simple loops (e.g., counting, summing numbers).
   - Writing and calling basic functions.

   **GitHub Integration:**
   - Encourage team members to fork the repository, complete the exercises, and submit them via pull requests for review.

2. **Week 3-4: Introduction to RobotPy**

   **Objective:**  
   Familiarize the team with RobotPy and the specific tools and libraries needed to program the robot using Python.

   **Topics:**
   - **Setting Up the Environment:**
     - Installing Python, pip, and RobotPy.
     - Setting up a virtual environment and installing necessary libraries.
   - **Basic RobotPy Code Structure:**
     - Understanding `robot.py` structure and how RobotPy mimics the WPILib structure used in Java.
     - Basic motor control using Python: Writing Python code to control motors, using PWM, CAN, etc.
     - Introduction to `wpilib` and its key components (`TimedRobot`, `MotorController`, etc.).

   **Resources:**
   - RobotPy documentation and example projects.
   - Tutorials on setting up and using RobotPy.
   - Example codes stored in `/training/robot_basics/`, focusing on translating Java motor control code into Python.

   **Exercises:**
   - Set up a simple Python project using RobotPy to control a motor with a joystick.
   - Write a script to read values from a sensor and print them to the console.

   **GitHub Integration:**
   - Store translated examples and new RobotPy exercises in `/training/robot_basics/`.
   - Use issues to track individual progress and challenges faced by the team.

3. **Week 5-6: Subsystem Development**

   **Objective:**  
   Enable team members to build and integrate Python subsystems for different parts of the robot.

   **Topics:**
   - **Writing Python Classes for Subsystems:**
     - Creating subsystem classes that encapsulate specific robot functionalities, such as drivetrain, shooter, or intake.
     - How to use commands to control subsystems (introducing the Command-Based model in Python).
     - Writing reusable components in `/components/` that can be used across subsystems.
   - **Testing and Debugging Subsystems:**
     - Writing unit tests for subsystems.
     - Debugging techniques in Python (using `print`, `logging`, and Python's debugging tools).

   **Resources:**
   - Detailed guides on writing subsystems in Python, available in the `/docs/` directory.
   - Sample code for a basic drivetrain subsystem, with tests included.

   **Exercises:**
   - Create a basic drivetrain subsystem that can drive in teleoperated mode.
   - Write unit tests for the drivetrain, ensuring all functionalities work as expected.

   **GitHub Integration:**
   - Use the `/sandbox/subsystems/` directory to house these subsystem classes.
   - Encourage team members to create feature branches for each subsystem they work on and submit PRs for code reviews.

4. **Week 7-8: Autonomous and Vision Processing**

   **Objective:**  
   Teach the team how to write and test autonomous routines and implement vision processing using Python.

   **Topics:**
   - **Autonomous Mode Programming:**
     - Writing Python code for autonomous routines that can control multiple subsystems.
     - Using the `/autonomous/` directory to store and organize autonomous routines.
   - **Vision Processing:**
     - Introduction to OpenCV (or ?) in Python for vision processing.
     - Writing code to capture, process, and analyze images from the robot’s camera.
     - Integrating vision data into autonomous routines for tasks like object detection or line following.

   **Resources:**
   - Tutorials on writing autonomous code using command-based structure.
   - OpenCV documentation and example Python scripts for simple image processing tasks.
   - Example autonomous routines that demonstrate basic autonomous behavior.

   **Exercises:**
   - Write an autonomous routine that drives the robot forward, turns, and comes back
   - Implement a simple vision processing script that identifies a colored object and calculates its position on the screen.
   - Integrate the vision processing code with the autonomous routine to drive toward a detected object.

   **GitHub Integration:**
   - Store autonomous routines in the `/sandbox/autonomous/` directory. Ensure each routine is well-documented with comments explaining its purpose and logic.
   - Use the `/pathplanner/` directory if working with pre-generated paths or trajectories. Include trajectory generation scripts and path-following logic here.
   - Encourage code reviews where team members analyze each other’s autonomous and vision processing code, offering suggestions for improvement.

5. **Week 9-10: Advanced Testing and Simulation**

   **Objective:**  
   Teach the team advanced testing techniques and how to use simulation tools to validate their code before deploying it to the robot.

   **Topics:**
   - **Writing Unit Tests:**
     - Introduction to Python testing frameworks like `unittest` or `pytest`.
     - Writing unit tests for subsystems and commands, ensuring they behave as expected under various conditions.
   - **Simulation:**
     - Setting up a simulation environment using tools like Gazebo or WPILib’s simulation tools.
     - Running the robot code in a simulated environment to test behaviors without the physical robot.
     - Debugging and refining code based on simulation results.

   **Resources:**
   - Tutorials on writing tests in Python and setting up a simulation environment.
   - Example unit tests for subsystems like the drivetrain or shooter.
   - Guides on using the simulation tools to test robot code.

   **Exercises:**
   - Write unit tests for each subsystem and command, covering various edge cases.
   - Set up a simulation for the drivetrain and run different autonomous routines to observe how the robot would behave in a real match.
   - Debug any issues found during simulation and refine the code accordingly.

   **GitHub Integration:**
   - Store all tests in the `/tests/` directory, organized by subsystem or command.
   - Use continuous integration (CI) tools like GitHub Actions to automatically run tests whenever code is pushed to the repository.
   - Store simulation configurations and any necessary scripts in the `/scripts/` directory.

6. **Week 11-12: Full Robot Integration**

   **Objective:**  
   Bring together all the subsystems, autonomous routines, and testing practices to finalize the robot’s codebase before competition.

   **Topics:**
   - **Subsystem Integration:**
     - Combining all the subsystems into a cohesive robot program.
     - Ensuring that commands properly control the subsystems and that all parts work together smoothly.
   - **Final Testing and Debugging:**
     - Comprehensive testing of the entire robot program, including edge cases and stress testing.
     - Debugging and resolving any issues found during integration.

   **Resources:**
   - Full robot integration guides, tips for ensuring that subsystems don’t interfere with each other.
   - Documentation on best practices for final testing before deployment.

   **Exercises:**
   - Perform full system tests where the entire robot’s functionality is tested, including teleoperated and autonomous modes.
   - Run stress tests where multiple commands are executed in quick succession to ensure the robot can handle real match conditions.

   **GitHub Integration:**
   - Ensure all final code is merged into the `main` branch.
   - Use the `/docs/` directory to document the final robot architecture, including diagrams and explanations of how each part works together.
   - Prepare a final code release that is competition-ready, and create a version tag in the GitHub repository.

### **3. Long-Term Maintenance and Growth**

- **Ongoing Documentation:**
  - Encourage the team to keep the `/docs/` directory up to date with the latest information, including new learnings or changes in the project.

- **Expand Repository Usage:**
  - We will use the [RobotPython2025](https://github.com/Team2556/RobotPython2025) repository to host not just code but also design discussions, strategy documentation, and more.

- **Future Projects:**
  - Once the transition is complete, consider adding new Python projects to the repository, such as off-season experiments or new tool development, to keep skills sharp.

By following this structured approach, we will have a well-organized codebase and a robust training program that can proficiently use Python within the three-month timeframe. 