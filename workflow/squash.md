# squash

This article outlines our develoment workflow - "squash".

## How We Work

**One branch:** `main` - this is production  
**Everything else:** temporary feature branches that get deleted after merge

## The Process

### 1. Pick a Task
- Grab an issue from "This Week" column
- Move it to "In Progress"

### 2. Create Your Branch
- Click the issue on GitHub
- Create branch from the issue (bottom right sidebar)
- Name it whatever - `fix-thing`, `feature-123`, `temp` - doesn't matter
- This branch will die soon anyway

### 3. Write Code
- Commit however helps you work - messy is fine
- WIP commits, test commits, "asdfasdf" - all fine
- Push whenever you want
- **Stay in your lane** - only do what the issue asks for

### 4. Open a PR When Ready
Format your PR properly - this becomes the permanent record:

```
action_type(scope): brief overview

* what changed
* why it changed  
* anything reviewers should know
```

Example:
```
feat(auth): add password reset flow

* added forgot password link to login page
* sends reset email with secure token
* tokens expire after 1 hour
```

### 5. Review at Weekly Sync
- We review PRs together as a team
- Screen share, walk through code
- Discuss, approve, merge on the spot
- Squash merge → your PR becomes the commit in main


## The Golden Rule

**One issue = One PR = One commit in main**

Keep it focused. If you see other problems while working, create new issues. This keeps PRs reviewable and rollbacks simple.