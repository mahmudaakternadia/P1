# AI-Driven Disaster Relief Coordination Platform

## Overview

A platform to collect, analyze, and coordinate disaster relief operations using AI and human-in-the-loop workflows.

## Features

- Real-time situation reporting
- AI-driven needs assessment and resource matching
- Gradio dashboards for all users
- Modular, extensible MCP agent architecture

## Getting Started

### 1. Install requirements

```bash
cd backend
pip install -r requirements.txt
cd ../frontend
pip install gradio requests
```

### 2. Set up Environment Variables

Set your Hugging Face API key in your environment:

```bash
export HF_API_TOKEN=your_huggingface_token
```

### 3. Run backend

```bash
cd backend
uvicorn app:app --reload
```

### 4. Run frontend

```bash
cd ../frontend
python gradio_dashboard.py
```

## Credits

- Built for MCP Course Competition with support from Modal Labs, Hugging Face, OpenAI, and others.