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

## 2. Vector Operations

### Dot Product (Scalar Product)
The dot product returns a scalar value representing the angular relationship between two vectors. It is the backbone of the Phong reflection model, used to determine how directly light strikes a surface.

$$ \vec{A} \cdot \vec{B} = A_x B_x + A_y B_y + A_z B_z + A_w B_w $$

*   If $\vec{A} \cdot \vec{B} = 1$, the vectors are perfectly aligned.
*   If $\vec{A} \cdot \vec{B} = 0$, the vectors are orthogonal (perpendicular).
*   If $\vec{A} \cdot \vec{B} = -1$, the vectors point in exact opposite directions.

### Cross Product (Vector Product)
The cross product of two 3D vectors yields a new vector that is orthogonal (perpendicular) to both original vectors. It is essential for calculating surface normals on polygonal shapes like triangles.

$$ \vec{A} \times \vec{B} = \begin{pmatrix} A_y B_z - A_z B_y \\ A_z B_x - A_x B_z \\ A_x B_y - A_y B_x \\ 0 \end{pmatrix} $$

### Magnitude and Normalization
To calculate lighting accurately, direction vectors must often be normalized (converted to unit vectors with a length of 1).
*   **Magnitude (Length):** $|\vec{V}| = \sqrt{V_x^2 + V_y^2 + V_z^2 + V_w^2}$
*   **Normalization:** $\hat{V} = \frac{\vec{V}}{|\vec{V}|}$

---

## 3. Matrices and Transformations

The engine uses $4 \times 4$ matrices to manipulate tuples in 3D space. 

### Matrix Multiplication
Multiplying a $4 \times 4$ transformation matrix by a $4 \times 1$ tuple (point or vector) applies the transformation to the tuple.

Because matrix multiplication is associative but **not commutative**, the order of transformations matters. To apply scaling ($S$), then rotation ($R$), then translation ($T$) to a point $P$, the matrices are multiplied in reverse order:
$$ P_{transformed} = T \times R \times S \times P $$

### Transformation Matrices

**1. Translation:** Moves a point by $x, y, z$. Notice how multiplying this matrix by a Vector ($w=0$) neutralizes the rightmost column, proving mathematically that vectors cannot be translated.
$$
\begin{bmatrix}
1 & 0 & 0 & x \\
0 & 1 & 0 & y \\
0 & 0 & 1 & z \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

**2. Scaling:** Multiplies the coordinates by $x, y, z$.
$$
\begin{bmatrix}
x & 0 & 0 & 0 \\
0 & y & 0 & 0 \\
0 & 0 & z & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

**3. Rotation (Around Axes):** 
Uses trigonometric functions to rotate points around a specific axis by $\theta$ radians. For example, rotation around the X-axis:
$$
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & \cos\theta & -\sin\theta & 0 \\
0 & \sin\theta & \cos\theta & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

---

## 4. Matrix Inversion and Object Space

Instead of calculating complex intersections by transforming a sphere or a cube into world space, the ray tracer uses **Matrix Inversion**. 

If a shape has a transformation matrix $M$, we calculate its inverse $M^{-1}$. We then multiply the incoming Ray by $M^{-1}$. This effectively transforms the ray into the object's local space (where all spheres are unit spheres at the origin `(0,0,0)` with radius `1`).

### Inversion Process
To invert a matrix $A$, the engine calculates:
1.  **Determinant:** The scalar scaling factor of the linear transformation. If $\det(A) = 0$, the matrix is uninvertible (singular).
2.  **Minors & Cofactors:** The determinant of the submatrix left after removing a specific row and column, multiplied by $+1$ or $-1$ based on its position.
3.  **Inverse Formula:** The transposed matrix of cofactors, divided by the original determinant.

---

## 5. Rays and Intersections

A **Ray** is defined by a starting point (Origin, $O$) and a direction vector (Direction, $\vec{D}$). The position of the ray at any given "time" or distance $t$ is defined by the parametric equation:

$$ P(t) = O + t\vec{D} $$

To find an intersection, the engine substitutes the ray equation $P(t)$ into the algebraic equation of a shape. For example, the equation of a unit sphere at the origin is:
$$ x^2 + y^2 + z^2 = 1 $$

By substituting the ray's components into the sphere's equation, we yield a quadratic equation ($at^2 + bt + c = 0$). Solving for $t$ using the quadratic formula determines if and where the ray intersects the sphere:
*   **Discriminant < 0:** No intersection (the ray misses).
*   **Discriminant = 0:** One intersection (the ray grazes the surface).
*   **Discriminant > 0:** Two intersections (the ray pierces through the object).