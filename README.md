# The gem5 Simulator

## Randomization of CPU Execution Order

### Overview

The gem5 simulator, a widely used tool for computer architecture research and education, now includes an innovative feature: the randomization of CPU execution order. This feature is designed to introduce non-determinism into the execution order of instructions at the CPU level, offering a more varied simulation environment. This capability is especially beneficial for exploring the performance implications of instruction execution variability and for enhancing the robustness of systems against timing-based security attacks.

### Benefits

- **Performance Analysis**: Helps in identifying performance bottlenecks under varied execution scenarios.
- **Security Research**: Aids in the development and testing of systems resistant to timing and side-channel attacks by simulating unpredictable execution patterns.
- **Testing Robustness**: Improves the testing coverage for systems by exposing them to a broader range of execution sequences, potentially uncovering rare or unforeseen issues.

### Activation

To enable the randomization of CPU execution order in your simulations, you need to supply the `--CPU_EXEC_RANDOMIZATION` flag when starting gem5. This flag activates the randomization mechanism, allowing the CPU to execute instructions in a non-deterministic order within the constraints of the simulation's architecture and logic.

#### Usage Example

```bash
./build/ARM/gem5.opt --CPU_EXEC_RANDOMIZATION configs/example/se.py -c tests/test-progs/hello/bin/arm/linux/hello
