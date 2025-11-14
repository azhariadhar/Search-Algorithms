# ==========================================
# Lab Report: LAB REPORT 1 - Search Algorithms
# Student ID: [SD23058]
# File Name: Lab_Report_1.py
# ==========================================

import streamlit as st
from collections import deque

# -------------------------------
# Streamlit Page Setup
# -------------------------------
st.title("SD23058 Lab Report 1")
st.subheader("Python: Search Algorithms (BFS & DFS)")

st.write("""
This program demonstrates **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**  
on a directed graph. The algorithm follows **alphabetical tie-breaking** when multiple adjacent nodes are available.
""")

# -------------------------------
# Define Graph
# -------------------------------
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'G'],
    'C': ['D'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': ['F', 'H'],
    'H': []
}

# Sort neighbors alphabetically
for node in graph:
    graph[node].sort()

# -------------------------------
# Breadth-First Search (BFS)
# -------------------------------
def bfs(start):
    visited = []
    queue = deque([start])
    level = {start: 0}
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
                    level[neighbor] = level[node] + 1
    return visited, level

# -------------------------------
# Depth-First Search (DFS)
# -------------------------------
def dfs(start):
    visited = []
    
    def dfs_recursive(node):
        if node not in visited:
            visited.append(node)
            for neighbor in graph[node]:
                dfs_recursive(neighbor)
                
    dfs_recursive(start)
    return visited

# -------------------------------
# User Input and Run
# -------------------------------
st.write("### Run the Search Algorithms")

start_node = st.text_input("Enter starting node (default = A):", "A").strip().upper()

if st.button("Run Algorithms"):
    if start_node not in graph:
        st.error("Invalid node. Please enter a valid node (A–H).")
    else:
        bfs_result, level_result = bfs(start_node)
        dfs_result = dfs(start_node)
        
        # BFS Results
        st.success("Breadth-First Search (BFS) Completed")
        st.write("**Traversal Order:**", " → ".join(bfs_result))
        st.write("**Node Levels:**")
        st.json(level_result)
        
        # DFS Results
        st.success("Depth-First Search (DFS) Completed")
        st.write("**Traversal Order:**", " → ".join(dfs_result))
        
        # Conclusion
        st.write("---")
        st.write("""
        **Observation:**
        - BFS explores the graph level by level, ensuring all nodes at one level are visited before moving deeper.  
        - DFS explores as far as possible along one branch before backtracking.
        """)
