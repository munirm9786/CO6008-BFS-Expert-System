# CO6008 Knowledge-Based Systems Coursework 1
### Title: A Simple Knowledge-Based Expert System for Pathfinding Using Breadth-First Search (BFS)

**Author:** Munir Mohammed  
**Date:** October 2025  

---

##  Project Overview
This project is a simple expert system that finds the shortest path between two nodes using the Breadth-First Search (BFS) algorithm.  
It demonstrates how a computer can reason through a knowledge base in a step-by-step way, similar to how a human plans a route.

---

##  Features
- Knowledge base stored as a graph (Python dictionary)  
- Inference engine uses BFS to explore and find paths  
- Input validation for lowercase or invalid nodes  
- Clear text output for successful or failed searches  

---

##  How to Run
1. Open `bfs_expert_system.py` in Visual Studio Code or any Python IDE.  
2. Run the file.  
3. Enter a start and goal node (for example, A and I).  
4. The program will show the shortest path or say if no path exists.  


## Testing Summary
The expert system was tested with several different inputs:

- **A → I:** Found shortest path A → C → F → I  
- **A → H:** Found shortest path A → B → E → H  
- **B → G:** Found shortest path B → D → G  
- **C → H:** Correctly showed “No path found.”  
- **a → i:** Worked after converting input to uppercase.  
- **Z → I:** Showed “Start node 'Z' is not in the graph.”  

Testing evidence (screenshots and notes) can be found in **EVIDENCE TESTING.docx**.

---

## Files in This Repository
| File | Description 
`bfs_expert_system.py` | Python code for the expert system |
 `CO6008_BFS_Expert_System_Final_Report.docx` | Full coursework report |
`EVIDENCE TESTING.docx` | Screenshots and test results |
`README.md` | Project overview (this file) 
