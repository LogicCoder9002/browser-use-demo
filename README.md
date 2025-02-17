# Browser-Use Demo

A demonstration project that integrates the [ChatGoogleGenerativeAI](https://github.com/your-link) model with the [browser-use](https://docs.browser-use.com/) library to perform automated web tasks using asynchronous Python code.

## Overview

This project showcases how to use a generative AI model (via `langchain_google_genai`) together with a browser automation agent (via `browser-use`). The example task demonstrated is:

> "Search for 'latest AI trends 2024' on Google and summarize the top result."

The project also demonstrates how to:
- Load sensitive configuration data (API keys) using a `.env` file and the `python-dotenv` library.
- Execute asynchronous code with Python's `asyncio`.

## Features

- **Generative AI Integration:** Uses `ChatGoogleGenerativeAI` to generate responses.
- **Browser Automation:** Leverages `browser-use` to interact with a browser for task execution.
- **Asynchronous Programming:** Uses `asyncio` to handle asynchronous tasks.
- **Secure Configuration:** Loads API keys from a `.env` file using `python-dotenv`.

## Prerequisites

- **Python 3.7+**: Make sure you have Python installed.
- **Git** (optional): For cloning the repository.
- A valid **Google API Key** for ChatGoogleGenerativeAI.
