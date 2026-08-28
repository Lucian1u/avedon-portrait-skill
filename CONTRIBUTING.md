# 参与项目

先读 [`SKILL.md`](SKILL.md) 和 [`references/`](references/)。改规则要能指到 corpus 记录，不要只靠感觉改。

## 不要做的事

- 不要把侧脸、背影、半张脸改成正脸
- 不要为了拿到 `supported` 标签多裁一刀
- 不要把 In the American West 套到用户没要求的人身上
- 不要提交 Avedon 照片或其它版权图片；验收图只放在 `evals/visual/`，而且必须是合成夹具
- 不要把没看过的候选写成风格结论

## 改规则时

1. 先改 `research/` 里的标注或发现
2. 再改 `references/` 里对应的那一处，不要把同一条规则复制到多份文件
3. 跑 `python3 scripts/validate_research.py`
4. 如果动了生成行为，补 [`evals/cases.yaml`](evals/cases.yaml) 或 [`evals/visual/visual-results.md`](evals/visual/visual-results.md)

## Pull request

写清改了哪条规则、依据哪些 `record_id`、跑过哪条验证。一次只做一件事。
