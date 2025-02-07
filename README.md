# Week in Review assistant

A Python-based tool that generates personalized "Week in Review" reports by analyzing multiple data sources including:

- Personal journal entries (via jrnl)
- Git commit history

The assistant processes this data to create a structured review that:

1. Identifies and groups key themes
2. Highlights important entries for each theme
3. Summarizes wins, learnings, and planned actions

## Features

- Modular data source system (easily extendable)
- Customizable system prompts for report generation
- Support for multiple git repositories
- Integration with jrnl for personal notes

## Configuration

Create a `config.yaml` file to customize the assistant's behavior:

see example in `config.example.yaml`

```yaml
system_prompt: |
  Custom prompt to guide the report generation
  Base on following data create a "Week in Review" report...

data_sources:
  # Journal entries from jrnl
  - type: jrnl
    name: "Personal journal entries"
  
  # Git commit history from specified repositories
  - type: git_commits
    name: "Git commits" 
    repositories:
      - "/path/to/your/repository"
```

### Data Sources

- **jrnl**: Analyzes entries from your jrnl journal
- **git_commits**: Processes commit history from specified git repositories

## Usage

Grab the output from the CLI and paste it into your favorite AI chat.

```bash
python cli.py | pbcopy
```
