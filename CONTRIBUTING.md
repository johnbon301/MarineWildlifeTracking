# Contributing

This file describes how our team works, where work lives, what "done" means, how
reviews happen, and what each of us commits to every sprint. Everyone on the team
is expected to follow it. If something here stops matching how we actually work,
open an issue and fix the file. Don't just ignore it.

## Table of Contents

- [Team and Ownership](#team-and-ownership)
- [Where Work Lives](#where-work-lives)
- [Workflow](#workflow)
- [Definition of Done](#definition-of-done)
- [Review Expectations](#review-expectations)
- [The Contribution Norm](#the-contribution-norm)
  - [Sprint contribution lines](#sprint-contribution-lines)
- [Checkpoint Submission](#checkpoint-submission)
- [AI-Assisted Work](#ai-assisted-work)
- [Reporting Bugs and Asking Questions](#reporting-bugs-and-asking-questions)
- [Styleguides](#styleguides)
- [Code of Conduct](#code-of-conduct)

## Team and Ownership

| Member | Primary area | Owns these gates (see Definition of Done) |
|---|---|---|
| Jonathan | Tests | Test coverage and the test job (#4) |
| Alex | Repository checks | Branch rules, required reviews, CI status, and dependency alerts (#1, #2, #5, #7) |
| Cash | Tooling and partner contact | Formatting, lint, and checks for secrets and large files (#3, #6) |
| Conner | Documentation | Documentation review, including changes to setup and usage (#8) |

Our project partner is Marg Daly at Pacific Northwest National Laboratory.
Cash handles partner contact. Sprint issues identify who owns each deliverable.

## Where Work Lives

| Kind of work | Where it lives |
|---|---|
| Code, configs, scripts | This GitHub repository |
| Tasks, bugs, planning | [GitHub Issues](https://github.com/johnbon301/MarineWildlifeTracking/issues). Assign an owner and identify the sprint on each issue |
| Design docs, research notes, experiment results | In this repository (Markdown) |
| Partner deliverables | The location agreed with PNNL. Record the deliverable and its acceptance in the matching issue |
| Large data / model weights | Storage approved for the dataset. **Keep large data and weights out of Git.** Commit only shareable paths and download scripts |

Every piece of work, including research and writing, starts as an issue on the
board. If it isn't in an issue, it doesn't count toward the contribution norm.

## Workflow

1. Pick or create an issue for the sprint. Assign yourself and write what the
   reviewer can check when the work is ready.
2. Create a branch from `main` named `<issue-number>-short-description`
   (e.g. `14-add-tile-loader`).
3. Commit early and often. Push your branch.
4. Open the PR from your own GitHub account. Link the issue (`Closes #14`),
   describe what changed, and say how you checked it. Complete the PR checklist
   if one is available. For paired work, name each contributor and their part.
5. Request a review from a teammate who did not author the change. The reviewer
   records approval on the PR before merge. See [Review Expectations](#review-expectations).
6. The author squash-merges to `main` after approval and the applicable checks
   pass. The merged PR keeps the author, diff, review, and merge date together.

Nobody pushes directly to `main`.

## Definition of Done

A repository change is done when it is **merged to `main`** and every applicable
check below passes. The author and reviewer share responsibility for the checks.
Until an automated check is in place, the reviewer checks the item by hand.

| # | Check | Enforced by | Status | Owner |
|---|---|---|---|---|
| 1 | All changes to `main` go through a PR | Merge from the PR. Use branch protection to block direct pushes | Required for each merge | Alex |
| 2 | At least one teammate who did not author the change approves it before merge | Reviewer selects **Approve** on the PR. Use branch protection to require one approval | Required for each merge | Alex |
| 3 | Code is formatted and passes lint | Run `ruff check` and `ruff format --check` for Python changes | Pre-commit hook and CI lint job planned for Sprint 2 | Cash |
| 4 | Tests pass and cover new logic | Author records the test command and result. Reviewer checks the result | CI test job planned for Sprint 2 | Jonathan |
| 5 | CI passes before merge | Reviewer checks the run for the PR's latest commit | Required status checks planned after #3 and #4 | Alex |
| 6 | The change contains no secrets, API keys, large datasets, or model weights | Reviewer inspects the changed files | `detect-secrets` and `check-added-large-files` hooks planned for Sprint 2 | Cash |
| 7 | Dependencies have no known high-severity vulnerabilities | Reviewer checks alerts for affected dependencies | Dependabot alerts planned for Sprint 2 | Alex |
| 8 | Docs reflect changes to behavior, constraints, setup, or usage | Reviewer checks the affected sections and follows any changed README quickstart from a clean clone | Required when docs are affected | Conner |
| 9 | The change meets the linked issue's acceptance criteria | Reviewer compares the change with the issue. `Closes #N` closes the issue on merge | Required for each issue | Whole team |

When a gate lands, its owner updates the Status column in this file in the same
PR that adds the gate.

## Review Expectations

- **Who reviews:** request a teammate familiar with the affected work. For paired
  work, ask someone outside the pair. If someone else opens the PR on your
  behalf, identify who wrote the change and request an independent review.
- **Turnaround:** reviewers respond within **48 hours** of being requested
  (24 hours in the last 3 days of a sprint). If you can't review in time, say so
  on the PR so the author can ask someone else.
- **What a review checks:** the Definition of Done items, whether the code does
  what the issue asked, and whether someone else could understand and maintain it.
  Record what you tested, read, or compared. Use **Approve** when the change is ready.
- **Feedback:** comments marked `nit:` are optional. Anything else must be
  resolved or discussed before approval.
- **Size:** keep PRs small enough to review in about 20 minutes (roughly under
  400 changed lines). Split larger work into multiple PRs.
- **Stuck PRs:** if a PR has had no review after 48 hours, raise it at the next
  standup or in the team channel.

## The Contribution Norm

**Every team member owns at least one piece of accepted work per sprint**, as
defined by the course's [contribution lines](https://capstone.alexulbrich.com/assignments/sprint-notes/).
This norm feeds the individual contribution modifier on Sprint Notes, so we
follow it as written.

### What "accepted" means

| Kind of work | Accepted when |
|---|---|
| Code | A teammate approved the PR before it merged to `main`, and it meets the Definition of Done |
| Documentation / design docs | A teammate approved the PR that added or changed the document, and it merged to `main` |
| Research (paper reviews, model comparisons) | Written summary merged to `docs/research/`, with a teammate's approval |
| Experiments / training runs | Results (metrics, config, notes) merged to `docs/experiments/` and reviewed |
| Partner deliverables | The issue names the contributor, identifies the delivered version, and records who accepted it and when. Cash records PNNL's confirmation there when it happens outside GitHub |

Work that is in progress, sitting in an unmerged branch, or unreviewed does not
count yet.

### Sprint contribution lines

Each member writes one line in the Sprint Notes for a piece they owned. Use the
links a reviewer can open to see the work and the decision.

```text
Name (@GitHub account) | What I delivered | Issue link | Merged PR or accepted artifact link | Accepted by whom and when
```

Before submitting the notes, a teammate opens each link and checks the owner,
the specific change, the approval, and the merge or acceptance date against the
sprint dates. For paired work, each line names that person's part. If a review
is missing or the work is still open, report its actual status. If no piece was
accepted for a member, say so on their line. Each member adds a sentence in
their own words about how their main contribution was checked.

### How we make it workable

- **Pairing:** when work is hard to split (e.g. setting up the training
  environment), we pair. The issue lists one owner and one pair partner, and each
  person owns a distinct accepted piece (e.g. one writes the code, the other
  writes the tests or the docs).
- **Early warning:** if your piece is at risk of not landing by mid-sprint, say
  so at standup so it can be resized or you can get help.
- **Review turnaround:** the 48-hour review rule above exists so no one misses
  the norm because they were waiting on a reviewer.

## AI-Assisted Work 

AI coding tools are allowed. Our AI context file, [`AGENTS.md`](AGENTS.md),
describes the project, conventions, and commands for those tools, and it is
updated in the same PR whenever those change. You are responsible for every line
you submit, whether you or a tool wrote it. AI-generated code goes through the
same Definition of Done and review as anything else.

## Reporting Bugs and Asking Questions

- Search existing [issues](https://github.com/johnbon301/MarineWildlifeTracking/issues) first.
- Otherwise open a new issue with: what you expected, what happened, steps to
  reproduce, and relevant versions (Python, OS, library versions).
- Label it `bug`, `question`, or `enhancement`.
- Never put secrets, credentials, or partner-confidential data in an issue.
  For partner data, contact Cash privately.

## Styleguides

### Code

- TBD by the team depending on the image detection model framework.

### Commit Messages

Use short, imperative summaries that reference the issue:

```
Add tile loader for aerial images (#14)
Fix off-by-one in bbox scaling (#22)
```

## Code of Conduct

Be respectful, give constructive feedback, and assume good intent. Report
problems to the team.

Be respectful, give constructive feedback, and assume good intent. Report
problems to the team.
