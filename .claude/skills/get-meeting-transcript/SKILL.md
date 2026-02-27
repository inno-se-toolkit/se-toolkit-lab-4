---
name: get-meeting-transcript
description: Process a meeting transcript for a given lab and iteration
argument-hint: "<lab-number> <iteration-number> [--merge X=Y ...]"
---

Process the meeting transcript for lab N, iteration M.

## Steps

1. Parse `$ARGUMENTS` to extract N (lab number), M (iteration number), and any optional `--merge X=Y` flags. N and M are required — if missing, ask the user.
2. Run `python instructors/scripts/process-meeting-transcript/process-meeting-transcript.py instructors/lab-design/lab-N/iteration-M/meeting-transcripts` (substituting the actual values of N and M). Pass through any `--merge` flags as-is.
3. Do NOT summarize, analyze, or comment on the output. Just confirm the command ran successfully.
