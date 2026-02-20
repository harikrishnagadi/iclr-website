# HierLoc Video - Multi-Agent Development Workflow

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    CODER AGENT                              │
│  Implements Scene N per HIERLOC_VIDEO_PLAN.md               │
│  - Writes Manim Python code                                 │
│  - Requests media assets from user                          │
│  - Tests for readability & geometry                         │
│  - Submits for review                                       │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ↓
         [Scene Implementation]
                 │
                 ↓
┌─────────────────────────────────────────────────────────────┐
│                  REVIEWER AGENT                             │
│  Scores against CODE_REVIEW_RUBRIC.md                       │
│  - 100-point scoring system                                 │
│  - 6 scoring categories                                     │
│  - Automatic rejection triggers                             │
│  - Quality gates (readability, geometry, colors, etc.)      │
└────────────────┬────────────────────────────────────────────┘
                 │
        ┌────────┴────────┐
        ↓                 ↓
    ✅ ≥95%          ❌ <95%
    APPROVED         REJECTED
        │                 │
        ↓                 │
   [Next Scene]      [Feedback to Coder]
   or            │
   [Final Review]│
                 ↓
         [Coder Revises]
                 ↓
         [Re-submit to Reviewer]
                 │
                 └─→ Loop until 95%
```

---

## Workflow Steps

### Phase 1: Setup
**Task #6: Build render script and project structure**
- [ ] Create `/manim_video/` directory
- [ ] Create `config.py` with website colors/fonts
- [ ] Create `render.sh` script
- [ ] Create `utils.py` helpers
- [ ] Setup complete ✅

### Phase 2: Scene 1 Implementation
**Task #4: Coder Agent - Implement Scene 1 (Hook)**
- [ ] Write `scenes/scene1_hook.py`
- [ ] Implement title animation ("HierLoc" with gold accent)
- [ ] Implement subtitle ("Where Are You?")
- [ ] Implement background (geodesic pattern)
- [ ] Animate street view images
- [ ] Add text animations and narration notes
- [ ] Test render (no errors)
- [ ] Request media assets (street view images) from user
- [ ] Submit to reviewer

### Phase 3: Scene 1 Review
**Task #5: Reviewer Agent - Review Scene 1**
- [ ] Score Narrative Alignment (20 pts)
- [ ] Score Visual Design & Consistency (25 pts)
- [ ] Score Readability & Geometric Consistency (20 pts) ⚠️ Critical
- [ ] Score Technical Implementation (20 pts)
- [ ] Score Asset Handling (10 pts)
- [ ] Score Requirements Compliance (5 pts)
- [ ] Calculate total score
- [ ] If ≥95%: **APPROVE** ✅
- [ ] If <95%: **REJECT** with detailed feedback ❌

### Phase 4: Feedback Loop (if <95%)
- [ ] Reviewer provides detailed feedback + specific improvements
- [ ] Coder revises based on feedback
- [ ] Coder re-submits
- [ ] Reviewer re-scores
- [ ] **Repeat until 95%**

### Phase 5: Scenes 2-5
- Repeat workflow for each scene in order
- Each scene must reach 95% before next scene starts
- Build incrementally on previous scenes' success

---

## Success Criteria

| Metric | Target |
|--------|--------|
| Scene 1 Acceptance Rate | ≥ 95% |
| Scene 2 Acceptance Rate | ≥ 95% |
| Scene 3 Acceptance Rate | ≥ 95% |
| Scene 4 Acceptance Rate | ≥ 95% |
| Scene 5 Acceptance Rate | ≥ 95% |
| **Total Scenes Approved** | **5/5 (100%)** |
| Avg Revisions per Scene | ≤ 2 |
| Final Video Duration | 3-5 minutes |

---

## Key Documents

- **HIERLOC_VIDEO_PLAN.md** — Scene specifications and narrative
- **CODE_REVIEW_RUBRIC.md** — Scoring system (95% threshold)
- **HIERLOC_VIDEO_PLAN.md** → "Production Rules & Expert Principles" → Non-negotiable rules

---

## Kickoff Checklist

Before launching agents:

- [ ] User has reviewed HIERLOC_VIDEO_PLAN.md
- [ ] User has reviewed CODE_REVIEW_RUBRIC.md
- [ ] User is ready to provide media assets when requested
- [ ] User agrees with 95% acceptance threshold
- [ ] Project structure will be created (Task #6)
- [ ] Coder ready to implement Scene 1 (Task #4)
- [ ] Reviewer ready to review Scene 1 (Task #5)

---

## Escalation Protocol

If coder gets stuck (> 3 revisions without 95%):
1. Coder escalates with current implementation + blockers
2. Reviewer notes if requirements are unclear
3. **User clarifies requirements or adjusts plan**
4. Resume from that point

---

## Timeline Estimate (Rough)

- Task #6 (Setup): ~30 min
- Task #4 (Scene 1 Coder): ~45 min
- Task #5 (Scene 1 Review): ~15 min
- Feedback + Revision (if needed): ~20 min per round
- **Total per scene: 60-120 min** (varies by complexity)
- **All 5 scenes: 5-10 hours** (depending on feedback cycles)

---

## Ready to Launch?

```
✅ Documentation created (HIERLOC_VIDEO_PLAN.md)
✅ Review rubric defined (CODE_REVIEW_RUBRIC.md)
✅ Tasks queued and ready (Tasks #4, #5, #6)
✅ Workflow diagram established (this document)

👉 User approval needed to:
   1. Launch Task #6 (Project structure setup)
   2. Launch Task #4 (Coder agent for Scene 1)
   3. Begin review cycle with Task #5
```
