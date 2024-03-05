# The gem5 Simulator

## Randomization of CPU Execution Order

### Overview

This patch introduces the feature of randomization of CPU execution order. This is designed to introduce non-determinism into the execution order of instructions at the CPU level, offering a more varied simulation environment. This capability is especially beneficial for exploring the performance implications of instruction execution variability and for enhancing the robustness of systems against timing-based security attacks.

### Build
scons build/ARM_MESI_Two_Level/gem5.opt -j 9

### Run

build/ARM_MESI_Two_Level/gem5.opt configs/example.py --cpu_randomize --ruby_randomize
