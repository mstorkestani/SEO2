#!/usr/bin/env python3
"""
Simple command‑line utility to run prompts against OpenAI’s ChatCompletion API.

The script accepts a prompt string or a text file containing a prompt and
allows you to adjust the `temperature` and `top_p` sampling parameters.  It
prints the model’s response to standard output.  Set your OpenAI API key via
the `OPENAI_API_KEY` environment variable or the `--api-key` argument.

Usage examples::

    python run_prompts.py --prompt "Write a meta description for ..." --temperature 0.5 --top-p 0.9
    python run_prompts.py --prompt-file ../prompts/seo_prompts.txt --temperature 0.7

Note: You must install the `openai` package to use this script (pip install openai).
"""
import argparse
import os
import sys
from typing import Optional

def read_prompt(path: str) -> str:
    """Read a prompt from a file.  Strips trailing newlines."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()

def get_openai_client(api_key: str):
    """Lazy import openai and set the API key."""
    try:
        import openai  # type: ignore
    except ImportError as e:
        raise SystemExit(
            "The 'openai' package is not installed. Please run 'pip install openai' before using this script."
        ) from e
    openai.api_key = api_key
    return openai

def call_openai(prompt: str, model: str, temperature: float, top_p: float, api_key: str) -> str:
    """Send the prompt to OpenAI and return the response text."""
    openai = get_openai_client(api_key)
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            top_p=top_p,
        )
    except Exception as exc:
        raise SystemExit(f"API request failed: {exc}") from exc
    # The completion API returns a list of choices; take the first one
    return response.choices[0].message["content"].strip()

def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Run a prompt against OpenAI's chat completion API")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--prompt", type=str, help="Prompt text to send to the model")
    group.add_argument("--prompt-file", type=str, help="Path to a file containing the prompt")
    parser.add_argument("--model", type=str, default="gpt-3.5-turbo", help="OpenAI model name (default: gpt-3.5-turbo)")
    parser.add_argument("--temperature", type=float, default=0.7, help="Sampling temperature (0.0–2.0)")
    parser.add_argument("--top-p", type=float, default=1.0, help="Top‑p sampling value (0.0–1.0)")
    parser.add_argument("--api-key", type=str, default=os.environ.get("OPENAI_API_KEY", ""), help="OpenAI API key (overrides environment)")

    args = parser.parse_args(argv)
    if not args.api_key:
        parser.error("No API key provided. Set OPENAI_API_KEY or use --api-key.")
    # Load the prompt
    if args.prompt_file:
        if not os.path.exists(args.prompt_file):
            parser.error(f"Prompt file not found: {args.prompt_file}")
        prompt = read_prompt(args.prompt_file)
    else:
        prompt = args.prompt
    # Call the API
    text = call_openai(prompt=prompt, model=args.model, temperature=args.temperature, top_p=args.top_p, api_key=args.api_key)
    print(text)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())