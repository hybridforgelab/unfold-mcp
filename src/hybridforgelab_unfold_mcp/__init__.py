"""hybridforgelab-unfold-mcp moved to bytestay-unfold-mcp. This package only forwards to it."""
import sys

__version__ = "0.3.0"

NOTICE = ("hybridforgelab-unfold-mcp has moved to bytestay-unfold-mcp. This name only forwards to it and gets no more updates. "
          "Switch your MCP config to: uvx --from bytestay-unfold-mcp unfold-mcp")


def main() -> None:
    """Print the notice on stderr (stdout is the MCP stdio channel), then run the ByteStay server."""
    print(NOTICE, file=sys.stderr, flush=True)
    from unfold_mcp.server import main as bytestay_main

    bytestay_main()
