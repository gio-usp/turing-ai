#!/bin/bash
pip install -r requirements.txt > /dev/null && fastapi dev --host 0.0.0.0 src/main.py