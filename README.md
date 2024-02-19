# The gem5 Simulator

## Randomization of CPU Execution Order

### Overview

This patch introduces the feature of randomization of CPU execution order. This is designed to introduce non-determinism into the execution order of instructions at the CPU level, offering a more varied simulation environment. This capability is especially beneficial for exploring the performance implications of instruction execution variability and for enhancing the robustness of systems against timing-based security attacks.

### Activation

To enable the randomization of CPU execution order in your simulations, you need to supply the `--CPU_EXEC_RANDOMIZATION` flag when starting gem5. This flag activates the randomization mechanism, allowing the CPU to execute instructions in a non-deterministic order within the constraints of the simulation's architecture and logic.

#### Usage Example

```bash
./build/ARM/gem5.opt --CPU_EXEC_RANDOMIZATION configs/example/se.py -c tests/test-progs/hello/bin/arm/linux/hello
