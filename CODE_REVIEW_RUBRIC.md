# HierLoc Video Implementation - Code Review Rubric

## 95% Acceptance Threshold

For each scene implementation, the **Reviewer Agent** will score against this rubric.
**Acceptance Rate = (Points Earned / Total Points) × 100%**

**Minimum for approval: 95%**

---

## Scoring Categories (Out of 100 points)

### 1. Narrative Alignment (20 points)
- [ ] **Story adherence** (5 pts): Does the scene follow the HIERLOC_VIDEO_PLAN.md narrative exactly?
- [ ] **Pacing** (5 pts): Does duration match plan (~20s for Scene 1, etc.)?
- [ ] **Purpose** (5 pts): Does the scene accomplish its stated purpose?
- [ ] **Narration clarity** (5 pts): Are narration notes incorporated? Is text clear?

### 2. Visual Design & Consistency (25 points)
- [ ] **Color palette** (8 pts): Uses correct colors (#0a0a0f bg, #e8a838 accent, #e8e4da text)?
- [ ] **Typography** (8 pts): DM Serif Display for titles, Syne for body, DM Mono for code/numbers?
- [ ] **Aesthetic cohesion** (5 pts): Matches "Dark Cosmos · Editorial Serif · Geodesic Gold"?
- [ ] **Visual hierarchy** (4 pts): Elements are visually organized logically?

### 3. Readability & Geometric Consistency (20 points)
- [ ] **Text legibility** (10 pts): All text readable on dark backgrounds? Contrast sufficient?
- [ ] **Geometric accuracy** (10 pts): Shapes/diagrams proportionally correct? No distortions? Hierarchies visually match concepts?

**Critical Rule**: If readability or geometric consistency fails, automatic rejection (score = 0/20).

### 4. Technical Implementation (20 points)
- [ ] **Manim best practices** (5 pts): Uses proper Manim classes (VGroup, Group, Tex, etc.)?
- [ ] **Animation smoothness** (5 pts): Transitions smooth? Uses website ease functions (cubic-bezier)?
- [ ] **Performance** (5 pts): Renders without errors? Reasonable render time?
- [ ] **Code quality** (5 pts): Clean, commented, follows Manim conventions?

### 5. Asset Handling (10 pts)
- [ ] **Media requests** (10 pts): If images/icons/SVGs needed, explicitly requested from user? Not assumed?

**Automatic Rejection Triggers** (10 pts failure):
- Missing images that should have been requested
- Incorrect asset references
- No request submitted to user

### 6. Requirements Compliance (5 pts)
- [ ] **Plan adherence**: Scene matches all details from HIERLOC_VIDEO_PLAN.md?
- [ ] **No rule violations**: Follows Production Rules & Expert Principles?

---

## Scoring Calculation

```
Total Score = Points from Categories 1-6
Acceptance Rate = (Total Score / 100) × 100%

If Acceptance Rate ≥ 95% → ✅ APPROVED
If Acceptance Rate < 95% → ❌ REJECTED (return to coder with feedback)
```

---

## Reviewer's Feedback Template

When rejecting a scene (< 95%), provide:

```markdown
### Scene [N] Review - REJECTED

**Acceptance Rate: [X]%**

#### Failed Categories:
- [Category Name]: [X/Y points] - [Specific issue]
- [Category Name]: [X/Y points] - [Specific issue]

#### Detailed Feedback:
1. [Issue 1]: [Explanation] → [Required fix]
2. [Issue 2]: [Explanation] → [Required fix]
3. [Issue 3]: [Explanation] → [Required fix]

#### Specific Improvements Needed:
- [ ] Fix [specific requirement]
- [ ] Improve [specific aspect]
- [ ] Request assets for [specific elements]

**Return to Coder for Revision**
```

---

## Reviewer's Approval Template

When approving a scene (≥ 95%), provide:

```markdown
### Scene [N] Review - APPROVED ✅

**Acceptance Rate: [X]%**

#### Strengths:
- [Strong point 1]
- [Strong point 2]
- [Strong point 3]

#### Minor Notes (for future reference):
- [Optional suggestion 1]
- [Optional suggestion 2]

**Ready for Integration**
```

---

## Quality Gates (Must Pass)

These will **automatically fail** a scene regardless of points:

1. **Readability Failure**: Any text unreadable or insufficient contrast
2. **Geometric Distortion**: Any shape/diagram proportionally incorrect
3. **Color Scheme Violation**: Wrong colors used or inconsistent palette
4. **Missing Asset Requests**: Images needed but not requested from user
5. **Manim Syntax Errors**: Code doesn't run or has runtime errors

---

## Scene Implementation Order

Scenes should be implemented in this order:

1. **Scene 1** (Hook): 20 seconds - Simplest, establishes style
2. **Scene 2** (Problem): 40 seconds - Introduces complexity
3. **Scene 3** (Insight): 30 seconds - Most visual, requires care
4. **Scene 4** (Solution): 70 seconds - Most complex, technical
5. **Scene 5** (Results): 30 seconds - Charts, conclusion

**Each scene must reach 95% before moving to the next.**

---

## Reviewer Responsibilities

1. **Score objectively** against the rubric (no subjective preferences)
2. **Cite specific failures** (don't just say "bad", explain why)
3. **Suggest concrete improvements** (what to change and how)
4. **Request missing assets** if the coder hasn't (help catch oversights)
5. **Celebrate successes** (95%+ approvals deserve recognition)

---

## Coder Responsibilities

1. **Implement exactly per plan** (no creative deviations without user approval)
2. **Request assets early** (don't assume you can generate/find them)
3. **Test readability** (render and manually check text contrast)
4. **Verify geometry** (shapes should be intentional, not distorted)
5. **Handle feedback professionally** (revise per reviewer suggestions)

---

## Escalation Path

If stuck in feedback loop (> 3 revisions without 95%):
- **Coder**: Escalate to user with current implementation + blocker list
- **Reviewer**: Note that requirements may be unclear
- **User**: Clarify requirements or adjust plan

---

## Success Metrics

- **Per-scene acceptance rate**: Target 95%+ on first or second attempt
- **Total video acceptance**: All 5 scenes ≥ 95%
- **Revision efficiency**: Feedback addressed within 1-2 iterations
- **Asset quality**: All requested media provided by user promptly
