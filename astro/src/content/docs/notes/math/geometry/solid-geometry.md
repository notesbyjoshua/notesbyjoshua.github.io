---
title: "Solid (3D) Geometry"
status: developing
progress: 68
sidebar:
  order: 6
description: "Competition geometry notes on 3D distances, sections, projections, volumes, spheres, and surface paths with worked spatial problems."
---

## Lines, Planes, and Spatial Coordinates

In three dimensions, two lines may intersect, be parallel, or be **skew**, meaning they are nonparallel but lie in no common plane. Do not infer an intersection from a perspective drawing.

Place a box corner at the origin and its edges along coordinate axes when possible. The distance between $$(x_1,y_1,z_1)$$ and $$(x_2,y_2,z_2)$$ is

$$
d=\sqrt{(\Delta x)^2+(\Delta y)^2+(\Delta z)^2}.
$$

The dot product $$\mathbf u\cdot\mathbf v=u_1v_1+u_2v_2+u_3v_3$$ detects perpendicularity and gives the angle between nonzero vectors.

<div class="theorem-box">

**Example.** A rectangular box has side lengths $$3,4,12$$. Find its space diagonal and the cosine of the angle between that diagonal and the edge of length twelve.

Take a diagonal vector $$\mathbf d=(3,4,12)$$. Its length is $$\sqrt{9+16+144}=13$$. Comparing with $$\mathbf e=(0,0,12)$$,

$$
\cos\theta=\frac{\mathbf d\cdot\mathbf e}{\lVert\mathbf d\rVert\lVert\mathbf e\rVert}
=\frac{144}{13\cdot12}=\frac{12}{13}.
$$

</div>

---

## Planes, Distances, and Dihedral Angles

A plane has equation $$ax+by+cz=d$$ with nonzero normal vector $$\mathbf n=(a,b,c)$$. The distance from $$P=(x_0,y_0,z_0)$$ to the plane is

$$
\frac{\lvert ax_0+by_0+cz_0-d\rvert}{\sqrt{a^2+b^2+c^2}}.
$$

The acute or right angle $$\theta$$ between two planes satisfies

$$
\cos\theta=\frac{\lvert\mathbf n_1\cdot\mathbf n_2\rvert}{\lVert\mathbf n_1\rVert\lVert\mathbf n_2\rVert}.
$$

An interior **dihedral angle** of a solid may be the supplementary angle, depending on which sides of the planes contain the solid. Alternatively, cut perpendicular to the intersection edge; the angle between the two face traces is the required dihedral angle.

<div class="theorem-box">

**Example.** Find the distance from $$(1,2,3)$$ to the plane $$2x-y+2z=3$$.

Substitute into the distance formula:

$$
d=\frac{\lvert2-2+6-3\rvert}{\sqrt{4+1+4}}=\frac33=1.
$$

</div>

---

## Cross Sections and Similarity

A plane parallel to the base of a pyramid or cone cuts out a similar figure. If its distance from the vertex is a fraction $$t$$ of the full height, lengths scale by $$t$$, areas by $$t^2$$, and the volume of the smaller solid by $$t^3$$.

<div class="theorem-box">

**Example.** A cone of height twelve has volume $$216\pi$$. A cut parallel to the base is made four units below the vertex. Find the volume of the remaining frustum.

The smaller cone has scale factor $$4/12=1/3$$ and volume $$(1/3)^3(216\pi)=8\pi$$. Subtracting it leaves

$$
216\pi-8\pi=208\pi.
$$

</div>

Distances must be measured from corresponding points. If the cut is described as four units above the base, the small cone instead has height eight.

---

## Surface Area and Volume

A prism or cylinder has volume $$Bh$$, where $$B$$ is its base area. A pyramid or cone has volume $$Bh/3$$. A sphere has volume $$4\pi r^3/3$$ and surface area $$4\pi r^2$$. A cone's lateral area is $$\pi r\ell$$, where $$\ell$$ is its slant height, not its vertical height.

For a tetrahedron with three edge vectors $$\mathbf u,\mathbf v,\mathbf w$$ from one vertex,

$$
V=\frac16\lvert\det(\mathbf u,\mathbf v,\mathbf w)\rvert.
$$

The determinant gives a parallelepiped's signed volume; the tetrahedron occupies one-sixth of it.

<div class="theorem-box">

**Example.** Find the volume of the tetrahedron with vertices $$(0,0,0),(6,0,0),(0,4,0),(0,0,3)$$.

Its base in the horizontal plane is a right triangle of area $$6\cdot4/2=12$$, and its height is three. Thus

$$
V=\frac13(12)(3)=12.
$$

The determinant gives the same result: $$6\cdot4\cdot3/6=12$$.

</div>

For a convex polyhedron, Euler's relation is $$V-E+F=2$$, with $$V$$ now denoting the number of vertices rather than volume. It is a counting relation, not a metric formula. For a cube, $$8-12+6=2$$.

---

## Spheres, Projections, and Inscribed Solids

If a sphere of radius $$R$$ is cut by a plane at distance $$d\le R$$ from its center, the cross-sectional circle has radius

$$
r=\sqrt{R^2-d^2}.
$$

The perpendicular from the sphere's center meets the section at its center, producing a right triangle with hypotenuse $$R$$.

<div class="theorem-box">

**Example.** A cube of side length six is inscribed in a sphere. Find the sphere's radius. Also find the radius of the largest sphere inside the cube.

The circumsphere's diameter equals the cube's space diagonal, $$6\sqrt3$$, so its radius is $$3\sqrt3$$. The insphere touches opposite faces six units apart, so its diameter is six and its radius is three.

</div>

Projection can also turn a spatial problem into a plane problem. A segment's projected length is at most its actual length. When several distances are known, use a perpendicular cross section to expose the relevant right triangle.

---

## Unfolding Surface Paths

For paths across flat faces, unfold the faces into one plane. A straight segment gives the shortest path for that unfolding, provided it crosses the intended shared edges within their segments. Compare possible unfoldings when the face route is not specified.

<div class="theorem-box">

**Example.** Find the shortest path along the surface of a cube of side two between opposite vertices.

Unfold two adjacent faces into a $$4\times2$$ rectangle, with the vertices at opposite corners. The straight path has length

$$
\sqrt{4^2+2^2}=2\sqrt5.
$$

The symmetric choices of face orientation give the same length. To justify minimality, any surface path must leave the three faces incident to its starting vertex and enter the three incident to the opposite vertex across an edge between these groups. Reflect the two relevant faces across that edge; the path through its crossing point is at least the straight distance in the unfolded $$4\times2$$ rectangle. Hence $$2\sqrt5$$ is the minimum.

</div>

:::strategy
Draw the useful cross section before working in all three coordinates. Distinguish vertical height, slant height, and projected length. Use similarity for parallel cuts and unfold flat faces for surface paths. For an angle between planes, check whether the problem wants the acute plane angle or the solid's interior dihedral angle.
:::

## Volume from Two Faces and Their Dihedral Angle

Suppose two tetrahedron faces share an edge of length $$\ell$$, have areas $$K_1,K_2$$, and meet at interior dihedral angle $$\theta$$. Their perpendicular heights to the common edge are $$u=2K_1/\ell$$ and $$v=2K_2/\ell$$.

Choose the common edge as an axis. The two height directions span angle $$\theta$$ in a perpendicular cross section, so the scalar triple product gives

$$
V=\frac{\ell uv\sin\theta}{6}
=\frac{2K_1K_2\sin\theta}{3\ell}.
$$

This is useful when no individual altitude to a whole face is immediately known. The sine is unchanged by replacing an angle by its supplement, but a cosine-based dihedral calculation must distinguish those possibilities.

<div class="theorem-box">

**Example.** Two faces of a tetrahedron have areas fifteen and twelve, share an edge of length three, and meet at a thirty-degree dihedral angle. Find the volume.

Substitute into the shared-edge formula:

$$
V=\frac{2(15)(12)\sin30^\circ}{3(3)}=20.
$$

Using either face area as a base still works, but its perpendicular height would first have to be recovered from the other face and the dihedral angle.

</div>

---

## Coordinates for a Regular Tetrahedron

A symmetric coordinate model makes all six edges equal:

$$
A=(t,t,t),\quad B=(t,-t,-t),\quad
C=(-t,t,-t),\quad D=(-t,-t,t).
$$

Each edge has length $$2\sqrt2\,t$$. For edge length $$a$$, choose $$t=a/(2\sqrt2)$$. The center is the origin, and its distance to a vertex gives the circumradius

$$
R=\sqrt3\,t=\frac{a\sqrt6}{4}.
$$

The face $$BCD$$ lies in $$x+y+z=-t$$, so the center-to-face distance is $$t/\sqrt3=a\sqrt6/12$$. This is the inradius $$r$$. The altitude is $$R+r=a\sqrt{2/3}$$, yielding volume $$a^3/(6\sqrt2)$$.

Adjacent outward face normals have cosine negative one-third. The interior dihedral angle is supplementary to the angle between those outward normals, hence has cosine positive one-third.

<div class="theorem-box">

**Example.** A regular tetrahedron has edge length six. Find its volume and the ratio of circumradius to inradius.

The volume is $$6^3/(6\sqrt2)=18\sqrt2$$. The radius formulas give $$R/r=3$$. The ratio is independent of scale, as it must be for similar tetrahedra.

</div>

The symmetric coordinates avoid solving several intersecting-altitude equations. They also provide convenient vectors for angles between opposite edges or between a line and a face.

---

## Opposite-Edge Midpoints

Let $$M,N$$ be the midpoints of opposite edges $$AB,CD$$ of any tetrahedron. Vector expansion gives

$$
4MN^2=AC^2+AD^2+BC^2+BD^2-AB^2-CD^2.
$$

To derive it, use $$2(N-M)=C+D-A-B$$ and expand its squared norm. Grouping the pairwise dot products into squared distances produces the displayed combination.

<div class="theorem-box">

**Example.** A tetrahedron has vertices $$(0,0,0),(6,0,0),(0,8,0),(0,0,10)$$. Find the distance between the midpoints of the first edge and the opposite edge.

The first midpoint is $$(3,0,0)$$ and the second is $$(0,4,5)$$. Their squared distance is $$9+16+25=50$$, so the distance is $$5\sqrt2$$.

Using only edge lengths, the midpoint identity gives the same value:

$$
4MN^2=64+100+100+136-36-164=200.
$$

</div>

The identity is particularly valuable when six edge lengths are given without coordinates. It avoids constructing the tetrahedron's altitude or the angle between the opposite edges.

---

## Frustums and Cross-Sectional Area

A pyramid frustum has similar parallel bases with areas $$B_1,B_2$$ and height $$h$$. Its volume is

$$
V=\frac h3\left(B_1+\sqrt{B_1B_2}+B_2\right).
$$

To derive it, extend the sides to recover the full pyramid. If the smaller-to-larger linear ratio is $$t$$, the areas have ratio $$t^2$$ and the volumes ratio $$t^3$$. Subtract the smaller pyramid and use $$(1-t^3)/(1-t)=1+t+t^2$$.

The same formula applies to a circular cone frustum because all parallel sections are similar circles. Their square-root area ratio is the radius ratio.

<div class="theorem-box">

**Example.** A square-pyramid frustum has parallel bases of side lengths two and five and vertical height six. Find its volume.

The base areas are four and twenty-five, so

$$
V=\frac63(4+\sqrt{100}+25)=78.
$$

Averaging just the two base areas would give eighty-seven and is not valid: the sectional area changes quadratically with height, not linearly.

</div>

More generally, Cavalieri's principle says that solids with the same height and equal cross-sectional areas at every corresponding height have equal volumes. The phrase “at every height” matters; equal base and top areas alone do not determine the intermediate sections.

---

## Tangent Spheres on a Plane

If two externally tangent spheres of radii $$r,s$$ both touch the same horizontal plane, their centers have vertical separation $$\lvert r-s\rvert$$ and total distance $$r+s$$. The horizontal separation of their projected centers is therefore

$$
d^2=(r+s)^2-(r-s)^2=4rs,
\qquad d=2\sqrt{rs}.
$$

This formula translates a sphere-packing configuration into a planar distance problem.

<div class="theorem-box">

**Example.** Can three spheres of radii one, four, and nine all touch a horizontal plane and be pairwise externally tangent?

Their projected center distances would have to be four, six, and twelve. These cannot be the side lengths of a triangle, since $$4+6<12$$. They cannot be collinear with those distances either.

Thus no such configuration exists. Checking each pair separately gives consistent tangencies, but the three pairs cannot coexist in one plane projection.

</div>

For a tetrahedron with an insphere of radius $$r$$ and total face area $$S$$, split it into four pyramids with common apex at the sphere center. Each has perpendicular height $$r$$, so $$V=rS/3$$ and $$r=3V/S$$. The analogous planar triangle relation is $$K=rs$$.

---

## Comparing Box Unfoldings

For opposite vertices of a box with side lengths $$a,b,c$$, the three essential unfoldings give candidate distances

$$
\sqrt{(a+b)^2+c^2},\quad
\sqrt{(a+c)^2+b^2},\quad
\sqrt{(b+c)^2+a^2}.
$$

Take the smallest. The common squared sum $$a^2+b^2+c^2$$ shows that the comparison is equivalent to comparing $$ab,ac,bc$$. If $$a\le b\le c$$, joining the two smaller side lengths in the unfolding gives the shortest candidate.

<div class="theorem-box">

**Example.** Find the shortest surface path between opposite vertices of a box of dimensions two, three, five.

The squared candidates are fifty, fifty-eight, and sixty-eight. The minimum distance is $$\sqrt{50}=5\sqrt2$$.

The space diagonal is $$\sqrt{38}$$, which is shorter but passes through the interior and is not an allowed surface path.

</div>

For other endpoint locations, a straight segment in an unfolding may cross beyond a shared edge's endpoint and fail to represent the proposed face sequence. Verify the crossings before treating a planar distance as an admissible path.

---

## Unrolling a Cone

A cone's lateral surface unrolls to a circular sector whose radius is the slant height $$\ell$$. Its arc length equals the base circumference $$2\pi r$$, so the sector angle in radians is $$2\pi r/\ell$$.

Angles around the cone's axis are therefore multiplied by $$r/\ell$$ in the unrolled sector. Distances from the vertex remain unchanged. A shortest surface path can then become a straight segment between suitable unfolded copies of the endpoints.

<div class="theorem-box">

**Example.** A cone has base radius five and slant height ten. Two points lie on opposite generators, at slant distances six and eight from the vertex. Find their shortest path on the lateral surface.

The half-turn around the axis becomes an unfolded angle $$\pi(5/10)=\pi/2$$. The endpoint radii in the sector are six and eight, so the cosine law gives distance

$$
\sqrt{6^2+8^2-2(6)(8)\cos(\pi/2)}=10.
$$

The segment stays within the unfolded half-disk and within slant radius ten, so it is a valid surface path. A route through the apex would have length fourteen and is longer.

</div>

For a configuration permitting different winding directions, compare the corresponding unfolded copies. The shortest algebraic segment must still map to a path lying on the actual finite cone.

:::strategy
Use symmetry before general spatial coordinates, reduce tangency to center distances, and compare all relevant unfoldings. For volume, identify the perpendicular height or derive it from a cross section; a visually convenient slanted segment is not automatically an altitude.
:::

---

## Key Equations

:::equations
| Tool | Formula |
| --- | --- |
| Spatial distance | $$d^2=(\Delta x)^2+(\Delta y)^2+(\Delta z)^2$$ |
| Point-to-plane distance | $$d=\lvert ax_0+by_0+cz_0-d_0\rvert/\sqrt{a^2+b^2+c^2}$$ for plane $$ax+by+cz=d_0$$ |
| Similar solids | Length, area, volume ratios are $$t,t^2,t^3$$ |
| Prism/pyramid volumes | $$Bh$$ and $$Bh/3$$ |
| Sphere | Volume $$4\pi r^3/3$$; surface area $$4\pi r^2$$ |
| Tetrahedron | $$V=\lvert\det(\mathbf u,\mathbf v,\mathbf w)\rvert/6$$ |
| Sphere section | $$r^2=R^2-d^2$$ |
| Convex polyhedron | $$V-E+F=2$$, with $$V$$ the vertex count |
| Shared-edge volume | $$V=2K_1K_2\sin\theta/(3\ell)$$ |
| Regular tetrahedron | $$R=a\sqrt6/4,\ r=a\sqrt6/12,\ V=a^3/(6\sqrt2)$$ |
| Opposite-edge midpoints | $$4MN^2=AC^2+AD^2+BC^2+BD^2-AB^2-CD^2$$ |
| Pyramid frustum | $$V=h(B_1+\sqrt{B_1B_2}+B_2)/3$$ |
| Tangent-sphere projections | $$d=2\sqrt{rs}$$ |
| Tetrahedron inradius | $$r=3V/S$$ |
| Unrolled cone angle | $$\Theta=2\pi r/\ell$$ |
:::
