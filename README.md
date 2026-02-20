# HierLoc: Hyperbolic Entity Embeddings for Hierarchical Visual Geolocation

> **Published at ICLR 2026**
> A scalable, interpretable approach to global visual geolocation using hyperbolic geometry and hierarchical entity embeddings.

[![arXiv](https://img.shields.io/badge/arXiv-2601.23064-b31b1b.svg)](https://arxiv.org/abs/2601.23064)
[![ICLR 2026](https://img.shields.io/badge/ICLR-2026-informational.svg)](https://iclr.cc/)

## 📍 Project Overview

**HierLoc** addresses the challenge of visual geolocation—predicting where an image was taken—by reformulating it as an **image-to-entity alignment problem** in hyperbolic space. Rather than retrieving from millions of image embeddings, our method aligns images to a compact hierarchy of geographic entities (countries, regions, subregions, cities) embedded in hyperbolic geometry.

### Key Innovations

1. **Hyperbolic Embeddings for Hierarchies**: Exploit the exponential volume growth of hyperbolic space to faithfully represent geographic hierarchies where the number of entities grows exponentially with depth.

2. **Geo-Weighted Hyperbolic InfoNCE Loss**: Incorporate great-circle (haversine) distance into the contrastive objective to emphasize geographically proximal negatives.

3. **240k Entity Embeddings vs. 5M Image Embeddings**: Achieve 95%+ compression while improving accuracy, enabling:
   - Efficient inference with hierarchical beam search
   - Interpretable predictions (which entities matched)
   - Potential for client-side deployment

### Results on OSV5M Benchmark

| Metric | Improvement |
|--------|-------------|
| Mean Geodesic Error | **↓19.5%** vs. SOTA |
| Country Accuracy | **+8.8%** |
| Region Accuracy | **+20.1%** |
| Subregion Accuracy | **+43.2%** (significant fine-grained gain) |
| City Accuracy | **+16.8%** |

Also validated on **MediaEval'16**, **IM2GPS**, **IM2GPS3K**, and **YFCC4K**.

## 👥 Authors

**Hari Krishna Gadi**¹·², **Hongyi Luo**¹·², **Daniel Matos**¹, **Lu Liu**¹, **Yongliang Wang**¹, **Yanfeng Zhang**¹, **Liqiu Meng**²

¹ Huawei Riemann Lab
² Chair of Cartography, Technical University of Munich

**Contact**: `harikrishna.gadi1@huawei.com`

## 📚 Resources

- **Paper**: [arXiv:2601.23064](https://arxiv.org/abs/2601.23064) | [PDF](static/paper.pdf)
- **Website**: Interactive project page with visualizations and results
- **Conference**: [ICLR 2026](https://iclr.cc/)

## 🏗️ Repository Structure

```
iclr-website/
├── index.html                    # Project website (main entry point)
├── static/
│   ├── css/                      # Stylesheets (Bulma framework)
│   ├── js/                       # JavaScript (carousel, slider, animations)
│   ├── images/                   # Project images, plots, and visual assets
│   ├── videos/                   # Demo and explainer videos
│   ├── pdfs/                     # PDFs (paper, poster, etc.)
│   └── webfonts/                 # Font files
├── iclr2026/                     # LaTeX source for ICLR 2026 submission
│   ├── hierloc.tex               # Main paper LaTeX
│   ├── *.bst, *.sty              # BibTeX and LaTeX style files
│   ├── plots/                    # Generated paper plots (PDFs)
│   └── *.bib                     # Bibliography database
├── paper.pdf                     # Final paper PDF
└── .gitignore                    # Git ignore rules

```

See [STRUCTURE.md](STRUCTURE.md) for detailed explanation of directory organization and development guidelines.

## 🚀 Website Setup & Deployment

### Local Development

No build step required—simply open `index.html` in a browser:

```bash
# Clone the repository
git clone https://github.com/harikrishnagadi/iclr-website.git
cd iclr-website

# Serve locally (requires Python or Node.js)
# Python 3
python -m http.server 8000

# Or Node.js
npx http-server
```

Visit `http://localhost:8000` to view the website.

### GitHub Pages Deployment

This repository is configured for automatic deployment to GitHub Pages:

1. Ensure the repository is public
2. Go to **Settings → Pages**
3. Set source to `master` branch
4. The site will be available at `https://<your-username>.github.io/iclr-website`

### Customization

The website is built on the **Academic Project Page Template**. To customize:

1. **Edit content**: Modify `index.html` directly (HTML comments show where to update)
2. **Update styling**: Edit `static/css/index.css` for colors, fonts, and layout
3. **Replace images/videos**: Place new assets in `static/images/` or `static/videos/`
4. **Update links**: arXiv, GitHub, paper PDF, etc.

**Important**: Replace `static/images/favicon.ico` with your own favicon.

## 📖 Technical Details

### Hyperbolic Geometry

We operate in the **Lorentz model** of hyperbolic space with constant curvature -1/K. Key properties:

- **Exponential volume growth**: Naturally accommodates branching hierarchies
- **Distance metric**: Geodesic distance via arcosh formula
- **Operations**: Performed in tangent space at origin using exponential/logarithmic maps

### Entity Hierarchy

```
World
├── Continent (e.g., Europe, Asia)
│   ├── Country (e.g., Germany, China)
│   │   ├── Region (e.g., Bavaria, Jiangsu)
│   │   │   └── Subregion (e.g., Munich, Nanjing)
│   │   │       └── City (e.g., specific urban areas)
```

The hyperbolic space maintains semantic relationships while keeping fine-grained locations well-separated.

### Contrastive Learning

**Geo-Weighted Hyperbolic InfoNCE Loss**:

```
ℒ = -log [ exp(sim(i, e+)) / Σ_j w_j · exp(sim(i, e_j)) ]
```

Where `w_j = exp(-haversine_distance(entity_j) / σ)` weights negatives by geographic proximity.

## 📊 Benchmarks & Evaluation

| Dataset | Split | # Images | Scenes |
|---------|-------|----------|--------|
| **OSV5M** | Train: 4.8M, Test: 200k | 5M+ | Global street view |
| **MediaEval'16** | Train: 4.7M | 4.7M | Flickr images |
| **IM2GPS** | Test: 143k | 143k | Diverse geo-tagged images |
| **IM2GPS3K** | Test: 3k | 3k | Geographic diversity challenge |
| **YFCC4K** | Test: 4k | 4k | Flickr dataset (hard cases) |

## 🔬 Research Contributions

1. **Reformulate geolocation** from image-image retrieval to image-entity alignment
2. **Demonstrate hyperbolic advantage** for hierarchical geographic representation
3. **Introduce GWH-InfoNCE** loss incorporating great-circle distance
4. **Achieve SOTA** across all hierarchy levels on OSV5M
5. **Enable scalable inference** via hierarchical beam search and 95% embedding reduction

## 📝 Citation

```bibtex
@article{gadi2026hierloc,
  title={HierLoc: Hyperbolic Entity Embeddings for Hierarchical Visual Geolocation},
  author={Gadi, Hari Krishna and Luo, Hongyi and Matos, Daniel and Liu, Lu and Wang, Yongliang and Zhang, Yanfeng and Meng, Liqiu},
  journal={arXiv preprint arXiv:2601.23064},
  year={2026}
}
```

## 📄 License

Website: Licensed under [Creative Commons Attribution-ShareAlike 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
Paper: See the paper for research publication terms.

## 🙏 Acknowledgments

- Built on the [Academic Project Page Template](https://github.com/eliahuhorwitz/Academic-project-page-template)
- Visualization and carousel components via [Bulma CSS Framework](https://bulma.io/)
- Icons from [FontAwesome](https://fontawesome.com/) and [Academicons](https://jpswalsh.github.io/academicons/)
- Inspired by [Nerfies](https://nerfies.github.io/) project page design
