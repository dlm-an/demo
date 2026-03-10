from duration_scaling_samples_info import samples
from templates import accent_filter_tabs, build_accent_table


systems = [
    ("Source", "source", "{spk}_{sid}.wav"),
    ("Duration x0.75", "duration_x0.75", "{spk}_{sid}.wav"),
    ("Duration x1.0", "dlman_2", "{spk}_{sid}.wav"),
    ("Duration x1.25", "duration_x1.25", "{spk}_{sid}.wav"),
]


def get_table(root="./samples", control_width_px=240):
    accent_filter_tabs("table-duration", samples)
    build_accent_table("table-duration", systems, samples, root, control_width_px)
