---
name: get-meeting-report
description: Generate a meeting report for a given lab and iteration
argument-hint: "<lab-number> <iteration-number>"
---

Generate a meeting report for lab N, iteration M.

## Steps

1. Parse `$ARGUMENTS` to extract N (lab number) and M (iteration number). Both are required — if missing, ask the user.
2. Read `instructors/context/meeting-report/meeting-report-prompt.md` for the report format and rules.
3. Read `instructors/lab-design/lab-N/iteration-M/meeting-transcripts/transcript-by-speaker.txt` (substituting actual N and M).
4. Following the rules and structure from the prompt file, write the meeting report to `instructors/lab-design/lab-N/iteration-M/meeting-report.md`.
5. Do NOT summarize, analyze, or comment on the report contents. Just confirm the file was written.
