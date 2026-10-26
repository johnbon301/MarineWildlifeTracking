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
- [AI-Assisted Work](#ai-assisted-work)
- [Reporting Bugs and Asking Questions](#reporting-bugs-and-asking-questions)
- [Styleguides](#styleguides)
- [Code of Conduct](#code-of-conduct)

## Team and Ownership

| Member | Primary area | Owns these gates (see Definition of Done) |
|---|---|---|
| Jonathan | [e.g. model training / evaluation] | [e.g. test suite, CI test job] |
| Cash | [e.g. data pipeline] | [e.g. lint + format hooks] |
| Alex | [e.g. infrastructure / tooling] | [e.g. CI workflow, branch protection] |
| Connor | [e.g. docs / partner liaison] | [e.g. PR template, docs check] |

Project partner: Marg Daly, Pacific Northwest National Laboratory. Partner contact goes through
Cash.

## Where Work Lives

| Kind of work | Where it lives |
|---|---|
| Code, configs, scripts | This GitHub repository |
| Tasks, bugs, planning | GitHub Issues, organized on the GitHub Projects board |
| Design docs, research notes, experiment results | In this repository (Markdown) |
| Partner deliverables | [Partner's system, e.g. shared Google Drive folder], with a link recorded in the matching issue |
| Large data / model weights | [e.g. OSU HPC storage / Google Drive]. **Never committed to git**; only paths and download scripts are committed |

Every piece of work, including research and writing, starts as an issue on the
board. If it isn't in an issue, it doesn't count toward the contribution norm.

## Workflow

1. Pick or create an issue on the board and assign yourself.
2. Create a branch from `main` named `<issue-number>-short-description`
   (e.g. `14-add-tile-loader`).
3. Commit early and often. Push your branch.
4. Open a pull request that references the issue (`Closes #14`) and fill out the
   PR template checklist.
5. Get the required review (see [Review Expectations](#review-expectations)).
6. The author merges once every Definition of Done check passes. We use
   squash-merge to keep `main` history readable.

Nobody pushes directly to `main`. Branch protection enforces this.

## Definition of Done

A change is done when it is **merged to `main`** and every check below passes.
This is a shared commitment: the reviewer is responsible for confirming these
just as much as the author. Each check names what enforces it. Gates that don't
exist yet are listed with the sprint they land in and who owns building them.
Until a gate exists, the reviewer checks that item by hand.

| # | Check | Enforced by | Status | Owner |
|---|---|---|---|---|
| 1 | No direct pushes to `main`; all changes go through a PR | GitHub branch protection on `main` | [In place now / lands Sprint 1] | Alex |
| 2 | At least 1 approving review from a teammate who is not the author | GitHub branch protection ("Require approvals: 1") | [In place now / lands Sprint 1] | Alex |
| 3 | Code is formatted and passes lint | `pre-commit` hook running `ruff check` and `ruff format` (`.pre-commit-config.yaml`), plus the same check as the `lint` job in `.github/workflows/ci.yml` | Lands Sprint [2] | Cash |
| 4 | All tests pass, and new logic has tests | `test` job in `.github/workflows/ci.yml` running `pytest` | Lands Sprint [2] (once there is code to test) | Jonathan |
| 5 | CI is green before merge | Branch protection "Require status checks to pass" with `lint` and `test` marked required | Lands Sprint [2], after #3 and #4 exist | Alex |
| 6 | No secrets, API keys, or large data files committed | `pre-commit` hooks `detect-secrets` and `check-added-large-files` | Lands Sprint [2] | Cash |
| 7 | Dependencies have no known high-severity vulnerabilities | GitHub Dependabot alerts enabled on the repo | Lands Sprint [2] | Alex |
| 8 | Docs are updated if behavior, setup, or usage changed (README, `docs/`, AI context file) | Checkbox in `.github/pull_request_template.md`; reviewer confirms | Lands Sprint [1] | Connor |
| 9 | The linked issue's acceptance criteria are met | Reviewer confirms against the issue; issue closes on merge via `Closes #N` | In place now | Whole team |

When a gate lands, its owner updates the Status column in this file in the same
PR that adds the gate.

## Review Expectations

- **Who reviews:** any teammates other than the author. For changes touching
  [model training / the data pipeline / partner-facing output], request a review
  from that area's owner in the table above.
- **Turnaround:** reviewers respond within **48 hours** of being requested
  (24 hours in the last 3 days of a sprint). If you can't review in time, say so
  on the PR so the author can ask someone else.
- **What a review checks:** the Definition of Done items, whether the code does
  what the issue asked, and whether someone else could understand and maintain it.
- **Feedback:** comments marked `nit:` are optional. Anything else must be
  resolved or discussed before approval.
- **Size:** keep PRs small enough to review in about 20 minutes (roughly under
  400 changed lines). Split larger work into multiple PRs.
- **Stuck PRs:** if a PR has had no review after 48 hours, raise it at the next
  standup or in the team channel.

## The Contribution Norm

**Every team member owns at least one piece of accepted work per sprint**, as
defined by the course's [contribution lines](https://capstone.alexulbrich.com/assignments/sprint-notes/#contribution-lines).
This norm feeds the individual contribution modifier on Sprint Notes, so we
follow it as written.

### What "accepted" means

| Kind of work | Accepted when |
|---|---|
| Code | PR merged to `main` and passes the full Definition of Done |
| Documentation / design docs | PR adding it to `docs/` is reviewed and merged |
| Research (paper reviews, model comparisons) | Written summary merged to `docs/research/`, with a teammate's approval |
| Experiments / training runs | Results (metrics, config, notes) merged to `docs/experiments/` and reviewed |
| Partner deliverables | Delivered through the partner's system, and the partner (or our partner liaison, on their behalf) confirms receipt in the linked issue |

Work that is in progress, sitting in an unmerged branch, or unreviewed does not
count yet.

### How we make it workable

- **Sizing:** at sprint planning, issues are broken down until each one can be
  finished and reviewed within one sprint. Anything bigger gets split.
- **Assignment:** by the end of sprint planning, every member has at least one
  issue assigned on the board that they own.
- **Pairing:** when work is hard to split (e.g. setting up the training
  environment), we pair. The issue lists one owner and one pair partner, and each
  person owns a distinct accepted piece (e.g. one writes the code, the other
  writes the tests or the docs).
- **Early warning:** if your piece is at risk of not landing by mid-sprint, say
  so at standup so it can be resized or you can get help.
- **Review turnaround:** the 48-hour review rule above exists so no one misses
  the norm because they were waiting on a reviewer.

## AI-Assisted Work

AI coding tools are allowed. Our AI context file, [`AGENTS.md` / `CLAUDE.md`],
describes the project, conventions, and commands for those tools, and it is
updated in the same PR whenever those change. You are responsible for every line
you submit, whether you or a tool wrote it. AI-generated code goes through the
same Definition of Done and review as anything else.

## Reporting Bugs and Asking Questions

- Search existing [issues](../../issues) first.
- Otherwise open a new issue with: what you expected, what happened, steps to
  reproduce, and relevant versions (Python, OS, library versions).
- Label it `bug`, `question`, or `enhancement`.
- Never put secrets, credentials, or partner-confidential data in an issue.
  Message [NAME] directly instead.

## Styleguides

### Code

- Python [3.11], formatted and linted with `ruff` (enforced by the pre-commit
  hook once it lands; see Definition of Done #3).
- Type hints on public functions.

### Commit Messages

Use short, imperative summaries that reference the issue:

```
Add tile loader for aerial images (#14)
Fix off-by-one in bbox scaling (#22)
```

## Code of Conduct

Be respectful, give constructive feedback, and assume good intent. Report
problems to the team.
