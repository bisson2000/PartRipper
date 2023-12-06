from data_fetch import import_cpu
from dataclasses import dataclass


class CPU_Specs:
    name: str = None
    brand: str = None
    core_count: int
    usage: float
    avg_freq: float
    max_freq: float
    integrated_graphics: bool = False

    def __init__(self, brand: str, name: str, core_count: int, usage: float, avg_freq: float, max_freq: float, integrated_graphics: bool = False) -> None:
        self.brand = brand
        self.name = name
        self.core_count = core_count
        self.usage = usage
        self.avg_freq = avg_freq
        self.max_freq = max_freq
        self.integrated_graphics = integrated_graphics




def cpu_suggestion(current_specs: CPU_Specs):
    cpu_data = import_cpu()

    scale_factor = 3.0 / 2.0
    scaled_usage = min(current_specs.usage / 100.0 * scale_factor , 1.0)
    target_frequency_ghz = scaled_usage * current_specs.avg_freq / 1000.0

    current_cpu_infos = None
    for cpu in cpu_data:
        if current_specs.brand == cpu["Brand"] and current_specs.name == cpu["Name"]:
            current_cpu_infos = cpu
    
    # TODO: Remove this
    assert current_cpu_infos is not None, "TODO error: Must handle this case"

    min_cpu = None
    min_freq = target_frequency_ghz * 2.0
    min_TDP = float(current_cpu_infos["TDP"].split(" ")[0])

    for cpu in cpu_data:
        # check compatibility:
        if cpu["Socket"] != current_cpu_infos["Socket"]:
            continue

        compared_clock = cpu["Clock"]
        compared_clock = compared_clock.split(" ")
        compared_clock = float(compared_clock[-2]) if compared_clock[-1] == "GHz" else float(compared_clock[-2]) / 1000
        compared_TDP = float(cpu["TDP"].split(" ")[0])

        should_replace = compared_clock >= target_frequency_ghz and compared_TDP <= min_TDP
        if should_replace and compared_TDP == min_TDP:
            should_replace = compared_clock < min_freq

        if should_replace:
            min_cpu = cpu
            min_freq = compared_clock
            min_TDP = compared_TDP

    print("suggestion CPU: ", min_cpu)
    print("suggestion FREQ (GHz): ", min_freq)
    print("suggestion TDP: ", min_TDP)







if __name__ == "__main__":
    pass
