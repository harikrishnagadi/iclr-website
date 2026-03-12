/* ═══════════════════════════════════════════════════════════
   HierLoc — Three.js Hero: Lorentz Hyperboloid + Poincaré Disk
   Interactive 3D visualization of hyperbolic embedding space
   ═══════════════════════════════════════════════════════════ */
window.addEventListener('DOMContentLoaded', function () {
  'use strict';
  if (typeof THREE === 'undefined') { console.warn('Three.js not loaded'); return; }
  var container = document.getElementById('hero-3d-container');
  if (!container) { console.warn('hero-3d-container not found'); return; }

  /* ── Dimensions (use parent or window as fallback) ───────── */
  var W = container.offsetWidth  || container.parentElement.offsetWidth  || window.innerWidth;
  var H = container.offsetHeight || container.parentElement.offsetHeight || window.innerHeight;
  if (W === 0 || H === 0) { W = window.innerWidth; H = window.innerHeight; }

  /* ── Config ──────────────────────────────────────────────── */
  var ACCENT     = 0x007aff;
  var ACCENT_DIM = 0x0033aa;
  var PURPLE   = 0x2a1f3d;
  var U_MAX    = 1.55;
  var isMobile = W < 768;

  var LEVELS = [
    { u: 0.28, count: isMobile ? 4  : 6,   size: 0.09,  color: 0xf5cc7a, label: 'continent' },
    { u: 0.58, count: isMobile ? 8  : 14,  size: 0.06,  color: 0xe8a838, label: 'country' },
    { u: 0.92, count: isMobile ? 16 : 28,  size: 0.038, color: 0xc88a30, label: 'region' },
    { u: 1.32, count: isMobile ? 24 : 48,  size: 0.022, color: 0x9c6a2e, label: 'city' },
  ];

  /* ── Scene, Camera, Renderer ─────────────────────────────── */
  var scene  = new THREE.Scene();
  var camera = new THREE.PerspectiveCamera(36, W / H, 0.1, 100);
  camera.position.set(0, 3.8, 6.2);
  camera.lookAt(0, 0.8, 0);

  var renderer = new THREE.WebGLRenderer({
    antialias: !isMobile,
    alpha: true,
    powerPreference: isMobile ? 'low-power' : 'default',
  });
  renderer.setSize(W, H);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, isMobile ? 1.5 : 2));
  renderer.setClearColor(0x000000, 0);
  container.appendChild(renderer.domElement);

  /* ── Master Group ────────────────────────────────────────── */
  var world = new THREE.Group();
  world.position.y = -1.0;
  scene.add(world);

  /* ── Hyperboloid Helpers ─────────────────────────────────── */
  function hypPt(u, v) {
    return new THREE.Vector3(
      Math.sinh(u) * Math.cos(v),
      Math.cosh(u),
      Math.sinh(u) * Math.sin(v)
    );
  }

  function toPoincare(pos, diskR) {
    var x0 = pos.y;
    var x1 = pos.x, x2 = pos.z;
    var d = x0 + 1;
    return new THREE.Vector3((x1 / d) * diskR, 0, (x2 / d) * diskR);
  }

  /* ── Hyperboloid Surface ─────────────────────────────────── */
  var SEG = isMobile ? 32 : 48;
  var RING = isMobile ? 16 : 24;
  var verts = [], idx = [];

  for (var i = 0; i <= RING; i++) {
    var u = (i / RING) * U_MAX;
    for (var j = 0; j <= SEG; j++) {
      var v = (j / SEG) * Math.PI * 2;
      var p = hypPt(u, v);
      verts.push(p.x, p.y, p.z);
    }
  }
  for (var i = 0; i < RING; i++) {
    for (var j = 0; j < SEG; j++) {
      var a = i * (SEG + 1) + j;
      var b = a + SEG + 1;
      idx.push(a, b, a + 1, b, b + 1, a + 1);
    }
  }

  var hGeom = new THREE.BufferGeometry();
  hGeom.setAttribute('position', new THREE.Float32BufferAttribute(verts, 3));
  hGeom.setIndex(idx);
  hGeom.computeVertexNormals();

  // Translucent surface
  world.add(new THREE.Mesh(hGeom, new THREE.MeshBasicMaterial({
    color: PURPLE,
    transparent: true,
    opacity: 0.35,
    side: THREE.DoubleSide,
    depthWrite: false,
  })));

  // Wireframe overlay
  world.add(new THREE.LineSegments(
    new THREE.WireframeGeometry(hGeom),
    new THREE.LineBasicMaterial({
      color: ACCENT,
      transparent: true,
      opacity: 0.2,
    })
  ));

  /* ── Hierarchy Rings on Hyperboloid ──────────────────────── */
  LEVELS.forEach(function (lv) {
    var pts = [];
    var N = isMobile ? 64 : 128;
    for (var j = 0; j <= N; j++) {
      pts.push(hypPt(lv.u, (j / N) * Math.PI * 2));
    }
    world.add(new THREE.Line(
      new THREE.BufferGeometry().setFromPoints(pts),
      new THREE.LineBasicMaterial({
        color: lv.color,
        transparent: true,
        opacity: 0.4,
      })
    ));
  });

  /* ── Glow Sprite Texture ─────────────────────────────────── */
  var gc = document.createElement('canvas');
  gc.width = gc.height = 64;
  var gx = gc.getContext('2d');
  var gr = gx.createRadialGradient(32, 32, 0, 32, 32, 32);
  gr.addColorStop(0,    'rgba(255,255,255,1)');
  gr.addColorStop(0.15, 'rgba(255,255,255,0.85)');
  gr.addColorStop(0.4,  'rgba(255,255,255,0.2)');
  gr.addColorStop(1,    'rgba(255,255,255,0)');
  gx.fillStyle = gr;
  gx.fillRect(0, 0, 64, 64);
  var glowTex = new THREE.CanvasTexture(gc);

  /* ── Entity Points ───────────────────────────────────────── */
  var entities = [];

  LEVELS.forEach(function (lv) {
    for (var i = 0; i < lv.count; i++) {
      var v  = (i / lv.count) * Math.PI * 2 + (Math.random() - 0.5) * 0.35;
      var uJ = lv.u + (Math.random() - 0.5) * 0.1;
      var pos = hypPt(uJ, v);

      var sprite = new THREE.Sprite(new THREE.SpriteMaterial({
        map: glowTex,
        color: lv.color,
        transparent: true,
        opacity: 0.9,
        blending: THREE.AdditiveBlending,
        depthWrite: false,
      }));
      sprite.position.copy(pos);
      sprite.scale.setScalar(lv.size * 4);
      world.add(sprite);

      entities.push({
        sprite: sprite,
        basePos: pos.clone(),
        level: lv.label,
        phase: Math.random() * Math.PI * 2,
        baseScale: lv.size * 4,
      });
    }
  });

  /* ── Geodesic Connections (parent → child) ───────────────── */
  for (var li = 0; li < LEVELS.length - 1; li++) {
    var parents  = entities.filter(function (e) { return e.level === LEVELS[li].label; });
    var children = entities.filter(function (e) { return e.level === LEVELS[li + 1].label; });

    parents.forEach(function (parent) {
      var nearby = children
        .map(function (c) { return { c: c, d: parent.basePos.distanceTo(c.basePos) }; })
        .sort(function (a, b) { return a.d - b.d; })
        .slice(0, 1 + Math.floor(Math.random() * 2));

      nearby.forEach(function (item) {
        var pts = [];
        var N = 14;
        for (var i = 0; i <= N; i++) {
          var t   = i / N;
          var mid = new THREE.Vector3().lerpVectors(parent.basePos, item.c.basePos, t);
          var r   = Math.sqrt(mid.x * mid.x + mid.z * mid.z);
          if (r > 0.001) mid.y = Math.sqrt(1 + r * r);
          pts.push(mid);
        }
        world.add(new THREE.Line(
          new THREE.BufferGeometry().setFromPoints(pts),
          new THREE.LineBasicMaterial({
            color: ACCENT,
            transparent: true,
            opacity: 0.15,
          })
        ));
      });
    });
  }

  /* ── Poincaré Disk (projected floor) ─────────────────────── */
  var DISK_R = 2.2;
  var DISK_Y = -0.15;

  // Boundary circle
  var bPts = [];
  var bN = isMobile ? 64 : 128;
  for (var i = 0; i <= bN; i++) {
    var a = (i / bN) * Math.PI * 2;
    bPts.push(new THREE.Vector3(Math.cos(a) * DISK_R, DISK_Y, Math.sin(a) * DISK_R));
  }
  world.add(new THREE.Line(
    new THREE.BufferGeometry().setFromPoints(bPts),
    new THREE.LineBasicMaterial({ color: ACCENT, transparent: true, opacity: 0.35 })
  ));

  // Concentric Poincaré rings
  [0.25, 0.45, 0.65, 0.85].forEach(function (frac) {
    var rPts = [];
    for (var j = 0; j <= bN; j++) {
      var a = (j / bN) * Math.PI * 2;
      rPts.push(new THREE.Vector3(
        Math.cos(a) * DISK_R * frac, DISK_Y, Math.sin(a) * DISK_R * frac
      ));
    }
    world.add(new THREE.Line(
      new THREE.BufferGeometry().setFromPoints(rPts),
      new THREE.LineBasicMaterial({ color: ACCENT, transparent: true, opacity: 0.12 })
    ));
  });

  // Radial spokes on disk
  for (var i = 0; i < 12; i++) {
    var a = (i / 12) * Math.PI * 2;
    world.add(new THREE.Line(
      new THREE.BufferGeometry().setFromPoints([
        new THREE.Vector3(0, DISK_Y, 0),
        new THREE.Vector3(Math.cos(a) * DISK_R, DISK_Y, Math.sin(a) * DISK_R),
      ]),
      new THREE.LineBasicMaterial({ color: ACCENT, transparent: true, opacity: 0.08 })
    ));
  }

  // Project entities onto disk + projection lines
  entities.forEach(function (e) {
    var dp = toPoincare(e.basePos, DISK_R);
    dp.y = DISK_Y;

    var ds = new THREE.Sprite(new THREE.SpriteMaterial({
      map: glowTex,
      color: e.sprite.material.color,
      transparent: true,
      opacity: 0.6,
      blending: THREE.AdditiveBlending,
      depthWrite: false,
    }));
    ds.position.copy(dp);
    ds.scale.setScalar(e.baseScale * 0.7);
    world.add(ds);

    world.add(new THREE.Line(
      new THREE.BufferGeometry().setFromPoints([e.basePos.clone(), dp]),
      new THREE.LineBasicMaterial({
        color: ACCENT_DIM,
        transparent: true,
        opacity: 0.06,
      })
    ));

    e.diskSprite = ds;
  });

  /* ── Ambient Dust Particles ──────────────────────────────── */
  var PCOUNT = isMobile ? 60 : 150;
  var pGeom  = new THREE.BufferGeometry();
  var pPos   = new Float32Array(PCOUNT * 3);
  var pVel   = [];

  for (var i = 0; i < PCOUNT; i++) {
    var u = Math.random() * U_MAX;
    var v = Math.random() * Math.PI * 2;
    var p = hypPt(u, v);
    var off = (Math.random() - 0.5) * 0.5;
    pPos[i * 3]     = p.x + off;
    pPos[i * 3 + 1] = p.y + off * 0.3;
    pPos[i * 3 + 2] = p.z + off;
    pVel.push(0.0004 + Math.random() * 0.0015);
  }
  pGeom.setAttribute('position', new THREE.Float32BufferAttribute(pPos, 3));

  var dust = new THREE.Points(pGeom, new THREE.PointsMaterial({
    color: ACCENT,
    size: 0.015,
    transparent: true,
    opacity: 0.4,
    blending: THREE.AdditiveBlending,
    depthWrite: false,
    sizeAttenuation: true,
  }));
  world.add(dust);

  /* ── Mouse Tracking ──────────────────────────────────────── */
  var mouse = { x: 0, y: 0, tx: 0, ty: 0 };
  window.addEventListener('mousemove', function (e) {
    mouse.tx = (e.clientX / window.innerWidth  - 0.5) * 2;
    mouse.ty = (e.clientY / window.innerHeight - 0.5) * 2;
  });

  /* ── Resize Handler ──────────────────────────────────────── */
  var resizeTimer;
  window.addEventListener('resize', function () {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function () {
      var w = container.offsetWidth  || window.innerWidth;
      var h = container.offsetHeight || window.innerHeight;
      camera.aspect = w / h;
      camera.updateProjectionMatrix();
      renderer.setSize(w, h);
    }, 100);
  });

  /* ── Fade-in ─────────────────────────────────────────────── */
  renderer.domElement.style.opacity = '0';
  renderer.domElement.style.transition = 'opacity 1.5s ease';
  setTimeout(function () {
    renderer.domElement.style.opacity = '1';
  }, 50);

  /* ── Animation Loop ──────────────────────────────────────── */
  var t = 0;
  var isVisible = true;

  var visObs = new IntersectionObserver(function (entries) {
    isVisible = entries[0].isIntersecting;
  }, { threshold: 0.05 });
  visObs.observe(container);

  function animate() {
    requestAnimationFrame(animate);
    if (!isVisible) return;

    t += 0.003;

    mouse.x += (mouse.tx - mouse.x) * 0.025;
    mouse.y += (mouse.ty - mouse.y) * 0.025;

    world.rotation.y = t * 0.1 + mouse.x * 0.2;
    world.rotation.x = mouse.y * 0.06 - 0.05;

    for (var i = 0; i < entities.length; i++) {
      var e = entities[i];
      var pulse = 1 + 0.18 * Math.sin(t * 2.5 + e.phase);
      e.sprite.scale.setScalar(e.baseScale * pulse);
    }

    var pos = dust.geometry.attributes.position.array;
    for (var i = 0; i < PCOUNT; i++) {
      var x = pos[i * 3], z = pos[i * 3 + 2];
      var angle = Math.atan2(z, x) + pVel[i];
      var r = Math.sqrt(x * x + z * z);
      pos[i * 3]     = r * Math.cos(angle);
      pos[i * 3 + 2] = r * Math.sin(angle);
    }
    dust.geometry.attributes.position.needsUpdate = true;

    renderer.render(scene, camera);
  }

  animate();
  console.log('HierLoc 3D hero initialized:', W + 'x' + H);
});
