from system_samples_info import samples
from templates import accent_filter_tabs, build_accent_table


systems = [
    ("Source", "source", "{spk}_{sid}.wav"),
    ("TokAN-1", "tokan_1", "{spk}_{sid}.wav"),
    ("TokAN-2", "tokan_2", "{spk}_{sid}.wav"),
    ("CosyAccent-1", "cosyaccent_1", "{spk}_{sid}.wav"),
    ("CosyAccent-2", "cosyaccent_2", "{spk}_{sid}.wav"),
    ("DLM-AN-1", "dlman_1", "{spk}_{sid}.wav"),
    ("DLM-AN-2 (Threshold=1.0)", "dlman_2", "{spk}_{sid}.wav"),
    ("DLM-AN-2 (Threshold=0.3)", "dlman_2_reuse", "{spk}_{sid}.wav"),
    ("DLM-AN-2 (Threshold=0.0)", "dlman_2_resynthesis", "{spk}_{sid}.wav"),
]


def get_table(root="./samples", control_width_px=240):
    accent_filter_tabs("table-systems", samples)
    build_accent_table(
        "table-systems", systems, samples, root, control_width_px,
        highlight_prefixes=["DLM-AN"],
    )
