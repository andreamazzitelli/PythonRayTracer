# Mathematics of the Ray Tracer

This engine relies entirely on linear algebra and analytic geometry to simulate light, calculate intersections, and apply transformations. This document outlines the mathematical theories and formulas forming the foundation of the rendering engine.

## 1. Homogeneous Coordinates (Tuples)

To perform both linear transformations (rotation, scaling) and affine transformations (translation) using a single matrix multiplication, the engine uses **homogeneous coordinates**. Points and vectors are represented as 4-element tuples $(x, y, z, w)$.

*   **Point:** A specific location in space. Indicated by $w = 1.0$.
*   **Vector:** A direction and magnitude, independent of location. Indicated by $w = 0.0$.

This $w$ component enforces strict algebraic rules during tuple operations:
*   $Point - Point = Vector$ (since $1 - 1 = 0$)
*   $Point + Vector = Point$ (since $1 + 0 = 1$)
*   $Vector + Vector = Vector$ (since $0 + 0 = 0$)

---

## 2. Vector Operations

### Dot Product (Scalar Product)
The dot product returns a scalar value representing the angular relationship between two vectors. 
$$ \vec{A} \cdot \vec{B} = A_x B_x + A_y B_y + A_z B_z + A_w B_w $$

### Cross Product (Vector Product)
The cross product of two 3D vectors yields a new vector orthogonal (perpendicular) to both original vectors, essential for calculating polygon surface normals.
$$ \vec{A} \times \vec{B} = \begin{pmatrix} A_y B_z - A_z B_y \\ A_z B_x - A_x B_z \\ A_x B_y - A_y B_x \\ 0 \end{pmatrix} $$

### Magnitude and Normalization
Direction vectors must be normalized (converted to unit vectors with a length of 1) for accurate lighting calculations.
*   **Magnitude (Length):** $|\vec{V}| = \sqrt{V_x^2 + V_y^2 + V_z^2 + V_w^2}$
*   **Normalization:** $\hat{V} = \frac{\vec{V}}{|\vec{V}|}$

### Reflection Vector
When light hits a surface, it reflects. Given an incoming light vector $\vec{I}$ and a surface normal $\vec{N}$, the reflection vector $\vec{R}$ is calculated as:
$$ \vec{R} = \vec{I} - 2(\vec{I} \cdot \vec{N})\vec{N} $$

---

## 3. Matrices and Transformations

The engine uses $4 \times 4$ matrices to manipulate tuples in 3D space. Transformations are applied via matrix multiplication: $P_{transformed} = M \times P$. When chaining transformations, matrices are multiplied in reverse order (e.g., Translation $\times$ Rotation $\times$ Scaling).

**1. Translation:** Moves a point by $x, y, z$.
$$ \begin{bmatrix} 1 & 0 & 0 & x \\ 0 & 1 & 0 & y \\ 0 & 0 & 1 & z \\ 0 & 0 & 0 & 1 \end{bmatrix} $$

**2. Scaling:** Multiplies the coordinates by $x, y, z$.
$$ \begin{bmatrix} x & 0 & 0 & 0 \\ 0 & y & 0 & 0 \\ 0 & 0 & z & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix} $$

**3. Rotation (X-Axis):** Rotates points by $\theta$ radians.
$$ \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & \cos\theta & -\sin\theta & 0 \\ 0 & \sin\theta & \cos\theta & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix} $$

**4. Shearing (Skew):** Shifts a coordinate in proportion to another (e.g., $x$ in proportion to $y$ is $x_y$).
$$ \begin{bmatrix} 1 & x_y & x_z & 0 \\ y_x & 1 & y_z & 0 \\ z_x & z_y & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix} $$

---

## 4. Object Space and Matrix Inversion

To calculate intersections efficiently, the ray tracer uses **Matrix Inversion**. Instead of transforming a complex, scaled, and rotated shape into "world space," we transform the Ray into the shape's "object space" by multiplying the Ray by the shape's inverse transformation matrix ($M^{-1}$).

### Transforming Surface Normals
When a ray hits a transformed shape, the resulting surface normal is in object space. To convert this normal back to world space, we cannot simply multiply it by the transformation matrix $M$ (this distorts the normal if the shape was unevenly scaled). We must multiply the normal by the **transpose of the inverse** of the transformation matrix:
$$ \vec{N}_{world} = (M^{-1})^T \times \vec{N}_{local} $$
*(Note: the $w$ component of the resulting normal is manually forced back to 0, and the vector must be re-normalized).*

---

## 5. Rays and Intersections

A **Ray** is defined by a starting point (Origin, $O$) and a direction vector (Direction, $\vec{D}$). The position of the ray at any given distance $t$ is:
$$ P(t) = O + t\vec{D} $$

### Ray-Sphere Intersection
By substituting the ray equation into the equation for a unit sphere at the origin ($x^2 + y^2 + z^2 = 1$), we yield a quadratic equation ($at^2 + bt + c = 0$) where:
*   $a = \vec{D} \cdot \vec{D}$
*   $b = 2(\vec{O} \cdot \vec{D})$
*   $c = \vec{O} \cdot \vec{O} - 1$

We solve for $t$ using the discriminant ($\Delta = b^2 - 4ac$):
*   $\Delta < 0$: No intersection.
*   $\Delta \ge 0$: Ray intersects at $t = \frac{-b \pm \sqrt{\Delta}}{2a}$.

### Ray-Plane Intersection
For an infinite, perfectly flat plane resting on the XZ axes (where $y = 0$), the math simplifies drastically. We only need to check if the ray is parallel to the plane. If $\vec{D}_y$ is not $0$, the intersection is found at:
$$ t = \frac{-\vec{O}_y}{\vec{D}_y} $$

---

## 6. The Phong Reflection Model

To calculate the final color of a pixel, the engine uses the Phong reflection model, which sums three distinct lighting components.

Given:
*   $\vec{N}$: Surface Normal vector
*   $\vec{L}$: Light vector (pointing from the surface to the light source)
*   $\vec{E}$: Eye/Camera vector (pointing from the surface to the camera)
*   $\vec{R}$: Reflection vector (light reflecting off the surface)

**1. Ambient Reflection:** Background light affecting all surfaces equally.
$$ Ambient = Color_{light} \times Color_{material} \times Ambient_{material} $$

**2. Diffuse Reflection:** Light scattered in all directions by matte surfaces. Requires $\vec{L} \cdot \vec{N} > 0$ (light is in front of the surface).
$$ Diffuse = Color_{light} \times Color_{material} \times Diffuse_{material} \times (\vec{L} \cdot \vec{N}) $$

**3. Specular Reflection:** The bright, localized highlight on shiny surfaces. Requires $\vec{L} \cdot \vec{N} > 0$ and $\vec{R} \cdot \vec{E} > 0$.
$$ Specular = Color_{light} \times Specular_{material} \times (\vec{R} \cdot \vec{E})^{Shininess_{material}} $$

**Final Pixel Color:**
$$ Color = Ambient + Diffuse + Specular $$