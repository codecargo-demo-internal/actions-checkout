#!/usr/bin/env python3
"""
Simple Python application for release testing.
"""
import os


def main():
    """Main entry point."""
    version = os.getenv("APP_VERSION", "dev")
    print(f"Application started - version: {version}")


if __name__ == "__main__":
    main()
