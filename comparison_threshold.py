from threshold_samples_info import samples
from templates import accent_filter_tabs, build_accent_table


systems = [
    ("Source", "source", "{spk}_{sid}.wav"),
    ("Threshold=0.00 (Resynthesis)", "threshold_0.0", "{spk}_{sid}.wav"),
    ("Threshold=0.01", "threshold_0.01", "{spk}_{sid}.wav"),
    ("Threshold=0.10", "threshold_0.1", "{spk}_{sid}.wav"),
    ("Threshold=0.30", "threshold_0.3", "{spk}_{sid}.wav"),
    ("Threshold=0.50", "threshold_0.5", "{spk}_{sid}.wav"),
    ("Threshold=0.70", "threshold_0.7", "{spk}_{sid}.wav"),
    ("Threshold=0.90", "threshold_0.9", "{spk}_{sid}.wav"),
    ("Threshold=0.99", "threshold_0.99", "{spk}_{sid}.wav"),
    ("Threshold=1.00 (From-scratch)", "threshold_1.0", "{spk}_{sid}.wav"),
]


def get_table(root="./samples", control_width_px=240):
    accent_filter_tabs("table-threshold", samples)
    build_accent_table("table-threshold", systems, samples, root, control_width_px)
