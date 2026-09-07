"""Encoding rules for shields.io badge URLs."""

from __future__ import annotations

from urllib.parse import quote


def shields_segment(text: str) -> str:
    """Encode one segment of a shields.io badge path.

    In a shields URL '-' delimits the label/message/colour segments, '_' means
    a space, and '__' means a literal underscore. Those are escaped first, then
    the result is percent-encoded.

    Known limitation: an underscore adjacent to a space cannot round-trip through
    shields.io's decoding, since both "literal underscore" and "space" render as
    runs of '_' and are decoded greedily. For example, "a _b" and "a_ b" both
    encode to "a___b", but shields.io decodes "a___b" to "a_ b". Badge text
    should avoid underscore-space combinations to prevent silent data loss.
    """
    if not isinstance(text, str):
        raise TypeError(f"shields_segment expects str, got {type(text).__name__}: {text!r}")
    escaped = text.replace("_", "__").replace("-", "--").replace(" ", "_")
    return quote(escaped, safe="_.")
