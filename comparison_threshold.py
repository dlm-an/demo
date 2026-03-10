from dominate.tags import *


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

from threshold_samples_info import samples


def get_table(
    root: str = "./samples",
    control_width_px=240,
) -> html_tag:
    _div = div(cls="table-responsive", style="overflow-x: scroll").add(
        table(cls="table table-sm")
    )
    with _div:
        with thead():
            with tr():
                th(
                    "Speaker (Accent)",
                    scope="row",
                    style="position: sticky; left: 0; z-index:10; opacity: 1.0; background-color: white;",
                )
                for spk, act, _, _ in samples:
                    th(f"{spk} ({act})", scope="col")
        with tbody():
            with tr():
                th(
                    "Text",
                    scope="row",
                    style="position: sticky; left: 0; z-index:10; opacity: 1.0; background-color: white;",
                )
                for _, _, _, text in samples:
                    td(p(text))

            for sys_name, sys_id, fname_pattern in systems:
                with tr():
                    th(
                        sys_name,
                        scope="row",
                        style="white-space: nowrap; position: sticky; left: 0; z-index:10; opacity: 1.0; background-color: white;",
                    )
                    for spk, _, key, _ in samples:
                        fname = fname_pattern.format(spk=spk, sid=key)
                        td(
                            audio(
                                source(
                                    src=f"{root}/{sys_id}/{fname}",
                                    type="audio/wav",
                                ),
                                controls="",
                                style=f"width: {control_width_px:d}px",
                                preload="none",
                            )
                        )
    return _div
