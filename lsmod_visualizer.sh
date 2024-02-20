lsmod | awk 'NR > 1{print $1,$4;}' | python $(dirname $0)/visualizer.py 
dot lsmod_vis.dot -Tpng >> lsmod_vis.png
