# 📈 Interactive Function Plotter (Python)

An interactive terminal-based Python tool that lets you **plot mathematical functions dynamically** using `matplotlib`.  
You enter any math expression (like `x**2`, `math.sin(x)`, or `math.exp(x)`), and it instantly generates a customizable graph — complete with axes, tick spacing, and smart padding.

---

## 🧠 Features
- Accepts **any valid Python math expression**
- Adjustable **plot range** and **tick spacing**
- Automatically detects axis limits and scales
- Handles math errors safely (e.g., division by zero)
- Highlights **X** and **Y** axes for easy reference

---

## 🖼️ Example Usage

### 🧮 Input:
Enter the function you want to plot: math.sin(x)
Enter the plot range: 10
Enter xaxis_scale and yaxis_scale, make sure to choose a scale that's visible: 2 1


### 📊 Output:
Displays a sine wave plotted from -10 to 10 with axes labeled and colored.  

---

## ⚙️ Requirements
- Python 3.8+
- [Matplotlib](https://pypi.org/project/matplotlib/)

Install dependencies:
```bash
pip install matplotlib
```

---
## 🚀 How to Run

Run the script:
```
python plot_graph.py
```
Then follow the on-screen prompts to:

1. Enter a mathematical function (e.g., x**2, math.sin(x), math.exp(x)).

2. Set the range for x (e.g., 10 → plots from -10 to 10).

3. Define tick scales for x and y axes.

---

🧩 How It Works

- Uses Python’s built-in eval() in a restricted environment allowing only x and the math module.

- Automatically generates x values and computes corresponding y values.

- Uses Matplotlib to plot the data and color-code axes:

- Red dashed line → X-axis

- Blue dashed line → Y-axis

- Green solid line → function graph

---

📜 License

MIT License — use, modify, and share freely.

“Plot smarter, not harder.”
— Daniel Adeoluwa Ademoye 🧮
