---
name: get-meeting-transcript
description: Process a meeting transcript for a given lab and iteration
argument-hint: "<lab-number> <iteration-number>"
---

Process the meeting transcript for lab N, iteration M.

## Steps

1. Parse `$ARGUMENTS` to extract N (lab number) and M (iteration number). Both are required — if missing, ask the user.
2. Run `python lab/lab-design/process-transcript.py lab/lab-design/lab-N/iteration-M/meeting-transcripts` (substituting the actual values of N and M).
3. Do NOT summarize, analyze, or comment on the output. Just confirm the command ran successfully.
