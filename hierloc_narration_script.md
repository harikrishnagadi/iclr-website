# HierLoc Explainer Video - Narration Script

**Total Video Duration**: ~3:35 (215 seconds)
**Platform**: Website hero + YouTube
**Audience**: Mixed (general tech + researchers)
**Tone**: Conversational, accessible, building excitement through the narrative arc

---

## Scene 1: THE HOOK 🎣
**Duration**: 24.4 seconds
**Tone**: Curious, building intrigue
**Pacing**: Fast, engaging, questioning

### Narration (Read in conversational, slightly questioning tone)

```
[0:00 - 0:05]
"Can you guess where this photo was taken?"

[0:05 - 0:12]
"Without any landmarks, language, or people... without any obvious clues?"

[0:12 - 0:20]
"How would a computer solve this?"

[0:20 - 0:24.4]
[Silent - visual payoff with "HierLoc" title reveal and subtitle]
```

### Notes for Recording

- **Delivery**: Start with genuine curiosity, like asking a friend
- **Pacing**: Pause briefly between questions (0.5s) to let viewer think
- **Emphasis**: Stress "Without" and "How" slightly
- **Energy level**: Start at 6/10, build to 7/10 by the end
- **Mic technique**: Speak clearly but naturally; avoid robotic tone

### Visual Sync Points

- 0:00 → Street view images begin fading in
- 0:05 → Images shift (multiple perspectives)
- 0:12 → "How would a computer solve this?" → Visual transition
- 0:20 → HierLoc title appears with gold accent
- 0:24.4 → Scene ends

---

## Scene 2: THE PROBLEM ⚠️
**Duration**: 36.5 seconds
**Tone**: Matter-of-fact, building tension
**Pacing**: Slower, methodical, slightly urgent

### Narration (Read with confidence but subtle concern)

```
[0:00 - 0:08]
"Modern geolocation works like this: you have millions of photos indexed globally.
In the case of OSV5M, that's over 5 million street view images."

[0:08 - 0:18]
"When you submit your photo, the system compares it against every single one.
Finding the closest match takes time, uses huge amounts of memory..."

[0:18 - 0:26]
"...and here's the kicker: the system doesn't actually 'understand' that places
have structure. Cities are just scattered points in a sea of 5 million."

[0:26 - 0:36.5]
"What if we thought about this differently?"
[Pause, let it sink in]
```

### Notes for Recording

- **Delivery**: Start matter-of-fact, build concern by 0:18
- **Pacing**: Read the first part at normal pace, then slightly slower from 0:18
- **Emphasis**:
  - "5 million" (wow moment)
  - "every single one" (stress the scale)
  - "doesn't actually understand" (the pain point)
  - "What if we thought differently?" (build hope)
- **Energy level**: 6/10 → 7/10 (building tension)
- **Mic technique**: Speak with slight urgency; avoid sounding depressed

### Visual Sync Points

- 0:00 → Millions of dots appear (cloud formation)
- 0:05 → Camera pulls back (scale revealed)
- 0:08 → One image highlights (your test photo)
- 0:12 → Arrows fan out from image
- 0:18 → Pain point labels appear
- 0:26 → Scene shifts (transition)
- 0:36.5 → Scene ends (transition to next)

---

## Scene 3: THE INSIGHT 💡
**Duration**: 39.5 seconds
**Tone**: Building excitement, "aha moment"
**Pacing**: Medium, progressive revelation

### Narration (Read with growing enthusiasm)

```
[0:00 - 0:06]
"But wait. Geography isn't random—it's hierarchical."

[0:06 - 0:16]
"Take a street photo from Paris. This is a specific location in Paris.
But Paris is also in France. France is in Europe. Europe is on Earth.
Each location exists at multiple levels of a hierarchy."

[0:16 - 0:26]
"Zoom out and it's even more dramatic. Earth has 7 continents.
Those contain 195 countries. Each country has thousands of regions.
Those have tens of thousands of cities. Each level branches exponentially."

[0:26 - 0:33]
"Here's the problem: in regular, Euclidean space, everything at the
deepest level gets crammed together."

[0:33 - 0:39.5]
"But there's a geometry perfectly suited to this. Hyperbolic space.
It has exponential volume growth—just like hierarchy itself."
```

### Notes for Recording

- **Delivery**: Start thoughtful, accelerate to excited by 0:26
- **Pacing**:
  - 0:00-0:06: Slow, realization
  - 0:06-0:16: Medium, unfolding the idea
  - 0:16-0:26: Slightly faster, excitement building
  - 0:26-0:39.5: Triumphant, "eureka" moment
- **Emphasis**:
  - "hierarchical" (key insight)
  - "millions" or "thousands of regions" (scale)
  - "crammed together" (the pain point again)
  - "perfectly suited" (the breakthrough)
  - "exponential volume growth" (match the concept to the geometry)
- **Energy level**: 7/10 → 8/10 (building excitement)
- **Mic technique**: Let your enthusiasm show; speak with wonder

### Visual Sync Points

- 0:00 → Geographic dots begin organizing
- 0:06 → Paris street photo appears
- 0:10 → Containers expand (Paris ⊂ France ⊂ Europe ⊂ Earth)
- 0:16 → Tree structure appears (Earth → Continents → Countries → Regions → Cities)
- 0:22 → Exponential branching shown
- 0:26 → Euclidean space problem (crowding visualization)
- 0:33 → Hyperbolic disk introduction
- 0:39.5 → Scene ends

---

## Scene 4: THE SOLUTION ✨
**Duration**: 70 seconds (1:10)
**Tone**: Confident, satisfied, technical but accessible
**Pacing**: Brisk, showing elegance

### Narration (Read with confidence and satisfaction)

```
[0:00 - 0:10]
"Here's HierLoc's key insight: instead of comparing against every image,
we encode the image into a vector—just like we encode geographic entities."

[0:10 - 0:25]
"We've already learned embeddings for every country, region, subregion, and city.
We place all 240,000 entity embeddings into hyperbolic space,
where hierarchy naturally 'belongs.'"

[0:25 - 0:38]
"Now your image 'votes' for which entities it belongs to.
The embedding moves toward the entity space and aligns with the closest match.
Gold highlights show which entities won the vote."

[0:38 - 0:55]
"And here's the elegant part: search is fast. Start at the country level.
Does it feel American? Chinese? Brazilian? Narrow it down.
Then refine to the region. Then the subregion. Then the city.
Hierarchical beam search—like a smart funnel narrowing down the possibilities."

[0:55 - 1:10]
"And the efficiency gain? 240,000 entity embeddings instead of 5 million images.
That's a 95% reduction in what we need to store and search.
Fast, efficient, and interpretable. You know exactly which entities matched."
```

### Notes for Recording

- **Delivery**: Start confident, end with satisfaction
- **Pacing**:
  - 0:00-0:10: Steady introduction
  - 0:10-0:25: Explanation (clear, not rushed)
  - 0:25-0:38: The "magic" moment (let it shine)
  - 0:38-0:55: Technical but exciting (show understanding)
  - 0:55-1:10: The payoff (celebrate the efficiency)
- **Emphasis**:
  - "instead of comparing against every image" (contrast with old way)
  - "just like we encode geographic entities" (parallel concept)
  - "240,000" (the key number)
  - "votes for which entities" (personify the algorithm)
  - "smart funnel" (simplify the technical concept)
  - "95% reduction" (the wow statistic)
  - "You know exactly which entities matched" (interpretability benefit)
- **Energy level**: 7/10 → 8/10 (confident, not frantic)
- **Mic technique**: Speak like you're explaining something you're proud of

### Visual Sync Points

- 0:00 → Image appears on left, encoding animation begins
- 0:05 → Embedding vector formed
- 0:10 → Entity space appears on right (hyperbolic background)
- 0:15 → Entity nodes light up (countries, regions, cities)
- 0:25 → Image vector moves toward entity space
- 0:30 → Alignment and gold glows appear
- 0:35 → Voting arrows light up
- 0:40 → Hierarchical search visualization starts
- 0:50 → Search refines through hierarchy
- 0:55 → Efficiency comparison (240k vs 5M)
- 1:00 → Reduction percentage highlighted
- 1:10 → Scene ends

---

## Scene 5: THE PAYOFF 🏆
**Duration**: ~45 seconds
**Tone**: Triumphant, proud, celebratory
**Pacing**: Fast, punchy, building to climax

### Narration (Read with celebration)

```
[0:00 - 0:10]
"The results? State-of-the-art performance across every geographic level.
Mean geodesic error drops 19.5%. Country accuracy jumps 8.8%.
Region accuracy jumps 20.1%. Subregion jumps 43.2%—that's huge.
City accuracy jumps 16.8%."

[0:10 - 0:20]
"It's faster, more memory-efficient, and interpretable.
You don't just get 'nearest match.' You get: this place is in Germany,
in Bavaria, in Munich. You understand the reasoning."

[0:20 - 0:30]
"But there's something bigger here. Hyperbolic geometry is the right tool
for hierarchical data. Not just for geolocation—for any data with structure."

[0:30 - 0:45]
"This is HierLoc: Hierarchical Visual Geolocation.
Learn more at the paper, code, and website links below.
Bringing the elegance of hyperbolic geometry to one of computer vision's
toughest problems."
```

### Notes for Recording

- **Delivery**: Start celebratory, end with vision/inspiration
- **Pacing**:
  - 0:00-0:10: Fast, rattling off impressive results
  - 0:10-0:20: Medium, explaining benefits
  - 0:20-0:30: Slightly slower, bigger picture (vision)
  - 0:30-0:45: Closing, inspiring call-to-action
- **Emphasis**:
  - "State-of-the-art" (achievement)
  - "19.5%", "43.2%" (the big numbers)
  - "interpretable" (key advantage)
  - "Germany, Bavaria, Munich" (make it concrete)
  - "hyperbolic geometry is the right tool" (the bigger insight)
  - "any data with structure" (broader implications)
  - "elegance" and "toughest problems" (final punch)
- **Energy level**: 8/10 (celebratory, but not over-the-top)
- **Mic technique**: Smile while speaking; let pride come through

### Visual Sync Points

- 0:00 → Results bars appear and animate
- 0:05 → Percentage counters fill
- 0:10 → Efficiency comparison shows up
- 0:15 → Memory reduction visual
- 0:20 → Interpretability path (Germany → Bavaria → Munich)
- 0:25 → Broader impact statement (hyperbolic geometry background)
- 0:30 → Final title frame "HierLoc"
- 0:35 → Subtitle and CTA appear
- 0:40 → Links highlighted
- 0:45 → Video ends with fade to black

---

## General Recording Guidelines

### Mic Setup

1. **Distance**: 6-12 inches from microphone
2. **Angle**: Speak slightly off-axis (avoid directly into mic) to reduce plosives
3. **Levels**: Aim for -3dB to -6dB peaks (leave headroom)
4. **Environment**: Quiet room (no background noise, fans, AC)

### Recording Best Practices

1. **Do multiple takes**: Aim for 2-3 clean takes per scene
2. **Warm up**: Read the script once before recording
3. **Consistency**: Try to maintain similar energy across takes
4. **Mark breaks**: Note natural pause points (0.5-1s pauses)
5. **Save separately**: `scene1_narration_take1.wav`, `take2.wav`, etc.
6. **Edit if needed**: Trim silence, adjust levels in post-production

### Post-Recording Checklist

- [ ] All 5 scenes recorded
- [ ] Audio is clear and intelligible
- [ ] Levels are consistent (±2dB between scenes)
- [ ] No harsh plosives (p, t, k sounds)
- [ ] Tone matches scene (curious → confident → triumphant)
- [ ] Timing matches animation cues
- [ ] Files saved with clear naming convention

---

## Tone Summary by Scene

| Scene | Tone | Energy | Key Words |
|-------|------|--------|-----------|
| 1 | Curious, questioning | 6→7/10 | Question, intrigue, wonder |
| 2 | Tense, building concern | 6→7/10 | Scale, complexity, challenge |
| 3 | Excited, "aha moment" | 7→8/10 | Elegant, hierarchical, perfect |
| 4 | Confident, satisfied | 7→8/10 | Efficient, interpretable, brilliant |
| 5 | Triumphant, visionary | 8/10 | Results, impact, inspiration |

---

## Timing Reference

### Total Word Count
- Scene 1: ~45 words (24.4s) = 111 words/min (slow, intentional)
- Scene 2: ~105 words (36.5s) = 173 words/min (medium)
- Scene 3: ~155 words (39.5s) = 236 words/min (faster)
- Scene 4: ~195 words (70s) = 167 words/min (medium, technical)
- Scene 5: ~155 words (45s) = 207 words/min (fast)

**Average**: ~170 words/min (conversational pace)

---

## Recording Session Plan

**Option A: One Session (All in one day)**
- Scene 1: 10 min (read + take 2-3)
- Scene 2: 15 min
- Scene 3: 20 min
- Scene 4: 25 min
- Scene 5: 20 min
- **Total**: ~90 minutes

**Option B: Phased (More relaxed)**
- Day 1: Scenes 1-2 (25 min)
- Day 2: Scene 3 (20 min)
- Day 3: Scene 4 (25 min)
- Day 4: Scene 5 (20 min)
- **Total**: 4 sessions

---

## Final Notes

✅ **This script is final**—use it as-is for recording
✅ **Timing is intentional**—match the visual cues provided
✅ **Tone matters**—it's part of the narrative impact
✅ **Natural delivery**—don't sound robotic; be conversational

Once recorded, save narration files to:
```
/Volumes/SSD/iclr-website/manim_video/audio/
├── scene1_narration.wav
├── scene2_narration.wav
├── scene3_narration.wav
├── scene4_narration.wav
└── scene5_narration.wav
```

Ready to record? 🎤
