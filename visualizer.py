import sys

def main(input_str):
    f = open("lsmod_vis.dot", "w")
    f.write("digraph lsmod {\n")
    for line in input_str:
        split_str = line.split()
        k_mod = split_str[0]
        
        if(len(split_str) > 1):
            k_used = split_str[1]
            for used_by in k_used.split(","):
                f.write("\t"+used_by+"->"+k_mod+"\n")
        else:
            f.write("\t"+k_mod+"\n")
    f.write("}\n")
if __name__ == "__main__":
    main([line.rstrip('\n') for line in sys.stdin])
