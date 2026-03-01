"""CLI entry point for das-server."""

import argparse


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="das-server",
        description="Run the DAS search API server.",
    )
    p.add_argument("--host", default="127.0.0.1", help="Bind host (default: 127.0.0.1)")
    p.add_argument("--port", type=int, default=8000, help="Bind port (default: 8000)")
    p.add_argument("--reload", action="store_true", help="Auto-reload on code changes")
    return p


def main():
    args = build_parser().parse_args()

    import uvicorn
    uvicorn.run(
        "das.server.app:app",
        host=args.host,
        port=args.port,
        reload=args.reload,
    )


if __name__ == "__main__":
    main()
