import matplotlib.pyplot as plt  # Import the matplotlib.pyplot module for plotting
import math  # Import the math module to allow mathematical functions (e.g., sin, cos, exp) in the user's function

def plot_graph():
    """
    Plot a graph for a mathematical function provided by the user. It allows customization
    of the plot range and axis scaling for more visible and defined graphs. The function
    handles mathematical errors safely during computation of y-values. The graph includes
    axes with tick settings controlled by user-defined scales. It also dynamically generates
    and adjusts axis limits to fit the graph data.

    :raises Exception: If errors arise during evaluation of the provided function string.
    """
    while True:
        # Prompt user for the mathematical function string (e.g., "x**2", "math.sin(x)")
        function = input("Enter the function you want to plot: ")
        # Prompt user for the symmetrical range for x-values (e.g., 10 means x from -10 to 10)
        plot_range = input("Enter the plot range: ")
        try:
            # Convert the range input to an integer
            plot_range = int(plot_range)
        except ValueError:
            # Handle case where the plot range input is not a valid integer
            print("Invalid input. Please enter a number.")
            continue
        # Ask for tick spacing (so user doesn't need to stress over axis bounds)
        # Prompt user for x and y axis tick spacing, separated by a space
        graph_details = input("Enter xaxis_scale and yaxis_scale, make sure to choose a scale that's visible: ").split()
        try:
            # Map the two split string values to integers for x and y axis scales
            x_axis_scale, y_axis_scale = map(int, graph_details)
        except Exception:
            # Handle case where the input for scales is invalid (e.g., not two numbers, or not integers)
            print("Invalid input. enter two values separated by spaces.")
            continue

        # Create a figure and a set of subplots (only one plot in this case)
        fig, ax = plt.subplots()

        # Generate x-values dynamically from -plot_range to +plot_range (inclusive)
        x_values = list(range(-plot_range, plot_range + 1))
        y_values = []  # Initialize an empty list to store the computed y-values

        # Compute y-values and handle math errors safely
        for x in x_values:
            try:
                # Evaluate the function string, allowing 'x' and functions from the 'math' module
                y = eval(function, {"x": x, "math": math})
                y_values.append(y)
                print(f"{x} \t {y}")
            except Exception as e:
                # Catch any errors (e.g., division by zero, invalid function call) during evaluation
                print(f"Error computing y for x={x}: {e}")
                # If an error occurs, append 0 to y_values (a simple way to handle the point)
                y_values.append(0)
                print(f"{x} \t 0")

        # Automatically determine axis limits from data
        # Find the minimum and maximum y-values, and x-values
        y_min, y_max, x_min, x_max = min(y_values), max(y_values), min(x_values), max(x_values)

        # Add small padding around the graph so it doesn't touch edges
        # Calculate a 10% padding for the x-axis
        x_pad = (x_max - x_min) * 0.1
        # Calculate a 10% padding for the y-axis
        y_pad = (y_max - y_min) * 0.1

        # Set the limits of the axes [xmin, xmax, ymin, ymax] with padding
        ax.axis([x_min - x_pad, x_max + x_pad, y_min - y_pad, y_max + y_pad])

        # Draw x and y axes
        # Plot a dashed red line for the x-axis (where y=0)
        ax.plot([x_min, x_max], [0, 0], color='red', linestyle='--')
        # Plot a dashed blue line for the y-axis (where x=0)
        ax.plot([0, 0], [y_min, y_max], color='blue', linestyle='--')

        # Set ticks
        # Set x-axis ticks using the user-defined scale
        ax.set_xticks(range(int(x_min), int(x_max) + 1, x_axis_scale))
        # Set y-axis ticks using the user-defined scale (uses x_min, x_max for range calculation, which might be a bug, should likely use y_min, y_max)
        ax.set_yticks(range(int(y_min), int(y_max) + 1, y_axis_scale)) # NOTE: This line in the original code uses x_min and x_max for the range of y-ticks, which is likely incorrect. It should use y_min and y_max. The original code is kept as requested.

        # Plot the function
        # Plot the calculated x and y values with a green line and circle markers
        ax.plot(x_values, y_values, color='green', marker='o')
        # Display the plot
        plt.show()
        break


# Example: Call the function to start the plotting process
plot_graph()