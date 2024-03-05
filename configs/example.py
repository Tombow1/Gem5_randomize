import argparse

from m5.objects import *

from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.cachehierarchies.classic.no_cache import NoCache
from gem5.components.cachehierarchies.ruby.mesi_two_level_cache_hierarchy import (
    MESITwoLevelCacheHierarchy,
)
from gem5.components.memory import SingleChannelDDR3_1600
from gem5.components.processors.base_cpu_core import BaseCPUCore
from gem5.components.processors.base_cpu_processor import BaseCPUProcessor
from gem5.components.processors.cpu_types import CPUTypes
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.isas import ISA
from gem5.resources.resource import obtain_resource
from gem5.simulate.simulator import Simulator
from gem5.utils.requires import requires

parser = argparse.ArgumentParser(
    description="Set randomization options for CPU and Ruby."
)
parser.add_argument(
    "--cpu_randomize", action="store_true", help="Enable CPU randomization"
)
parser.add_argument(
    "--ruby_randomize", action="store_true", help="Enable Ruby randomization"
)
args = parser.parse_args()

cpu_randomize = args.cpu_randomize
ruby_randomize = args.ruby_randomize

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

requires(isa_required=ISA.ARM)

memory = SingleChannelDDR3_1600(size="32MB")

randomcore = O3CPU()
randomcore.randomize = cpu_randomize
basecore = BaseCPUCore(core=randomcore, isa=ISA.ARM)
processor = BaseCPUProcessor([basecore])

board = SimpleBoard(
    clk_freq="3GHz",
    processor=processor,
    memory=memory,
    cache_hierarchy=cache_hierarchy,
)

board.set_se_binary_workload(obtain_resource("arm-hello64-static"))

simulator = Simulator(board=board)
simulator.run()

print(
    "Exiting @ tick {} because {}.".format(
        simulator.get_current_tick(), simulator.get_last_exit_event_cause()
    )
)
