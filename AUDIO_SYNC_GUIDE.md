# HierLoc Video - Audio Synchronization Guide

**Date**: February 20, 2026
**Purpose**: Add narration audio to rendered video scenes
**Tool**: FFmpeg (free, open-source)

---

## 🎙️ AUDIO SYNC OVERVIEW

After recording narration files, this guide covers:
1. Verifying audio files
2. Syncing audio with video timing
3. Adjusting audio levels
4. Composing the final video

---

## 📋 PREREQUISITES

### Audio Files Required:
```
/Volumes/SSD/iclr-website/manim_video/audio/
├── scene1_narration.wav     (24.4s)
├── scene2_narration.wav     (36.5s)
├── scene3_narration.wav     (39.5s)
├── scene4_narration.wav     (70s)
└── scene5_narration.wav     (45s)
```

### Video Files (Already Rendered):
```
/Volumes/SSD/iclr-website/manim_video/output/videos/
├── scene1_hook/1080p60/Scene1Hook.mp4          (2.3M)
├── scene2_problem/1080p60/Scene2Problem.mp4    (1.1M)
├── scene3_insight/1080p60/Scene3Insight.mp4    (1.0M)
├── scene4_solution/1080p60/Scene4Solution.mp4  (878K)
└── scene5_results/1080p60/Scene5Results.mp4    (671K)
```

### Tools:
- **FFmpeg**: Audio/video processing
  - Install: `brew install ffmpeg` (macOS) or `apt-get install ffmpeg` (Linux)
  - Verify: `ffmpeg -version`

---

## 🔍 STEP 1: VERIFY AUDIO FILES

Before syncing, verify all audio files are properly recorded.

### Check Audio Duration:
```bash
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1:novalue=1 \
  /Volumes/SSD/iclr-website/manim_video/audio/scene1_narration.wav

# Expected output: 24.4 (seconds)
```

### Check All Audio Files:
```bash
#!/bin/bash
# Save as check_audio.sh and run: bash check_audio.sh

AUDIO_DIR="/Volumes/SSD/iclr-website/manim_video/audio"

echo "Audio File Duration Check:"
echo "=========================="

for scene in 1 2 3 4 5; do
  file="$AUDIO_DIR/scene${scene}_narration.wav"
  if [ -f "$file" ]; then
    duration=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1:novalue=1 "$file")
    printf "Scene $scene: %.1f seconds\n" "$duration"
  else
    echo "Scene $scene: MISSING ⚠️"
  fi
done
```

### Expected Durations:
| Scene | Expected | Tolerance |
|-------|----------|-----------|
| 1 | 24.4s | 23.5s - 25.5s |
| 2 | 36.5s | 35.5s - 37.5s |
| 3 | 39.5s | 38.5s - 40.5s |
| 4 | 70s | 69s - 71s |
| 5 | 45s | 44s - 46s |

**Note**: Slight variations (±0.5s) are acceptable and can be adjusted in editing.

---

## 🎬 STEP 2: SYNC AUDIO WITH VIDEO

### Option A: Simple Audio Overlay (Recommended First Try)

This adds audio to video without re-encoding video (fast):

```bash
ffmpeg -i /Volumes/SSD/iclr-website/manim_video/output/videos/scene1_hook/1080p60/Scene1Hook.mp4 \
  -i /Volumes/SSD/iclr-website/manim_video/audio/scene1_narration.wav \
  -c:v copy -c:a aac -shortest \
  /Volumes/SSD/iclr-website/manim_video/output/videos/scene1_hook/1080p60/Scene1Hook_with_audio.mp4
```

**Parameters explained**:
- `-i [video]`: Input video file
- `-i [audio]`: Input audio file
- `-c:v copy`: Copy video stream without re-encoding (fast)
- `-c:a aac`: Encode audio to AAC (web-friendly)
- `-shortest`: Use shorter stream duration (audio or video)
- `[output]`: Output filename with `_with_audio` suffix

### Option B: Full Re-encode (For Quality Control)

If you need precise timing adjustments:

```bash
ffmpeg -i /Volumes/SSD/iclr-website/manim_video/output/videos/scene1_hook/1080p60/Scene1Hook.mp4 \
  -i /Volumes/SSD/iclr-website/manim_video/audio/scene1_narration.wav \
  -c:v libx264 -preset slow -crf 18 -c:a aac -b:a 128k \
  /Volumes/SSD/iclr-website/manim_video/output/videos/scene1_hook/1080p60/Scene1Hook_with_audio.mp4
```

**Quality settings**:
- `-preset slow`: Higher quality encoding (slower)
- `-crf 18`: Quality (0-51, lower = better; 18 is high quality)
- `-b:a 128k`: Audio bitrate (128k is good for voice)

### Batch Process All Scenes:

Create a script file (save as `sync_all_audio.sh`):

```bash
#!/bin/bash

# Script to sync audio with all video scenes

BASE_PATH="/Volumes/SSD/iclr-website/manim_video"
VIDEOS_PATH="$BASE_PATH/output/videos"
AUDIO_PATH="$BASE_PATH/audio"

echo "Starting audio sync for all scenes..."
echo "====================================="

# Scene 1
echo "Processing Scene 1..."
ffmpeg -i "$VIDEOS_PATH/scene1_hook/1080p60/Scene1Hook.mp4" \
  -i "$AUDIO_PATH/scene1_narration.wav" \
  -c:v copy -c:a aac -shortest \
  "$VIDEOS_PATH/scene1_hook/1080p60/Scene1Hook_with_audio.mp4"

# Scene 2
echo "Processing Scene 2..."
ffmpeg -i "$VIDEOS_PATH/scene2_problem/1080p60/Scene2Problem.mp4" \
  -i "$AUDIO_PATH/scene2_narration.wav" \
  -c:v copy -c:a aac -shortest \
  "$VIDEOS_PATH/scene2_problem/1080p60/Scene2Problem_with_audio.mp4"

# Scene 3
echo "Processing Scene 3..."
ffmpeg -i "$VIDEOS_PATH/scene3_insight/1080p60/Scene3Insight.mp4" \
  -i "$AUDIO_PATH/scene3_narration.wav" \
  -c:v copy -c:a aac -shortest \
  "$VIDEOS_PATH/scene3_insight/1080p60/Scene3Insight_with_audio.mp4"

# Scene 4
echo "Processing Scene 4..."
ffmpeg -i "$VIDEOS_PATH/scene4_solution/1080p60/Scene4Solution.mp4" \
  -i "$AUDIO_PATH/scene4_narration.wav" \
  -c:v copy -c:a aac -shortest \
  "$VIDEOS_PATH/scene4_solution/1080p60/Scene4Solution_with_audio.mp4"

# Scene 5
echo "Processing Scene 5..."
ffmpeg -i "$VIDEOS_PATH/scene5_results/1080p60/Scene5Results.mp4" \
  -i "$AUDIO_PATH/scene5_narration.wav" \
  -c:v copy -c:a aac -shortest \
  "$VIDEOS_PATH/scene5_results/1080p60/Scene5Results_with_audio.mp4"

echo "====================================="
echo "All scenes synced with audio! ✅"
```

**Run the script**:
```bash
chmod +x sync_all_audio.sh
./sync_all_audio.sh
```

---

## 🔊 STEP 3: ADJUST AUDIO LEVELS (Optional)

If audio is too loud or quiet, normalize it:

### Check Audio Levels:
```bash
ffmpeg -i /Volumes/SSD/iclr-website/manim_video/audio/scene1_narration.wav -af volumedetect -f null -
```

### Normalize Audio (Recommended):
This brings all scenes to consistent loudness:

```bash
ffmpeg -i /Volumes/SSD/iclr-website/manim_video/audio/scene1_narration.wav \
  -af loudnorm=I=-16:TP=-1.5:LRA=11 \
  /Volumes/SSD/iclr-website/manim_video/audio/scene1_narration_normalized.wav
```

### Then Sync with Normalized Audio:
```bash
ffmpeg -i /Volumes/SSD/iclr-website/manim_video/output/videos/scene1_hook/1080p60/Scene1Hook.mp4 \
  -i /Volumes/SSD/iclr-website/manim_video/audio/scene1_narration_normalized.wav \
  -c:v copy -c:a aac -shortest \
  /Volumes/SSD/iclr-website/manim_video/output/videos/scene1_hook/1080p60/Scene1Hook_with_audio.mp4
```

---

## ⏱️ STEP 4: FINE-TUNE TIMING (If Needed)

If audio doesn't sync perfectly, adjust playback speed slightly:

### Slow Down Audio by 5%:
```bash
ffmpeg -i /Volumes/SSD/iclr-website/manim_video/audio/scene1_narration.wav \
  -filter:a "atempo=0.95" \
  /Volumes/SSD/iclr-website/manim_video/audio/scene1_narration_slower.wav
```

### Speed Up Audio by 5%:
```bash
ffmpeg -i /Volumes/SSD/iclr-website/manim_video/audio/scene1_narration.wav \
  -filter:a "atempo=1.05" \
  /Volumes/SSD/iclr-website/manim_video/audio/scene1_narration_faster.wav
```

**Typical range**: ±5% adjustment is imperceptible to viewers

---

## 🎞️ STEP 5: CREATE MASTER VIDEO (Concatenate All Scenes)

After syncing all 5 scenes with audio, concatenate them:

### Create Concat File:
Save as `/Volumes/SSD/iclr-website/concat_list.txt`:

```
file '/Volumes/SSD/iclr-website/manim_video/output/videos/scene1_hook/1080p60/Scene1Hook_with_audio.mp4'
file '/Volumes/SSD/iclr-website/manim_video/output/videos/scene2_problem/1080p60/Scene2Problem_with_audio.mp4'
file '/Volumes/SSD/iclr-website/manim_video/output/videos/scene3_insight/1080p60/Scene3Insight_with_audio.mp4'
file '/Volumes/SSD/iclr-website/manim_video/output/videos/scene4_solution/1080p60/Scene4Solution_with_audio.mp4'
file '/Volumes/SSD/iclr-website/manim_video/output/videos/scene5_results/1080p60/Scene5Results_with_audio.mp4'
```

### Concatenate Scenes:
```bash
ffmpeg -f concat -safe 0 -i /Volumes/SSD/iclr-website/concat_list.txt \
  -c copy \
  /Volumes/SSD/iclr-website/manim_video/output/HierLoc_Explainer_Full.mp4
```

**Result**: 215-second master video with all audio

---

## 🌐 STEP 6: CREATE WEB-OPTIMIZED VERSION (Optional)

For website deployment, create a smaller, web-friendly version:

```bash
ffmpeg -i /Volumes/SSD/iclr-website/manim_video/output/HierLoc_Explainer_Full.mp4 \
  -c:v libx264 -preset fast -crf 25 -c:a aac -b:a 96k \
  -movflags +faststart \
  /Volumes/SSD/iclr-website/static/videos/hierloc_explainer.mp4
```

**Parameters**:
- `-preset fast`: Balance speed/quality (faster encoding)
- `-crf 25`: Good quality for web (slightly lower than production)
- `-b:a 96k`: Smaller audio bitrate for web
- `-movflags +faststart`: Allows playback to start before download completes

---

## 📊 WORKFLOW SUMMARY

### Complete Sync Workflow:

```bash
# 1. Verify audio files exist
ls -la /Volumes/SSD/iclr-website/manim_video/audio/

# 2. Run batch sync script (all scenes at once)
chmod +x sync_all_audio.sh
./sync_all_audio.sh

# 3. Concatenate all scenes
ffmpeg -f concat -safe 0 -i /Volumes/SSD/iclr-website/concat_list.txt \
  -c copy \
  /Volumes/SSD/iclr-website/manim_video/output/HierLoc_Explainer_Full.mp4

# 4. Create web version
ffmpeg -i /Volumes/SSD/iclr-website/manim_video/output/HierLoc_Explainer_Full.mp4 \
  -c:v libx264 -preset fast -crf 25 -c:a aac -b:a 96k -movflags +faststart \
  /Volumes/SSD/iclr-website/static/videos/hierloc_explainer.mp4

# 5. Verify final file
ls -lh /Volumes/SSD/iclr-website/static/videos/hierloc_explainer.mp4
```

---

## 🛠️ TROUBLESHOOTING

### Problem: Audio and Video Out of Sync
**Solution**: Adjust audio speed by small percentage (±2-5%)
```bash
# Slow down audio by 2%
ffmpeg -i audio.wav -filter:a "atempo=0.98" audio_slower.wav
```

### Problem: Audio is Clipped or Distorted
**Solution**: Lower audio gain before syncing
```bash
# Reduce audio volume by 3dB
ffmpeg -i audio.wav -af "volume=0.7" audio_quieter.wav
```

### Problem: FFmpeg: Unrecognized Option
**Solution**: Ensure FFmpeg is installed: `brew install ffmpeg`

### Problem: File Not Found Error
**Solution**: Verify file paths are correct (use absolute paths, not relative)

### Problem: Audio Out of Sync After Concat
**Solution**: Manually adjust audio delay when syncing individual scenes
```bash
# Delay audio by 0.5 seconds
ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac \
  -itsoffset -0.5 -i audio.wav \
  output.mp4
```

---

## ✅ POST-SYNC CHECKLIST

After syncing all audio:

- [ ] All 5 audio files recorded and verified
- [ ] All 5 video scenes synced with audio
- [ ] Audio levels are consistent (±2dB)
- [ ] No clipping or distortion
- [ ] Timing matches visual cues (±0.5s acceptable)
- [ ] Master video concatenated (215 seconds)
- [ ] Web-optimized version created
- [ ] File sizes verified (master ~100-150M, web ~30-50M)
- [ ] Test playback on different devices
- [ ] Ready for website deployment

---

## 📁 OUTPUT LOCATIONS

After audio sync:

```
/Volumes/SSD/iclr-website/
├── manim_video/
│   └── audio/
│       ├── scene1_narration.wav         (original recording)
│       ├── scene2_narration.wav
│       ├── scene3_narration.wav
│       ├── scene4_narration.wav
│       └── scene5_narration.wav
│
│   └── output/
│       ├── HierLoc_Explainer_Full.mp4   (master video, all scenes concatenated)
│       └── videos/
│           ├── scene1_hook/1080p60/Scene1Hook_with_audio.mp4
│           ├── scene2_problem/1080p60/Scene2Problem_with_audio.mp4
│           ├── scene3_insight/1080p60/Scene3Insight_with_audio.mp4
│           ├── scene4_solution/1080p60/Scene4Solution_with_audio.mp4
│           └── scene5_results/1080p60/Scene5Results_with_audio.mp4
│
└── static/videos/
    └── hierloc_explainer.mp4            (web-optimized, final version)
```

---

## 📖 REFERENCE

### FFmpeg Common Options:
```
-i             Input file
-c:v           Video codec (copy, libx264, libx265)
-c:a           Audio codec (aac, mp3, flac)
-preset        Encoding speed (ultrafast, superfast, veryfast, faster, fast, medium, slow, slower)
-crf           Quality (0-51, lower is better; 18-23 recommended)
-b:a           Audio bitrate (128k, 96k, 192k)
-af            Audio filter (loudnorm, atempo, volume)
-shortest      Use shortest stream duration
-movflags      Metadata options (faststart for web)
-f concat      Use concat demuxer
-safe 0        Allow absolute paths in concat file
```

---

## 🎬 FINAL STEPS

1. **Record narration** using `/Volumes/SSD/iclr-website/AUDIO_RECORDING_GUIDE.md`
2. **Sync audio** using commands in this guide
3. **Concatenate scenes** to create master video
4. **Create web version** for deployment
5. **Deploy to website** at `/static/videos/hierloc_explainer.mp4`

---

**Status**: Ready for Audio Sync Phase ✅
**Total Time**: ~30-45 minutes (once audio is recorded)
**Next Document**: `/Volumes/SSD/iclr-website/PROJECT_STATUS_v0.4.0.md`

🎤 Record narration first, then return to this guide! 📖
