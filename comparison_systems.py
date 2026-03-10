from dominate.tags import *


systems = [
    ("Source", "source", "{spk}_{sid}.wav"),
    ("TokAN-1", "tokan_1", "{spk}_{sid}.wav"),
    ("TokAN-2", "tokan_2", "{spk}_{sid}.wav"),
    ("CosyAccent-1", "cosyaccent_1", "{spk}_{sid}.wav"),
    ("CosyAccent-2", "cosyaccent_2", "{spk}_{sid}.wav"),
    ("DLM-AN-1", "dlman_1", "{spk}_{sid}.wav"),
    ("DLM-AN-2 (threshold=1.0)", "dlman_2", "{spk}_{sid}.wav"),
    ("DLM-AN-2 (threshold=0.3)", "dlman_2_reuse", "{spk}_{sid}.wav"),
    ("DLM-AN-2 (threshold=0.0)", "dlman_2_resynthesis", "{spk}_{sid}.wav"),
]

from system_samples_info import samples


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
