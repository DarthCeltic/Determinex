from __future__ import annotations

import json


def render_sample_html() -> str:
    payload = {
        "status": "sample_only",
        "release_ready": False,
        "open_availability_ready": False,
        "authority_boundary": "closed",
    }
    return (
        "<html><body><pre>" + json.dumps(payload, indent=2, sort_keys=True) + "</pre></body></html>"
    )


def main() -> int:
    print(render_sample_html())
    return 0
