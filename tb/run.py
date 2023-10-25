import sys
import subprocess

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python run.py <testbench_file>.sv')
        sys.exit(-1)
    
    filename = sys.argv[1]
    subprocess.Popen(f"iverilog -g2012 -Y .sv -y ../rtl/ -y ./sram/ -o ../build/{filename[:filename.find('.')]}.iverilog {filename} && vvp ../build/{filename[:filename.find('.')]}.iverilog && gtkwave ../build/{filename[:filename.find('.')]}.vcd", shell=True)