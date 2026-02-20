# HierLoc Explainer Video - Narration Scripts

**Date**: February 20, 2026
**Total Duration**: ~7-8 minutes (all scenes)
**Recording Specifications**:
- Sample Rate: 48 kHz
- Bit Depth: 24-bit
- Format: WAV (lossless)
- Peak Levels: -3dB to -6dB
- Silence: 0.2-0.3s between sentences for natural pacing

---

## Scene 1: The Hook – Visual Geolocation (40-50 seconds)

**Duration**: ~45 seconds
**Timing Notes**:
- Title fade in: 0-1s (read 0.5s in)
- Image sequences + arrow: 1-20s
- Visual Geolocation text: 5-8s (read 1-2s after appearing)
- Definition/Challenge text: 8-15s (read during display)
- Use cases section: 20-40s (read throughout)
- Closing statement: 40-45s

### Narration Script

**[0.5-1.0s] (As title appears)**
"Can you guess where this photo was taken?"

**[1.0-3.0s] (As images appear and arrow forms)**
"Just from looking at it—no GPS, no metadata. Looks simple, right? Well, imagine you have five million photos like this, and you need to find this exact location in seconds."

**[3.0-8.0s] (Definition text appearing)**
"This is visual geolocation: finding where a photo was taken just by what's in the image. It's how we verify breaking news, coordinate emergency response, and map the entire world."

**[8.0-15.0s] (Challenge text appearing)**
"But here's the problem: comparing this photo to five million others, one by one, would take forever. Even with clever algorithms. We need something fundamentally different."

**[15.0-20.0s] (Transition to use cases)**
"And that something... is what HierLoc does. But first, let's see why this matters."

**[20.0-25.0s] (Use cases appearing - Emergency Response)**
"When disaster strikes, first responders have minutes to act. A photo from the scene... but where? In the old world, finding the location could take hours. With visual geolocation, it's seconds. Lives saved."

**[25.0-30.0s] (News & Journalism case)**
"Breaking news spreads instantly online. But is it real? Where was it actually taken? Automated verification matters when you're fighting misinformation at scale."

**[30.0-35.0s] (Wildlife & Urban Planning)**
"Scientists monitor endangered species through camera traps scattered across remote forests. City planners need to understand urban infrastructure comprehensively. Both need to process thousands of images automatically."

**[35.0-40.0s] (Climate & closing statement appearing)**
"Climate scientists track environmental damage in real-time. Agricultural systems monitor crop health across continents. All of these problems—emergency response, journalism, conservation, infrastructure, climate—they all share the same bottleneck."

**[40.0-45.0s] (Closing statement)**
"How do we find a location from a photo at planetary scale? That's where HierLoc comes in. And the answer... is beautiful."

---

## Scene 2: The Problem – Why Naive Search Fails (35-45 seconds)

**Duration**: ~40 seconds
**Timing Notes**:
- Title fade in: 0-1.5s
- Geometric background stabilizes: 1-2s
- Problem labels appear: 2-12s (read during appearance)
- Impact statement: 12-40s

### Narration Script

**[0.5-2.0s] (As title appears and background stabilizes)**
"The problem is simple: brute force doesn't scale."

**[2.0-6.0s] (Five Million Images label appears)**
"If you have five million reference images of Earth..."

**[6.0-10.0s] (Query Photo label appears)**
"...and someone gives you a query photo..."

**[10.0-14.0s] (5M Comparisons label appears)**
"...comparing pixel by pixel to all five million would take forever. Even comparing embeddings—compressed representations of images—still requires millions of calculations per query."

**[14.0-25.0s] (Impact text appears)**
"This isn't just slow. It's impractical. It doesn't scale to planetary data. It doesn't exploit the structure of geography. And it treats all pixels equally, even though mountains, cities, and landscapes follow hierarchical patterns."

**[25.0-35.0s]**
"We need a fundamentally different approach. One that understands that Earth isn't a flat grid of disconnected locations. It's hierarchical: countries contain regions, regions contain cities, cities contain neighborhoods."

**[35.0-40.0s]**
"If we could search hierarchically instead of exhaustively... that changes everything."

---

## Scene 3: The Insight – Hierarchical Structure & Hyperbolic Geometry (40-50 seconds)

**Duration**: ~45 seconds
**Timing Notes**:
- Title fade in: 0-1.5s
- Hierarchy visualization: 2-15s
- Hyperbolic geometry concept: 15-35s
- Key insight: 35-45s

### Narration Script

**[0.5-2.0s] (As title appears)**
"Geography is hierarchical."

**[2.0-8.0s] (As tree/hierarchy visualizations appear)**
"Think about it. The world divides into continents, countries, regions, cities, neighborhoods. Each level contains the next. This isn't accidental—it's fundamental to how we organize space."

**[8.0-15.0s] (Geometry visualizations)**
"And mathematicians discovered something remarkable: there's a geometry perfectly suited to hierarchical data. It's called hyperbolic geometry."

**[15.0-25.0s]**
"In hyperbolic space, distance grows exponentially as you move away from the center. This means nearby points stay close, but distant points spread apart very far. It's as if the space naturally expands at the edges."

**[25.0-35.0s]**
"This is exactly what we need for Earth. Countries spread apart as you go to different continents, but within a country, cities can be distinguished precisely. Hyperbolic geometry handles this elegantly."

**[35.0-45.0s] (Key insight emphasis)**
"Hyperbolic geometry isn't just a mathematical curiosity. For hierarchical data—whether it's geography, taxonomy, or the internet—it's the right tool. And this is the insight that makes HierLoc work."

---

## Scene 4: The Solution – HierLoc Search Algorithm (50-60 seconds)

**Duration**: ~55 seconds
**Timing Notes**:
- Title fade in: 0-1.5s
- Step 1 (Encoding): 2-15s
- Step 2 (Hierarchical Search): 15-35s
- Step 3 (Results): 35-50s
- Closing insight: 50-55s

### Narration Script

**[0.5-2.0s] (As title appears)**
"So how does it work?"

**[2.0-8.0s] (Step 1 appears - Encoding)**
"First, we encode every image into an embedding—a point in hyperbolic space. Not the original coordinate system where distance is Euclidean. Hyperbolic space."

**[8.0-15.0s]**
"This is where the magic happens. Images from the same country cluster together in hyperbolic space, but they're ordered hierarchically. Within each country cluster, cities are separated. Within city clusters, neighborhoods spread out."

**[15.0-22.0s] (Step 2 appears - Hierarchical Search)**
"Now, when you give us a query image, we encode it the same way. Then we don't compare it to all five million reference images."

**[22.0-30.0s]**
"Instead, we search hierarchically. First: which continent or country is most similar? Next: which region within that country? Then: which city? Then: which neighborhood?"

**[30.0-35.0s]**
"We progressively narrow down the search space. At each level, hyperbolic geometry guides us—similar items stay close in the hierarchy, dissimilar items spread far apart."

**[35.0-45.0s] (Results visualization)**
"The result? We only need to compare to thousands of candidates instead of millions. Sub-linear time complexity. Massive computational savings. The search is both faster and more accurate because it respects geographic structure."

**[45.0-55.0s]**
"But there's another breakthrough here: we reduce five million reference images to 240,000 embeddings. That's 95% fewer data points to store and search. HierLoc makes planetary-scale visual geolocation practical."

---

## Scene 5: Results – The Metrics (45-55 seconds)

**Duration**: ~50 seconds
**Timing Notes**:
- Title fade in: 0-1s
- Metrics appear sequentially: 1-18s (read during appearance)
- "Why This Matters" section: 18-28s
- Big insight: 28-40s
- Call to action: 40-50s

### Narration Script

**[0.5-1.5s] (As title appears)**
"The results speak for themselves."

**[1.5-5.0s] (Mean Geodesic Error appears)**
"On the standard benchmark, we reduce mean geodesic error by 19.5%. That means our guesses are, on average, 19.5% closer to the true location."

**[5.0-8.0s] (Country Accuracy appears)**
"We improve country-level accuracy by 8.8 percentage points."

**[8.0-11.0s] (Region Accuracy appears)**
"Region accuracy goes up by 20.1 percentage points."

**[11.0-15.0s] (Subregion Accuracy appears)**
"But the real breakthrough? Subregion accuracy improves by 43.2 percentage points."

**[15.0-18.0s]**
"That's not a marginal improvement. That's transformative."

**[18.0-25.0s] (Why This Matters section)**
"What makes this powerful? The search runs in sub-linear time—with each step, we eliminate huge swaths of the search space. We use 95% fewer embeddings than naive approaches. And the predictions are interpretable—we can see exactly which country, region, city the model chose."

**[25.0-28.0s]**
"This isn't just faster. It's practical."

**[28.0-38.0s] (Big insight emphasized)**
"And here's the profound insight: hyperbolic geometry is the right tool for hierarchical data. It's not specific to geography. It applies anywhere you have hierarchies—biology, organizations, networks, knowledge itself."

**[38.0-45.0s]**
"HierLoc is a proof of concept that mathematical elegance can solve real-world problems at scale."

**[45.0-50.0s] (Call to action)**
"Want to learn more? Check out the HierLoc paper and open-source code. The future of visual geolocation—and hierarchical reasoning in general—is here."

---

## Scene 6: Use Cases at Scale – Real-World Impact (For Future Reference)

**Note**: Currently integrated into Scene 1 ending. This is the narration that appears there.

**Duration**: ~20 seconds (already covered in Scene 1)

---

## Recording Guidelines

### Session Structure
Recommend recording in this order (by scene difficulty):
1. **Scene 2** (Easiest - straightforward explanation)
2. **Scene 4** (Medium - some technical concepts)
3. **Scene 5** (Medium - metrics to explain)
4. **Scene 3** (Harder - abstract geometry concepts)
5. **Scene 1** (Hardest - longest, multiple topic transitions)

### Tone & Style
- **Overall tone**: Clear, engaging, slightly enthusiastic about the elegance of the solution
- **Pacing**: Moderate pace with natural pauses between major ideas
- **Emphasis**: Emphasize the word "hierarchical" and "hyperbolic" as they're central concepts
- **Emotion arc**: Curiosity → Frustration (with naive approach) → Wonder (at geometry insight) → Triumph (at results)

### Technical Terms - Pronunciation
- **HierLoc**: "Hier-lock" (with emphasis on first syllable)
- **Hyperbolic**: "Hy-per-BOLL-ic"
- **Geolocation**: "Jee-oh-loh-KAY-shun"
- **Geodesic**: "Jee-oh-DESS-ic"
- **Embedding**: "Em-BED-ing"

### Emphasis Points (Natural Stress, Not Artificial)
- Scene 1: "billions of times faster," "planetary scale"
- Scene 2: "brute force doesn't scale," "all five million"
- Scene 3: "the right tool," "fundamental to how we organize"
- Scene 4: "the magic happens," "only need thousands"
- Scene 5: "43.2 percentage points," "practical"

### Breathing Points
Mark natural places to breathe (these are already built into the scripts with periods/sentence breaks):
- After each major concept
- Between examples
- Before emphasis statements

---

## Audio File Organization

Once recorded, save audio files as:
```
/Volumes/SSD/iclr-website/static/audio/
├── scene1_narration.wav (48kHz, 24-bit, ~45s)
├── scene2_narration.wav (48kHz, 24-bit, ~40s)
├── scene3_narration.wav (48kHz, 24-bit, ~45s)
├── scene4_narration.wav (48kHz, 24-bit, ~55s)
├── scene5_narration.wav (48kHz, 24-bit, ~50s)
└── AUDIO_PROCESSING_LOG.md
```

---

## Total Spoken Content
- **Scene 1**: ~245 words (45 seconds)
- **Scene 2**: ~195 words (40 seconds)
- **Scene 3**: ~195 words (45 seconds)
- **Scene 4**: ~225 words (55 seconds)
- **Scene 5**: ~210 words (50 seconds)
- **TOTAL**: ~1,070 words (~235 seconds = ~4 minutes of narration)

The visual animations add another 3-4 minutes of silent visual storytelling, bringing the total video to ~7-8 minutes.

---

## Next Steps After Recording

1. **Audio Quality Check**
   - Verify peak levels are -3dB to -6dB
   - Check for background noise
   - Ensure consistent EQ across all scenes

2. **Sync with Video**
   - Use FFmpeg to overlay audio with Manim-rendered scenes
   - Test sync points between narration and animations
   - Adjust timing if needed

3. **Master Video Assembly**
   - Concatenate all 5 scenes with audio
   - Add crossfade transitions (0.2-0.3s)
   - Final color grade and export

4. **Deployment**
   - Create web-optimized version (H.264, VP9)
   - Generate multiple quality variants (480p, 720p, 1080p)
   - Deploy to `/static/videos/hierloc_explainer.mp4`
