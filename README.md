# Craftlytics

Craftlytics is a Python program designed to analyze extracted Minecraft crafting recipe JSON files from any modern version of the game. It calculates the frequency with which each item and block is used in crafting recipes, offering valuable insights into their versatility and importance. By considering changes across Minecraft versions, the output can help you optimize your Minecraft storage system, prioritize frequently used items, and better understand which resources are essential for crafting efficiency.

---

## **Features**
- **Analyze Crafting Recipes**: Scans a collection of Minecraft crafting recipe JSON files.
- **Crafting Usage Insights**:
  - Provides a total count of crafting uses for each item and block.
  - Lists all crafting recipes that use a specific item or block.
- **Sorted Results**: Outputs a priority list of crafting elements, ordered from most used to least used, to help optimize storage systems or gameplay strategies.

---

## **How It Works**
1. **Input**: The program processes a set of crafting recipe JSON files extracted from a Minecraft `.jar` file.
2. **Analysis**:
   - Counts the total crafting uses for each item or block.
   - Tracks every occurrence of each item in individual recipes.
3. **Output**:
   - A sorted list of items and blocks by crafting use frequency.
   - Optionally, a detailed breakdown of occurrences in specific recipes.

---

## **Project Goals**
1. **Efficient Storage System**: Identify versatile crafting items like wood, cobblestone, and iron ingots to prioritize their placement in storage systems.
2. **Scalable Design**:
   - Follows clean coding principles, including separation of concerns.
   - Implements Object-Oriented Programming (OOP).
3. **Future-Proofing**:
   - CLI-based program for now, with plans for a GUI extension in a separate folder.
   - Designed for modularity and potential public use.

---

## **Architecture**
- **`main.py`**: Entry point; coordinates CLI inputs and program execution.
- **`parser.py`**: Handles command-line arguments using Python's `argparse`.
- **`tracker.py`**: Core logic for analyzing crafting recipes and tracking usage statistics.
- **Future Plans**:
  - Add GUI functionality in a separate folder.
  - Include unit tests to ensure all use cases are handled properly.

---

## **Usage**
### **Prerequisites**
- Python 3.10 or higher
- JSON files containing Minecraft crafting recipes (e.g., extracted from the game's `.jar` file)

### **Run the Program**
```bash
python main.py -a
```

- `-a`: Analyze all recipes and generate the sorted usage list.

### **Example Output**
```
1. Wood: 235 uses
2. Iron Ingot: 180 uses
3. Cobblestone: 145 uses
...
```

---

## **Installation**
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/craftlytics.git
   ```
2. Navigate to the project directory:
   ```bash
   cd craftlytics
   ```
3. Install dependencies (if required):
   ```bash
   pip install -r requirements.txt
   ```

---

## **References**
- [Python JSON Documentation](https://docs.python.org/3/library/json.html)
- [Python Collections Documentation](https://docs.python.org/3/library/collections.html#collections.Counter)
- [Python Argparse Documentation](https://docs.python.org/3/library/argparse.html)

---

## **Planned Enhancements**
- Add a user-friendly graphical interface (GUI).
- Extend the program with a detailed report generation feature (e.g., export results to a file).
- Publish as an open-source tool for the Minecraft community.
- Implement comprehensive unit tests for all core functionalities.

---

## **Contribution**
This is a personal project, but feedback and contributions are welcome! If you'd like to collaborate, feel free to fork the repository or open an issue for suggestions.

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.
