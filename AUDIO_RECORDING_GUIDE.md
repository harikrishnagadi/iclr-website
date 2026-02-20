# HierLoc Video - Audio Narration Recording Guide

**Date**: February 20, 2026
**Status**: Ready for Recording
**Total Duration**: ~215 seconds (3:35) across 5 scenes

---

## 🎤 QUICK START CHECKLIST

- [ ] Quiet room (no fans, AC, background noise)
- [ ] Microphone tested and levels set (-3dB to -6dB peaks)
- [ ] Speaking 6-12 inches from mic, slightly off-axis
- [ ] Narration script open and reviewed
- [ ] Recording software ready (Audacity, GarageBand, or DAW)
- [ ] Output folder: `/Volumes/SSD/iclr-website/manim_video/audio/`

---

## 📋 RECORDING SPECIFICATIONS

| Parameter | Specification |
|-----------|---|
| **Sample Rate** | 48 kHz (broadcast quality) |
| **Bit Depth** | 24-bit (or 16-bit minimum) |
| **Format** | WAV (lossless) |
| **Mono/Stereo** | Stereo recommended (mix to mono in post if needed) |
| **Audio Levels** | Peak -3dB to -6dB (leave headroom) |

---

## 🎬 SCENE-BY-SCENE BREAKDOWN

### **SCENE 1: THE HOOK (24.4 seconds)**

**Tone**: Curious, building intrigue
**Energy**: 6/10 → 7/10
**Pacing**: Fast, engaging, questioning

#### Narration:
```
[0:00 - 0:05] "Can you guess where this photo was taken?"

[0:05 - 0:12] "Without any landmarks, language, or people...
               without any obvious clues?"

[0:12 - 0:20] "How would a computer solve this?"

[0:20 - 0:24.4] [Silent - visual payoff]
```

#### Recording Notes:
- **Delivery**: Speak like you're asking a friend, with genuine curiosity
- **Pacing**: Natural conversational pace with slight emphasis on questions
- **Emphasis**: Stress "Without" and "How" slightly
- **Natural pauses**: 0.5s between questions (let viewer think)
- **Energy**: Start conversational (6/10), build to interested (7/10)

#### Visual Sync Points:
- 0:00 → Street view images fading in
- 0:05 → Images shift (multiple perspectives)
- 0:12 → Visual transition to new section
- 0:20 → HierLoc title appears
- 0:24.4 → Scene ends

---

### **SCENE 2: THE PROBLEM (36.5 seconds)**

**Tone**: Matter-of-fact, building tension
**Energy**: 6/10 → 7/10
**Pacing**: Slower, methodical, slightly urgent

#### Narration:
```
[0:00 - 0:08] "Modern geolocation works like this: you have
               millions of photos indexed globally. In the case
               of OSV5M, that's over 5 million street view images."

[0:08 - 0:18] "When you submit your photo, the system compares
               it against every single one. Finding the closest
               match takes time, uses huge amounts of memory..."

[0:18 - 0:26] "...and here's the kicker: the system doesn't
               actually 'understand' that places have structure.
               Cities are just scattered points in a sea of 5 million."

[0:26 - 0:36.5] "What if we thought about this differently?"
                [Pause - let it sink in]
```

#### Recording Notes:
- **Delivery**: Start matter-of-fact, build concern by 0:18
- **Pacing**: Read first section at normal pace, then slightly slower from 0:18
- **Emphasis**:
  - "5 million" (wow moment - slight emphasis)
  - "every single one" (stress the exhaustive scale)
  - "doesn't actually understand" (the pain point)
  - "What if" (build hope, leading into next scene)
- **Energy**: Builds from 6/10 → 7/10 with subtle urgency
- **Tone**: Confident but concerned, not depressed

#### Visual Sync Points:
- 0:00 → Millions of dots appear
- 0:05 → Camera pulls back (scale revealed)
- 0:08 → One image highlights (test photo)
- 0:12 → Arrows fan out from image
- 0:18 → Pain point labels appear
- 0:26 → Scene shifts (transition)
- 0:36.5 → Scene ends

---

### **SCENE 3: THE INSIGHT (39.5 seconds)**

**Tone**: Building excitement, "aha moment"
**Energy**: 7/10 → 8/10
**Pacing**: Medium, progressive revelation with acceleration

#### Narration:
```
[0:00 - 0:06] "But wait. Geography isn't random—it's hierarchical."

[0:06 - 0:16] "Take a street photo from Paris. This is a specific
               location in Paris. But Paris is also in France.
               France is in Europe. Europe is on Earth. Each
               location exists at multiple levels of a hierarchy."

[0:16 - 0:26] "Zoom out and it's even more dramatic. Earth has
               7 continents. Those contain 195 countries. Each
               country has thousands of regions. Those have tens
               of thousands of cities. Each level branches exponentially."

[0:26 - 0:33] "Here's the problem: in regular, Euclidean space,
               everything at the deepest level gets crammed together."

[0:33 - 0:39.5] "But there's a geometry perfectly suited to this.
                 Hyperbolic space. It has exponential volume
                 growth—just like hierarchy itself."
```

#### Recording Notes:
- **Delivery**: Start thoughtful, accelerate to excited by 0:26
- **Pacing**:
  - 0:00-0:06: Slow, realization (let it breathe)
  - 0:06-0:16: Medium, unfolding the idea (clear enunciation)
  - 0:16-0:26: Slightly faster, excitement building
  - 0:26-0:39.5: Triumphant, "eureka" moment (crescendo)
- **Emphasis**:
  - "hierarchical" (key insight - lean in)
  - "Paris → France → Europe → Earth" (flow naturally)
  - "exponentially" (emphasis shows scale)
  - "crammed together" (the crowding problem)
  - "perfectly suited" (breakthrough moment)
  - "exponential volume growth" (match wonder to concept)
- **Energy**: Builds from 7/10 → 8/10 with visible enthusiasm
- **Tone**: Thoughtful turning into delighted

#### Visual Sync Points:
- 0:00 → Geographic dots begin organizing
- 0:06 → Paris street photo appears
- 0:10 → Containers expand (Paris ⊂ France ⊂ Europe ⊂ Earth)
- 0:16 → Tree structure appears (hierarchy visualization)
- 0:22 → Exponential branching shown
- 0:26 → Euclidean space crowding visualization
- 0:33 → Hyperbolic disk introduction
- 0:39.5 → Scene ends

---

### **SCENE 4: THE SOLUTION (70 seconds = 1:10)**

**Tone**: Confident, satisfied, technical but accessible
**Energy**: 7/10 → 8/10
**Pacing**: Brisk, showing elegance

#### Narration:
```
[0:00 - 0:10] "Here's HierLoc's key insight: instead of comparing
               against every image, we encode the image into a
               vector—just like we encode geographic entities."

[0:10 - 0:25] "We've already learned embeddings for every country,
               region, subregion, and city. We place all 240,000
               entity embeddings into hyperbolic space, where
               hierarchy naturally 'belongs.'"

[0:25 - 0:38] "Now your image 'votes' for which entities it belongs to.
               The embedding moves toward the entity space and aligns
               with the closest match. Gold highlights show which
               entities won the vote."

[0:38 - 0:55] "And here's the elegant part: search is fast. Start at
               the country level. Does it feel American? Chinese?
               Brazilian? Narrow it down. Then refine to the region.
               Then the subregion. Then the city. Hierarchical beam
               search—like a smart funnel narrowing down the possibilities."

[0:55 - 1:10] "And the efficiency gain? 240,000 entity embeddings
               instead of 5 million images. That's a 95% reduction
               in what we need to store and search. Fast, efficient,
               and interpretable. You know exactly which entities matched."
```

#### Recording Notes:
- **Delivery**: Start confident, end with satisfaction
- **Pacing**:
  - 0:00-0:10: Steady introduction (clear, not rushed)
  - 0:10-0:25: Explanation (technical but flowing)
  - 0:25-0:38: The "magic" moment (let it shine)
  - 0:38-0:55: Technical but exciting (show understanding)
  - 0:55-1:10: The payoff (celebrate the efficiency)
- **Emphasis**:
  - "instead of comparing against every image" (contrast)
  - "just like we encode geographic entities" (parallel concept)
  - "240,000" (key magic number - slight emphasis)
  - "votes for which entities" (personify it - subtle smile)
  - "smart funnel" (simplify the concept)
  - "95% reduction" (the wow statistic)
  - "You know exactly which entities matched" (interpretability)
- **Energy**: Steady 7/10 → 8/10 (confident, not frantic)
- **Tone**: Like explaining something you're genuinely proud of

#### Visual Sync Points:
- 0:00 → Image appears left, encoding starts
- 0:05 → Embedding vector forms
- 0:10 → Entity space appears right (hyperbolic background)
- 0:15 → Entity nodes light up
- 0:25 → Image vector moves toward entities
- 0:30 → Alignment and gold glows
- 0:35 → Voting arrows light up
- 0:40 → Hierarchical search visualization
- 0:50 → Search refines through hierarchy
- 0:55 → Efficiency comparison (240k vs 5M)
- 1:00 → Reduction percentage highlighted
- 1:10 → Scene ends

---

### **SCENE 5: THE PAYOFF (45 seconds)**

**Tone**: Triumphant, proud, celebratory
**Energy**: 8/10
**Pacing**: Fast, punchy, building to climax

#### Narration:
```
[0:00 - 0:10] "The results? State-of-the-art performance across
               every geographic level. Mean geodesic error drops
               19.5%. Country accuracy jumps 8.8%. Region accuracy
               jumps 20.1%. Subregion jumps 43.2%—that's huge.
               City accuracy jumps 16.8%."

[0:10 - 0:20] "It's faster, more memory-efficient, and interpretable.
               You don't just get 'nearest match.' You get: this place
               is in Germany, in Bavaria, in Munich. You understand
               the reasoning."

[0:20 - 0:30] "But there's something bigger here. Hyperbolic geometry
               is the right tool for hierarchical data. Not just for
               geolocation—for any data with structure."

[0:30 - 0:45] "This is HierLoc: Hierarchical Visual Geolocation.
               Learn more at the paper, code, and website links below.
               Bringing the elegance of hyperbolic geometry to one of
               computer vision's toughest problems."
```

#### Recording Notes:
- **Delivery**: Start celebratory, end with vision/inspiration
- **Pacing**:
  - 0:00-0:10: Fast, rattling off impressive results (punch)
  - 0:10-0:20: Medium, explaining benefits (clarity)
  - 0:20-0:30: Slightly slower, bigger picture (vision)
  - 0:30-0:45: Closing, inspiring call-to-action (strength)
- **Emphasis**:
  - "State-of-the-art" (achievement - pride)
  - "19.5%", "43.2%" (big numbers - punch them)
  - "interpretable" (key advantage - lean in)
  - "Germany, Bavaria, Munich" (make it concrete and specific)
  - "hyperbolic geometry is the right tool" (bigger insight)
  - "any data with structure" (broader implications)
  - "elegance" and "toughest problems" (final punch)
- **Energy**: 8/10 (celebratory but not over-the-top)
- **Tone**: Smile while speaking, let pride come through

#### Visual Sync Points:
- 0:00 → Results bars appear and animate
- 0:05 → Percentage counters fill
- 0:10 → Efficiency comparison appears
- 0:15 → Memory reduction visual
- 0:20 → Interpretability path (Germany → Bavaria → Munich)
- 0:25 → Broader impact statement
- 0:30 → Final title frame "HierLoc"
- 0:35 → Subtitle and CTA appear
- 0:40 → Links highlighted
- 0:45 → Video ends with fade to black

---

## 🎙️ MICROPHONE TECHNIQUE

### Optimal Setup:
- **Distance**: 6-12 inches from microphone
- **Angle**: Speak slightly off-axis (10-15° from center) to avoid harsh plosives
- **Height**: Mic should be at mouth level or slightly below
- **Plosives**: Avoid hard p, t, k sounds; if unavoidable, angle mouth away slightly

### Level Management:
- **Target**: -3dB to -6dB peaks
- **Why**: Leaves headroom for peaks without clipping
- **Check**: Do a test recording of each scene to verify levels

### Background Noise Elimination:
- Close windows and doors
- Turn off fans, AC, refrigerators
- Use silent room (office, bedroom, closet with blankets work well)
- If noise present: Gate/noise reduction in post-production

---

## 📝 RECORDING WORKFLOW

### Pre-Recording:
1. **Warm-up** (5 min): Read entire script aloud once to get comfortable
2. **Level check** (2 min): Record 30-second test of Scene 1, verify levels
3. **Take planning**: Plan 2-3 takes per scene

### Recording Session:
1. **Scene 1**: Record 2-3 takes (5-10 min total)
   - Take 1: Learn the flow
   - Take 2: Go for energy
   - Take 3: Polish it
2. **Rest briefly** (1-2 min between scenes)
3. **Repeat for Scenes 2-5**

### Post-Recording:
1. **Review takes**: Listen to all takes, pick best one per scene
2. **Level matching**: Ensure all scenes are within ±2dB of each other
3. **Trim silence**: Remove leading/trailing silence
4. **Save with naming**: `scene1_narration.wav`, `scene2_narration.wav`, etc.

---

## 📊 TIME ESTIMATES

| Scene | Duration | Word Count | Est. Recording Time | Typical Retakes |
|-------|----------|-----------|-------|--|
| 1 | 24.4s | ~45 words | 5-10 min | 2-3 |
| 2 | 36.5s | ~105 words | 10-15 min | 2-3 |
| 3 | 39.5s | ~155 words | 15-20 min | 3-4 |
| 4 | 70s | ~195 words | 20-25 min | 3-4 |
| 5 | 45s | ~155 words | 15-20 min | 2-3 |
| **TOTAL** | **215s** | **~655 words** | **~90 min** | — |

---

## ✅ POST-RECORDING CHECKLIST

Before finalizing audio files, verify:

- [ ] All 5 scenes recorded
- [ ] Audio is clear and intelligible (no muddiness)
- [ ] Levels are consistent (±2dB between scenes)
- [ ] No harsh plosives (p, t, k sounds sharp)
- [ ] Tone matches scene progression (curious → confident → triumphant)
- [ ] Timing roughly matches visual cues (can adjust in sync phase)
- [ ] No background noise, clicks, or artifacts
- [ ] Files saved with clear naming: `scene[N]_narration.wav`
- [ ] Backup copy saved to external drive

---

## 💾 FILE NAMING & STORAGE

### Naming Convention:
```
scene1_narration.wav
scene2_narration.wav
scene3_narration.wav
scene4_narration.wav
scene5_narration.wav
```

### Storage Location:
```
/Volumes/SSD/iclr-website/manim_video/audio/
```

### Backup Location:
```
Recommended: External drive or cloud backup
```

---

## 🎯 TONE REFERENCE SUMMARY

| Scene | Tone Profile | Energy | Key Words | Facial Expression |
|-------|---|---|---|---|
| 1 | Curious questioning | 6→7/10 | "Can you?", "Without?", "How?" | Eyebrows raised, slight smile |
| 2 | Building concern | 6→7/10 | "Scale", "complexity", "challenge" | Thoughtful, slightly worried |
| 3 | Excited realization | 7→8/10 | "Elegant", "hierarchical", "perfect" | Eyes wide, smile growing |
| 4 | Confident satisfaction | 7→8/10 | "Efficient", "interpretable", "brilliant" | Knowing smile, proud |
| 5 | Triumphant vision | 8/10 | "Results", "impact", "elegance" | Big smile, proud and inspired |

---

## 🚀 NEXT STEPS AFTER RECORDING

Once narration is recorded and saved:

1. **Audio Synchronization** (1-2 hours)
   - Use FFmpeg to sync audio with video timings
   - Adjust audio levels if needed

2. **Video Composition** (30 min)
   - Concatenate all 5 scenes with audio
   - Create master video (215s total)

3. **Website Deployment** (15 min)
   - Copy to `/static/videos/hierloc_explainer_full.mp4`
   - Test on different devices

---

## 📞 TROUBLESHOOTING

| Problem | Solution |
|---------|----------|
| Audio level too loud/soft | Re-record with mic moved further/closer (adjust by 2-3 inches) |
| Background hum/buzz | Ensure AC and electrical equipment are off; use noise gate |
| Plosives on p/t/k sounds | Angle mouth away from mic slightly; use plosive filter if available |
| Inconsistent energy | Do all scenes in one session or use same environment |
| Timing doesn't match video | Can be adjusted in sync phase using FFmpeg; slight variations (±0.5s) okay |
| Dry mouth/throat issues | Keep water nearby; warm up voice before recording |

---

## 📄 RESOURCES

- **Narration Script**: `/Volumes/SSD/iclr-website/hierloc_narration_script.md`
- **Video Files**: `/Volumes/SSD/iclr-website/manim_video/output/videos/`
- **Audio Output**: `/Volumes/SSD/iclr-website/manim_video/audio/`
- **Project Summary**: `/Volumes/SSD/iclr-website/PROJECT_SUMMARY_v0.3.0.md`

---

## 🎬 FINAL CHECKLIST BEFORE RECORDING

- [ ] Room is quiet (tested)
- [ ] Microphone is tested and working
- [ ] Recording software is open and configured
- [ ] Script is printed or displayed on second screen
- [ ] Water is nearby for hydration
- [ ] Phone is on silent
- [ ] Narration timing reference is accessible
- [ ] Output folder path is known
- [ ] You've reviewed the tone for each scene
- [ ] You're ready to record! 🎤

---

**Status**: Ready for Recording ✅
**Created**: February 20, 2026
**Total Estimated Time**: ~90 minutes for all 5 scenes

Good luck! 🚀
