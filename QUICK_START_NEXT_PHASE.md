# HierLoc Video Project - Quick Start for Next Phase

**Status**: Rendering ✅ Complete | Audio Recording ⏳ Next

---

## 🎯 WHERE YOU ARE

**Current State**:
- ✅ All 5 video scenes rendered (6.0M total, 215 seconds)
- ✅ Scene 1 Earth visualization complete with improvements
- ✅ All documentation finalized
- ✅ Narration script ready
- ⏳ Audio files: Not yet recorded
- ⏳ Final video: Not yet composed

**Time Remaining**: ~3-4 hours total
- Audio recording: ~1.5-2 hours
- Audio sync & composition: ~1-2 hours

---

## 🎤 IMMEDIATE NEXT STEP: RECORD NARRATION

### Quick Summary:
You need to record 5 audio files (narration) that match the 5 video scenes.

**Total time**: ~90 minutes (1.5 hours) for all 5 scenes

### How to Start:

**Step 1: Read the Recording Guide**
```bash
open /Volumes/SSD/iclr-website/AUDIO_RECORDING_GUIDE.md
```

**Step 2: Prepare Your Setup**
- Quiet room (close windows, turn off fans)
- USB microphone or headset with mic
- Recording software: Audacity (free), GarageBand, or DAW
- Water nearby for hydration
- The guide recommends 6-12 inches from mic

**Step 3: Record Each Scene**

Scene 1 (5-10 min):
- 24.4 seconds of narration
- Tone: Curious, questioning (6→7/10 energy)
- Text: "Can you guess where this photo was taken?..."

Scene 2 (10-15 min):
- 36.5 seconds of narration
- Tone: Building concern (6→7/10 energy)
- Text: "Modern geolocation works like this:..."

Scene 3 (15-20 min):
- 39.5 seconds of narration
- Tone: Excited "aha moment" (7→8/10 energy)
- Text: "But wait. Geography isn't random—it's hierarchical..."

Scene 4 (20-25 min):
- 70 seconds of narration
- Tone: Confident satisfaction (7→8/10 energy)
- Text: "Here's HierLoc's key insight:..."

Scene 5 (15-20 min):
- 45 seconds of narration
- Tone: Triumphant vision (8/10 energy)
- Text: "The results? State-of-the-art performance..."

**Step 4: Save Files**

Save each recording as:
```
/Volumes/SSD/iclr-website/manim_video/audio/scene1_narration.wav
/Volumes/SSD/iclr-website/manim_video/audio/scene2_narration.wav
/Volumes/SSD/iclr-website/manim_video/audio/scene3_narration.wav
/Volumes/SSD/iclr-website/manim_video/audio/scene4_narration.wav
/Volumes/SSD/iclr-website/manim_video/audio/scene5_narration.wav
```

**Specs**:
- Format: WAV (lossless)
- Sample rate: 48 kHz (48000 Hz)
- Bit depth: 24-bit (or 16-bit minimum)
- Audio levels: -3dB to -6dB peaks

---

## 📖 WHAT TO READ BEFORE RECORDING

### 1. AUDIO_RECORDING_GUIDE.md (Essential)
Path: `/Volumes/SSD/iclr-website/AUDIO_RECORDING_GUIDE.md`

Contains:
- ✅ Scene-by-scene narration text
- ✅ Tone and pacing guidance
- ✅ Microphone technique
- ✅ Recording specifications
- ✅ Time estimates
- ✅ Post-recording checklist

**Read first**: Sections for each scene (1-5) and Microphone Technique

### 2. hierloc_narration_script.md (Reference)
Path: `/Volumes/SSD/iclr-website/hierloc_narration_script.md`

Contains:
- ✅ Complete narration for all 5 scenes
- ✅ Timing cues for each segment
- ✅ Visual sync points
- ✅ Tone notes

**Use during recording**: Reference for exact wording

---

## ⏱️ TIME BREAKDOWN

### Recording Phase: ~90 minutes
| Scene | Duration | Recording Time | Notes |
|-------|----------|---|---|
| 1 | 24.4s | 5-10 min | 2-3 takes |
| 2 | 36.5s | 10-15 min | 2-3 takes |
| 3 | 39.5s | 15-20 min | 3-4 takes |
| 4 | 70s | 20-25 min | 3-4 takes |
| 5 | 45s | 15-20 min | 2-3 takes |

### Audio Sync Phase: ~30-45 minutes
| Task | Time |
|---|---|
| Verify audio files | 5 min |
| Sync audio with video | 15-20 min |
| Concatenate all scenes | 5 min |
| Create web version | 5 min |
| Test playback | 5 min |

---

## 🎬 COMPLETE WORKFLOW

### Phase 1: Audio Recording (Now)
1. Open `AUDIO_RECORDING_GUIDE.md`
2. Prepare recording setup
3. Record Scene 1 (5-10 min)
4. Record Scene 2 (10-15 min)
5. Record Scene 3 (15-20 min)
6. Record Scene 4 (20-25 min)
7. Record Scene 5 (15-20 min)
8. Save all files to `manim_video/audio/`

### Phase 2: Audio Synchronization (After Recording)
1. Open `AUDIO_SYNC_GUIDE.md`
2. Verify audio files (ffprobe)
3. Sync audio with video (ffmpeg)
4. Concatenate all 5 scenes
5. Create web-optimized version
6. Test playback

### Phase 3: Website Deployment (Final)
1. Copy master video to `/static/videos/`
2. Test on different devices/browsers
3. Update website documentation
4. ✅ Done!

---

## 🛠️ TOOLS YOU'LL NEED

### For Recording:
- **Audacity** (Free): https://www.audacityteam.org/
- **GarageBand** (macOS built-in)
- **Your DAW** of choice (Reaper, Logic, etc.)

### For Audio Sync:
- **FFmpeg** (Already installed or `brew install ffmpeg`)

---

## 📋 CHECKLIST - BEFORE YOU START RECORDING

- [ ] Read `AUDIO_RECORDING_GUIDE.md`
- [ ] Quiet room prepared (no fans, AC, background noise)
- [ ] Microphone tested and working
- [ ] Recording software open (Audacity, GarageBand, etc.)
- [ ] Audio output folder created: `manim_video/audio/`
- [ ] Narration script printed or displayed
- [ ] Water nearby for hydration
- [ ] Phone on silent
- [ ] Warm up your voice (read script once aloud)
- [ ] Ready to record! 🎤

---

## 🚀 ONE-LINER TO GET STARTED

Just need to know where to go?

```bash
# Read the recording guide
open /Volumes/SSD/iclr-website/AUDIO_RECORDING_GUIDE.md

# Or view narration script
open /Volumes/SSD/iclr-website/hierloc_narration_script.md

# After recording, read audio sync guide
open /Volumes/SSD/iclr-website/AUDIO_SYNC_GUIDE.md
```

---

## 📊 PROJECT STATISTICS

| Metric | Value |
|---|---|
| Total Video Duration | 215 seconds (3:35) |
| Number of Scenes | 5 |
| Total Video Size | 6.0M |
| Rendering Quality | 1080p60 |
| Narration Word Count | ~655 words |
| Estimated Recording Time | ~90 minutes |
| Estimated Sync Time | ~30-45 minutes |
| Final Video Size | ~100-150M (master) or ~30-50M (web) |

---

## 🎯 SUCCESS CRITERIA

After recording, you'll know you're ready for the next phase when:

✅ All 5 WAV files exist in `manim_video/audio/`
✅ Audio durations roughly match script (±0.5s tolerance)
✅ Audio is clear and intelligible
✅ Levels are consistent (±2dB between scenes)
✅ Tone progression: curious → confident → triumphant
✅ No harsh plosives or background noise
✅ Files follow naming: `scene[N]_narration.wav`

---

## 🎤 TONE QUICK REFERENCE

Each scene needs different energy and tone:

| Scene | Tone | Energy | Example |
|---|---|---|---|
| 1 | Curious, questioning | 6→7/10 | "Can you guess...?" (friendly) |
| 2 | Building concern | 6→7/10 | "...doesn't scale" (worried) |
| 3 | Excited realization | 7→8/10 | "...perfect fit!" (delighted) |
| 4 | Confident satisfaction | 7→8/10 | "95% reduction" (proud) |
| 5 | Triumphant vision | 8/10 | "...elegance..." (inspiring) |

**Pro tip**: Smile when recording Scene 5. It changes your vocal tone!

---

## 📞 REFERENCE DOCUMENTS

### For Recording:
- `AUDIO_RECORDING_GUIDE.md` - Scene-by-scene recording specs
- `hierloc_narration_script.md` - Complete narration text

### For Audio Sync:
- `AUDIO_SYNC_GUIDE.md` - FFmpeg commands and workflow

### For Verification:
- `PROJECT_STATUS_v0.4.0.md` - Current project status
- `PROJECT_SUMMARY_v0.3.0.md` - Complete project overview

---

## 💡 TIPS FOR GREAT RECORDINGS

1. **Warm up**: Read the script once before recording
2. **Take breaks**: Rest between scenes (1-2 minutes)
3. **Do multiple takes**: Aim for 2-3 per scene
4. **Consistency**: Try to maintain similar energy across takes
5. **Natural delivery**: Don't sound robotic; be conversational
6. **Smile**: Affects your vocal tone positively
7. **Emphasis**: Follow the script's guidance for emphasis points
8. **Pause appropriately**: Let questions breathe in Scenes 1-2

---

## ⚡ QUICK COMMANDS (After Recording)

Once you've recorded all audio files, you can use these commands:

### Check audio durations:
```bash
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1:novalue=1 \
  /Volumes/SSD/iclr-website/manim_video/audio/scene1_narration.wav
```

### Sync single scene:
```bash
ffmpeg -i /Volumes/SSD/iclr-website/manim_video/output/videos/scene1_hook/1080p60/Scene1Hook.mp4 \
  -i /Volumes/SSD/iclr-website/manim_video/audio/scene1_narration.wav \
  -c:v copy -c:a aac -shortest \
  /Volumes/SSD/iclr-website/manim_video/output/videos/scene1_hook/1080p60/Scene1Hook_with_audio.mp4
```

### Concatenate all scenes:
```bash
ffmpeg -f concat -safe 0 -i /Volumes/SSD/iclr-website/concat_list.txt \
  -c copy \
  /Volumes/SSD/iclr-website/manim_video/output/HierLoc_Explainer_Full.mp4
```

*(Full commands and batch scripts are in AUDIO_SYNC_GUIDE.md)*

---

## 🏁 FINAL GOAL

**End State**: Complete, web-ready HierLoc explainer video with:
- ✅ All 5 scenes with narration
- ✅ Professional audio/video sync
- ✅ Web-optimized file size
- ✅ Ready for website deployment

**File**: `/Volumes/SSD/iclr-website/static/videos/hierloc_explainer.mp4`

---

## 📞 NEXT STEPS SUMMARY

1. **Right now**: Open `AUDIO_RECORDING_GUIDE.md`
2. **Prepare**: Set up quiet recording environment
3. **Record**: All 5 scenes (~90 minutes total)
4. **Save**: Files to `manim_video/audio/` directory
5. **Then**: Open `AUDIO_SYNC_GUIDE.md` for next phase
6. **Finally**: Deploy to website

---

**You're 57% done. Let's finish strong! 🎬**

Next phase: Audio Recording
Estimated time: 2-3 hours total (1.5 hours recording + 1-2 hours sync)

Ready? Open `/Volumes/SSD/iclr-website/AUDIO_RECORDING_GUIDE.md` 🎤
