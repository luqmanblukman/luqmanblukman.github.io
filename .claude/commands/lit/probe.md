---
description: Socratic questions on one area of a review, starting with open questions
argument-hint: <review path> [area: problem | context | method | evaluation | evidence | limitations | reproducibility | research-context]
---
Follow `AGENTS.md`. Run in the main conversation; this is a dialogue. Input: $ARGUMENTS

1. Read the review and get the paper (see `.claude/agents/paper-critic.md`). If no area was given, ask which one.
2. Ask **one** question at a time, at **rung 1** of the hint ladder (open question, no locations, no named concern). Aim at the weakest point in his treatment of that area.
3. Respond to his answer by asking a follow-up that goes one level deeper, or by moving to the next question. Don't confirm a right answer at length, and don't reveal what you were looking for.
4. Stay at rung 1 unless he runs `/lit:hint` or asks for a hint. Track the current rung per question.
5. Stop after 5 questions or when he says so. Then list the questions asked and the rung each ended on, without answers.

End with:
---
**Next step:** Fold anything new into the review yourself, then `/lit:critique` or `/lit:verify`.
