#!/usr/bin/env python3
import app.models
from app import app

app.run('0.0.0.0', port=5000, debug=True)
