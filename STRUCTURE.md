# Repository Structure & Development Guidelines

This document explains the organization of the HierLoc repository and the principles that guide its structure.

## Directory Organization

### Root Level Files

```
index.html           # Main website (entry point)
paper.pdf            # PDF copy of the published paper
README.md            # Project overview, resources, and setup
STRUCTURE.md         # This file - repository guidelines
.gitignore          # Git ignore rules
.nojekyll           # Disable Jekyll processing for GitHub Pages
```

### `/iclr2026/` — Conference Submission & Paper

Contains all academic paper materials for ICLR 2026:

```
iclr2026/
├── hierloc.tex                  # Main paper LaTeX file
├── iclr2026_conference.bib      # Bibliography database
├── iclr2026_conference.sty      # ICLR style file (conference template)
├── arxiv.sty                    # ArXiv style file
├── natbib.sty                   # Bibliography package style
├── fancyhdr.sty                 # Header/footer styling
├── iclr2026_conference.bst      # BibTeX style
├── math_commands.tex            # Shared LaTeX math macros
├── algo.tex                     # Algorithm descriptions
├── performance_comparison.tex   # Performance tables and comparison
├── graphs.tex                   # Graph/plot definitions
├── iclr2026_conference.pdf      # Compiled paper PDF
└── plots/                       # Generated paper figures (PDF & PNG)
    ├── main_architecture.pdf    # System architecture diagram
    ├── banner_plot.pdf          # Banner/teaser image
    ├── mean_error_raster_grid.pdf
    ├── scaling_wallclock_to_2B.pdf
    ├── lorentz.pdf              # Hyperbolic space visualization
    ├── island_nonisland_panels.pdf
    ├── hierloc_vs_sc_inference.pdf
    ├── beam_width_plots.pdf
    └── [plus PNG versions for web display]
```

**Purpose**: Maintains the complete paper source and generation pipeline. These files are the authoritative academic record.

### `/static/` — Website Assets

Web-facing static files served directly to visitors.

```
static/
├── css/                         # Stylesheets
│   ├── bulma.min.css           # Bulma CSS framework (minified)
│   ├── bulma.css.map.txt       # CSS source map
│   ├── index.css               # Project-specific styles
│   ├── fontawesome.all.min.css # Icon font styles
│   ├── bulma-carousel.min.css  # Carousel component styles
│   └── bulma-slider.min.css    # Slider component styles
│
├── js/                          # JavaScript files
│   ├── index.js                # Custom project scripts
│   ├── fontawesome.all.min.js  # Icon font library
│   ├── bulma-carousel.min.js   # Carousel component
│   └── bulma-slider.min.js     # Slider component
│
├── images/                      # Visual assets
│   ├── favicon.ico             # Website favicon
│   ├── carousel1.jpg           # Carousel images (1-4)
│   ├── carousel2.jpg
│   ├── carousel3.jpg
│   ├── carousel4.jpg
│   ├── banner_plot.pdf         # Plots for display (PDF & PNG)
│   ├── banner_plot.png
│   ├── main_architecture.pdf
│   ├── main_architecture.png
│   ├── beam_width_plots.pdf
│   ├── beam_width_plots.png
│   ├── [other plot files]
│   ├── carousel_final/         # Web-optimized PNG versions of paper plots
│   │   ├── main_banner.png     # (converted from iclr2026/plots/ for web)
│   │   ├── main_architecture.png
│   │   ├── beam_width_plots.png
│   │   └── [other plot PNGs]
│   └── scene1_photo.jpg        # Additional media
│
├── videos/                      # Video content
│   ├── hierloc_explainer_new.mp4   # Explainer video
│   ├── hierloc_methodology.mp4     # Method overview
│   ├── hierloc_scale.mp4           # Scaling demonstration
│   └── [other demo videos]
│
└── pdfs/                        # PDF documents
    └── sample.pdf              # Sample/poster PDF
```

**Purpose**: Only web-optimized assets that are served to users. Images/plots should be compressed for web.

**Guidelines**:
- Use **PNG for plots** (rasterized for web display)
- Optimize image sizes with [TinyPNG](https://tinypng.com)
- Keep PDFs small (<5MB each)
- Use modern video codecs (H.264/H.265)

### `/.venv/` — Python Virtual Environment

Python virtual environment for development (e.g., for building LaTeX papers, generating plots):

```
.venv/
├── bin/              # Executables (python, pip, etc.)
├── lib/              # Python packages
├── share/            # Shared data
└── pyvenv.cfg       # Virtual environment configuration
```

**Guidelines**:
- Included in `.gitignore` — not committed to git
- Recreate with `python -m venv .venv`
- Install dependencies from a `requirements.txt` if needed

### `/.git/` — Git Repository

Git version control metadata. Not user-editable.

```
.git/
├── objects/          # Commit and object data
├── refs/             # Branch/tag references
├── hooks/            # Git hooks
├── logs/             # Reference logs
└── HEAD, config, etc.
```

## Core Principles

### 1. No Duplicate Files or Folders ⛔

**Strict Rule**: Never create multiple copies of the same content, EXCEPT for format conversion (PDF → PNG for web).

❌ **Bad Examples**:
```
plots/
iclr2026/plots/
static/images/plots/     ← Duplication!

paper.pdf
paper_final.pdf
paper_updated.pdf        ← Multiple versions!

scene_implementation.md
scene_implementation_v2.md
scene_implementation_final.md  ← Numbered variants!
```

✅ **Correct Approach**:
- **Single source of truth**: Keep content in ONE location
- **Format conversion is OK**: `iclr2026/plots/*.pdf` → `static/images/carousel_final/*.png` (different formats for different purposes)
- **No duplicate logic**: Don't have the same code/content in multiple places
- Use version control (git) for version history, not filename suffixes

### 2. Clear Separation of Concerns

Each directory has ONE purpose:

| Directory | Purpose | Who Uses | Commit to Git? |
|-----------|---------|----------|---|
| `index.html`, `static/` | Website & web display | Users/Visitors | ✅ Yes |
| `iclr2026/` | Paper source & academic record | Researchers | ✅ Yes |
| `.venv/` | Development environment | Local developers | ❌ No (.gitignore) |
| `.git/` | Version control | Git system | (auto-managed) |

### 3. Naming Conventions

**Files**:
- Use **snake_case** for filenames: `main_architecture.pdf`, `mean_error.py`
- Be **descriptive**: `beam_width_comparison.pdf` not `fig1.pdf`
- Avoid numbers unless essential: `carousel1.jpg` (component 1) is OK; `plot_final_v3.pdf` is NOT

**Directories**:
- Use **lowercase**: `/static/images` not `/Static/Images`
- Use **plural** for collections: `/plots`, `/images`, `/videos`
- Use **singular** for unique items: `index.html` (one file)

### 4. File Organization Rules

**When adding new files**:

1. **Identify the purpose**: Is this for the website or the paper?
   - Website? → Put in `static/`
   - Paper? → Put in `iclr2026/`
   - Both? → Put in `iclr2026/plots/` and **symlink or copy with clear naming** to `static/images/`

2. **Check for existing content**: Search the repo first
   ```bash
   find . -name "*keyword*" -type f
   ```

3. **Never create variants**: Don't create `file_v2.txt` or `file_final.txt`
   - Use git branches and commits for versions
   - Use git tags for releases

4. **Update only when necessary**:
   - Don't duplicate files just because they're needed in multiple places
   - Use symlinks if OS allows, or reference one file from multiple locations
   - If content must exist in two places, document why in a comment

### 5. Git Workflow

```bash
# ✅ Good: Atomic, well-named commits
git add index.html
git commit -m "Update teaser video link in hero section"

git add iclr2026/plots/*.pdf
git commit -m "Add performance comparison plots for paper"

# ❌ Bad: Generic messages, multiple unrelated changes
git add -A
git commit -m "updates"

# ❌ Bad: Creating duplicate files
git add paper_final.pdf paper_final_updated.pdf
```

**Branch Strategy**:
- `master` → stable, deployed version (matches website)
- Feature branches for work-in-progress (e.g., `feature/add-video`, `fix/typo-abstract`)
- Use git history (`git log`) for version tracking

## Common Tasks & Best Practices

### Adding a New Plot/Figure

**Scenario**: Generated a new plot from analysis.

1. Generate plot in `iclr2026/plots/` (keeps paper assets organized)
2. If needed for website, copy to `static/images/` with clear naming
3. If same content, add one file and reference it:
   ```markdown
   # In index.html
   <img src="iclr2026/plots/new_result.pdf">
   ```
4. Update `iclr2026/hierloc.tex` to reference the plot
5. **Commit once**:
   ```bash
   git add iclr2026/plots/new_result.pdf
   git add index.html iclr2026/hierloc.tex
   git commit -m "Add performance comparison plot"
   ```

### Updating the Website

**Scenario**: Changing text, images, or videos on the website.

1. Edit `index.html` or `static/css/index.css`
2. Replace/add images in `static/images/` (optimize first!)
3. Add videos to `static/videos/` if needed
4. Test locally: `python -m http.server 8000`
5. Commit changes:
   ```bash
   git add index.html static/
   git commit -m "Update project teaser and description"
   ```

### Updating the Paper

**Scenario**: Revising text, adding results, updating figures.

1. Edit `iclr2026/hierloc.tex` or include files
2. Update plots in `iclr2026/plots/` if needed
3. Compile LaTeX locally if you have tools
4. Update bibliography in `iclr2026/iclr2026_conference.bib`
5. Commit:
   ```bash
   git add iclr2026/
   git commit -m "Revise methodology section and add performance tables"
   ```

### Avoiding "Files Everywhere"

**Problem**: Over time, repos accumulate `file_v1`, `file_v2`, `final_file`, `backup_file`, etc.

**Solution**:
- Use git branches for parallel development
- Use git tags for stable versions: `git tag v1.0.0`
- Delete old temporary files immediately: `git rm old_file.txt`
- Trust git history: `git log --oneline` shows all past versions
- Archive old work in a separate (separate) branch if needed

```bash
# ✅ Good: Clean history with tags
git tag iclr2026-submission
git tag paper-revision-1

# ❌ Bad: Cluttered directory
ls *.pdf
→ paper.pdf, paper_final.pdf, paper_final_v2.pdf, paper_updated.pdf
```

## Development Environment Setup

### Python Virtual Environment

If you need to generate LaTeX PDFs or process plots:

```bash
# Create environment
python3 -m venv .venv

# Activate
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows

# Install dependencies (if you have a requirements.txt)
pip install -r requirements.txt

# Deactivate when done
deactivate
```

### Local Website Testing

```bash
# Python 3
python -m http.server 8000

# Or Node.js
npx http-server

# Or Ruby
ruby -run -ehttpd . -p8000
```

Visit `http://localhost:8000`

## Troubleshooting

### "I've created duplicate files by accident. How do I fix this?"

1. Identify the authoritative version (which is most up-to-date?)
2. Delete all duplicates:
   ```bash
   git rm file_v2.pdf file_final.pdf
   ```
3. Keep only one:
   ```bash
   git add file.pdf
   git commit -m "Remove duplicate file versions"
   ```

### "Large files are making the repo slow"

1. Check file sizes: `du -sh .`
2. Remove from git history if needed:
   ```bash
   git filter-branch --tree-filter 'rm -f large_file.zip' HEAD
   git push --force
   ```
3. Use `.gitignore` to prevent future large files (see `.gitignore` in repo)

### "I don't understand where to put a file"

Ask yourself:
- **Is it part of the website users see?** → `static/`
- **Is it part of the paper/research?** → `iclr2026/`
- **Is it temporary/development only?** → `.gitignore` or don't commit
- **When in doubt**, store in the primary location (`iclr2026/` for paper, `static/` for web) and reference from the other

## Summary

| Rule | Why |
|------|-----|
| **One source of truth** | Easier to maintain, reduces confusion |
| **Clear directory purposes** | Developers know where to look |
| **Descriptive naming** | No mystery about what a file contains |
| **Use git for versions** | Reliable, auditable history |
| **Keep repo clean** | Fast to clone, easy to navigate |

For questions or suggestions about structure, open an issue or update this document (STRUCTURE.md).
