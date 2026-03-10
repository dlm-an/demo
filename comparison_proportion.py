from proportion_samples_info import samples
from templates import accent_filter_tabs, build_accent_table


systems = [
    ("Source", "source", "{spk}_{sid}.wav"),
    ("Proportion=1.00 (Resynthesis)", "proportion_1.0", "{spk}_{sid}.wav"),
    ("Proportion=0.90", "proportion_0.9", "{spk}_{sid}.wav"),
    ("Proportion=0.70", "proportion_0.7", "{spk}_{sid}.wav"),
    ("Proportion=0.50", "proportion_0.5", "{spk}_{sid}.wav"),
    ("Proportion=0.30", "proportion_0.3", "{spk}_{sid}.wav"),
    ("Proportion=0.10", "proportion_0.1", "{spk}_{sid}.wav"),
    ("Proportion=0.00 (From-scratch)", "proportion_0.0", "{spk}_{sid}.wav"),
]


def get_table(root="./samples", control_width_px=240):
    accent_filter_tabs("table-proportion", samples)
    build_accent_table("table-proportion", systems, samples, root, control_width_px)
