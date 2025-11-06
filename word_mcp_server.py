#!/usr/bin/env python3
"""
Run script for the Word Document Server.

This script provides a simple way to start the Word Document Server.
"""

import os

from word_document_server.main import run_server


def ensure_default_transport():
    """Make sure SSE is the default so an HTTP endpoint is available."""

    if os.getenv("MCP_TRANSPORT"):
        # User already set a transport, keep their choice.
        return

    # Use SSE by default so the server exposes http://localhost:8080/md2doc.
    os.environ["MCP_TRANSPORT"] = "sse"
    # Host/port/path defaults allow quick local testing without extra setup.
    os.environ.setdefault("MCP_HOST", "0.0.0.0")
    os.environ.setdefault("MCP_PORT", "8080")
    os.environ.setdefault("MCP_SSE_PATH", "/md2doc")
    print("未检测到 MCP_TRANSPORT，已默认启用 SSE，可访问 http://localhost:8080/md2doc")


if __name__ == "__main__":
    ensure_default_transport()
    run_server()
