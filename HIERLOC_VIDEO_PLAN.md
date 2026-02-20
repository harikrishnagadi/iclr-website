# HierLoc: Explainer Video Plan

## Project Overview

**Video**: "HierLoc: Where Are You? A New Way to Think About Global Geolocation"
**Duration**: 3-5 minutes
**Style**: 3Blue1Brown-inspired, casual & conversational
**Audience**: Mixed (accessible to broad tech audience, scales to technical depth)
**Platform**: Website hero section + YouTube

---

## Narrative Framework

### The Story Arc

1. **Hook (0:00-0:20)**: Pose the problem → "Can you guess where this photo was taken...?"
2. **The Tension (0:20-1:00)**: Why is this hard? Show the naive solution failing at scale
3. **The Insight (1:00-2:00)**: Introduce hyperbolic geometry and hierarchy as the key (explain how hierarchy and geographic locations are related (for example a picture in paris is also in France, Europe Geographical entities are structured by hierarchy (this is rough idea refine it for visualisation)))
4. **The Solution (2:00-3:30)**: Show HierLoc in action—entity-based thinking
5. **The Payoff (3:30-4:00)**: Results, efficiency gains, wow moments

---

## Visual Design System

### Color Palette (Matching Website)

- **Background**: `#0a0a0f` (ink/dark cosmos)
- **Primary Accent**: `#e8a838` (geodesic gold)
- **Gold Light**: `#f5cc7a` (highlights)
- **Text Primary**: `#e8e4da` (cream/off-white)
- **Text Muted**: `#8c8a84` (secondary text)
- **Surfaces**: `#14141e` (panels, containers)

### Typography

- **Titles/Headlines**: DM Serif Display (italic for emphasis)
- **Body/Labels**: Syne (geometric, modern sans-serif)
- **Code/Numbers**: DM Mono (monospace)
- **Overall Aesthetic**: "Dark Cosmos · Editorial Serif · Geodesic Gold"

### Design Principles

- **Minimize motion sickness**: Use smooth easing (cubic-bezier preferred)
- **Gold accents sparingly**: Let them guide attention
- **High contrast**: Cream text on dark backgrounds
- **Geometric elegance**: Clean lines, mathematical forms
- **Progressive revelation**: Reveal information in layers

---

## Production Rules & Expert Principles

### ⚡ Core Rules (Non-Negotiable)

**Rule 1: Request Media Assets Early**
- If the narrative requires images, icons, SVGs, or PNGs, **ask the user immediately**
- Don't assume you can generate them; get the real assets
- Examples: street view photos, architectural renders, custom graphics
- This applies to every scene where visuals are critical

**Rule 2: Frame Consistency & Readability Audit**
- **Always, always double-check** readability and geometric consistency of every frame
- Before finalizing each scene:
  - ✅ Are all text elements legible on dark backgrounds?
  - ✅ Do geometric shapes align with intention (no accidental distortions)?
  - ✅ Do hierarchical structures visually match their conceptual meaning?
  - ✅ Are proportions correct? (No lopsided trees, misaligned nodes, etc.)
  - ✅ Does the frame look intentional, not accidental?

**Rule 3: Narrative Clarity Through Hierarchy**
- Every visual must reinforce the hierarchical concept
- **Concrete Example**: When showing Paris:
  - Start with: Image of a street
  - Reveal: "This is Paris" (city level)
  - Expand: "Paris is in France" (country level)
  - Zoom out: "France is in Europe" (continent level)
  - Visually show this nesting: Paris ⊂ France ⊂ Europe ⊂ Earth
  - Use indentation, size changes, or spatial positioning to show hierarchy

### 🧠 Expert Principles (60 Years of Storytelling)

**Be a Creative Storyteller**
- Think like a documentarian: every scene should tell part of a larger narrative
- Use tension and release: build confusion, then resolve with clarity
- Create "aha moments" that feel earned, not spoon-fed

**Be a Research Expert**
- Ground visuals in correct concepts (no hand-wavy approximations)
- When unsure about representation, ask questions
- Prefer accuracy over simplification; complexity can still be beautiful

**Be a Visual Designer**
- Let negative space breathe; don't clutter
- Color is a tool; use sparingly and intentionally
- Motion should enhance understanding, not distract

### 📋 Quality Checklist (Before Each Scene Implementation)

- [ ] Readability: Can someone with poor eyesight read this?
- [ ] Hierarchy: Do visual relationships match conceptual relationships?
- [ ] Media: Do I need assets from the user? (Ask now, don't assume)
- [ ] Consistency: Does this match the aesthetic and pacing of previous scenes?
- [ ] Purpose: Can I explain in one sentence why this scene exists?
- [ ] Narrative: Does this move the story forward?

---

## Scene-by-Scene Breakdown


### Scene 1: HOOK – The Problem Space
**Duration**: ~20 seconds
**Purpose**: Capture attention, pose the central question

#### Visual Elements
- **Title animation**: "HierLoc" in DM Serif Display, gold accent on "Loc"
- **Subtitle**: "Where Are You?" appears below
- **Background**: Subtle geodesic pattern (dark gold, low opacity)
- **Transition**: Smooth fade-in from black

#### Content
- Open with a mysterious street view image (no text, no UI)
- Text appears: "Can you guess where this photo was taken?"
- Image transitions to next photo (completely different continent)
- Text: "Without relying on people, landmarks, or language..."
- Beat pause (1 second)
- Question: "How would a computer solve this?"

#### Narration Notes
- Tone: Curious, inviting. "Let's think about something fascinating..."
- Pacing: Give images 2-3 seconds each to absorb
- Hook: Make the viewer feel the difficulty

#### Technical Notes
- Use `Group` for title + subtitle layering
- Fade images in with `FadeIn` animation
- Text appears character-by-character with `Write` for emphasis
- If you think an image, icon, svg, png are required to convey the narrative please ask the user for the media

---

### Scene 2: THE PROBLEM – Traditional Approach
**Duration**: ~40 seconds
**Purpose**: Explain the naive/existing solution and why it fails

#### Visual Elements
- **Scale representation**: Show 5M+ images as a grid/cloud
- **Search metaphor**: Simple arrows showing image-to-image search
- **Pain points**: Annotate with red/muted gold: "Slow", "Memory-intensive", "No structure"
- **A globe**: Show geographic distribution (hint at structure they're missing)

#### Content
- **Scene opens** with millions of dots representing images
  - Narration: "Modern geolocation works like this: you have millions of photos indexed globally"
  - Camera pulls back to show overwhelming scale
- **One image highlights** (your test photo)
  - Narration: "Your photo compares against every single one"
  - Animated arrows fan out from your image to thousands of others
- **Comparison metric**: Appears as labels (distances, similarity scores)
  - Narration: "Finding the closest match takes time, uses huge amounts of memory..."
- **Geography is invisible**: Dots are scattered randomly
  - Narration: "And the system doesn't 'understand' that places have structure"

#### Narration Notes
- Tone: Matter-of-fact, building tension. "This works... but..."
- Pacing: Let the scale sink in (5M is *big*)
- Transition: "What if we thought differently?"

#### Technical Notes
- Create a `Dot` cloud with random positions
- Animate search with `AnimatedBracketedLine` or `Arrow`
- Text labels fade in over pain points with color change (muted gold)
- Use `Axes` or custom grid for scale sense

---

### Scene 3: THE INSIGHT – Geographic Hierarchy
**Duration**: ~30 seconds
**Purpose**: Reveal that geography has inherent structure (hierarchy)

#### Visual Elements
- **Organizational chart**: Branching tree from "Earth" → Continents → Countries → Regions → Cities
- **Concrete example visualization**: Nested structure (Paris ⊂ France ⊂ Europe ⊂ Earth)
- **Exponential growth animation**: Visually show how branches multiply
- **Problem highlighted**: Euclidean space vs Hyperbolic space comparison
- **Hyperbolic disk**: Introduce Poincaré disk representation (subtle, not overwhelming)

#### Content
- **Scene opens** with flattened geographic dots
  - Narration: "But wait. Geography isn't random—it's *hierarchical*"
- **Concrete example appears** (Using Paris as tangible example):
  - Single street photo appears with label "Paris"
  - Narration: "Take a street photo from Paris..."
  - Container expands around it: "This is also France"
  - Another container expands: "Which is in Europe"
  - Final container: "Which is on Earth"
  - Visually show nesting with indentation or box-within-box layout
  - Use gold coloring to highlight the containment relationships
- **Generalize to tree structure**: Earth → Continents (7) → Countries (195) → Regions (1000s) → Cities (10,000s+)
  - Narration: "Each level branches exponentially. One continent contains countries; each country contains regions..."
  - Visual: Gold lines connect nodes, showing the hierarchy
  - Narration: "The deeper you go, the more entities multiply"
- **Problem appears**: In Euclidean space
  - Narration: "Here's the problem. In regular (Euclidean) space..."
  - Animation: Show entities at deep levels crowding together (distances collapse)
  - Highlight with visual crowding effect: cities squeezed tightly, hard to distinguish
  - Paint problem areas in dim red/muted gold
  - Narration: "...everything at the deepest level gets crammed together. Cities lose their distinctiveness."
- **Solution hint**: Hyperbolic space
  - Narration: "But there's a geometry that matches this structure perfectly..."
  - Hyperbolic disk briefly appears, rotates, then fades
  - Narration: "Hyperbolic space. It has exponential volume growth—like hierarchy itself."
  - Visual: Show same entities (cities, regions) spread out nicely in hyperbolic space (implied)

#### Narration Notes
- Tone: Building excitement. "This is elegant..."
- Pacing: Let hierarchy reveal gradually (start concrete with Paris, then generalize)
- Key insight: Geometry mirrors structure
- **Avoid**: Overwhelming the viewer with too many branches at once; build gradually

#### Technical Notes
- **Concrete example (Paris)**:
  - Use nested `Rectangle` or `VGroup` objects to show containment
  - Start with street photo (size: TBD, request from user if needed)
  - Animate expanding rectangles with appropriate labels
  - Color: Gold for highlight, muted for secondary
- Use `Tex` for branching tree labels
- Animate branches with `Create` animations (one level at a time)
- Show crowding with a zoomed-in view of deep level (cities layer should look cramped in Euclidean)
- Hyperbolic disk: Could use `BezierPath` or custom drawing (don't need full geometric accuracy, just aesthetic)
- Color transitions: Gold accents on key insight moments
- ⚠️ **CHECK READABILITY**: Ensure city/region names are legible even when "cramped" in Euclidean space

---

### Scene 4: THE SOLUTION – Entity Alignment
**Duration**: ~70 seconds
**Purpose**: Show how HierLoc works: image → entity embedding → hierarchical search

#### Visual Elements
- **Entity embedding space**: Hyperbolic visualization (simplified)
- **Image input**: Photo appears, gets encoded into embedding vector
- **Entity hierarchy on the right**: Countries/regions/cities as nodes
- **Matching animation**: Image embedding aligns with entity embeddings
- **Hierarchical search**: Visualize beam search (narrow down through hierarchy)
- **Efficiency metric**: "240k embeddings vs 5M+ images" appears as comparison

#### Content
- **Scene opens** with an image appearing on the left
  - Narration: "Here's HierLoc's key insight: instead of comparing against every image..."
- **Image gets vectorized**: Encoder animation (maybe a funnel narrowing the image)
  - Narration: "...we encode the image into a vector, just like we encode geographic entities"
- **Entity space appears on the right**: Hyperbolic background, countries/regions/cities as glowing nodes
  - Gold nodes (primary entities), dimmer ones (secondary)
  - Narration: "We've already learned embeddings for every country, region, subregion, city..."
- **Alignment happens**: Image vector moves toward the space and aligns with nearest entity
  - Narration: "The image 'votes' for which entity it belongs to"
  - Gold glow appears around nearest matches
- **Hierarchical search visualized**:
  - Narration: "And search is fast: start at the country level, then refine to region, then subregion..."
  - Animation: Progressively narrow down (like a funnel or tree traversal)
  - Show comparison: arrows pointing from image to entities get shorter/faster
- **Efficiency metric appears**:
  - "240k entity embeddings" (small set, animates in) vs "5M+ image embeddings" (large set, fades behind)
  - Narration: "95% reduction in what we need to store and search"

#### Narration Notes
- Tone: Confident, satisfied. "Elegant, right?"
- Pacing: This is the technical heart; give it time but keep it intuitive
- Avoid: Heavy math; focus on the idea

#### Technical Notes
- Create a custom hyperbolic embedding visualization (don't need true Lorentz model, just aesthetics)
- Use `Dot` objects for entities, possibly with varying sizes (hierarchy depth)
- Animate `Arrow` or `AnimatedLine` for image → entity matching
- Branching search: Use `Indicate` or glow effects to show refinement
- Text comparisons: Use `Table` or side-by-side text + numbers
- Color: Primary entities in full gold, secondary in dimmed gold

---

### Scene 5: THE PAYOFF – Results & Impact
**Duration**: ~30 seconds
**Purpose**: Show concrete results, efficiency gains, why this matters

#### Visual Elements
- **Results table/bars**: Accuracy improvements (19.5% error reduction, +43.2% subregion)
- **Efficiency visualization**: Speed/memory comparison
- **Globe with highlights**: Show geographic coverage
- **"State of the art" badge**: Achievement highlight
- **Call to action**: Point to paper/research

#### Content
- **Scene opens** with results appearing as animated bars or table
  - Metrics: Mean geodesic error ↓ 19.5%, Country +8.8%, Region +20.1%, Subregion +43.2%
  - Narration: "The results? State-of-the-art performance across every geographic level"
- **Efficiency comparison**:
  - "Traditional methods: O(N) comparisons, massive memory overhead"
  - "HierLoc: Sub-linear search, 95% fewer embeddings to store"
  - Animation: Progress bar or speedometer showing improvement
  - Narration: "It's faster, more memory-efficient, and—here's the kicker—interpretable."
- **Interpretability bonus**:
  - Narration: "You know *which entities* matched. Not just 'nearest image,' but 'this place is in Germany, Bavaria, Munich'"
  - Show a path: Image → Germany → Bavaria → Munich (highlighted in gold)
- **Broader impact**:
  - Narration: "This shows something bigger: hyperbolic geometry is the right tool for hierarchical data"
  - Quick montage of other potential uses (if applicable) or just emphasis on the elegance
- **Final frame**:
  - Title appears: "HierLoc: Hierarchical Visual Geolocation"
  - Subtitle: "Learn more"
  - Links/CTA (Paper, Code, Website)

#### Narration Notes
- Tone: Triumphant, proud of the work. This is the "aha moment" payoff
- Pacing: Let results breathe; they're impressive
- Transition: Bridge to "this matters because..."

#### Technical Notes
- Use `BarChart` or `PieChart` from Manim for results
- Animated counters for percentages (use `DecimalNumber` with `ChangingDecimal`)
- Speedometer: Could be a custom arc animation or `Arc` object
- Path visualization: Use `Indicate` for highlighting sequential locations
- Final frame: Use elegant typography, minimal design
- Optional: Brief replay of key visual (globe, hyperbolic disk) in background fade

---

## Transitions & Flow

### Overall Pacing
- **Hook** (0-0:20): Fast, punchy. Build curiosity.
- **Problem** (0:20-1:00): Slower. Let complexity sink in.
- **Insight** (1:00-2:00): Medium. Building excitement.
- **Solution** (2:00-3:30): Fast. Show the elegance.
- **Results** (3:30-4:00): Triumphant. Celebration.

### Recurring Visual Motifs
1. **Gold accents**: Appear at "aha moments," highlight breakthroughs
2. **Hierarchical structures**: Trees, branching patterns appear throughout
3. **Hyperbolic geometry**: Subtle Poincaré disk or hyperboloid appears (build up to it)
4. **Entity nodes**: Small glowing dots represent geographic entities (establish visual language early)

### Transition Techniques
- **Fade to black** between major sections
- **Expand/contract**: Zoom in/out to shift scales (problem → solution)
- **Reposition**: Objects slide into new roles (e.g., image becomes vector becomes entity)
- **Color shift**: Gold accent guides attention through transitions

---

## Mathematical Content to Render

### Required Equations/Formulas

1. **Contrastive loss** (InfoNCE or GWH-InfoNCE):
   ```
   ℒ = -log [ exp(sim(image, entity+)) / Σ_j w_j · exp(sim(image, entity_j)) ]
   ```
   - Where w_j incorporates haversine distance

2. **Haversine distance** (optional, can simplify):
   ```
   d = 2R · arcsin(√[sin²(Δφ/2) + cos(φ1)·cos(φ2)·sin²(Δλ/2)])
   ```
   - Visual: Just show "geographic distance weighting"

3. **Hyperbolic distance** (Lorentz model):
   ```
   d_ℍ(x,y) = arcosh(-⟨x,y⟩_ℒ / K)
   ```
   - Visual: Just the formula, no deep derivation needed

4. **Efficiency metrics**:
   - Image embeddings: O(N) where N ≈ 5M
   - Entity embeddings: O(K) where K ≈ 240k
   - Improvement: 95% reduction

### What to Highlight (Not Derive)
- Don't prove why hyperbolic geometry works
- Do show visually why it makes sense (exponential volume = exponential hierarchy)
- Don't derive the loss function
- Do show it incorporates distance weighting

---

## Implementation Strategy

### Phase 1: Core Scenes (Non-Math)
1. Scene 1: Hook
2. Scene 2: Problem
3. Scene 3: Insight (geometry visual)
4. Scene 4: Solution
5. Scene 5: Results

### Phase 2: Add Polish
- Smooth transitions between scenes
- Consistent color application
- Pacing refinement

### Phase 3: Mathematical Visualizations (If Time)
- Embed equations with proper formatting
- Animate formula reveals
- Show comparisons side-by-side

### Phase 4: Audio & Narration
- Record narration (match the script)
- Add background music (subtle, supporting)
- Sound design (whoosh, chimes, etc.) for animations

---

## Design Checklist

- [ ] Color scheme matches website (`#0a0a0f` bg, `#e8a838` accent)
- [ ] Typography uses DM Serif Display & Syne fonts
- [ ] Scenes are visually distinct (different backgrounds/compositions)
- [ ] Transitions are smooth (no jarring cuts, except where intentional)
- [ ] Pacing feels natural (silence/pause for insight)
- [ ] Mathematical content is clear (not overwhelming)
- [ ] Call-to-action at the end (link to paper/code)
- [ ] Total duration 3-5 minutes
- [ ] No spelling/grammar errors in text overlays
- [ ] Animations use website's ease/spring timing functions
- [ ] Final output readable on mobile (text sizes appropriate)

---

## Next Steps

1. **Review this plan together** ← You are here
2. **Clarify any scenes** (adjust depth, emphasis, visuals)
3. **Extract website color/font files** for Manim
4. **Build render script** (`render_hierloc.sh`) to compile scenes
5. **Implement scenes** (Scene 1 → Scene 5, iteratively)
6. **Test and refine** (pacing, colors, transitions)
7. **Record narration** and add audio
8. **Deploy** to website and YouTube

---

## Questions for the User

As we review, think about:

1. **Scene balance**: Does each scene feel like the right length? Any you'd expand/contract?
2. **Visuals**: Are the metaphors (globe, hyperbolic disk, entity nodes) compelling?
3. **Depth**: Is the technical content approachable or too simplified?
4. **Narrative**: Does the story flow naturally? Any missing pieces?
5. **Color/style**: Does the design direction feel right for your brand?

Let's discuss! 🎬
