from dominate.tags import *
from dominate.util import raw


def section_abstract():
    h3("Abstract")
    p(
        raw(
            """
            Existing accent normalization methods do not typically offer control over accent strength, yet many applications—such as language learning and dubbing—require tunable accent retention. We propose DLM-AN, a controllable accent normalization system built on masked discrete diffusion over self-supervised speech tokens. A Common Token Predictor identifies source tokens that likely encode native pronunciation; these tokens are selectively reused to initialize the reverse diffusion process. This provides a simple yet effective mechanism for controlling accent strength: reusing more tokens preserves more of the original accent. DLM-AN further incorporates a flow-matching Duration Ratio Predictor that automatically adjusts the total duration to better match the native rhythm. Experiments on multi-accent English data show that DLM-AN achieves the lowest word error rate among all compared systems while delivering competitive accent reduction and smooth, interpretable accent strength control.
            """
        ),
        _class="lead",
    )
