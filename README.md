# Unfold MCP server

Give your AI agent the content of PDF, Word (DOCX), PowerPoint (PPTX) and Excel (XLSX) documents as Markdown, from a URL or a local file.

The server is open source (MIT). It calls the [Unfold API](https://unfold.hybridforgelab.com), which is paid, with a free plan.

- You use **your own RapidAPI key**.
- Every tool call is one request on your plan.
- The free Basic plan has 15 requests a month, with a hard limit, so it never runs up a bill.

## 1. Get a key

| marketplace | |
|---|---|
| RapidAPI | [plans](https://rapidapi.com/hybrid-forge-lab-hybrid-forge-lab-default/api/unfold-document-to-markdown-api/pricing) |

## 2. Add the server to your MCP client

The server runs locally over stdio with [uv](https://docs.astral.sh/uv/). Put your key in its environment.

**JSON configuration** (Claude Desktop, Cursor, VS Code and most clients):

```json
{
  "mcpServers": {
    "unfold": {
      "command": "uvx",
      "args": ["--from", "hybridforgelab-unfold-mcp", "unfold-mcp"],
      "env": { "RAPIDAPI_KEY": "your-rapidapi-key" }
    }
  }
}
```

**Claude Code:**

```bash
claude mcp add unfold --env RAPIDAPI_KEY=your-rapidapi-key -- uvx --from hybridforgelab-unfold-mcp unfold-mcp
```

### Environment

| variable | meaning |
|---|---|
| `RAPIDAPI_KEY` | your RapidAPI key |

Without a key the server still starts. The first tool call then explains where to get one.

## 3. Tools

| tool | what it does |
|---|---|
| `convert_document(url=… \| path=…, max_chars=20000)` | converts one document to Markdown; give a public URL, or a local file to upload |

The format is detected from the content.

Every tool returns the API's JSON response.

- When the marketplace reports it, `quota_remaining` is added: the requests left on your plan this month.
- Errors are explained in plain words, with what to do next:
  - key refused, with the link to subscribe;
  - quota reached, with the plans;
  - input the API couldn't process, with the API's reason.

## Privacy

- Local files are read only when a tool is given their path. They are sent to the API for that one request.
- The API processes inputs in memory and doesn't store them. See the [privacy policy](https://unfold.hybridforgelab.com/privacy.html).
- Your key is only sent to the marketplace you chose.

## Limits

- Local files up to 10 MB.
- Markdown up to 500,000 characters.
- The server needs Python 3.10+ (uv installs it for you).

## Development

```bash
uv venv && uv pip install -e ".[dev]"
.venv/bin/pytest            # unit tests, no network; 100% coverage required
.venv/bin/ruff check src tests scripts
```

`scripts/e2e_stdio.py unfold` runs the server over stdio, as a client would, and calls its tools against the real API. It needs `RAPIDAPI_KEY`.

## Licence

MIT. Unfold itself is a paid API with a free plan, run by [Hybrid Forge Lab](https://hybridforgelab.com).
