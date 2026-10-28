name: Knowledge-base integrity

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

permissions:
  contents: read

jobs:
  validate-knowledge:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Validate book index, topic graph and links
        run: python3 scripts/validate_library.py

## Discussions 类别与投稿表单

- 当前类别设计与手动设置步骤见 [DISCUSSIONS_SETUP.md](DISCUSSIONS_SETUP.md)。
- 自定义类别在 GitHub 网页端管理；对应的表单文件放在 `.github/DISCUSSION_TEMPLATE/<category-slug>.yml`。
- 不要将类别表单文件已提交误报为 GitHub 类别已创建。类别 slug 与表单文件名必须对应。
- 第一条欢迎讨论的正文可从 [templates/discussion-welcome.md](templates/discussion-welcome.md) 复制。
