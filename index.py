import inspect
import os
from pathlib import Path
import dominate
from dominate.tags import *
from dominate.util import raw

from templates import header, authors_row


def scroll_hint():
    """A subtle, muted hint to scroll horizontally."""
    p(
        raw("&#x2194; Scroll horizontally to explore additional columns."),
        cls="text-muted small mt-2 mb-0",
    )


# Where to save the generated file.
root_path = Path(inspect.getfile(inspect.currentframe())).parent
doc = dominate.document(title=None)

with doc.head:
    meta(charset="utf-8")
    meta(http_equiv="X-UA-Compatible", content="IE=edge")
    meta(name="viewport", content="width=device-width, initial-scale=1")
    title("Accent Normalization Demo")
    link(
        href="/demo/statics/bootstrap-5.2.3-dist/css/bootstrap.min.css",
        rel="stylesheet",
    )
    link(href="/demo/statics/my.css", rel="stylesheet")

with doc:
    # Title and Metadata:
    with div(cls="container").add(div(cls="row")):
        with div(cls="container pt-5 mt-5 shadow p-5 mb-5 bg-white rounded"):
            header(
                title="Controllable Accent Normalization via Discrete Diffusion",
                sub="",
            )
            br()
            from abstract import section_abstract

            section_abstract()
            p(
                "You can download all audio files on this page by cloning this",
                a(
                    "github repository",
                    href="https://github.com/dlm-an/demo",
                ),
                ".",
                cls="lead",
            )

        with div(cls="container pt-5 mt-5 shadow p-5 mb-5 bg-white rounded"):
            from comparison_systems import get_table

            h3("General System Comparison")
            p(
                raw(
                    "Each column corresponds to a different speaker utterance and each row to a different system. "
                    "The first row contains the <strong>original accented source</strong> audio; "
                    "subsequent rows show the accent-normalized outputs from various systems."
                ),
                cls="lead",
            )
            with div(cls="alert alert-light border py-2 px-3 mb-3"):
                p(
                    raw(
                        "<strong>Naming convention:</strong> "
                        "<strong>-1</strong>&nbsp;systems are <em>duration-free</em> (no total-duration constraint); "
                        "<strong>-2</strong>&nbsp;systems are <em>duration-controlled</em> (preserving the source total duration)."
                    ),
                    cls="mb-1",
                )
                p(
                    raw(
                        "<strong>DLM-AN-2 threshold:</strong> "
                        "Controls accent strength via token reuse &mdash; "
                        "<code>threshold&thinsp;=&thinsp;1.0</code> generates entirely from scratch (strongest normalization), "
                        "while <code>threshold&thinsp;=&thinsp;0.0</code> resynthesizes with all source tokens (original accent preserved)."
                    ),
                    cls="mb-0",
                )
            get_table()
            scroll_hint()


        with div(cls="container pt-5 mt-5 shadow p-5 mb-5 bg-white rounded"):
            from comparison_proportion import get_table

            h3(raw("Accent Strength Control &mdash; Proportion of Token Reuse"))
            p(
                raw(
                    "This panel demonstrates smooth accent strength control by varying the <em>proportion</em> of source tokens reused during generation. "
                    "A higher proportion retains more of the original accent; a lower proportion yields stronger normalization."
                ),
                cls="lead",
            )
            with ul(cls="list-group list-group-flush mb-3"):
                li(
                    raw(
                        "<strong>Proportion&thinsp;=&thinsp;1.00</strong> (top row) &mdash; "
                        "Full resynthesis: all source tokens are reused, preserving the original accent."
                    ),
                    cls="list-group-item py-1",
                )
                li(
                    raw(
                        "<strong>Proportion&thinsp;=&thinsp;0.00</strong> (bottom row) &mdash; "
                        "Generation from scratch: no source tokens are reused, maximizing accent normalization."
                    ),
                    cls="list-group-item py-1",
                )
            get_table()
            scroll_hint()

        with div(cls="container pt-5 mt-5 shadow p-5 mb-5 bg-white rounded"):
            from comparison_threshold import get_table

            h3(raw("Accent Strength Control &mdash; Thresholding Token Reuse"))
            p(
                raw(
                    "This panel demonstrates accent strength control via <em>thresholding</em>. "
                    "The Common Token Predictor assigns each source token a probability of being native-like; "
                    "only tokens whose probability exceeds the threshold are reused."
                ),
                cls="lead",
            )
            with ul(cls="list-group list-group-flush mb-3"):
                li(
                    raw(
                        "<strong>Threshold&thinsp;=&thinsp;0.00</strong> (top row) &mdash; "
                        "All tokens pass the threshold and are reused (resynthesis, original accent preserved)."
                    ),
                    cls="list-group-item py-1",
                )
                li(
                    raw(
                        "<strong>Threshold&thinsp;=&thinsp;1.00</strong> (bottom row) &mdash; "
                        "No tokens pass the threshold (generation from scratch, strongest normalization)."
                    ),
                    cls="list-group-item py-1",
                )
            get_table()
            scroll_hint()

        with div(cls="container pt-5 mt-5 shadow p-5 mb-5 bg-white rounded"):
            from comparison_duration_scaling import get_table

            h3(raw("Duration Control &mdash; Scaling the Total Duration"))
            p(
                raw(
                    "This panel showcases DLM-AN's ability to control the total duration of generated speech. "
                    "The Duration Ratio Predictor scales the source utterance length by a given factor: "
                    "<strong>&times;0.75</strong> produces faster speech, "
                    "<strong>&times;1.0</strong> preserves the original duration, and "
                    "<strong>&times;1.25</strong> produces slower speech &mdash; "
                    "all while maintaining the same level of accent normalization."
                ),
                cls="lead",
            )
            get_table()
            scroll_hint()

with doc.footer:
    script(src="/statics/jquery/jquery-3.7.1.slim.min.js")
    script(src="/statics/bootstrap-5.2.3-dist/bootstrap.min.js")

# Script for allowing only one audio to play at the same time:
doc.children.append(
    script(
        raw(
            """ $(function(){
        $("audio").on("play", function() {
            $("audio").not(this).each(function(index, audio) {
                audio.pause();
                audio.currentTime = 0;
            });
        });
    }); """
        )
    )
)

with open(root_path / "index.html", "w") as index:
    index.write(doc.render())
