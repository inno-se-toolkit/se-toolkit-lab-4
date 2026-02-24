---
name: review-meeting-report
description: Review a meeting report against the transcript and files discussed
argument-hint: "<lab-number> <iteration-number>"
---

Review the meeting report for lab N, iteration M by cross-checking it against the transcript and the files discussed during the meeting.

## Steps

1. Parse `$ARGUMENTS` to extract N (lab number) and M (iteration number). Both are required — if missing, ask the user.
2. Read `instructors/context/meeting-report/meeting-report-prompt.md` for the report format rules.
3. Read `instructors/lab-design/lab-N/iteration-M/meeting-report.md` (substituting actual N and M).
4. Read `instructors/lab-design/lab-N/iteration-M/meeting-transcripts/transcript-by-speaker.txt`.
5. If the report's **Metadata → Files discussed** section lists any files, read each of them.
6. Produce a review covering the categories below. For each finding, cite the relevant transcript timestamp or report line so the author can locate it quickly.

## Review categories

### A. Transcript coverage

Go through the transcript **line by line**. Flag each substantive point, decision, question, disagreement, example, or topic that appears in the transcript but is **missing or under-represented** in the report. Ignore filler, greetings, and non-substantive noise.

### B. Accuracy

Flag each claim in the report that **contradicts** the transcript — wrong speaker attribution, incorrect timestamp, misquoted text, a decision recorded as unanimous when there was dissent, etc.

### C. Files discussed

For every file listed under **Metadata → Files discussed**:

- Verify that the report's references to that file's content (task names, structure, terminology, etc.) are **consistent** with the actual file content.
- Flag each reference in the report that does not match what the file actually says.

If no files are listed, skip this category and note that explicitly.

### D. Format compliance

Check the report against the rules in `meeting-report-prompt.md`. Flag violations — missing sections, items written as bullet lists instead of subsections, bold labels used instead of headings, PII leaks, missing cross-references, etc.

### E. Internal consistency

Check for contradictions **within** the report itself — e.g., a decision that conflicts with an open question, an action point referencing a non-existent decision, broken anchor links, duplicate numbering, etc.

## Output format

Write the review directly in the conversation. Use a heading for each category (A–E). Under each heading, list findings as numbered items. If a category has no findings, write "No issues found." At the end, add a **Summary** section with a short overall assessment.
