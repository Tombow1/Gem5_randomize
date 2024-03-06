# The gem5 Simulator

## Randomization of CPU Execution Order

### Overview

This patch introduces the feature of randomization of CPU execution order. It is designed to introduce non-determinism into the execution order of instructions at the CPU level, offering a more varied simulation environment. This capability is especially beneficial for exploring the performance implications of instruction execution variability and for enhancing the robustness of systems against timing-based security attacks. 

* When CPU randomization is enabled, the patched gem5 simulator will randomize the order of ready-to-execute instructions in the instruction queue at the execute stage of the O3 CPU. Without this patch, the original simulator executes ready instructions in FIFO order. 

* When ruby randomization is enabled, the patched simulator will randomly add extra cycles of latency to cache events between L1 cache and L2 cache. Currently, the chance of having a one-cycle increase is 50%.


### Build Instructions

To build the simulation with the new randomization feature, use the following command:

```bash
scons build/ARM_MESI_Two_Level/gem5.opt -j <number_of_cores>
```
* Replace <number_of_cores> with the number of CPU cores available on your platform. This example uses -j 9 to specify that 9 cores are used for compilation.
Running the Simulation
To run the simulation with the provided example.py configuration, use the following command:


### Running the Simulation
To run the simulation with the provided example.py configuration, use the following command:
```bash
build/ARM_MESI_Two_Level/gem5.opt configs/example.py --cpu_randomize --ruby_randomize
```
* The **--cpu_randomize** flag enables CPU instruction execution order randomization.
* The **--ruby_randomize** flag activates randomization within the Ruby memory system.
* All randomization are off by default.

### Understand the Patch and Extend Yourself

The provided script may not fully meet your needs, and you might find yourself wanting to write your own gem5 scripts with this patch. Here is how to do it.

#### CPU randomization
This patch supports two types of randomization: O3 CPU and Ruby cache system with MESI two-level protocol. To manually turn on CPU randomization, you can easily access and modify the `randomize` variable of the CPU object. However, this variable is patched into the m5 object, making it inaccessible for direct modification through the gem5 standard library, as the standard library's CPU classes wrap the m5 object. You can bypass this limitation through the standard library's `BaseCPUCore` type.

Here's how you should configure it yourself:

```python
randomcore = O3CPU()
randomcore.randomize = cpu_randomize
basecore = BaseCPUCore(core=randomcore, isa=ISA.ARM)
processor = BaseCPUProcessor([basecore])
```
#### Ruby randomization
Ruby cache system is easy and strit forward to configure. When creating the cache system, simply set randomize to true/false:
```bash
cache_hierarchy = MESITwoLevelCacheHierarchy(
    l1d_size="32kB",
    l1d_assoc=8,
    l1i_size="32kB",
    l1i_assoc=8,
    l2_size="256kB",
    l2_assoc=16,
    num_l2_banks=2,
    randomize=ruby_randomize,
)
```
