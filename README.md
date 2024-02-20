# Kernel Modules Visualizer

A script to visualize loaded modules within the Linux Kernel and kernel dependencies.

## Dependencies 

- Awk
- Python
- Graphviz

## Running

Make the script executable

```chmod +x lsmod_visualizer.sh```

And then run the script

```./lsmod_visualizer.sh```

The script will produce a Graphviz `.dot` file and use Graphviz to create a PNG of the visualization.
