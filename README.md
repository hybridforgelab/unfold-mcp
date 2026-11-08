# hybridforgelab-unfold-mcp: moved to bytestay-unfold-mcp

This package has moved to **[bytestay-unfold-mcp](https://pypi.org/project/bytestay-unfold-mcp/)**. Hybrid Forge Lab is now ByteStay.

This last version only installs bytestay-unfold-mcp and forwards to it. It prints a one-line notice on stderr and gets no more updates.

## Switch

Replace `hybridforgelab-unfold-mcp` with `bytestay-unfold-mcp` in your MCP client config:

```json
"command": "uvx",
"args": ["--from", "bytestay-unfold-mcp", "unfold-mcp"]
```

Or with Claude Code:

```bash
claude mcp add unfold --env RAPIDAPI_KEY=your-rapidapi-key -- uvx --from bytestay-unfold-mcp unfold-mcp
```

The environment variables are the same, so your keys keep working.

## Links

- Package: [bytestay-unfold-mcp](https://pypi.org/project/bytestay-unfold-mcp/)
- Source: [Bytestay/unfold-mcp](https://github.com/Bytestay/unfold-mcp)
- Unfold API: [unfold.bytestay.pt](https://unfold.bytestay.pt)
