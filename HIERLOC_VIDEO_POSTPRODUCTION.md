# HierLoc Video - Post-Production Assembly Guide

## Status: All 5 Scenes Approved ✅

**Current Phase**: Post-Production Assembly (Audio, Narration, Final Export)

### Scene Completion Summary

| Scene | Status | Duration | Quality |
|-------|--------|----------|---------|
| Scene 1: Hook | ✅ Approved | 24.4s | 98% |
| Scene 2: Problem | ✅ Approved | 36.5s | 100% |
| Scene 3: Insight | ✅ Approved | 39.5s | 99.5% |
| Scene 4: Solution | ✅ Approved | 70s | 97% |
| Scene 5: Results | ✅ Approved | ~45s | 98.5% |
| **TOTAL** | **✅ Ready** | **~215 seconds (3:35)** | **98.6% avg** |

---

## Post-Production Workflow

### Phase 1: Narration Recording (THIS WEEK)

**Goal**: Record professional narration matching the script in `hierloc_narration_script.md`

#### Step 1.1: Review the Narration Script
- Open `/Volumes/SSD/iclr-website/hierloc_narration_script.md`
- Each scene has:
  - **Narration text** (exactly what should be spoken)
  - **Timing cues** (when narration starts/stops relative to animations)
  - **Tone notes** (casual, confident, triumphant, etc.)

#### Step 1.2: Record Audio

**Setup**:
```bash
# Create audio directory
mkdir -p /Volumes/SSD/iclr-website/manim_video/audio

# Option A: Use built-in macOS recording tool
# System Preferences → Sound → Input device

# Option B: Use free tools
# - Audacity (https://www.audacityteam.org/)
# - ScreenFlow (macOS)
# - OBS Studio (cross-platform)
```

**Recording Guidelines**:
- **Microphone**: Use a decent mic (USB condenser, or laptop mic in quiet room)
- **Audio settings**:
  - Sample rate: 44.1 kHz or 48 kHz
  - Bit depth: 16-bit or 24-bit
  - Format: WAV or MP3 (no lossy compression initially; WAV is safer)
- **Tone**: Match the voice described in the script
  - Scene 1-2: Building curiosity (engaging, slightly questioning)
  - Scene 3: Building excitement (faster tempo, higher energy)
  - Scene 4: Confident, satisfied (smooth, assured tone)
  - Scene 5: Triumphant, proud (celebratory but not over-the-top)

**Record per-scene**:
- Record each scene's narration separately
- Save as: `manim_video/audio/scene1_narration.wav`, etc.
- Keep recordings with a small silence buffer at start/end (0.5s each side)

**Quality Check**:
- Level: Peaks around -6dB to -3dB (leave headroom)
- Noise floor: Virtually silent between words
- Clarity: No plosives (p, t, k sounds clipping)
- Re-record if needed

---

### Phase 2: Audio Synchronization (AFTER RECORDING)

**Goal**: Sync narration with scene animations and export individual scene videos

#### Step 2.1: Render Individual Scenes to Video

```bash
cd /Volumes/SSD/iclr-website/manim_video

# Render all scenes to MP4 (quality: medium, fps: 30)
./render.sh all

# Output goes to: ./output/scene1_hook.mp4, scene2_problem.mp4, etc.
```

**Expected Output**:
```
output/
├── scene1_hook.mp4          (24.4s, no audio yet)
├── scene2_problem.mp4       (36.5s, no audio yet)
├── scene3_insight.mp4       (39.5s, no audio yet)
├── scene4_solution.mp4      (70s, no audio yet)
└── scene5_results.mp4       (~45s, no audio yet)
```

#### Step 2.2: Sync Audio to Video Using FFmpeg

```bash
cd /Volumes/SSD/iclr-website/manim_video

# For each scene, sync the narration audio with the video
# (Replace <DELAY> with delay in seconds if narration doesn't start at 0)

# Scene 1
ffmpeg -i output/scene1_hook.mp4 -i audio/scene1_narration.wav \
  -c:v copy -c:a aac -shortest \
  output/scene1_hook_with_audio.mp4

# Scene 2
ffmpeg -i output/scene2_problem.mp4 -i audio/scene2_narration.wav \
  -c:v copy -c:a aac -shortest \
  output/scene2_problem_with_audio.mp4

# Scene 3
ffmpeg -i output/scene3_insight.mp4 -i audio/scene3_narration.wav \
  -c:v copy -c:a aac -shortest \
  output/scene3_insight_with_audio.mp4

# Scene 4
ffmpeg -i output/scene4_solution.mp4 -i audio/scene4_narration.wav \
  -c:v copy -c:a aac -shortest \
  output/scene4_solution_with_audio.mp4

# Scene 5
ffmpeg -i output/scene5_results.mp4 -i audio/scene5_narration.wav \
  -c:v copy -c:a aac -shortest \
  output/scene5_results_with_audio.mp4
```

**Verify Audio Sync**:
- Play each `*_with_audio.mp4` video
- Check that narration timing matches animations
- If timing is off, adjust narration recording or scene animations

---

### Phase 3: Background Music & Sound Design (OPTIONAL)

**Goal**: Add subtle background music and audio effects

#### Step 3.1: Background Music Selection

**Guidelines**:
- **Style**: Instrumental, modern, subtle
- **Mood progression**:
  - Scene 1: Mysterious, building curiosity (70-90 BPM)
  - Scene 2: Tension, urgency (90-100 BPM)
  - Scene 3: Insight, excitement (100-110 BPM, brighter)
  - Scene 4: Solution, confidence (110 BPM, steady)
  - Scene 5: Triumph, celebration (120+ BPM, uplifting)

**Suggested Sources**:
- **Epidemic Sound** (https://www.epidemicsound.com/) - Professional, subscription
- **Artlist** (https://artlist.io/) - Similar to Epidemic
- **Incompetech** (https://incompetech.com/) - Free, CC licensed
- **Free Music Archive** (https://freemusicarchive.org/) - Free, various CC licenses
- **YouTube Audio Library** (free with YouTube account)

**Format**: MP3 or WAV, ~2-3 dB lower than narration peak

#### Step 3.2: Sound Effects (Optional)

Small audio cues to enhance animations:
- **Whoosh**: Arrows flying, objects moving
- **Chime**: Insights, breakthroughs (gold accents)
- **Alert tone**: When pain points appear
- **Resolved tone**: When solutions appear

**Suggested Tools**:
- **Freesound.org** (free, CC licensed)
- **Zapsplat** (https://www.zapsplat.com/) - Free
- **Soundly** (paid plugin) or **Sforzando** (free)

#### Step 3.3: Mix Audio Tracks

```bash
# Create audio mix: narration (primary) + music (background) + effects (punctuation)
# Use Audacity (free) or Adobe Audition (paid)

# Basic FFmpeg approach:
ffmpeg -i scene_with_narration.mp4 -i background_music.mp3 \
  -filter_complex "[1]volume=0.3[music];[0:a][music]amix=inputs=2:duration=first[audio]" \
  -map 0:v -map "[audio]" -c:v copy -c:a aac \
  scene_with_music.mp4
```

---

### Phase 4: Video Composition & Master Edit

**Goal**: Combine all 5 scenes into one master video file

#### Step 4.1: Create Scene Concatenation List

```bash
# Create a text file: manim_video/output/concat_list.txt
file 'scene1_hook_with_audio.mp4'
file 'scene2_problem_with_audio.mp4'
file 'scene3_insight_with_audio.mp4'
file 'scene4_solution_with_audio.mp4'
file 'scene5_results_with_audio.mp4'
```

#### Step 4.2: Concatenate Scenes

```bash
cd /Volumes/SSD/iclr-website/manim_video/output

# Concatenate all scenes into master video
ffmpeg -f concat -safe 0 -i concat_list.txt \
  -c copy \
  hierloc_explainer_final.mp4

# Verify total duration
ffprobe -v error -show_entries format=duration \
  -of default=noprint_wrappers=1:nokey=1:novalue=1 \
  hierloc_explainer_final.mp4
```

**Expected Duration**: ~215 seconds (3:35), give or take audio margins

---

### Phase 5: Quality Check & Optimization

#### Step 5.1: Verify Master Video

```bash
# Play and verify:
# 1. All 5 scenes present and in order
# 2. Narration synced throughout
# 3. Audio levels consistent (no sudden jumps)
# 4. Transitions smooth (no glitches)
# 5. Text readable on all devices
# 6. Color consistency throughout

# Quick FFprobe check
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,r_frame_rate,codec_name -of csv=p=0 hierloc_explainer_final.mp4
ffprobe -v error -select_streams a:0 -show_entries stream=sample_rate,channels,codec_name -of csv=p=0 hierloc_explainer_final.mp4
```

#### Step 5.2: Optimize for Web & YouTube

```bash
# Create web-optimized version (smaller file, fast loading)
ffmpeg -i hierloc_explainer_final.mp4 \
  -c:v libx264 -preset medium -crf 23 \
  -c:a aac -b:a 128k \
  -movflags +faststart \
  hierloc_explainer_web.mp4

# For YouTube, use higher quality (less compression):
ffmpeg -i hierloc_explainer_final.mp4 \
  -c:v libx264 -preset slow -crf 18 \
  -c:a aac -b:a 192k \
  hierloc_explainer_youtube.mp4
```

**File Comparison**:
| Version | Use Case | Typical Size |
|---------|----------|--------------|
| `hierloc_explainer_final.mp4` | Master (lossless quality) | 200-400 MB |
| `hierloc_explainer_web.mp4` | Website embed | 30-50 MB |
| `hierloc_explainer_youtube.mp4` | YouTube upload | 50-80 MB |

---

### Phase 6: Website Integration

#### Step 6.1: Deploy Video to Website

```bash
# Copy final video to static assets
cp /Volumes/SSD/iclr-website/manim_video/output/hierloc_explainer_web.mp4 \
   /Volumes/SSD/iclr-website/static/videos/hierloc_explainer_full.mp4
```

#### Step 6.2: Update index.html

In `index.html`, locate the hero section video embed:

```html
<!-- Update this section -->
<video id="teaser" autoplay muted loop playsinline height="100%">
  <source src="static/videos/hierloc_explainer_full.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
```

#### Step 6.3: Test on Multiple Devices

- **Desktop** (Chrome, Safari, Firefox)
- **Tablet** (iPad, Android)
- **Mobile** (iPhone, Android phone)
- **Different networks** (WiFi, 4G/5G)

---

### Phase 7: YouTube Upload (OPTIONAL)

**If uploading to YouTube**:

```bash
# Create YouTube metadata file (youtube_metadata.txt):
Title: HierLoc: Hierarchical Visual Geolocation
Description:
  "Understanding geographic location through hyperbolic geometry 🌍

  Paper: [link to arXiv]
  Website: [link to project]
  Code: [link to GitHub]

  HierLoc reformulates visual geolocation as image-to-entity alignment
  in hyperbolic space, achieving state-of-the-art results with 95%
  embedding reduction.

  Presented at ICLR 2026."

Tags: hierloc, geolocation, hyperbolic-geometry, research, computer-vision
Category: Science & Technology
```

**Upload Settings**:
- **Visibility**: Public
- **Premiere**: Optional premiere date (notify community)
- **Cards/End Screen**: Link to paper and website
- **Playlist**: Add to "HierLoc Research" playlist if applicable

---

## Checklist: Final Delivery

- [ ] All 5 scenes approved (98.6% avg)
- [ ] Narration recorded and reviewed
- [ ] Audio synced to scenes
- [ ] Background music added (optional)
- [ ] Master video composed
- [ ] Quality verified (playback, audio, colors)
- [ ] Web-optimized version created
- [ ] Video deployed to website
- [ ] Website tested on mobile
- [ ] YouTube uploaded (optional)
- [ ] Links updated in paper/README
- [ ] Final video duration: 3-5 minutes ✅

---

## Troubleshooting

### Audio Sync Issues

**Problem**: Narration doesn't match animation

**Solution**:
1. Check narration recording duration vs script timing
2. If narration is too fast/slow, re-record or adjust playback speed:
   ```bash
   # Slow down audio by 10% (pitch-preserving)
   ffmpeg -i audio.wav -filter:a "atempo=0.9" audio_slower.wav
   ```
3. Check Manim scene duration in code (Scene config)

### Video Quality Issues

**Problem**: Video looks blurry or colors are wrong

**Solution**:
1. Re-render scene with higher quality:
   ```bash
   ./render.sh scene1 --quality high_quality  # or ultra_quality
   ```
2. Check that FFmpeg codec settings are correct (CRF value)
3. Verify color profile: Manim → HTML5 → FFmpeg → file

### File Size Too Large

**Problem**: Master video is > 500 MB

**Solution**:
1. Use better compression (higher CRF value):
   ```bash
   ffmpeg -i input.mp4 -c:v libx264 -crf 25 output.mp4  # Higher CRF = smaller
   ```
2. Reduce resolution (if acceptable):
   ```bash
   ffmpeg -i input.mp4 -vf scale=1280:720 output.mp4
   ```
3. Reduce frame rate (if smooth motion not critical):
   ```bash
   ffmpeg -i input.mp4 -r 24 output.mp4  # 24 fps instead of 30
   ```

---

## Timeline Estimate

| Phase | Duration | Status |
|-------|----------|--------|
| Recording narration | 2-4 hours | Pending |
| Syncing audio | 1-2 hours | Pending |
| Background music/SFX | 2-4 hours | Optional |
| Video composition | 1-2 hours | Pending |
| Quality checks | 1-2 hours | Pending |
| Website integration | 30 min | Pending |
| **Total** | **7-18 hours** | **In Progress** |

---

## Next Steps

1. **Narration Recording** (This week)
   - Review script in `hierloc_narration_script.md`
   - Record each scene's narration
   - Save audio files to `manim_video/audio/`

2. **Audio Sync & Composition** (Next week)
   - Render scenes to video
   - Sync narration with animations
   - Create master video file

3. **Website Deployment** (Final)
   - Copy final video to `static/videos/`
   - Update `index.html` if needed
   - Test on all devices

4. **YouTube Upload** (Optional)
   - Upload master video
   - Add metadata and links
   - Promote on social media

---

**Questions or Issues?**
- Check `manim_video/render.sh` for rendering options
- Refer to `CODE_REVIEW_RUBRIC.md` if scenes need revisions
- Update this document if new steps are needed

**Status**: ✅ All scenes approved. Ready for narration recording!
