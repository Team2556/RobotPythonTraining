# description 
Creating a simple exercise to teach systems engineering concepts can be highly effective. Let's use the example of "making a sandwich" as it's relatable and easy to break down into components and subsystems. 

### **Systems Engineering Exercise: "Making a Sandwich"**

#### **Objective:**
Teach the team how to break down a task into its components and subsystems, identify goals, and create a step-by-step plan that integrates these elements into a coherent process.

### **1. Define the Goal:**
   - **Primary Goal:**  
     - Make a sandwich that is ready to eat.
   - **Secondary Goals:**  
     - Ensure the sandwich is safe to eat (food safety).
     - Make the sandwich in a timely manner.
     - Customize the sandwich to individual preferences.

### **2. Identify the High-Level Systems:**
   - **Ingredients System:**
     - Components: Bread, filling (e.g., ham, turkey, vegetables), condiments.
   - **Tools System:**
     - Components: Knife, cutting board, plate.
   - **Process System:**
     - Actions: Gathering ingredients, preparing ingredients, assembling the sandwich.

### **3. Break Down into Subsystems:**
   - **Ingredients Preparation Subsystem:**
     - Tasks: 
       - Slice the bread.
       - Prepare fillings (e.g., slice meat, wash vegetables).
   - **Assembling Subsystem:**
     - Tasks:
       - Apply condiments to bread.
       - Layer fillings on bread.
       - Close the sandwich with another slice of bread.
   - **Presentation Subsystem:**
     - Tasks:
       - Cut sandwich into halves or quarters (optional).
       - Arrange on a plate for serving.

### **4. Develop Commands and Actions:**
   - **Commands:**
     - Each command corresponds to a specific task within a subsystem.
     - Example Command: "Slice Bread" for the Ingredients Preparation Subsystem.
   - **Actions:**
     - The specific steps to execute each command.
     - Example Actions for "Slice Bread":
       1. Place bread on cutting board.
       2. Use knife to slice bread evenly.

### **5. Define System Interactions:**
   - Understand how each subsystem interacts with others:
     - **Ingredients Preparation** feeds into **Assembling**.
     - **Tools** are used throughout the process, from preparation to presentation.
   - Discuss dependencies (e.g., you can't assemble the sandwich until ingredients are prepared).

### **6. Create a Flowchart:**
   - Have the team create a flowchart that visualizes the entire process from start to finish.
     - Start with the goal at the top.
     - Break down the high-level systems.
     - Detail subsystems and commands.
     - Connect the flow of actions with arrows showing the order of operations.

### **7. Discuss Optimization:**
   - How can the process be improved?
     - Are there steps that can be done simultaneously (e.g., one person slicing bread while another preps vegetables)?
     - What happens if an ingredient is missing? How does this affect the system?
   - Introduce concepts like parallel processing, redundancy (e.g., having an extra loaf of bread), and contingency planning.

### **8. Execute the Process:**
   - Optionally, have the team actually make a sandwich following the process they developed.
   - Afterwards, reflect on what worked well and what could be improved.

### **9. Relate to Robotics:**
   - Discuss how this process mirrors what they will do in robotics:
     - Breaking down complex tasks (e.g., autonomous navigation) into smaller subsystems.
     - Creating commands and actions (e.g., motor control, sensor feedback) to achieve goals.
     - Planning interactions between subsystems (e.g., drivetrain and sensors working together).

### **10. Reflection and Learning:**
   - Ask the team to reflect on what they learned about systems engineering through the exercise.
   - Discuss how this approach can be applied to larger, more complex projects, such as programming a robot.

### **Alternative Example: Cleaning a Bathroom**
If the "making a sandwich" example feels too simple, "cleaning a bathroom" can be a more complex alternative. It involves more subsystems (cleaning surfaces, mirrors, floors), safety considerations (use of chemicals), and requires a more detailed plan.

#### **Goal:**
   - Clean the bathroom thoroughly and safely.

#### **High-Level Systems:**
   - **Surface Cleaning System:**
     - Components: Counters, sinks, toilets.
   - **Floor Cleaning System:**
     - Components: Mopping, sweeping.
   - **Tool and Chemical System:**
     - Components: Cleaners, gloves, mop, broom.
   - **Process System:**
     - Actions: Gathering tools, applying cleaners, scrubbing, rinsing, drying.

This example introduces more complexity in terms of safety and procedure, providing an excellent bridge to real-world systems engineering challenges.

# training script

### **Script: Systems Engineering Training - "Making a Sandwich"**

---

**Introduction (5 minutes):**

- **Facilitator:** "Today, we're going to learn about systems engineering, a process used to break down complex problems into manageable parts. To make this fun and relatable, we'll use the example of making a sandwich. By the end of this session, you'll be able to apply these principles to robotics and other projects."

**Step 1: Define the Goal (5 minutes):**

- **Facilitator:** "Let's start by defining our primary goal: to make a sandwich that is ready to eat. We can also consider secondary goals, such as making sure it's safe to eat, making it quickly, and customizing it to preferences."
- **Activity:** "As a group, can you think of any additional goals? Let’s list them."

**Step 2: Identify High-Level Systems (10 minutes):**

- **Facilitator:** "To achieve our goal, we'll break the process down into high-level systems. For making a sandwich, these could include the Ingredients System, Tools System, and Process System."
- **Activity:** "In pairs, think about what components might belong to each system. For example, what would go into the Ingredients System? Share your ideas, and we'll list them together."

**Step 3: Break Down into Subsystems (10 minutes):**

- **Facilitator:** "Now that we have our high-level systems, let’s break them down further into subsystems. For instance, the Ingredients Preparation Subsystem could involve tasks like slicing bread and preparing fillings."
- **Activity:** "As a group, let’s identify the subsystems within each high-level system. What specific tasks are involved in each?"

**Step 4: Develop Commands and Actions (10 minutes):**

- **Facilitator:** "Each subsystem involves specific commands and actions. For example, the command 'Slice Bread' might include actions like placing the bread on the cutting board and slicing it evenly."
- **Activity:** "Individually, take one subsystem and list the commands and actions needed to complete it. Then, share your list with the group."

**Step 5: Define System Interactions (5 minutes):**

- **Facilitator:** "Now that we’ve broken down the tasks, let’s think about how the systems interact. For example, you can’t assemble the sandwich until the ingredients are prepared."
- **Activity:** "As a group, discuss how each system depends on the others. What needs to happen first? Are there any steps that can happen simultaneously?"

**Step 6: Create a Flowchart (10 minutes):**

- **Facilitator:** "To visualize our process, we’ll create a flowchart. This will help us see the sequence of actions and how the systems connect."
- **Activity:** "On a whiteboard or large sheet of paper, draw a flowchart starting with our goal. Break it down into high-level systems, subsystems, and actions. Use arrows to show the order of operations."

**Step 7: Discuss Optimization (5 minutes):**

- **Facilitator:** "With the process mapped out, let’s think about how we could optimize it. Are there steps that could be improved? Could any steps happen at the same time?"
- **Activity:** "As a group, brainstorm ways to make the process more efficient. Consider what might happen if an ingredient is missing or if we need to make multiple sandwiches quickly."

**Step 8: Relate to Robotics (5 minutes):**

- **Facilitator:** "The steps we’ve taken to make a sandwich mirror the approach we’ll use in robotics. Just like we broke down this task, we’ll break down robot tasks into subsystems, commands, and actions."
- **Activity:** "Discuss how this exercise can help us when programming the robot. What parallels do you see?"

**Conclusion and Reflection (5 minutes):**

- **Facilitator:** "To wrap up, think about what you’ve learned today. Systems engineering is a powerful tool for tackling complex problems, whether you’re making a sandwich or building a robot."
- **Activity:** "Each person, share one thing you learned today that you think will help with our robotics projects."

---

**Facilitator Notes:**

- Keep the atmosphere light and engaging. The goal is to make systems engineering approachable and fun.
- Encourage participation and make sure everyone feels comfortable sharing their ideas.
- Use the sandwich example as a concrete illustration, but continually draw parallels to robotics to help the team see the relevance.