# Ray Tracer

A from-scratch Python ray tracer built as a computer graphics learning project.

The repository is intentionally structured so that **theory, implementation, and tests evolve together**.

## Requirements

- Python 3.11+
- `venv`
- `pip`

## Development environment

Use a dedicated virtual environment for the project's development libraries.

Create the environment:

```bash
python3 -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Upgrade `pip`:

```bash
python -m pip install --upgrade pip
```

Install the project and development dependencies:

```bash
python -m pip install -e ".[dev]"
```

The development dependencies currently include:

- `pytest` — testing
- `ruff` — linting
- `mypy` — static type checking

Run the test suite:

```bash
pytest
```

You can also run the quality checks:

```bash
ruff check .
mypy src
```

The virtual environment is intentionally not committed to the repository. `.venv/` should be listed in `.gitignore`.

## Order of implementation

Implement the ray tracer incrementally. **Do not implement the whole architecture up front.** Each stage introduces a new mathematical or graphics concept.

### Phase 1 — Tuples, vectors, and points

Start with:

```text
src/raytracer/geometry/vector.py
src/raytracer/geometry/point.py

tests/unit/geometry/test_vector.py
tests/unit/geometry/test_point.py
```

Learn and implement:

- vector/point representation
- equality
- addition and subtraction
- scalar multiplication/division
- negation
- magnitude
- normalization
- dot product
- cross product

Goal: become comfortable representing geometry mathematically.

---

### Phase 2 — Rays

Implement:

```text
src/raytracer/geometry/ray.py
tests/unit/geometry/test_ray.py
```

Learn:

- ray origin
- ray direction
- parametric equations
- `P(t) = O + tD`

Goal: construct rays and calculate points along them.

---

### Phase 3 — Canvas and pixels

Implement:

```text
src/raytracer/image/canvas.py
tests/unit/image/test_canvas.py
```

Learn:

- representing an image
- pixel coordinates
- image boundaries
- eventually writing an image format such as PPM

Goal: have a way to visualize your mathematical results.

---

### Phase 4 — Sphere intersection

Implement:

```text
src/raytracer/shapes/sphere.py
tests/unit/shapes/test_sphere.py
```

Learn and derive yourself:

- sphere equation
- substituting a ray into the sphere equation
- quadratic equations
- discriminant
- ray/sphere intersection
- surface normals

Goal: render the silhouette of a sphere.

**Important:** derive the ray/sphere intersection mathematically before implementing it.

---

### Phase 5 — Materials and lighting

Implement:

```text
src/raytracer/rendering/material.py
src/raytracer/rendering/light.py

tests/unit/rendering/test_material.py
tests/unit/rendering/test_light.py
tests/unit/rendering/test_lighting.py
```

Learn:

- surface color
- point lights
- ambient lighting
- diffuse lighting
- specular lighting
- Lambert's cosine law
- reflection vectors

Goal: make the sphere look three-dimensional rather than flat.

---

### Phase 6 — Shadows

Extend the lighting implementation.

Learn:

- shadow rays
- visibility testing
- determining whether another object lies between a point and a light

Goal: render a lit sphere that casts and receives shadows.

---

### Phase 7 — Matrices and transformations

Implement:

```text
src/raytracer/geometry/matrix.py
src/raytracer/geometry/transform.py

tests/unit/geometry/test_matrix.py
tests/unit/geometry/test_transform.py
```

Learn:

- matrix multiplication
- identity matrices
- determinants
- matrix inversion
- translation
- scaling
- rotation
- coordinate transformations
- homogeneous coordinates

Goal: understand how objects and cameras move through 3D space.

---

### Phase 8 — Camera

Implement:

```text
src/raytracer/rendering/camera.py
tests/unit/rendering/test_camera.py
```

Learn:

- field of view
- aspect ratio
- pixel size
- camera transformation
- generating one ray per pixel

Goal: render an actual scene from a camera.

---

### Phase 9 — Scene / world

Implement:

```text
src/raytracer/scene/scene.py
tests/integration/test_render_scene.py
```

Learn:

- multiple objects
- object collections
- finding the closest intersection
- preparing intersection computations
- combining geometry, materials, lights, and camera

Goal: render a complete basic scene.

---

### Phase 10 — Planes

Implement:

```text
src/raytracer/shapes/plane.py
tests/unit/shapes/test_plane.py
```

Learn:

- infinite planes
- ray/plane intersection
- plane normals

Goal: create floors and walls for your scenes.

---

### Phase 11 — Triangles and meshes

Implement:

```text
src/raytracer/shapes/triangle.py
tests/unit/shapes/test_triangle.py
```

Learn:

- planes and triangles
- ray/triangle intersection
- barycentric coordinates
- mesh representation
- vertex normals

Eventually add support for loading `.obj` models.

Goal: render actual 3D models rather than primitive shapes.

---

### Phase 12 — Reflection

Add recursive rays.

Learn:

- reflection vectors
- recursive ray tracing
- recursion limits
- reflective materials

Goal: render mirrors and reflective surfaces.

---

### Phase 13 — Refraction

Learn:

- Snell's law
- refractive indices
- total internal reflection
- transparent materials

Goal: render glass and other transparent objects.

---

### Phase 14 — Acceleration

Only once the basic renderer works correctly, optimize it.

Learn:

- spatial partitioning
- bounding volumes
- Bounding Volume Hierarchies (BVH)
- computational complexity

Goal: make rendering large scenes practical.

---

### Phase 15 — Path tracing

This is the advanced stage.

Learn:

- Monte Carlo integration
- random sampling
- probability distributions
- indirect illumination
- global illumination
- variance
- noise
- importance sampling

Eventually move from traditional recursive ray tracing toward a physically based path tracer.

Goal: understand the foundations behind modern physically based rendering.

## Development philosophy

The project should follow this loop:

```text
THEORY
  ↓
derive the mathematics
  ↓
write tests
  ↓
implement
  ↓
run tests
  ↓
visualize the result
  ↓
move to the next concept
```

Avoid copying implementations from ray-tracing tutorials. Use the tests as a specification, derive the mathematics yourself, and implement the solution.

When a test fails, first ask:

> Is my understanding of the mathematics wrong, or is my implementation wrong?

That distinction is one of the main learning goals of the project.
