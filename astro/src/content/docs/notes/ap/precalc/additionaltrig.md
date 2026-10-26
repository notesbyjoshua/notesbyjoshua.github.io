---
title: "Unit 10: Additional Topics in Trigonometry (Triangle Laws, Parametric, Polar, and Vectors)"
description: "AP Precalculus notes on triangle laws, parametric and polar equations, vectors, dot products, and polar graph analysis."
sidebar:
  order: 7
---

## The Triangle Laws

<div class="theorem-box">

**Theorem.** For a triangle with angles $$A,B,C$$ and opposite side lengths $$a,b,c$$:

$$
\frac{\sin A}{a}=\frac{\sin B}{b}=\frac{\sin C}{c}.
$$

This is the **Law of Sines**. It is useful when a triangle has an angle-side opposite pair, especially in the following cases:

- **ASA** or **AAS**, when two angles and one side are known.
- **SSA**, when two sides and a non-included angle are known.

</div>

<div class="theorem-box">

**Proof (Law of Sines).** Draw the triangle's circumcircle, with radius $$R$$. Side $$a=BC$$ is a chord. If the smaller central angle subtending this chord is $$\phi$$, bisecting the isosceles triangle formed by the two radii gives

$$
\frac a2=R\sin\frac\phi2.
$$

By the inscribed-angle theorem, $$A$$ is either $$\phi/2$$ or its supplement, depending on which arc contains $$A$$. These two angles have the same sine, so $$a=2R\sin A$$. The same argument for the other two chords gives $$b=2R\sin B$$ and $$c=2R\sin C$$. Therefore,

$$
\frac{\sin A}{a}=\frac{\sin B}{b}=\frac{\sin C}{c}=\frac{1}{2R}.
$$

This proof uses only circle geometry and right-triangle trigonometry.

</div>

An important collorary of the Law of Sines is that the area of a triangle can also be written using two sides and the included angle:

$$
K=\frac12ab\sin C=\frac12bc\sin A=\frac12ac\sin B.
$$

<div class="theorem-box">

**Proof (Area formula).** First take $$AC=b$$ as the base. The perpendicular height from $$B$$ is $$h=c\sin A$$, including when the altitude meets an extension of the base. Thus $$K=\frac12bh=\frac12bc\sin A$$. Now apply the Law of Sines:

$$
\sin A=\frac ac\sin C=\frac ab\sin B.
$$

Substituting each expression into the same area formula gives

$$
K=\frac12bc\left(\frac ac\sin C\right)=\frac12ab\sin C,
\qquad
K=\frac12bc\left(\frac ab\sin B\right)=\frac12ac\sin B.
$$

The altitude establishes one form; the Law of Sines proves that all three forms agree.

</div>

The Law of Sines also has an extended version, which is not particularly important for AP Precalculus.

<div class="theorem-box">

**Extension.** Use the extended Law of Sines, $$a/\sin A=2R$$, and the area formula to prove $$K=abc/(4R)$$.

</div>

### The SSA case

The SSA case is called the **ambiguous case** because the given information may create no triangle, one triangle, or two triangles.

Suppose angle $$A$$ is known, and sides $$a$$ and $$b$$ are known, where $$a$$ is opposite $$A$$. Let

$$
h=b\sin A.
$$

For an acute angle $$A$$:

$$
\begin{array}{c|c}
\text{Condition} & \text{Number of triangles}\\
\hline
a<h & 0\\
a=h & 1\text{ (right triangle)}\\
h<a<b & 2\\
a\ge b & 1
\end{array}
$$

If $$A\ge90^\circ$$, there is exactly one triangle when $$a>b$$ and no triangle when $$a\le b$$, because the side opposite a right or obtuse angle must be the longest.

:::warning
When using the Law of Sines, remember that $$\sin \theta=\sin(180^\circ-\theta)$$, so a possible second angle may need to be checked.
:::

<div class="theorem-box">

**Example.** Suppose $$A=45^\circ$$, $$a=12$$, and $$b=15$$. Find the possible values for angle $$B$$ (opposite to side $$b$$).

First find the height:

$$
h=b\sin A=15\sin45^\circ=\frac{15\sqrt2}{2}\approx 10.61.
$$

Since

$$
h<a<b,
$$

there are two possible triangles.

Using Law of Sines,

$$
\frac{\sin B}{15}=\frac{\sin45^\circ}{12}.
$$

So

$$
\sin B=\frac{15\sin45^\circ}{12}\approx 0.884.
$$

This gives one possible angle $$B\approx 62.1^\circ$$, and the second possible angle

$$
180^\circ-62.1^\circ=117.9^\circ.
$$

Both angles create valid triangles because each leaves a positive value for angle $$C$$.

</div>

<div class="theorem-box">

**Example.** A triangle has $$A=30^\circ$$, $$a=6$$, and $$b=10$$. Find both possible lengths of $$c$$, then decide which triangle has perimeter greater than $$25$$.

The altitude is $$h=10\sin30^\circ=5$$. Since $$5<6<10$$, two triangles are possible. Put $$A$$ at the origin, $$C$$ at $$(10,0)$$, and $$B$$ on the ray making $$30^\circ$$ with the positive $$x$$-axis, at distance $$c$$ from $$A$$. The distance $$BC=6$$ gives

$$
(c\cos30^\circ-10)^2+(c\sin30^\circ)^2=36.
$$

Expanding and completing the square,

$$
c^2-10\sqrt3c+64=0,
\qquad (c-5\sqrt3)^2=11.
$$

Thus $$c=5\sqrt3\pm\sqrt{11}$$, approximately $$11.98$$ or $$5.34$$. Their perimeters are approximately $$27.98$$ and $$21.34$$, so only the longer choice meets the condition.

As an angle check, the Law of Sines gives $$\sin B=5/6$$. The two possible angles are approximately $$56.44^\circ$$ and $$123.56^\circ$$, leaving positive third angles in both cases.

</div>

### Law of Cosines

<div class="theorem-box">

**Theorem.** The **Law of Cosines** states that for a triangle with side lengths $$a$$, $$b$$, and $$c$$ (with oppposite angles $$A$$, $$B$$, and $$C$$, respectively):

$$
a^2=b^2+c^2-2bc\cos A.
$$

Similarly,

$$
b^2=a^2+c^2-2ac\cos B
$$

and

$$
c^2=a^2+b^2-2ab\cos C.
$$

Law of Cosines is useful for:

- **SSS**, when all three sides are known.
- **SAS**, when two sides and the included angle are known.

</div>

<div class="theorem-box">

**Proof (Law of Cosines).** Place the triangle on the coordinate plane so that angle $$A$$ is at the origin and side $$b$$ lies on the positive $$x$$-axis.

Then the endpoint of side $$b$$ is

$$
C=(b,0).
$$

The endpoint of side $$c$$ has coordinates

$$
B=(c\cos A,c\sin A).
$$

Side $$a$$ is the distance from $$B$$ to $$C$$, so by the distance formula,

$$
a^2=(c\cos A-b)^2+(c\sin A-0)^2.
$$

Expand:

$$
a^2=c^2\cos^2A-2bc\cos A+b^2+c^2\sin^2A.
$$

Group the trig terms:

$$
a^2=b^2+c^2(\cos^2A+\sin^2A)-2bc\cos A.
$$

Since

$$
\cos^2A+\sin^2A=1,
$$

we get

$$
a^2=b^2+c^2-2bc\cos A.
$$

</div>

<div class="theorem-box">

**Example.** If $$b=7$$, $$c=10$$, and $$A=60^\circ$$, find side $$a$$.

By Law of Cosines,

$$
a^2=7^2+10^2-2(7)(10)\cos60^\circ.
$$

Since $$\cos60^\circ=\frac12$$,

$$
a^2=49+100-70=79.
$$

Thus,

$$
a=\sqrt{79}.
$$

</div>

<div class="theorem-box">

**Example.** In triangle $$ABC$$, $$AB=9$$, $$AC=13$$, and $$A=60^\circ$$. Point $$D$$ lies on $$BC$$, and $$AD$$ bisects $$A$$. Find $$BC$$ and $$AD$$ using both triangle laws.

First use the Law of Cosines in the original triangle:

$$
BC^2=9^2+13^2-2(9)(13)\cos60^\circ=133,
\qquad BC=\sqrt{133}.
$$

The Law of Sines then gives $$\sin B=13\sin60^\circ/\sqrt{133}$$. To select the correct inverse-sine angle, note that $$13^2<9^2+133$$, so $$B$$ is acute. Thus $$B\approx77.48^\circ$$. In triangle $$ABD$$, $$A=30^\circ$$ and $$\angle ADB=150^\circ-B$$. Applying the Law of Sines again,

$$
\frac{AD}{\sin B}=\frac9{\sin(150^\circ-B)},
\qquad AD\approx9.21.
$$

For an exact answer, use $$\sin B=13\sqrt3/(2\sqrt{133})$$ and $$\cos B=5/(2\sqrt{133})$$ to get $$\sin(150^\circ-B)=11/\sqrt{133}$$. Therefore $$AD=117\sqrt3/22$$.

</div>

---

## Vectors in the Plane

A **scalar** is a quantity described by one number, such as temperature, length, or mass.

A **vector** is a quantity described by both magnitude and direction, such as force or velocity. They are usually bolded or denoted with arrows above them.

Geometrically, a vector is drawn as a directed line segment. The starting point is the **initial point**, and the ending point is the **terminal point**.

```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\begin{tikzpicture}[>=Stealth]
\coordinate (P) at (0,0);
\coordinate (Q) at (4,2);
\draw[blue, very thick, ->] (P) -- (Q) node[midway, above left] {$\overrightarrow{PQ}$};
\fill (P) circle (2pt) node[below left, align=center] {$P$\\initial point};
\fill (Q) circle (2pt) node[above right, align=center] {$Q$\\terminal point};
\end{tikzpicture}
```

The magnitude/norm of vector $$\overrightarrow{PQ}$$ is the length of the directed segment:

$$
\left\lvert \overrightarrow{PQ}\right \rvert.
$$

Two vectors are equal if they have the same magnitude and the same direction, even if they are drawn in different locations. Basically, they are the same vector just translated.

A vector can be written as $$\mathbf v$$, $$\vec v$$, or $$\overrightarrow{PQ}$$. Its **component form** is $$\langle a,b\rangle$$, meaning a horizontal change of $$a$$ and a vertical change of $$b$$. For $$P=(x_1,y_1)$$ and $$Q=(x_2,y_2)$$,

$$
\overrightarrow{PQ}=\langle x_2-x_1,y_2-y_1\rangle.
$$

The same vector can be written as a column $$\begin{pmatrix}a\\b\end{pmatrix}$$ using the standard unit vectors introduced below. Angle brackets distinguish vector components from the coordinates $$(a,b)$$ of a point. If not specified, a vector is assumed to start from the origin.

### Vector components

If a vector has magnitude $$\lvert \mathbf v \rvert$$ and direction angle $$\theta$$, then it can be broken down into horizontal and vertical components, each of which are parallel to one of the axes:

$$
v_x=\lvert \mathbf v \rvert\cos\theta \qquad v_y=\lvert \mathbf v\rvert \sin\theta.
$$

Thus,

$$
\mathbf v=\langle \lvert \mathbf v \rvert \cos\theta, \lvert \mathbf v \rvert\sin\theta\rangle.
$$

<div class="theorem-box">

**Proof (Component Definition).** Draw a vector $$\mathbf v$$ with direction angle $$\theta$$. Its horizontal and vertical components form a right triangle whose hypotenuse is $$\lvert \mathbf v \rvert$$.

```tikz
\usepackage{tikz}
\usetikzlibrary{angles,arrows.meta,quotes}
\begin{tikzpicture}[>=Stealth, scale=0.9]
\draw[->, gray!70] (-1,0) -- (5.2,0) node[right] {$x$};
\draw[->, gray!70] (0,-1) -- (0,3.6) node[above] {$y$};
\coordinate (O) at (0,0);
\coordinate (X) at (4,0);
\coordinate (P) at (4,2.4);
\draw[very thick, blue, ->] (O) -- (P) node[midway, above left] {$\mathbf v=\langle a,b\rangle$};
\draw[orange!85!black, thick] (O) -- (4,0) node[midway, below] {$v_x = a$};
\draw[orange!85!black, thick] (4,0) -- (P) node[midway, right] {$v_y = b$};
\draw pic[draw, angle radius=0.55cm] {angle=X--O--P};
\node at (1.05,0.24) {$\theta$};
\draw[dashed, gray!70] (P) -- (4,0);
\fill (P) circle (2pt) node[above right] {$(a,b)$};
\end{tikzpicture}
```

By right triangle trigonometry, $$\cos\theta=\frac{v_x}{\lvert \mathbf v \rvert}$$ and $$\sin\theta=\frac{v_y}{\lvert \mathbf v \rvert}$$.

Solving these equations gives

$$
v_x=\lvert \mathbf v \rvert\cos\theta
$$

and

$$
v_y=\lvert \mathbf v \rvert\sin\theta.
$$

</div>

For a vector $$\mathbf v=\langle a,b\rangle$$, the magnitude is

$$
\lvert \mathbf v \rvert=\sqrt{a^2+b^2}.
$$

The direction angle satisfies

$$
\tan\theta=\frac{b}{a},
$$

but the quadrant of the vector must be considered for the angle.

<div class="theorem-box">

**Example.** A force points from $$P=(4,-2)$$ toward $$Q=(-2,6)$$ and has magnitude $$25\text{ N}$$. Find its components and direction angle measured counterclockwise from the positive $$x$$-axis.

The displacement is $$\langle-6,8\rangle$$, whose magnitude is $$10$$. Scale this direction to length $$25$$:

$$
\mathbf F=\frac{25}{10}\langle-6,8\rangle=\langle-15,20\rangle\text{ N}.
$$

The vector lies in Quadrant II, so $$\theta=180^\circ-\tan^{-1}(4/3)\approx126.87^\circ$$. Checking $$\sqrt{(-15)^2+20^2}=25$$ confirms the magnitude.

</div>

### Vector addition

Like numbers, vectors can be added too. Vectors can be added geometrically by placing the initial point of one vector at the terminal point of the other. The resulting vector is called the **resultant**.

The **parallelogram method** starts both vectors at the same point. Translate each vector to the other's endpoint to complete a parallelogram; the diagonal from the shared initial point is the sum.

```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\begin{tikzpicture}[>=Stealth]
\coordinate (O) at (0,0);
\coordinate (U) at (3,0.4);
\coordinate (V) at (1,2);
\coordinate (S) at (4,2.4);
\draw[blue, very thick, ->] (O) -- (U) node[midway, below] {$\mathbf u$};
\draw[red!75!black, very thick, ->] (O) -- (V) node[midway, above left] {$\mathbf v$};
\draw[blue, dashed, ->] (V) -- (S) node[midway, above] {$\mathbf u$};
\draw[red!75!black, dashed, ->] (U) -- (S) node[midway, right] {$\mathbf v$};
\draw[green!45!black, very thick, ->] (O) -- (S) node[pos=0.55, above left] {$\mathbf u+\mathbf v$};
\fill (O) circle (1.8pt) node[below left] {$O$};
\end{tikzpicture}
```

As seen in the picture above, vector addition is commutative:

$$
\mathbf u+\mathbf v=\mathbf v+\mathbf u.
$$

For vectors written in component form,

$$
\mathbf u=\langle u_1,u_2\rangle,\qquad
\mathbf v=\langle v_1,v_2\rangle,
$$

their sum is

$$
\mathbf u+\mathbf v=\langle u_1+v_1,u_2+v_2\rangle.
$$

To understand vector addition, remember that a vector $$\langle u_1,u_2\rangle$$ means "move $$u_1$$ units horizontally and $$u_2$$ units vertically."

Adding $$\mathbf u=\langle u_1,u_2\rangle$$ and $$\mathbf v=\langle v_1,v_2\rangle$$ means doing both moves. Horizontally, the total movement is $$u_1+v_1.$$ Vertically, the total movement is $$u_2+v_2.$$

So,

$$
\mathbf u+\mathbf v=\langle u_1+v_1,u_2+v_2\rangle.
$$

Vector subtraction is the same with one of the vectors having a negative sign before it.

### Scalar multiplication

If $$\mathbf u=\langle u_1,u_2\rangle$$, then

$$
k\mathbf u=\langle ku_1,ku_2\rangle.
$$

The magnitude changes by a factor of $$\lvert k \rvert$$:

$$
\lvert k\mathbf u \rvert = \lvert k \rvert \lvert \mathbf u \rvert.
$$

If $$k>0$$, the direction stays the same. If $$k<0$$, the direction is reversed.

<div class="theorem-box">

**Example.** A survey drone flies for $$3$$ minutes with ground velocity $$\langle4,1\rangle\text{ m/s}$$, then $$2$$ minutes with velocity $$\langle-1,3\rangle\text{ m/s}$$. Taking east and north as positive, find its net displacement and the constant velocity needed to return to its starting point in $$4$$ minutes.

Convert times to seconds before multiplying:

$$
\Delta\mathbf r=180\langle4,1\rangle+120\langle-1,3\rangle
=\langle600,540\rangle\text{ m}.
$$

The return displacement is the negative of this vector, so the required return velocity is

$$
\mathbf v=\frac{-\Delta\mathbf r}{240}
=\left\langle-\frac52,-\frac94\right\rangle\text{ m/s}.
$$

Its speed is $$\sqrt{181}/4\approx3.36\text{ m/s}$$. Averaging the two outbound velocities without weighting by their travel times would give the wrong displacement.

</div>

### Unit vectors

A **unit vector** is any vector that has magnitude $$1$$.

The standard unit vectors, called basis vectors, are the vectors

$$
\mathbf i=\langle 1,0\rangle \qquad \mathbf j=\langle 0,1\rangle.
$$

So any vector can be written as

$$
\langle a,b\rangle=a\mathbf i+b\mathbf j.
$$

To find a unit vector in the direction of a nonzero vector $$\mathbf v$$, we can divide by its magnitude:

$$
\mathbf u=\frac{\mathbf v}{\lvert \mathbf v \rvert}.
$$

// talk a little bit about why we use unit vectors (to decompose vectors)

<div class="theorem-box">

**Example.** Find both unit vectors perpendicular to $$\mathbf v=\langle5,-12\rangle$$, then find the vector of magnitude $$26$$ in the same direction as $$\mathbf v$$.

Rotating $$\langle a,b\rangle$$ by a right angle gives $$\langle-b,a\rangle$$, so perpendicular directions are $$\pm\langle12,5\rangle$$. Their magnitude is $$13$$, giving the unit vectors

$$
\pm\left\langle\frac{12}{13},\frac5{13}\right\rangle.
$$

For the original direction, normalize first and then scale:

$$
26\frac{\mathbf v}{\lvert\mathbf v\rvert}
=26\frac{\langle5,-12\rangle}{13}=\langle10,-24\rangle.
$$

</div>

### Dot product

We have covered vector addition and subtraction, so how do we do vector multiplication? There are two ways to do multiplication, but we will only focus on the scalar version, known as the **dot product**.

For $$\mathbf A=\langle x_1,y_1\rangle$$ and $$\mathbf B=\langle x_2,y_2\rangle$$, the dot product is

$$
\mathbf A\cdot \mathbf B=x_1x_2+y_1y_2.
$$

The dot product can also be written as

$$
\mathbf A\cdot \mathbf B=\lvert \mathbf A \rvert \lvert \mathbf B \rvert \cos\theta,
$$

where $$\theta$$ is the angle between the two vectors.

Therefore,

$$
\cos\theta=\frac{\mathbf A\cdot \mathbf B}{\lvert \mathbf A \rvert \lvert \mathbf B \rvert}.
$$

The dot product always returns a *scalar*. The other form of vector multiplication, the cross product, returns a vector and will not be taught here.

<div class="theorem-box">

**Proof (Dot product formula).** Let $$\mathbf A=\langle x_1,y_1\rangle,\,\mathbf B=\langle x_2,y_2\rangle$$.

The vector between their terminal points is

$$
\mathbf A-\mathbf B.
$$

Using the magnitude formula,

$$
\lvert\mathbf A-\mathbf B\rvert^2=(x_1-x_2)^2+(y_1-y_2)^2.
$$

Expanding gives

$$
\lvert\mathbf A-\mathbf B\rvert^2=x_1^2+y_1^2+x_2^2+y_2^2-2(x_1x_2+y_1y_2).
$$

Since $$\lvert\mathbf A\rvert^2=x_1^2+y_1^2,\,\lvert\mathbf B\rvert^2=x_2^2+y_2^2$$, this becomes

$$
\lvert\mathbf A-\mathbf B\rvert^2=\lvert\mathbf A\rvert^2+\lvert\mathbf B\rvert^2-2(\mathbf A\cdot \mathbf B).
$$

Now use the Law of Cosines on the triangle formed by $$\mathbf A$$, $$\mathbf B$$, and $$\mathbf A-\mathbf B$$:

$$
\lvert\mathbf A-\mathbf B\rvert^2=\lvert\mathbf A\rvert^2+\lvert\mathbf B\rvert^2-2\lvert\mathbf A\rvert\lvert\mathbf B\rvert\cos\theta.
$$

Comparing the two equations,

$$
\mathbf A\cdot \mathbf B=\lvert\mathbf A\rvert\lvert\mathbf B\rvert\cos\theta.
$$

</div>

// add a hard example problem

### Components and projections along a vector

The **scalar projection**, or **component of $$\mathbf A$$ along $$\mathbf B$$**, is the signed length of the part of $$\mathbf A$$ pointing in the direction of a nonzero $$\mathbf B$$. If their angle is $$\theta$$, this length is $$\lvert\mathbf A\rvert\cos\theta$$. It is negative when the vectors point more than $$90^\circ$$ apart.

The **vector projection** has this signed length along the unit vector $$\mathbf B/\lvert\mathbf B\rvert$$. It gives the parallel part of $$\mathbf A$$; subtracting it from $$\mathbf A$$ leaves a vector perpendicular to $$\mathbf B$$.

Using these, we can define a couple of key formulas.

:::key{name="Dot product and projections"}

Useful vector formulas that follow from the dot product include

$$
\mathbf v\cdot \mathbf v=\lvert\mathbf v\rvert^2,
$$

so a vector dotted with itself gives the square of its magnitude. Also,

$$
\lvert\mathbf v\rvert=\sqrt{\mathbf v\cdot \mathbf v}.
$$

For two nonzero vectors $$\mathbf A$$ and $$\mathbf B$$,

$$
\mathbf A\perp \mathbf B\quad \text{if and only if}\quad \mathbf A\cdot \mathbf B=0.
$$

The scalar projection of $$\mathbf A$$ onto $$\mathbf B$$ is

$$
\operatorname{comp}_{\mathbf B}\mathbf A=\frac{\mathbf A\cdot \mathbf B}{\lvert\mathbf B\rvert},
$$

and the vector projection of $$\mathbf A$$ onto $$\mathbf B$$ is

$$
\operatorname{proj}_{\mathbf B}\mathbf A=\frac{\mathbf A\cdot \mathbf B}{\lvert \mathbf B \rvert^2}\mathbf B.
$$

These projection formulas require $$\mathbf B\ne\mathbf0$$. The scalar projection is a number; the vector projection is a vector.

:::

<div class="theorem-box">

**Example.** Find the angle between $$\mathbf A=\langle 3,4\rangle$$ and $$\mathbf B=\langle 5,0\rangle$$.

First,

$$
\mathbf A\cdot \mathbf B=3(5)+4(0)=15.
$$

Also,

$$
\lvert\mathbf A\rvert=5,\qquad \lvert\mathbf B\rvert=5.
$$

So

$$
\cos\theta=\frac{15}{5\cdot5}=\frac35.
$$

Therefore,

$$
\theta=\cos^{-1}\left(\frac35\right)\approx 53.1^\circ.
$$

// have this problem use the formulas you defined above

</div>

<div class="theorem-box">

**Example.** Let $$\mathbf A=\langle7,1\rangle$$ and $$\mathbf B=\langle2,-1\rangle$$. Decompose $$\mathbf A$$ into parts parallel and perpendicular to $$\mathbf B$$, and find the point on the line $$L:\ (x,y)=(1,2)+t\mathbf B$$ closest to $$P=(8,3)$$.

Since $$\mathbf A\cdot\mathbf B=13$$ and $$\mathbf B\cdot\mathbf B=5$$,

$$
\mathbf A_{\parallel}=\frac{13}{5}\langle2,-1\rangle
=\left\langle\frac{26}{5},-\frac{13}{5}\right\rangle,
\qquad
\mathbf A_{\perp}=\left\langle\frac95,\frac{18}{5}\right\rangle.
$$

The perpendicular check is $$\mathbf A_{\perp}\cdot\mathbf B=18/5-18/5=0$$. Since $$P-(1,2)=\mathbf A$$, the closest point is the foot of this perpendicular:

$$
Q=(1,2)+\mathbf A_{\parallel}
=\left(\frac{31}{5},-\frac35\right).
$$

The shortest distance is $$\lvert\mathbf A_{\perp}\rvert=9\sqrt5/5$$. Any other point on the line adds a nonzero parallel displacement to this perpendicular segment and is farther away.

</div>

---

## Parametric Equations

Sometimes, we have systems that evolve with time. We can describe the motion of these systems using parametric equations. In a parametric equation, both $$x$$ and $$y$$ are written in terms of a third variable, usually $$t$$:

$$
x=f(t),\qquad y=g(t).
$$

The variable $$t$$ is called the **parameter**.

Parametric equations describe both:

- the set of points on a curve,
- the **direction** the curve is traced as $$t$$ increases.

### Eliminating the parameter

Often, we want to find an explicit form for a set of parametric equations, which we do by eliminating the parameter. To eliminate the parameter, solve one equation for $$t$$ and substitute into the other equation.

For example, if $$x=3t$$, then

$$
t=\frac{x}{3}.
$$

Substituting this into the equation for $$y$$ gives a rectangular equation relating $$x$$ and $$y$$ directly.

The rectangular equation may not show the full behavior of the parametric curve, because the parameter can restrict the domain or determine the direction of travel. Always indicate the allowed domain for $$t$$, as well as the direction the graph is moving.

<div class="theorem-box">

**Example.** Eliminate the parameter from $$x=t^2-1$$, $$y=t^3-t$$ for $$-2\le t\le1$$, and describe exactly which portions of the resulting curve are traced.

Since $$y=t(t^2-1)=tx$$ and $$t^2=x+1$$, squaring gives

$$
y^2=x^2(x+1).
$$

However, this equation alone includes points the parameter never reaches. The possible $$x$$ values are $$-1\le x\le3$$. For $$-1\le x\le0$$, both signs of $$t=\pm\sqrt{x+1}$$ occur, so both values $$y=\pm x\sqrt{x+1}$$ appear. For $$0<x\le3$$, only the negative parameter is allowed, so only $$y=-x\sqrt{x+1}$$ appears.

As $$t$$ increases, the curve moves from $$(3,-6)$$ through $$(0,0)$$ at $$t=-1$$, then to $$(-1,0)$$ at $$t=0$$, and back to $$(0,0)$$ at $$t=1$$. Squaring preserved the equation but lost both the branch restriction and the repeated visit to the origin.

// make this harder and add a diagram for the problem

</div>

### Trig Substritutions

When dealing with trig, we can often use the identity $$\sin^2 t+\cos^2 t=1$$ (or equivalent expressions with the other trig functions) to eliminate the parameter

:::strategy
1. Isolate the two trig expressions (e.g. $$\cos t = \frac{x}{a}$$).
2. Use a version of the Pythagoren Identity (e.g. $$\cos^2 t + \sin^2 t = 1$$) to combine the two equations.
3. State any domain restrictions on the graph and indicate orientation/direction.
:::

<div class="theorem-box">

**Example.** Eliminate the parameter from $$x=2+3\cos t$$, $$y=-1+2\sin t$$ for $$-\pi/2\le t\le\pi/3$$, and identify the arc and orientation.

Isolate sine and cosine and square:

$$
\frac{(x-2)^2}{9}+\frac{(y+1)^2}{4}=1.
$$

The full equation is an ellipse, but $$\cos t\ge0$$ on the allowed interval, so $$x\ge2$$. Also $$\sin t$$ increases from $$-1$$ to $$\sqrt3/2$$, so $$-3\le y\le\sqrt3-1$$. These restrictions select exactly the required arc of the right half of the ellipse.

The motion starts at $$(2,-3)$$, passes through $$(5,-1)$$, and ends at $$(7/2,\sqrt3-1)$$. It follows the ellipse counterclockwise, even though $$x$$ first increases and then decreases.

// add the diagram

</div>

### Graphing parametric equations

:::strategy
1. Choose values of $$t$$.
2. Calculate the corresponding $$x$$ and $$y$$ values.
3. Plot the ordered pairs $$(x,y)$$.
4. Use arrows to show the direction of motion as $$t$$ increases.
5. An alternative is to solve for the combined equation and then graph that equation on the **allowed domain** and then draw the direction arrows.
:::

::::problem
**Parametric practice A.** For $$x=2t/(1+t^2)$$ and $$y=(1-t^2)/(1+t^2)$$, $$-1\le t\le2$$, eliminate the parameter. Identify the exact arc, endpoints, and direction, and sketch the graph.

:::solution
Combining squares gives $$x^2+y^2=1$$. Write $$\phi=2\tan^{-1}t$$; then $$x=\sin\phi$$ and $$y=\cos\phi$$. As $$t$$ increases, $$\phi$$ increases from $$-\pi/2$$ to $$2\tan^{-1}2$$. Because the coordinates are $$\sin\phi,\cos\phi$$ in that order, the curve moves clockwise from $$(-1,0)$$ through $$(0,1)$$ and $$(1,0)$$ to $$(4/5,-3/5)$$. The remainder of the unit circle is not traced.

```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\begin{tikzpicture}[>=Stealth, scale=2]
\draw[->, gray!70] (-1.4,0) -- (1.5,0) node[right] {$x$};
\draw[->, gray!70] (0,-1.35) -- (0,1.45) node[above] {$y$};
\draw[gray!50, dashed] (0,0) circle (1);
\draw[blue, very thick, domain=-1:2, samples=161] plot ({2*\x/(1+\x*\x)},{(1-\x*\x)/(1+\x*\x)});
\draw[blue, thick, ->] ({cos(60)},{sin(60)}) arc (60:40:1);
\fill (-1,0) circle (0.9pt) node[below left] {$(-1,0)$};
\fill (0.8,-0.6) circle (0.9pt) node[below right] {$(4/5,-3/5)$};
\end{tikzpicture}
```
:::
::::

::::problem
**Parametric practice B.** Sketch $$x=2\cos t$$, $$y=\sin(2t)$$ for $$0\le t\le2\pi$$. Eliminate the parameter, find every visit to the origin, and explain why the rectangular equation alone cannot specify the direction.

:::solution
Since $$y=2\sin t\cos t=x\sin t$$,

$$
y^2=x^2\left(1-\frac{x^2}{4}\right),\qquad -2\le x\le2.
$$

The origin occurs at $$t=\pi/2$$ and $$3\pi/2$$. The route is $$(2,0)\to(\sqrt2,1)\to(0,0)\to(-\sqrt2,-1)\to(-2,0)\to(-\sqrt2,1)\to(0,0)\to(\sqrt2,-1)\to(2,0)$$ at consecutive multiples of $$\pi/4$$. The equation gives the figure-eight point set, while the parameter gives the order and distinguishes the two passages through the crossing.

```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\begin{tikzpicture}[>=Stealth, scale=1.35]
\draw[->, gray!70] (-2.5,0) -- (2.6,0) node[right] {$x$};
\draw[->, gray!70] (0,-1.4) -- (0,1.5) node[above] {$y$};
\draw[blue, very thick, domain=0:360, samples=361] plot ({2*cos(\x)},{sin(2*\x)});
\draw[blue, thick, ->, domain=25:40, samples=20] plot ({2*cos(\x)},{sin(2*\x)});
\draw[blue, thick, ->, domain=205:220, samples=20] plot ({2*cos(\x)},{sin(2*\x)});
\fill (2,0) circle (1.5pt) node[below right] {start};
\end{tikzpicture}
```
:::
::::

// have these as examples and not like practice problems

---

## Polar Coordinates

### Introduction to polar coordinates

In rectangular coordinates, we write points as $$(x,y).$$ However, often times we describe problems with curves or rotations, which can be hard with rectangular coordinaets. When dealing with rotation, we often think of circles, which we can utilize.  

In polar coordinates, a point is written as $$(r,\theta),$$

where:

- $$r$$ is the directed distance from the pole (the origin),
- $$\theta$$ is the angle from the polar axis (the positive $$x$$-axis)

// talk about polar coordinates, the polar plane, and circles

A negative radius means that you are going in the *opposite* direction of the angle.

```tikz
\usepackage{tikz}
\usetikzlibrary{angles,arrows.meta,quotes}
\begin{tikzpicture}[>=Stealth, scale=0.95]
\draw[->, gray!70] (-3.8,0) -- (4.4,0) node[right] {polar axis};
\draw[->, gray!70] (0,-2.2) -- (0,3.2) node[above] {$y$};
\coordinate (O) at (0,0);
\coordinate (X) at (1,0);
\coordinate (P) at (3,2);
\coordinate (Q) at (-3,-2);
\draw[very thick, blue, ->] (O) -- (P) node[midway, above left] {$r$};
\draw[dashed, red!75!black, ->] (O) -- (Q) node[midway, below right] {$-r$};
\draw pic[draw, "$\theta$", angle radius=0.65cm] {angle=X--O--P};
\fill (O) circle (2pt) node[below right] {pole};
\fill[blue] (P) circle (2pt) node[above right] {$(r,\theta)$};
\fill[red!75!black] (Q) circle (2pt) node[below left] {$(-r,\theta)$};
\end{tikzpicture}
```

// draw the polar plane and make sure theta is outside the angle not inside the angle

### Converting between polar and rectangular form

To convert between polar and rectangular, we can use the following set of conversions:

$$
x=r\cos\theta \text{ and } y=r\sin\theta.
$$

Also, we have

$$
x^2+y^2=r^2
$$

and

$$
\tan\theta=\frac{y}{x}.
$$

<div class="theorem-box">

**Proof (Conversion formulas).** A polar point $$(r,\theta)$$ forms a right triangle with horizontal leg $$x$$, vertical leg $$y$$, and hypotenuse $$r$$.

```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\begin{tikzpicture}[>=Stealth]
\draw[->, gray!70] (-0.5,0) -- (4.8,0) node[right] {$x$};
\draw[->, gray!70] (0,-0.5) -- (0,3.6) node[above] {$y$};
\draw[blue, very thick, ->] (0,0) -- (3.6,2.4) node[midway, above left] {$r$};
\draw[orange!85!black, thick] (0,0) -- (3.6,0) node[midway, below] {$x=r\cos\theta$};
\draw[orange!85!black, dashed, thick] (3.6,0) -- (3.6,2.4) node[midway, right] {$y=r\sin\theta$};
\draw (3.35,0) -- (3.35,0.25) -- (3.6,0.25);
\draw (0.65,0) arc (0:33.69:0.65);
\node at (1.05,0.27) {$\theta$};
\fill (3.6,2.4) circle (2pt) node[above right] {$P=(x,y)$};
\end{tikzpicture}
```

The picture uses $$r>0$$ in Quadrant I. Signed components extend $$x=r\cos\theta$$ and $$y=r\sin\theta$$ to every quadrant and to negative $$r$$. At the pole, the angle is arbitrary; the ratio $$y/x$$ requires $$x\ne0$$.

By right triangle trig, $$\cos\theta=\frac{x}{r}$$ and $$\sin\theta=\frac{y}{r}$$.

Multiplying by $$r$$ gives

$$
x=r\cos\theta,\qquad y=r\sin\theta.
$$

The Pythagorean Theorem gives

$$
x^2+y^2=r^2.
$$

Similarly, since $$\tan\theta$$ represents the slope of the line connecting the origin to the point,

$$
\tan\theta=\frac{y}{x}.
$$

</div>

<div class="theorem-box">

**Example.** Convert

$$
\left(2,\frac{7\pi}{6}\right)
$$

to rectangular coordinates.

Use

$$
x=r\cos\theta,\qquad y=r\sin\theta.
$$

Then

$$
x=2\cos\left(\frac{7\pi}{6}\right)=2\left(-\frac{\sqrt3}{2}\right)=-\sqrt3
$$

and

$$
y=2\sin\left(\frac{7\pi}{6}\right)=2\left(-\frac12\right)=-1.
$$

So the rectangular point is

$$
(-\sqrt3,-1).
$$

</div>

However, as you may remember, trigonometry (which is used to convert from polar to cartesian and vice versa) is periodic, meaning that multiple angles can produce the same value. Thus, a polar point has infinitely many representations.

For any integer $$k$$,

$$
(r,\theta)=(r,\theta+2k\pi).
$$

A point can also be represented using a negative radius:

$$
(r,\theta)=(-r,\theta+(2k+1)\pi).
$$

<div class="theorem-box">

**Example.** Find two points that are the same point as $$\left(4,\frac{\pi}{3}\right)$$.

The polar points

$$
\left(4,\frac{\pi}{3}\right),\qquad
\left(4,\frac{\pi}{3}+2\pi\right),\qquad
\left(-4,\frac{4\pi}{3}\right)
$$

all represent the same point.

The first two use the same radius and coterminal angles. The third uses a negative radius, so it points in the opposite direction from $$\frac{4\pi}{3}$$, which lands at angle $$\frac{\pi}{3}$$.

</div>

### Converting equations

Using the polar-Cartesian conversion formulas, we can swap between polar and rectangular forms of equations

$$
x=r\cos\theta,\qquad y=r\sin\theta,\qquad r^2=x^2+y^2.
$$

Sometimes it helps to multiply both sides of a polar equation by $$r$$ so that $$r\cos\theta$$ or $$r\sin\theta$$ appears.

The two most common substitutions are:

$$
r\cos\theta=x
$$

and

$$
r\sin\theta=y.
$$

<div class="theorem-box">

**Example.** Convert $$r=\frac{6\cos\theta-4\sin\theta}{1+3\sin^2\theta}$$ to rectangular form and identify the curve.

The denominator is always positive. Multiply by it and then by $$r$$ to create the coordinate substitutions:

$$
\begin{aligned}
r+3r\sin^2\theta&=6\cos\theta-4\sin\theta,\\
r^2+3r^2\sin^2\theta&=6r\cos\theta-4r\sin\theta,\\
x^2+4y^2&=6x-4y.
\end{aligned}
$$

Completing the squares gives

$$
(x-3)^2+4\left(y+\frac12\right)^2=10.
$$

This is an ellipse centered at $$(3,-1/2)$$. Multiplying by $$r$$ can add the pole, so check it in the original equation: the numerator vanishes when $$\tan\theta=3/2$$, making $$r=0$$ valid. No extra point was added.

</div>

<div class="theorem-box">

**Example.** Convert $$(x-2)^2+(y+1)^2=5$$ to a single explicit polar equation, and explain what happens if you divide by $$r$$.

Expand before substituting:

$$
x^2+y^2-4x+2y=0
\quad\Longrightarrow\quad
r(r-4\cos\theta+2\sin\theta)=0.
$$

For nonzero $$r$$, the equation is $$r=4\cos\theta-2\sin\theta$$. This explicit equation still represents the pole, because some angles make its right side zero. It therefore traces the entire circle, including the point that division by $$r$$ temporarily excluded.

The same equation can be written as

$$
r=2\sqrt5\cos(\theta+\alpha),\qquad
\alpha=\tan^{-1}\frac12.
$$

Its center is $$\sqrt5$$ units from the pole at angle $$-\alpha$$, matching $$(2,-1)$$. If you restrict to $$r\ge0$$, use an interval where $$\cos(\theta+\alpha)\ge0$$.

</div>


### Rotating points and curves

One of the main reasons to use polar coordinates is the ease of rotation. To rotate a point counterclockwise through angle $$\alpha$$ about the pole, keep its radius and add the angle:

$$
(r,\theta)\longmapsto(r,\theta+\alpha).
$$

Clockwise rotation uses a negative $$\alpha$$. Combining this with the angle-sum identities gives the rectangular rule

$$
\begin{aligned}
x'&=x\cos\alpha-y\sin\alpha,\\
y'&=x\sin\alpha+y\cos\alpha.
\end{aligned}
$$

For example, rotating $$(2,-1)$$ counterclockwise by $$\pi/2$$ gives $$(1,2)$$. For a whole polar curve $$r=f(\theta)$$, counterclockwise rotation by $$\alpha$$ instead gives $$r=f(\theta-\alpha)$$: a point at the new angle $$\theta$$ has the radius the old curve had at $$\theta-\alpha$$.

:::warning
Rotating a point adds $$\alpha$$ to its angle, while rotating a curve's equation replaces $$\theta$$ with $$\theta-\alpha$$. These are two descriptions of the same motion.
:::

// add a hard problem (e.g. have a rectangular formula and rotating it or smth)

### Distance in polar coordinates

If two points are written in polar form as $$P(r_1,\theta_1)$$ and $$Q(r_2,\theta_2)$$,

then the distance between them is

$$
d=\sqrt{r_1^2+r_2^2-2r_1r_2\cos(\theta_2-\theta_1)}.
$$

This comes from the Law of Cosines.

<div class="theorem-box">

**Proof (Distance formula in polar).** Draw the two polar points from the pole. Their distances from the pole are $$r_1$$ and $$r_2$$.

The angle between the two segments is

$$
\theta_2-\theta_1.
$$

The distance $$d$$ between the points is the side opposite that angle. By the Law of Cosines,

$$
d^2=r_1^2+r_2^2-2r_1r_2\cos(\theta_2-\theta_1).
$$

Taking the square root gives

$$
d=\sqrt{r_1^2+r_2^2-2r_1r_2\cos(\theta_2-\theta_1)}.
$$

</div>

The polar distance formula uses only the two radii and their angle difference. If both points rotate by the same angle, their separation stays unchanged, and this is immediately visible because $$\theta_2-\theta_1$$ does not change. It also avoids expanding four separate sine and cosine coordinates. The algebraic formula remains valid for signed radii, although the triangle proof above first assumes nonnegative radii.

<div class="theorem-box">

**Example.** Two points move with polar coordinates $$P=(6,t)$$ and $$Q=(-4,2t)$$ for $$0\le t<2\pi$$. Find their minimum and maximum separation, and all times when their separation is $$2\sqrt{13}$$.

Keep the negative radius when substituting:

$$
d^2=6^2+(-4)^2-2(6)(-4)\cos(2t-t)=52+48\cos t.
$$

Because $$-1\le\cos t\le1$$, the squared distance ranges from $$4$$ to $$100$$. The minimum is $$d=2$$ at $$t=\pi$$, and the maximum is $$d=10$$ at $$t=0$$. A negative radius does not mean a negative length; at $$t=0$$ the points are on opposite sides of the pole.

Finally, $$d=2\sqrt{13}$$ means $$d^2=52$$, so $$\cos t=0$$. The requested times are $$t=\pi/2$$ and $$3\pi/2$$.

</div>

### Circles and lines in polar coordinates

A circle with center $$(r_0,\theta_0)$$ and radius $$a$$ can be written using

$$
a^2=r^2+r_0^2-2rr_0\cos(\theta-\theta_0).
$$

This is the polar distance formula applied to a moving point $$(r,\theta)$$ and a fixed center $$(r_0,\theta_0)$$.

<div class="theorem-box">

**Proof (Circle equation in polar).** A point $$(r,\theta)$$ is on a circle with center $$(r_0,\theta_0)$$ and radius $$a$$ exactly when its distance from the center is $$a$$.

Using the polar distance formula,

$$
a=\sqrt{r^2+r_0^2-2rr_0\cos(\theta-\theta_0)}.
$$

Squaring both sides gives

$$
a^2=r^2+r_0^2-2rr_0\cos(\theta-\theta_0).
$$

</div>

Alternatively, you can write the circle equation (centered at the origin) as $$r=a$$, which represents the set of all points $$a$$ away from origin (aka a circle).

A line through the pole has the form

$$
\theta=\theta_0.
$$

A line not passing through the pole can be written as

$$
d=r\cos(\theta-\alpha),
$$

where $$(d,\alpha)$$ is the polar point on the line closest to the pole.

<div class="theorem-box">

**Proof (Polar line equation).** Let $$(d,\alpha)$$ be the point on the line closest to the pole. The segment from the pole to this point is perpendicular to the line.

For any point $$(r,\theta)$$ on the line, draw the triangle formed by the pole, $$(d,\alpha)$$, and $$(r,\theta)$$.

The angle between the segment of length $$r$$ and the segment of length $$d$$ is

$$
\theta-\alpha.
$$

Since $$d$$ is the adjacent side of the right triangle and $$r$$ is the hypotenuse,

$$
\cos(\theta-\alpha)=\frac{d}{r}.
$$

Multiplying by $$r$$ gives

$$
d=r\cos(\theta-\alpha).
$$

</div>

<div class="theorem-box">

**Example.** A line is tangent to the circle $$x^2+y^2=36$$ at the point $$(-3,-3\sqrt3).$$ Find the equation of the line.

The circle has radius $$6$$, so the point of tangency is $$6$$ units from the origin. The point lies at angle $$\frac{4\pi}{3}$$, so the closest point on the tangent line to the pole is

$$
\left(6,\frac{4\pi}{3}\right).
$$

Using the polar line formula,

$$
6=r\cos\left(\theta-\frac{4\pi}{3}\right).
$$

You can also begin with the tangent $$x=6$$ at $$(6,0)$$. Its polar equation is $$r\cos\theta=6$$. Rotate the entire picture counterclockwise by $$4\pi/3$$, replacing $$\theta$$ with $$\theta-4\pi/3$$. This gives exactly $$r\cos(\theta-4\pi/3)=6$$, with the tangency point rotated to $$(-3,-3\sqrt3)$$.

</div>

---

## Curves in Polar Coordinates

// for the examples the helper tables should be horizontal and not vertical, and you should only have theta vs r and not 3theta vs r or smth like that

When writing curves in polar form, we don't write it as $$y=f(x)$$. Instead, we use $$r=f(\theta)$$ (Sometimes functions are defined implicitly so $$r$$ and $$\theta$$ are correlated on the same side).

:::strategy
1. Make a table of $$\theta$$ and $$r$$ values, and draw a helper $$r$$ vs. $$\theta$$ graph if necessary.
2. Plot each polar point.
3. Watch for negative $$r$$ values.
4. Use symmetry and periodicity to complete the curve.
:::

However, it is also very helpful to know some of the most common types of polar curves.

### Spirals

Spirals have equations in the form

$$
r=a\theta
$$

As $$\theta$$ increases, $$r$$ changes, so the point moves farther from or closer to the pole. These spirals are also known as Archimedian Spirals (as you may remember from *Spider-Man: No Way Home*).

<div class="theorem-box">

**Example.** Graph $$r=\frac{\theta}{\pi},$$

The radius grows as $$\theta$$ grows:

$$
\begin{array}{c|ccccc}
\theta & 0 & \frac{\pi}{2} & \pi & \frac{3\pi}{2} & 2\pi\\
\hline
r & 0 & \frac12 & 1 & \frac32 & 2
\end{array}
$$

So the graph spirals outward from the pole.

A graph of the function is shown below:

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{tikzpicture}
\begin{axis}[
  axis lines=middle, axis equal image,
  xmin=-2.2, xmax=2.2, ymin=-2.2, ymax=2.2,
  xtick={-2,-1,0,1,2}, ytick={-2,-1,0,1,2},
  grid=both, grid style={gray!18},
  width=9cm, height=9cm,
  xlabel=$x$, ylabel=$y$,
]
\addplot[blue, very thick, samples=260, domain=0:720]
  ({(x/180)*cos(x)}, {(x/180)*sin(x)});
\end{axis}
\end{tikzpicture}
```

</div>

### Cardioids and limaçons

A limaçon is a type of curve with the equation

$$
r=a+b\sin\theta \text{ or } r=a+b\cos\theta.
$$

If a limaçon uses $$\sin$$, it is symmetrical over the $$y$$-axis, and if it uses $$\cos$$, it is symmetrical over the $$x$$-axis.

If $$\lvert a \rvert = \lvert b \rvert$$, the graph is a special curve known as a **cardioid**.

If $$\lvert a \rvert < \lvert b \rvert$$, the graph has an inner loop.

A list of common limacon shapes is shown below (note that a circle is technically a limacon as well):

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\pgfplotsset{limacon/.style={scale only axis, width=3.8cm, height=3.2cm,
  axis lines=middle, axis equal image, xmin=-5, xmax=5, ymin=-5, ymax=5,
  xtick=\empty, ytick=\empty, axis line style={gray!60},
  title style={font=\footnotesize}, clip=true}}
\begin{tikzpicture}
\begin{axis}[limacon, at={(0cm,0cm)}, title={$|a|>|b|$: dimple/no loop}]
\addplot[blue, very thick, samples=220, domain=0:360] ({(3+1.5*cos(x))*cos(x)}, {(3+1.5*cos(x))*sin(x)});
\end{axis}
\begin{axis}[limacon, at={(4.6cm,0cm)}, title={$|a|=|b|$: cardioid}]
\addplot[blue, very thick, samples=220, domain=0:360] ({(2.5+2.5*cos(x))*cos(x)}, {(2.5+2.5*cos(x))*sin(x)});
\end{axis}
\begin{axis}[limacon, at={(9.2cm,0cm)}, title={$|a|<|b|$: inner loop}]
\addplot[blue, very thick, samples=260, domain=0:360] ({(2+4*cos(x))*cos(x)}, {(2+4*cos(x))*sin(x)});
\end{axis}
\end{tikzpicture}
```

<div class="theorem-box">

**Example.** Graph $$r=2+4\cos\theta.$$

Here $$a=2$$ and $$b=4$$. Since $$\lvert a \rvert < \lvert b \rvert$$, the graph is a limacon with an inner loop.

Since the equation uses cosine, the graph has symmetry across the polar axis.

The helper graph is the ordinary cosine graph $$r=2+4\cos\theta$$. Include the zeros as well as its maximum and minimum:

| $$\theta$$ | $$r$$ | Polar-graph feature |
|---|---|---|
| $$0$$ | $$6$$ | Outer tip $$(6,0)$$ |
| $$\pi/2$$ | $$2$$ | Point $$(0,2)$$ |
| $$2\pi/3$$ | $$0$$ | First passage through the pole |
| $$\pi$$ | $$-2$$ | Inner-loop tip $$(2,0)$$ |
| $$4\pi/3$$ | $$0$$ | Second passage through the pole |
| $$3\pi/2$$ | $$2$$ | Point $$(0,-2)$$ |
| $$2\pi$$ | $$6$$ | Return to the outer tip |

The interval $$2\pi/3<\theta<4\pi/3$$ has negative radius and traces the inner loop on the right of the pole.

A graph of the function is shown below:

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{tikzpicture}
\begin{axis}[
  axis lines=middle, axis equal image,
  xmin=-2.5, xmax=6.5, ymin=-4.5, ymax=4.5,
  xtick={-2,0,2,4,6}, ytick={-4,-2,0,2,4},
  grid=both, grid style={gray!18},
  width=10cm, height=8cm,
  xlabel=$x$, ylabel=$y$,
]
\addplot[blue, very thick, samples=360, domain=0:360]
  ({(2+4*cos(x))*cos(x)}, {(2+4*cos(x))*sin(x)});
\end{axis}
\end{tikzpicture}
```

</div>

### Rose curves

Rose curves have the form

$$
r=a\sin(n\theta) \text{ or } r=a\cos(n\theta).
$$

For positive integer $$n$$, a cosine rose is symmetric about the polar axis, and a sine rose is symmetric about the $$y$$-axis. A sine rose is also a rotated version of the corresponding cosine rose, since $$\sin(n\theta)=\cos(n(\theta-\pi/(2n)))$$. These need not be their only symmetry axes; for example, $$r=\sin(2\theta)$$ has diagonal petals and symmetry about both coordinate axes.

```tikz
\usepackage{tikz}
\begin{tikzpicture}[scale=0.9]
\begin{scope}
\draw[->, gray!60] (-3.5,0) -- (3.6,0);
\draw[->, gray!60] (0,-3.4) -- (0,3.6);
\draw[blue, very thick, domain=0:180, samples=361] plot ({3*cos(3*\x)*cos(\x)},{3*cos(3*\x)*sin(\x)});
\node at (0,4.1) {$r=3\cos(3\theta)$};
\end{scope}
\begin{scope}[xshift=8cm]
\draw[->, gray!60] (-3.5,0) -- (3.6,0);
\draw[->, gray!60] (0,-3.4) -- (0,3.6);
\draw[red!75!black, very thick, domain=0:180, samples=361] plot ({3*sin(3*\x)*cos(\x)},{3*sin(3*\x)*sin(\x)});
\node at (0,4.1) {$r=3\sin(3\theta)$};
\end{scope}
\end{tikzpicture}
```

The sine graph above is the cosine graph rotated counterclockwise by $$\pi/6$$. The petal-count rule below assumes $$n$$ is a positive integer.

The number of petals depends on $$n$$:

$$
\begin{array}{c|c}
n & \text{Number of petals}\\
\hline
\text{odd} & n\\
\text{even} & 2n
\end{array}
$$

The value $$\lvert a \rvert$$ controls the length of each petal.

Why is the cases for the odd and even petals different? The helper graph $$y=a\sin(n\theta)$$ (and the cosine version as well) has period $$\frac{2\pi}{n}.$$ For odd $$n$$, the negative radius portions trace the same petals that the positive radius portions already traced, so there are $$n$$ petals total. For even $$n$$, the negative radius portions trace new petals, so there are $$2n$$ petals total.

<div class="theorem-box">

**Example.** Draw the rose curve $$r=4\sin(3\theta)$$.

For this curve, the value of $$n$$ is $$3$$, which is odd. Therefore, the rose curve has $$3$$ petals, and each petal has length $$4$$.

The helper graph $$r=4\sin(3\theta)$$ has period $$2\pi/3$$. These points track one complete positive petal and the beginning of a negative-radius petal:

| $$\theta$$ | $$3\theta$$ | $$r$$ | What happens |
|---|---|---|---|
| $$0$$ | $$0$$ | $$0$$ | Start at the pole |
| $$\pi/12$$ | $$\pi/4$$ | $$2\sqrt2$$ | Move outward |
| $$\pi/6$$ | $$\pi/2$$ | $$4$$ | First petal tip |
| $$\pi/4$$ | $$3\pi/4$$ | $$2\sqrt2$$ | Move inward |
| $$\pi/3$$ | $$\pi$$ | $$0$$ | Complete the first petal |
| $$\pi/2$$ | $$3\pi/2$$ | $$-4$$ | Tip on the ray $$\theta=3\pi/2$$ |
| $$2\pi/3$$ | $$2\pi$$ | $$0$$ | Return to the pole |

The remaining positive petal has its tip at $$\theta=5\pi/6$$. The interval $$0\le\theta\le\pi$$ traces all three petals once; continuing to $$2\pi$$ retraces them.

To draw the rose, start at $$\theta=0$$ (point $$0,0$$) and start plotting points along a polar graph. Once you draw one petal, repeat for the other two petals and make sure they are evenly spread out.

A graph of the function is shown below:

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{tikzpicture}
\begin{axis}[
  axis lines=middle, axis equal image,
  xmin=-4.5, xmax=4.5, ymin=-4.5, ymax=4.5,
  xtick={-4,-2,0,2,4}, ytick={-4,-2,0,2,4},
  grid=both, grid style={gray!18},
  width=9cm, height=9cm,
  xlabel=$x$, ylabel=$y$,
]
\addplot[blue, very thick, samples=420, domain=0:360]
  ({(4*sin(3*x))*cos(x)}, {(4*sin(3*x))*sin(x)});
\end{axis}
\end{tikzpicture}
```

</div>

### Lemniscates

Lemniscates are figure-eight shaped curves. Common forms include

$$
r^2=a^2\cos(2\theta) \text{ and } r^2=a^2\sin(2\theta).
$$

Since $$r^2$$ cannot be negative, only angles that make the right side nonnegative appear on the graph. The positive cosine form has loops along the $$x$$-axis, while the positive sine form has loops along $$\theta=\pi/4$$ and $$5\pi/4$$, on the line $$y=x$$. Each also has symmetry across the line perpendicular to its loop axis.

What if we use $$-a^2$$ instead of $$a^2$$? This will rotate the graph $$\frac{\pi}{2}$$.

<div class="theorem-box">

**Extension.** Prove the statement above.

</div>

<div class="theorem-box">

**Example.** Graph $$r^2=9\sin(2\theta)$$.

For this graph, the maximum value of $$r^2$$ is $$9$$, so the maximum value of $$r$$ is $$3$$.

Use $$r=\sqrt{9\sin(2\theta)}$$ when the right side is nonnegative. The helper graph is $$r^2=9\sin(2\theta)$$, so remember to take a square root before plotting the radius:

| $$\theta$$ | $$r^2$$ | Nonnegative $$r$$ |
|---|---|---|
| $$0$$ | $$0$$ | $$0$$ |
| $$\pi/12$$ | $$9/2$$ | $$3/\sqrt2$$ |
| $$\pi/4$$ | $$9$$ | $$3$$ |
| $$5\pi/12$$ | $$9/2$$ | $$3/\sqrt2$$ |
| $$\pi/2$$ | $$0$$ | $$0$$ |
| $$3\pi/4$$ | $$-9$$ | No real point |
| $$\pi$$ | $$0$$ | $$0$$ |
| $$5\pi/4$$ | $$9$$ | $$3$$ |
| $$3\pi/2$$ | $$0$$ | $$0$$ |

Nonnegative radii on $$[0,\pi/2]$$ trace the first loop, and those on $$[\pi,3\pi/2]$$ trace the opposite loop. Choosing the negative square root places each point on the opposite loop and adds no new points to the full graph.

The graph is a lemniscate. Since it uses $$\sin(2\theta)$$, its loops lie along the diagonal directions rather than directly on the polar axis.

A graph of the lemniscate is shown below:

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{tikzpicture}
\begin{axis}[
  axis lines=middle, axis equal image,
  xmin=-3.5, xmax=3.5, ymin=-3.5, ymax=3.5,
  xtick={-3,-2,-1,0,1,2,3}, ytick={-3,-2,-1,0,1,2,3},
  grid=both, grid style={gray!18},
  width=9cm, height=9cm,
  xlabel=$x$, ylabel=$y$,
]
\addplot[blue, very thick, samples=220, domain=0:90]
  ({(3*sqrt(sin(2*x)))*cos(x)}, {(3*sqrt(sin(2*x)))*sin(x)});
\addplot[blue, very thick, samples=220, domain=180:270]
  ({(3*sqrt(sin(2*x)))*cos(x)}, {(3*sqrt(sin(2*x)))*sin(x)});
\end{axis}
\end{tikzpicture}
```

</div>

---

## Complex Numbers

If you remember from algebra, a **complex number** is any number of the form

$$
z=a+bi,
$$

where $$a$$ and $$b$$ are real numbers and

$$
i=\sqrt{-1}.
$$

The number $$a$$ is the **real part**, and $$b$$ is the **imaginary part**.

A key fact of $$i$$ that we will utilize is that the powers of $$i$$ repeat in a cycle:

$$
i^1=i,\qquad i^2=-1,\qquad i^3=-i,\qquad i^4=1.
$$

After that, the pattern repeats every four powers.

### The complex plane

Complex numbers can be graphed on the **complex plane**. The horizontal axis is the real axis, and the vertical axis is the imaginary axis. This means that the complex number

$$
z=a+bi
$$

corresponds to the point

$$
(a,b)
$$

in the plane. The magnitude, or **modulus** (also known as **norm**), of $$z$$ is

$$
\lvert z\rvert=\sqrt{a^2+b^2}.
$$

This is the distance from the origin to the point $$(a,b)$$, and is also the norm of the vector from the origin to that point.

The **complex conjugate** of $$z=a+bi$$ is defined as

$$
\overline z=a-bi.
$$

Conjugates have the interesting property that multiplying a complex number by its conjugate gives

$$
z\overline z=(a+bi)(a-bi)=a^2+b^2=\lvert z\rvert^2.
$$

### Operations with complex numbers

To add or subtract complex numbers, we can combine real parts with real parts and imaginary parts with imaginary parts like vector components:

$$
(a+bi)+(c+di)=(a+c)+(b+d)i
$$

and

$$
(a+bi)-(c+di)=(a-c)+(b-d)i.
$$

To multiply, we can FOIL and treat $$i$$ as a variable before substituting $$i^2=-1$$:

$$
(a+bi)(c+di)=ac+adi+bci+bdi^2.
$$

Since $$i^2=-1$$,

$$
(a+bi)(c+di)=(ac-bd)+(ad+bc)i.
$$

To divide complex numbers, multiply the numerator and denominator by the conjugate of the denominator, kind of like rationalizing the denominator.

<div class="theorem-box">

**Example.** Simplify

$$
\frac{3+2i}{1-4i}.
$$

Multiply by the conjugate of the denominator:

$$
\frac{3+2i}{1-4i}\cdot \frac{1+4i}{1+4i}.
$$

The numerator is

$$
(3+2i)(1+4i)=3+12i+2i+8i^2.
$$

Since $$i^2=-1$$,

$$
3+14i+8i^2=-5+14i.
$$

The denominator is

$$
(1-4i)(1+4i)=1^2+4^2=17.
$$

So

$$
\frac{3+2i}{1-4i}=-\frac5{17}+\frac{14}{17}i.
$$

</div>

### Polar form of complex numbers

Since $$a+bi$$ corresponds to the point $$(a,b)$$, a complex number can also be written using polar coordinates.

Let $$r=\lvert z\rvert=\sqrt{a^2+b^2}$$.

Let $$\theta$$ be the angle the point makes with the positive real axis. Then

$$
a=r\cos\theta \text{ and } b=r\sin\theta.
$$

Therefore,

$$
z=a+bi=r\cos\theta+ir\sin\theta.
$$

Factoring out $$r$$ gives the **polar form**:

$$
z=r(\cos\theta+i\sin\theta).
$$

This is sometimes abbreviated as

$$
z=r\operatorname{cis}\theta,
$$

where

$$
\operatorname{cis}\theta=\cos\theta+i\sin\theta.
$$

### Operations in polar form

Polar form makes multiplication and division easier because it separates the change in magnitude from the change in angle. Addition and subtraction still combine rectangular components. If $$z_1=r_1\operatorname{cis}\alpha$$ and $$z_2=r_2\operatorname{cis}\beta$$, then

$$
\begin{aligned}
z_1\pm z_2
&=(r_1\cos\alpha\pm r_2\cos\beta)\\
&\quad+i(r_1\sin\alpha\pm r_2\sin\beta).
\end{aligned}
$$

For example, $$2\operatorname{cis}(\pi/3)+2\operatorname{cis}(-\pi/3)=2$$, because the imaginary components cancel. You cannot add the moduli and angles separately: that would incorrectly give $$4\operatorname{cis}0=4$$. If a sum is needed in polar form, combine its components first, then find its modulus and quadrant.

Suppose $$z_1=r_1(\cos\alpha+i\sin\alpha)$$ and $$z_2=r_2(\cos\beta+i\sin\beta)$$.

Then

$$
z_1z_2=r_1r_2\left(\cos(\alpha+\beta)+i\sin(\alpha+\beta)\right).
$$

In words, when multiplying complex numbers in polar form, multiply the moduli and add the angles.

For division,

$$
\frac{z_1}{z_2}
=\frac{r_1}{r_2}\left(\cos(\alpha-\beta)+i\sin(\alpha-\beta)\right),
$$

where $$z_2\ne 0$$.

In words, when dividing, divide the moduli and subtract the angles.

<div class="theorem-box">

**Proof (Polar multiplication formula).** Multiply directly:

$$
z_1z_2=r_1r_2(\cos\alpha+i\sin\alpha)(\cos\beta+i\sin\beta).
$$

Distribute:

$$
z_1z_2=r_1r_2(\cos\alpha\cos\beta+i\cos\alpha\sin\beta+i\sin\alpha\cos\beta+i^2\sin\alpha\sin\beta).
$$

Since $$i^2=-1$$,

$$
z_1z_2=r_1r_2\left((\cos\alpha\cos\beta-\sin\alpha\sin\beta)+i(\sin\alpha\cos\beta+\cos\alpha\sin\beta)\right).
$$

Using the angle addition identities,

$$
\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta
$$

and

$$
\sin(\alpha+\beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta,
$$

we get

$$
z_1z_2=r_1r_2\left(\cos(\alpha+\beta)+i\sin(\alpha+\beta)\right).
$$

For example, multiplying $$z_1=2\operatorname{cis}(\pi/6)$$ by $$z_2=\frac32\operatorname{cis}(\pi/3)$$ stretches its vector by $$3/2$$ and rotates it by $$\pi/3$$. The product is $$3\operatorname{cis}(\pi/2)=3i$$. These are position vectors in the complex plane; the multiplication is complex multiplication, not a dot product.


</div>

<div class="theorem-box">

**Extension.** Derive the division formula for two complex numbers.

</div>

<div class="theorem-box">

**Example.** Simplify $$Z=\frac{(\sqrt3+i)^4(1-i)^3}{(-2i)^2}$$ in polar and rectangular form, giving its argument in $$[0,2\pi)$$.

The three bases are $$2\operatorname{cis}(\pi/6)$$, $$\sqrt2\operatorname{cis}(-\pi/4)$$, and $$2\operatorname{cis}(-\pi/2)$$. Repeated multiplication and division give

$$
\lvert Z\rvert=\frac{2^4(\sqrt2)^3}{2^2}=8\sqrt2,
\qquad
\arg Z=4\frac\pi6-3\frac\pi4-2\left(-\frac\pi2\right)
=\frac{11\pi}{12}.
$$

Hence $$Z=8\sqrt2\operatorname{cis}(11\pi/12)$$. The angle-sum identities for $$11\pi/12=3\pi/4+\pi/6$$ give

$$
Z=-4(\sqrt3+1)+4(\sqrt3-1)i.
$$

The quadrant is II, consistent with the negative real and positive imaginary components.

</div>

### Exponential form of complex numbers

You may have seen the famous identitiy $$e^{i\pi}=-1$$. This is a result of Euler's formula, which states that

$$
e^{i\theta}=\cos\theta+i\sin\theta
$$

A proof of this does require calculus and won't be discussed here.

Therefore, the polar form

$$
z=r(\cos\theta+i\sin\theta)
$$

can also be written in **exponential form**:

$$
z=re^{i\theta}.
$$

This means the following forms are equivalent:

$$
a+bi=r(\cos\theta+i\sin\theta)=r\operatorname{cis}\theta=re^{i\theta}.
$$

The exponential form is especially useful because it makes multiplication, division, and powers look like normal exponent rules.

For example,

$$
(r_1e^{i\alpha})(r_2e^{i\beta})=r_1r_2e^{i(\alpha+\beta)}.
$$

For division,

$$
\frac{r_1e^{i\alpha}}{r_2e^{i\beta}}=\frac{r_1}{r_2}e^{i(\alpha-\beta)}.
$$

For powers,

$$
(re^{i\theta})^n=r^ne^{in\theta}.
$$

These are the same rules as polar form, just written more compactly.

<div class="theorem-box">

**Example.** Write

$$
z=-2+2i
$$

in exponential form.

First find the modulus:

$$
r=\sqrt{(-2)^2+2^2}=2\sqrt2.
$$

The point $$(-2,2)$$ is in Quadrant II, with reference angle $$\frac{\pi}{4}$$. Therefore,

$$
\theta=\frac{3\pi}{4}.
$$

So

$$
z=2\sqrt2 e^{i3\pi/4}.
$$

</div>

<div class="theorem-box">

**Example.** Express $$Z=\frac{(-1+\sqrt3i)^5}{(1+i)^4(-i)}$$ in exponential and rectangular form, using a principal argument in $$(-\pi,\pi]$$.

Use $$-1+\sqrt3i=2e^{2\pi i/3}$$, $$1+i=\sqrt2e^{\pi i/4}$$, and $$-i=e^{-\pi i/2}$$. Then

$$
Z=\frac{32e^{10\pi i/3}}{4e^{\pi i}e^{-\pi i/2}}
=8e^{17\pi i/6}=8e^{5\pi i/6}.
$$

The principal argument is $$5\pi/6$$, and $$Z=8(-\sqrt3/2+i/2)=-4\sqrt3+4i$$. Subtracting $$2\pi$$ from an argument changes its representation but not the number.

</div>

### De Moivre's Theorem

<div class="theorem-box">

**Theorem.** If $$z=r(\cos\theta+i\sin\theta)$$ is nonzero, then for any integer $$n$$, $$z^n=r^n(\cos(n\theta)+i\sin(n\theta))$$. For $$z=0$$, use only positive integers $$n$$.

</div>

<div class="theorem-box">

**Proof (De Moivre's Theorem).** Multiplying complex numbers in polar form multiplies their moduli and adds their angles.

If

$$
z=r(\cos\theta+i\sin\theta),
$$

then

$$
z^2=r\cdot r \cdot (\cos(\theta + \theta) + i\sin(\theta + \theta)) = r^2(\cos(2\theta)+i\sin(2\theta)).
$$

Multiplying by another copy of $$z$$ gives

$$
z^3=r^3(\cos(3\theta)+i\sin(3\theta)).
$$

Repeating this process $$n$$ times gives

$$
z^n=r^n(\cos(n\theta)+i\sin(n\theta)),
$$

which is De Moivre's Theorem for positive integers. For $$n=0$$ and $$z\ne0$$, both sides equal $$1$$. For negative integers, apply the positive-power rule to $$1/z=r^{-1}\operatorname{cis}(-\theta)$$; this requires $$z\ne0$$.

</div>

<div class="theorem-box">

**Example.** Find

$$
(1+i)^6.
$$

First write $$1+i$$ in polar form:

$$
1+i=\sqrt2\left(\cos\frac{\pi}{4}+i\sin\frac{\pi}{4}\right).
$$

By De Moivre's Theorem,

$$
(1+i)^6=(\sqrt2)^6\left(\cos\frac{6\pi}{4}+i\sin\frac{6\pi}{4}\right).
$$

Since

$$
(\sqrt2)^6=8
$$

and $$\frac{6\pi}{4}=\frac{3\pi}{2}$$, we get

$$
(1+i)^6=8\left(\cos\frac{3\pi}{2}+i\sin\frac{3\pi}{2}\right)=-8i.
$$

</div>

### Roots of complex numbers

What if we want to solve for roots of a number instead of raising it to a power? For an equation

$$
w^n=z,
$$

we can start by writing $$z$$ in polar form (or exponent form):

$$
z=r(\cos\theta+i\sin\theta).
$$

Since angles repeat every $$2\pi$$ (very important!),

$$
z=r(\cos(\theta+2k\pi)+i\sin(\theta+2k\pi)).
$$

For nonzero $$z$$ and a positive integer $$n$$, the $$n$$ distinct complex roots are

$$
w_k=\sqrt[n]{r}\left(\cos\frac{\theta+2k\pi}{n}+i\sin\frac{\theta+2k\pi}{n}\right),
$$

where

$$
k=0,1,2,\ldots,n-1.
$$

This is essentially the reverse of De Moivre's Theorem! If $$z=0$$, the only distinct solution is $$w=0$$, with multiplicity $$n$$.

<div class="theorem-box">

**Example.** Solve $$(w-(1-i))^3=-8i$$, give every solution in rectangular form, and identify the solution in the upper half-plane.

Set $$u=w-(1-i)$$. Since $$-8i=8\operatorname{cis}(-\pi/2)$$,

$$
u_k=2\operatorname{cis}\left(-\frac\pi6+\frac{2k\pi}{3}\right),
\qquad k=0,1,2.
$$

These are $$\sqrt3-i$$, $$2i$$, and $$-\sqrt3-i$$. Add $$1-i$$ to each root to undo the translation:

$$
w=1+\sqrt3-2i,\qquad 1+i,\qquad 1-\sqrt3-2i.
$$

Only $$1+i$$ has positive imaginary part. The three solutions lie on a circle of radius $$2$$ centered at $$1-i$$, rather than at the origin.

</div>

### Roots of unity

The **$$n$$th roots of unity** are the complex numbers that solve the equation

$$
z^n=1.
$$

Since

$$
1=\cos0+i\sin0,
$$

and angles repeat every $$2\pi$$, we can also write

$$
1=\cos(2k\pi)+i\sin(2k\pi)
$$

for any integer $$k$$.

Using the complex-root formula, the $$n$$th roots of unity are

$$
z_k=\cos\left(\frac{2k\pi}{n}\right)+i\sin\left(\frac{2k\pi}{n}\right),
$$

where

$$
k=0,1,2,\ldots,n-1.
$$

In exponential form,

$$
z_k=e^{2k\pi i/n}.
$$

### Geometry of roots of unity

For a positive integer $$n$$, the $$n$$th roots of unity are evenly spaced around the unit circle. This is because after $$n$$ steps of angle $$2\pi/n$$, the total rotation is exactly $$2\pi$$.

The angle between consecutive roots is

$$
\frac{2\pi}{n}.
$$

So the roots form the vertices of a regular $$n$$-gon centered at the origin.

For example:

- The $$3$$rd roots of unity form an equilateral triangle.
- The $$4$$th roots of unity form a square.
- The $$5$$th roots of unity form a regular pentagon.

<div class="theorem-box">

**Example.** Find the fourth roots of unity.

Use

$$
z_k=e^{2k\pi i/4}
$$

for

$$
k=0,1,2,3.
$$

Then the roots are

$$
z_0=e^0=1,
$$

$$
z_1=e^{\pi i/2}=i,
$$

$$
z_2=e^{\pi i}=-1,
$$

and

$$
z_3=e^{3\pi i/2}=-i.
$$

So the fourth roots of unity are

$$
1,\ i,\ -1,\ -i.
$$

Geometrically, the solutions look like this:

```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\begin{tikzpicture}[>=Stealth, scale=1.25]
\draw[->, gray!70] (-1.6,0) -- (1.75,0) node[right] {real};
\draw[->, gray!70] (0,-1.6) -- (0,1.75) node[above] {imaginary};
\draw[blue, thick] (0,0) circle (1);
\foreach \p/\lab/\pos in {
(1,0)/$1$/below right,
(0,1)/$i$/above right,
(-1,0)/$-1$/below left,
(0,-1)/$-i$/below right}
{
  \fill[red!80!black] \p circle (2pt) node[\pos] {\lab};
}
\end{tikzpicture}
```

Note that the rendering on the $$y$$-axis shows that it is real, but treat it like the imaginary axis.

</div>

What if $$n$$ is an irrational number? The phrase "the $$n$$th roots of unity" normally assumes $$n$$ is a positive integer, so $$z^n-1$$ is a polynomial with exactly $$n$$ roots. For an irrational exponent $$\alpha$$, complex exponentiation requires a choice of logarithm; the ordinary polynomial root-count rule no longer applies.

For example, define a single value using $$z^\alpha=\exp(\alpha(\ln\lvert z\rvert+i\operatorname{Arg}z))$$ with $$-\pi<\operatorname{Arg}z\le\pi$$. Then $$z^\alpha=1$$ requires

$$
\lvert z\rvert=1,\qquad
\operatorname{Arg}z=\frac{2\pi k}{\alpha}
\quad\text{within the chosen argument interval}.
$$

For $$\alpha=\sqrt2$$, only $$k=0$$ fits, so this convention gives only $$z=1$$. If instead all possible logarithms are allowed, every $$e^{2\pi ik/\alpha}$$ is a possible solution for some logarithm. When $$\alpha$$ is irrational these points are all distinct: equality for two indices would force $$\alpha$$ to be rational. They do not form a finite regular polygon. This is why the integer assumption matters.

### Sum and product of roots of unity

For a positive integer $$n>1$$, let $$\omega=e^{2\pi i/n}$$. Its powers $$1,\omega,\ldots,\omega^{n-1}$$ are all the distinct $$n$$th roots of unity, and their sum is

$$
1+\omega+\omega^2+\cdots+\omega^{n-1}=0.
$$

There are two ways to understand this.

Geometrically, the roots are evenly spaced on the unit circle, so their vectors balance perfectly around the origin.

Algebraically, use the finite geometric series formula ([Unit 13 & 14: Additional Topics in Algebra](/notes/ap/precalc/addtopics/)):

$$
1+\omega+\omega^2+\cdots+\omega^{n-1}
=\frac{1-\omega^n}{1-\omega}.
$$

Since $$\omega^n=1$$ and $$\omega\ne1$$,

$$
\frac{1-\omega^n}{1-\omega}
=\frac{1-1}{1-\omega}=0.
$$

Additionally, the product of the $$n$$th roots of unity is $$(-1)^{n+1}$$.

<div class="theorem-box">

**Extension.** Prove that the product of the $$n$$ roots of unity is $$(-1)^{n+1}$$. (Hint: Add their arguments, or compare the constant term of $$z^n-1$$ with the product of its roots.)

</div>

<div class="theorem-box">

**Example.** Let $$\omega=e^{2\pi i/7}$$. Without computing the six nonreal roots individually, find

$$
S=\sum_{k=1}^{6}\frac1{1-\omega^k},
\qquad
P=\prod_{k=1}^{6}\lvert1-\omega^k\rvert.
$$

Pair $$k$$ with $$7-k$$. Writing $$u=\omega^k$$, each pair contributes

$$
\frac1{1-u}+\frac1{1-u^{-1}}
=\frac1{1-u}-\frac{u}{1-u}=1.
$$

There are three pairs, so $$S=3$$. For the product, factor the polynomial whose roots are all seventh roots of unity except $$1$$:

$$
1+z+z^2+\cdots+z^6=\prod_{k=1}^{6}(z-\omega^k).
$$

Substituting $$z=1$$ gives $$\prod_{k=1}^{6}(1-\omega^k)=7$$. Taking moduli gives $$P=7$$. Geometrically, $$P$$ is the product of the six chord lengths from $$1$$ to the other vertices of the regular heptagon.

</div>

---

:::equations

| Topic | Equation and conditions |
|---|---|
| Law of Sines | $$\dfrac a{\sin A}=\dfrac b{\sin B}=\dfrac c{\sin C}=2R$$ for a nondegenerate triangle with circumradius $$R$$ |
| Triangle area | $$K=\frac12ab\sin C=\frac12bc\sin A=\frac12ac\sin B$$ |
| Law of Cosines | $$a^2=b^2+c^2-2bc\cos A$$, with cyclic versions for the other sides |
| Vector from points | $$\overrightarrow{PQ}=\langle x_Q-x_P,y_Q-y_P\rangle$$ |
| Vector magnitude and direction | $$\lvert\mathbf v\rvert=\sqrt{v_x^2+v_y^2}$$; $$\mathbf v=\langle\lvert\mathbf v\rvert\cos\theta,\lvert\mathbf v\rvert\sin\theta\rangle$$ |
| Unit vector | $$\widehat{\mathbf v}=\mathbf v/\lvert\mathbf v\rvert,\quad\mathbf v\ne\mathbf0$$ |
| Linear combination | $$a\mathbf u+b\mathbf v=\langle au_x+bv_x,au_y+bv_y\rangle$$ |
| Dot product | $$\mathbf A\cdot\mathbf B=A_xB_x+A_yB_y=\lvert\mathbf A\rvert\lvert\mathbf B\rvert\cos\theta$$ |
| Scalar and vector projection | $$\operatorname{comp}_{\mathbf B}\mathbf A=\dfrac{\mathbf A\cdot\mathbf B}{\lvert\mathbf B\rvert}$$; $$\operatorname{proj}_{\mathbf B}\mathbf A=\dfrac{\mathbf A\cdot\mathbf B}{\lvert\mathbf B\rvert^2}\mathbf B$$, $$\mathbf B\ne\mathbf0$$ |
| Parametric curve | $$x=f(t),\ y=g(t)$$; retain the allowed $$t$$ interval, branch restrictions, and orientation |
| Polar conversion | $$x=r\cos\theta,\ y=r\sin\theta,\ r^2=x^2+y^2$$; $$\tan\theta=y/x$$ when $$x\ne0$$, with quadrant checked |
| Equivalent polar points | $$(r,\theta)\equiv(r,\theta+2k\pi)\equiv(-r,\theta+(2k+1)\pi),\quad k\in\mathbb Z$$ |
| Counterclockwise rotation | Point: $$(r,\theta)\mapsto(r,\theta+\alpha)$$; curve: $$r=f(\theta-\alpha)$$ |
| Rectangular rotation | $$x'=x\cos\alpha-y\sin\alpha,\quad y'=x\sin\alpha+y\cos\alpha$$ |
| Polar distance | $$d^2=r_1^2+r_2^2-2r_1r_2\cos(\theta_2-\theta_1)$$, valid for signed radii |
| Circle and line in polar | Circle: $$a^2=r^2+r_0^2-2rr_0\cos(\theta-\theta_0)$$; line: $$r\cos(\theta-\alpha)=d$$ |
| Common polar curves | Spiral: $$r=a\theta$$; limaçon: $$r=a+b\cos\theta$$ or $$a+b\sin\theta$$; rose: $$r=a\cos(n\theta)$$ or $$a\sin(n\theta)$$ |
| Rose petals | Positive integer $$n$$: $$n$$ petals if odd, $$2n$$ if even; petal length $$\lvert a\rvert$$ for $$a\ne0$$ |
| Lemniscates | $$r^2=a^2\cos(2\theta)$$ or $$r^2=a^2\sin(2\theta)$$; the right side must be nonnegative |
| Complex forms | $$z=a+bi=r\operatorname{cis}\theta=re^{i\theta},\quad r=\sqrt{a^2+b^2}$$ |
| Complex multiplication/division | $$z_1z_2=r_1r_2\operatorname{cis}(\alpha+\beta)$$; $$z_1/z_2=(r_1/r_2)\operatorname{cis}(\alpha-\beta)$$, $$z_2\ne0$$ |
| De Moivre | $$(r\operatorname{cis}\theta)^n=r^n\operatorname{cis}(n\theta)$$, integer $$n$$; nonzero base for $$n\le0$$ |
| Complex roots | $$w_k=r^{1/n}\operatorname{cis}((\theta+2k\pi)/n)$$, $$k=0,\ldots,n-1$$, positive integer $$n$$ and $$r>0$$ |
| Roots of unity | $$\omega_k=e^{2\pi ik/n}$$; sum $$0$$ for $$n>1$$; product $$(-1)^{n+1}$$ |

:::

## Practice

::::problem
1. Solve the triangle with $$A=60^\circ$$, $$a=9$$ cm, and $$b=10$$ cm. Determine whether there are zero, one, or two possible triangles. For each valid triangle, find the remaining side and angles.

:::solution
By the Law of Sines,

$$
\frac{\sin B}{10}=\frac{\sin 60^\circ}{9},
$$

so

$$
\sin B=\frac{10\sin 60^\circ}{9}=\frac{5\sqrt3}{9}.
$$

This gives two possible angles:

$$
B\approx 74.2^\circ\quad \text{or}\quad B\approx 105.8^\circ.
$$

If $$B\approx 74.2^\circ$$, then

$$
C\approx 45.8^\circ,\qquad c\approx 7.45\text{ cm}.
$$

If $$B\approx 105.8^\circ$$, then

$$
C\approx 14.2^\circ,\qquad c\approx 2.55\text{ cm}.
$$

Therefore, there are **two possible triangles**.
:::
::::

::::problem
2. A plane is flying above the ocean. The angle of depression to a submarine's periscope at the ocean surface is $$24^\circ$$, and the angle of depression to a ship is $$17^\circ$$. The distance from the plane to the ship is $$5120$$ feet. The periscope and ship are in the same vertical plane and on the same side of the point directly below the airplane. Find their horizontal separation.

:::solution
```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\begin{tikzpicture}[>=Stealth, scale=0.95]
\coordinate (P) at (0,2);
\coordinate (U) at (4.49,0);
\coordinate (S) at (6.54,0);
\draw[blue!55] (-0.6,0) -- (7.3,0) node[right] {sea level};
\draw[dashed, gray!70] (P) -- (7,2);
\draw[dashed] (P) -- (0,0) node[midway, left] {$h$};
\draw[orange!85!black, thick] (P) -- (U);
\draw[blue, thick] (P) -- (S) node[pos=0.82, above right] {$5120$ ft};
\draw (0.9,2) arc (0:-17:0.9);
\node at (1.05,2.25) {$17^\circ$};
\draw (1.4,2) arc (0:-24:1.4);
\node at (1.55,1.08) {$24^\circ$};
\fill (P) circle (2pt) node[above left] {plane};
\fill (U) circle (2pt) node[below] {periscope};
\fill (S) circle (2pt) node[below] {ship};
\draw[<->] (4.49,-0.85) -- (6.54,-0.85) node[midway, below] {$d$};
\end{tikzpicture}
```

The plane-to-ship distance is $$5120$$ ft, and the angle of depression to the ship is $$17^\circ$$. So the plane's height is

$$
h=5120\sin 17^\circ\approx 1496.94\text{ ft}.
$$

The horizontal distance from the plane to the ship is

$$
5120\cos 17^\circ\approx 4896.28\text{ ft}.
$$

The horizontal distance from the plane to the submarine is

$$
\frac{h}{\tan 24^\circ}\approx 3362.19\text{ ft}.
$$

Assuming the ship and submarine are on the same side of the plane, their distance apart is

$$
4896.28-3362.19\approx 1534.09\text{ ft}.
$$
:::
::::

::::problem
3. Two towns $$A$$ and $$B$$ are $$1.4$$ miles apart, with $$B$$ due east of $$A$$. A signal is detected on a bearing of $$S22^\circ E$$ from $$A$$ and $$S43^\circ W$$ from $$B$$. Draw a labeled diagram and find the distance from each town to the signal.

:::solution
```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\begin{tikzpicture}[>=Stealth]
\coordinate (A) at (0,0);
\coordinate (B) at (4.2,0);
\coordinate (S) at (1.269,-3.141);
\draw[thick] (A) -- (B) node[midway, above] {$1.4$ miles (east)};
\draw[blue, thick] (A) -- (S);
\draw[red!75!black, thick] (B) -- (S);
\draw[dashed, gray!70, ->] (A) -- (0,-2.5) node[below] {S};
\draw[dashed, gray!70, ->] (B) -- (4.2,-2.5) node[below] {S};
\draw (0,-0.9) arc (-90:-68:0.9);
\node at (0.32,-1.65) {$22^\circ$};
\draw (4.2,-0.9) arc (-90:-133:0.9);
\node at (3.5,-1.35) {$43^\circ$};
\fill (A) circle (2pt) node[above left] {$A$};
\fill (B) circle (2pt) node[above right] {$B$};
\fill (S) circle (2pt) node[below] {signal};
\end{tikzpicture}
```

Place town $$A$$ at $$(0,0)$$ and town $$B$$ at $$(1.4,0)$$. The bearing $$S22^\circ E$$ from $$A$$ points down and right, while $$S43^\circ W$$ from $$B$$ points down and left.

Solving the two bearing lines gives the signal at approximately

$$
(0.423,-1.047).
$$

Therefore,

$$
AS\approx 1.13\text{ miles},\qquad BS\approx 1.43\text{ miles}.
$$
:::
::::

::::problem
4. Prove that for any triangle with side lengths $$a,b,c$$ and semiperimeter $$s=\frac12(a+b+c)$$, $$\sin^2\left(\frac C2\right)=\frac{(s-a)(s-b)}{ab}.$$

:::solution
Use the half-angle identity:

$$
\sin^2\left(\frac C2\right)=\frac{1-\cos C}{2}.
$$

By the Law of Cosines,

$$
\cos C=\frac{a^2+b^2-c^2}{2ab}.
$$

Substitute:

$$
\sin^2\left(\frac C2\right)
=\frac{1}{2}\left(1-\frac{a^2+b^2-c^2}{2ab}\right)
=\frac{c^2-(a-b)^2}{4ab}.
$$

Factor the numerator:

$$
c^2-(a-b)^2=(c-a+b)(c+a-b).
$$

Since $$s=\frac12(a+b+c)$$,

$$
c-a+b=2(s-a),\qquad c+a-b=2(s-b).
$$

Thus,

$$
\sin^2\left(\frac C2\right)=\frac{(s-a)(s-b)}{ab}.
$$
:::
::::

::::problem
5. Let $$\mathbf u=\langle -2,1\rangle$$ and $$\mathbf v=\langle -5,3\rangle$$.

    $$(A)$$ Find $$2\mathbf u-3\mathbf v$$.

    $$(B)$$ Find the angle between $$\mathbf u$$ and $$\mathbf v$$ to the nearest degree.

    $$(C)$$ Find a unit vector in the direction of $$\mathbf u+\mathbf v$$.

:::solution
We have

$$
\mathbf u=\langle -2,1\rangle,\qquad \mathbf v=\langle -5,3\rangle.
$$

For part (A),

$$
2\mathbf u-3\mathbf v
=\langle -4,2\rangle-\langle -15,9\rangle
=\langle 11,-7\rangle.
$$

For part (B),

$$
\mathbf u\cdot \mathbf v=(-2)(-5)+(1)(3)=13.
$$

Also,

$$
\lvert \mathbf u \rvert=\sqrt5,\qquad \lvert \mathbf v \rvert=\sqrt{34}.
$$

So

$$
\cos\theta=\frac{13}{\sqrt5\sqrt{34}}=\frac{13}{\sqrt{170}}.
$$

Therefore,

$$
\theta\approx 4^\circ.
$$

For part (C), since $$\mathbf u+\mathbf v=\langle -7,4\rangle$$, a unit vector in that direction is

$$
\frac{\langle -7,4\rangle}{\sqrt{65}}
=\left\langle \frac{-7}{\sqrt{65}},\frac{4}{\sqrt{65}}\right\rangle.
$$
:::
::::

::::problem
6. A plane is heading $$40^\circ$$ east of north at $$120$$ mph. A wind blows directly from the east at $$10$$ mph. Find the ground-speed vector, the ground speed, and the drift angle from the plane's intended heading.

:::solution
```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\begin{tikzpicture}[>=Stealth]
\draw[->, gray!70] (0,0) -- (4.2,0) node[right] {east};
\draw[->, gray!70] (0,0) -- (0,4.6) node[above] {north};
\draw[blue, very thick, ->] (0,0) -- (3.085,3.677) node[pos=0.62, right] {air velocity};
\draw[red!75!black, very thick, ->] (3.085,3.677) -- (2.685,3.677);
\node[red!75!black, above] at (2.9,3.95) {wind: $10$ mph west};
\draw[green!45!black, very thick, ->] (0,0) -- (2.685,3.677) node[pos=0.8, above left] {ground velocity};
\draw (0,0.8) arc (90:50:0.8);
\node at (0.4,1.25) {$40^\circ$};
\end{tikzpicture}
```

Let east be positive $$x$$ and north be positive $$y$$. A heading of $$40^\circ$$ east of north at $$120$$ mph has velocity

$$
\langle 120\sin40^\circ,120\cos40^\circ\rangle.
$$

A wind directly from the east blows west, so its vector is

$$
\langle -10,0\rangle.
$$

The ground-speed vector is

$$
\langle 120\sin40^\circ-10,120\cos40^\circ\rangle
\approx \langle 67.13,91.93\rangle.
$$

The ground speed is

$$
\sqrt{67.13^2+91.93^2}\approx 113.83\text{ mph}.
$$

The actual direction is about

$$
\tan^{-1}\left(\frac{67.13}{91.93}\right)\approx 36.1^\circ
$$

east of north. Since the intended heading was $$40^\circ$$ east of north, the drift angle is about $$40^\circ-36.1^\circ=3.9^\circ$$ west of the intended heading.
:::
::::

::::problem
7. A force of $$18$$ Newtons acts in the direction $$235^\circ$$ from the positive $$x$$-axis. Decompose the force into components and then find the magnitude and direction of the vector obtained by adding this force to $$\langle 12,-5\rangle$$.

:::solution
The force components are

$$
\langle 18\cos235^\circ,18\sin235^\circ\rangle
\approx \langle -10.32,-14.74\rangle.
$$

Add $$\langle 12,-5\rangle$$:

$$
\langle -10.32,-14.74\rangle+\langle 12,-5\rangle
\approx \langle 1.68,-19.74\rangle.
$$

The magnitude is

$$
\sqrt{1.68^2+(-19.74)^2}\approx 19.82.
$$

The direction angle is approximately

$$
274.9^\circ.
$$
:::
::::

::::problem
8. A particle moves according to $$x(t)=2\cos t-\sin(2t),\,y(t)=6\sin t,$$ for $$0\le t\le 2\pi$$.

    $$(A)$$ Find all exact $$x$$-intercepts.

    $$(B)$$ Find the particle's position when $$t=\frac{\pi}{2}$$ and when $$t=\frac{7\pi}{6}$$.

    $$(C)$$ Write a formula for the particle's distance from the origin as a function of $$t$$.

:::solution
The particle has

$$
x(t)=2\cos t-\sin(2t),\qquad y(t)=6\sin t.
$$

For part (A), use $$\sin(2t)=2\sin t\cos t$$:

$$
x(t)=2\cos t-2\sin t\cos t=2\cos t(1-\sin t).
$$

So $$x(t)=0$$ when $$\cos t=0\,\text{or}\,\sin t=1$$.

On $$0\le t\le 2\pi$$, this gives

$$
t=\frac{\pi}{2},\frac{3\pi}{2}.
$$

The exact $$x$$-intercepts are

$$
(0,6)\quad \text{and}\quad (0,-6).
$$

For part (B), when $$t=\frac{\pi}{2}$$,

$$
(x,y)=(0,6).
$$

When $$t=\frac{7\pi}{6}$$,

$$
x=2\cos\frac{7\pi}{6}-\sin\frac{7\pi}{3}
=-\sqrt3-\frac{\sqrt3}{2}
=-\frac{3\sqrt3}{2},
$$

and

$$
y=6\sin\frac{7\pi}{6}=-3.
$$

So the position is

$$
\left(-\frac{3\sqrt3}{2},-3\right).
$$

For part (C), the distance from the origin is

$$
d(t)=\sqrt{x(t)^2+y(t)^2}.
$$

Therefore,

$$
d(t)=\sqrt{(2\cos t-\sin(2t))^2+36\sin^2t}.
$$
:::
::::

::::problem
9. Eliminate the parameter and describe the curve, including any domain restrictions and orientation: $$x=e^t$$, $$y=e^{2t}-3$$, $$-\ln2\le t\le \ln3.$$

:::solution
Since $$x=e^t$$, we have

$$
t=\ln x.
$$

Then

$$
y=e^{2t}-3=(e^t)^2-3=x^2-3.
$$

Because

$$
-\ln2\le t\le \ln3,
$$

the domain is

$$
\frac12\le x\le 3.
$$

The curve is the parabola

$$
y=x^2-3
$$

restricted to $$\frac12\le x\le 3$$. As $$t$$ increases, $$x=e^t$$ increases, so the curve moves from

$$
\left(\frac12,-\frac{11}{4}\right)
$$

to

$$
(3,6).
$$
:::
::::

::::problem
10. The curve $$x=4\cos t$$, $$y=-2\sin t$$ is traced for $$0\le t\le 2\pi$$. Eliminate the parameter, state where the curve starts, and determine the direction (clockwise or counterclockwise) the curve is traced in.

:::solution
```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\begin{tikzpicture}[>=Stealth, scale=0.85]
\draw[->, gray!70] (-4.8,0) -- (5,0) node[right] {$x$};
\draw[->, gray!70] (0,-2.8) -- (0,3) node[above] {$y$};
\draw[blue, very thick] (0,0) ellipse (4 and 2);
\draw[blue, thick, ->] (4,0) arc (0:-30:4 and 2);
\draw[blue, thick, ->] (-4,0) arc (180:150:4 and 2);
\fill (4,0) circle (2pt) node[above right] {$(4,0)$: start};
\node[below left] at (-4,0) {$(-4,0)$};
\node[above right] at (0,2) {$(0,2)$};
\node[below right] at (0,-2) {$(0,-2)$};
\end{tikzpicture}
```

From $$x=4\cos t$$, we get

$$
\cos t=\frac{x}{4}.
$$

From $$y=-2\sin t$$, we get

$$
\sin t=-\frac{y}{2}.
$$

Using $$\cos^2t+\sin^2t=1$$,

$$
\frac{x^2}{16}+\frac{y^2}{4}=1.
$$

This is an ellipse. At $$t=0$$, the curve starts at

$$
(4,0).
$$

For small positive $$t$$, $$y=-2\sin t$$ is negative, so the curve moves downward from $$(4,0)$$. Therefore, the ellipse is traced **clockwise**.
:::
::::

::::problem
11. Classify each polar curve as a cardioid, limacon, rose curve, lemniscate, circle, line, or spiral. For rose curves, state the number of petals. Graph each of the curves.

    $$(A)$$ Graph $$r=3-3\sin\theta$$

    $$(B)$$ Graph $$r=2+5\cos\theta$$

    $$(C)$$ Graph $$r=4\sin(3\theta)$$

    $$(D)$$ Graph $$r^2=25\sin(2\theta)$$

:::solution
$$(A)$$ The curve

$$
r=3-3\sin\theta
$$

is a cardioid because it has the form $$r=a-a\sin\theta$$. It opens downward and has a cusp at the pole when $$\theta=\frac{\pi}{2}$$.

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{tikzpicture}
\begin{axis}[
  axis lines=middle, axis equal image,
  xmin=-6.5, xmax=6.5, ymin=-6.5, ymax=2,
  xtick={-6,-3,0,3,6}, ytick={-6,-3,0},
  grid=both, grid style={gray!18},
  width=8.5cm, height=7cm,
  xlabel=$x$, ylabel=$y$,
]
\addplot[blue, very thick, samples=360, domain=0:360]
  ({(3-3*sin(x))*cos(x)}, {(3-3*sin(x))*sin(x)});
\addplot[only marks, mark=*, mark size=1.6pt, orange!85!black] coordinates {(0,0) (0,-6)};
\end{axis}
\end{tikzpicture}
```

$$(B)$$ The curve

$$
r=2+5\cos\theta
$$

is a limacon with an inner loop because $$\lvert 2\rvert<\lvert 5\rvert$$. It is symmetric about the polar axis.

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{tikzpicture}
\begin{axis}[
  axis lines=middle, axis equal image,
  xmin=-4, xmax=7.5, ymin=-4.5, ymax=4.5,
  xtick={-4,-2,0,2,4,6}, ytick={-4,-2,0,2,4},
  grid=both, grid style={gray!18},
  width=8.5cm, height=7cm,
  xlabel=$x$, ylabel=$y$,
]
\addplot[blue, very thick, samples=500, domain=0:360]
  ({(2+5*cos(x))*cos(x)}, {(2+5*cos(x))*sin(x)});
\addplot[only marks, mark=*, mark size=1.6pt, orange!85!black] coordinates {(7,0)};
\end{axis}
\end{tikzpicture}
```

$$(C)$$ The curve

$$
r=4\sin(3\theta)
$$

is a rose curve. Since $$3$$ is odd, it has $$3$$ petals.

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{tikzpicture}
\begin{axis}[
  axis lines=middle, axis equal image,
  xmin=-4.5, xmax=4.5, ymin=-4.5, ymax=4.5,
  xtick={-4,-2,0,2,4}, ytick={-4,-2,0,2,4},
  grid=both, grid style={gray!18},
  width=8cm, height=8cm,
  xlabel=$x$, ylabel=$y$,
]
\addplot[blue, very thick, samples=600, domain=0:360]
  ({(4*sin(3*x))*cos(x)}, {(4*sin(3*x))*sin(x)});
\end{axis}
\end{tikzpicture}
```

$$(D)$$ The curve

$$
r^2=25\sin(2\theta)
$$

is a lemniscate. Since $$\sin(2\theta)\ge0$$ in Quadrants I and III, its two loops lie along the line $$y=x$$.

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{tikzpicture}
\begin{axis}[
  axis lines=middle, axis equal image,
  xmin=-4.5, xmax=4.5, ymin=-4.5, ymax=4.5,
  xtick={-4,-2,0,2,4}, ytick={-4,-2,0,2,4},
  grid=both, grid style={gray!18},
  width=8cm, height=8cm,
  xlabel=$x$, ylabel=$y$,
]
\addplot[blue, very thick, samples=240, domain=0:90]
  ({sqrt(25*sin(2*x))*cos(x)}, {sqrt(25*sin(2*x))*sin(x)});
\addplot[blue, very thick, samples=240, domain=180:270]
  ({sqrt(25*sin(2*x))*cos(x)}, {sqrt(25*sin(2*x))*sin(x)});
\end{axis}
\end{tikzpicture}
```
:::
::::

::::problem
12. Graph both $$r=2+2\cos\theta$$ and $$r=2-2\cos\theta$$. Then, find the number of intersection points.

:::solution
The curves are $$r=2+2\cos\theta$$ and $$r=2-2\cos\theta$$.

Both are cardioids. The first opens to the right, and the second opens to the left.

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{tikzpicture}
\begin{axis}[
  axis lines=middle, axis equal image,
  xmin=-4.5, xmax=4.5, ymin=-3, ymax=3,
  xtick={-4,-2,0,2,4}, ytick={-2,0,2},
  grid=both, grid style={gray!18},
  width=8.8cm, height=6.5cm,
  xlabel=$x$, ylabel=$y$,
]
\addplot[blue, very thick, samples=360, domain=0:360]
  ({(2+2*cos(x))*cos(x)}, {(2+2*cos(x))*sin(x)});
\addplot[red!75!black, very thick, samples=360, domain=0:360]
  ({(2-2*cos(x))*cos(x)}, {(2-2*cos(x))*sin(x)});
\addplot[only marks, mark=*, mark size=1.6pt, orange!85!black] coordinates {(0,2) (0,-2) (0,0)};
\end{axis}
\end{tikzpicture}
```

To find intersections with the same angle, set the equations equal:

$$
2+2\cos\theta=2-2\cos\theta.
$$

Then

$$
4\cos\theta=0,
$$

so

$$
\cos\theta=0.
$$

Thus,

$$
\theta=\frac{\pi}{2},\frac{3\pi}{2}.
$$

These give the points

$$
(0,2)\quad \text{and}\quad (0,-2).
$$

Both cardioids also pass through the pole: $$r=0$$ for the first curve when $$\theta=\pi$$, and $$r=0$$ for the second curve when $$\theta=0$$. Therefore, the curves have

$$
\boxed{3}
$$

intersection points.
:::
::::

::::problem
13. Martina and Carl are part of a team that is studying weather patterns.
  The team is about to launch a weather balloon to collect data. Martina’s
  rope is $$7.8$$ meters long and makes an angle of $$36.0\circ$$ with the ground. Carl’s rope
  is $$5.9$$ meters long. Assuming that Martina and Carl form a triangle in a vertical
  plane with the weather balloon, what is the distance between Martina and
  Carl, to the nearest tenth of a meter?
:::solution
```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\begin{tikzpicture}[>=Stealth]
\coordinate (M) at (0,0);
\coordinate (B) at (3.47,2.52);
\coordinate (C1) at (1.43,0);
\coordinate (C2) at (5.51,0);
\draw[gray!70] (-0.3,0) -- (6.3,0);
\draw[blue, thick] (M) -- (B) node[midway, above left] {$7.8$ m};
\draw[orange!85!black, thick, dashed] (B) -- (C1) node[pos=0.65, right] {$5.9$ m};
\draw[green!45!black, thick] (B) -- (C2) node[midway, above right] {$5.9$ m};
\draw (0.8,0) arc (0:36:0.8);
\node at (1.05,0.3) {$36^\circ$};
\fill (M) circle (2pt) node[below] {Martina};
\fill (B) circle (2pt) node[above] {balloon};
\fill (C1) circle (2pt) node[below] {$C_1$};
\fill (C2) circle (2pt) node[below] {$C_2$};
\node at (3,-0.85) {Two possible positions for Carl};
\end{tikzpicture}
```

Let $$d$$ be the distance between Martina and Carl. The triangle has one side of length $$7.8$$ m, one side of length $$5.9$$ m, and the angle at Martina is $$36.0^\circ$$. By the Law of Cosines,

$$
5.9^2=7.8^2+d^2-2(7.8)(d)\cos(36.0^\circ).
$$

Move everything to one side:

$$
d^2-15.6\cos(36.0^\circ)d+(7.8^2-5.9^2)=0.
$$

Using $$\cos(36.0^\circ)\approx0.8090$$,

$$
d^2-12.6207d+25.03=0.
$$

Apply the quadratic formula:

$$
d=\frac{12.6207\pm\sqrt{12.6207^2-4(25.03)}}{2}.
$$

This gives

$$
d\approx10.0
\qquad\text{or}\qquad
d\approx2.6.
$$

So there are two possible distances unless the diagram or context says which side Carl is on:

$$
\boxed{10.0\text{ m or }2.6\text{ m}}.
$$
:::
::::

::::problem
14. Let $$z_1=-2+2\sqrt3i,\,z_2=1-i.$$

    $$(A)$$ Write both numbers in polar form.

    $$(B)$$ Write both numbers in exponential form.

    $$(C)$$ Compute $$z_1z_2$$ in polar form and rectangular form.

:::solution
For part (A), for $$z_1=-2+2\sqrt3i$$, the magnitude is

$$
\lvert z_1 \rvert=\sqrt{(-2)^2+(2\sqrt3)^2}=4.
$$

Since $$z_1$$ is in Quadrant II, $$\theta_1=120^\circ=\frac{2\pi}{3}$$.

So

$$
z_1=4\left(\cos\frac{2\pi}{3}+i\sin\frac{2\pi}{3}\right).
$$

For $$z_2=1-i$$, the magnitude is $$\sqrt2$$ and the angle is $$-45^\circ=-\frac{\pi}{4}$$. So

$$
z_2=\sqrt2\left(\cos\left(-\frac{\pi}{4}\right)+i\sin\left(-\frac{\pi}{4}\right)\right).
$$

For part (B), in exponential form,

$$
z_1=4e^{2\pi i/3},\qquad z_2=\sqrt2e^{-\pi i/4}.
$$

For part (C), multiply magnitudes and add angles:

$$
z_1z_2=4\sqrt2e^{i(2\pi/3-\pi/4)}=4\sqrt2e^{5\pi i/12}.
$$

In polar form,

$$
z_1z_2=4\sqrt2\left(\cos\frac{5\pi}{12}+i\sin\frac{5\pi}{12}\right).
$$

In rectangular form,

$$
z_1z_2=(2\sqrt3-2)+(2\sqrt3+2)i.
$$
:::
::::

::::problem
15. Solve $$(z-(1-i))^4=16\left(\cos\frac{2\pi}{3}+i\sin\frac{2\pi}{3}\right)$$. Give every solution in rectangular form, find their sum and product, and identify the solution with greatest real part.

:::solution
First set $$w=z-(1-i)$$. The equation for $$w$$ has right side

$$
16\left(\cos\frac{2\pi}{3}+i\sin\frac{2\pi}{3}\right).
$$

The fourth roots have magnitude

$$
\sqrt[4]{16}=2.
$$

Their angles are

$$
\frac{\frac{2\pi}{3}+2\pi k}{4}
=\frac{\pi}{6}+\frac{k\pi}{2},
$$

where $$k=0,1,2,3$$. Therefore the roots are

$$
2\operatorname{cis}\frac{\pi}{6},\quad
2\operatorname{cis}\frac{2\pi}{3},\quad
2\operatorname{cis}\frac{7\pi}{6},\quad
2\operatorname{cis}\frac{5\pi}{3}.
$$

In rectangular form, these are

$$
\sqrt3+i,\quad -1+\sqrt3i,\quad -\sqrt3-i,\quad 1-\sqrt3i.
$$

Add $$1-i$$ to each value to recover the four solutions:

$$
z=1+\sqrt3,\quad (\sqrt3-1)i,\quad
1-\sqrt3-2i,\quad 2-(1+\sqrt3)i.
$$

Their sum is $$4(1-i)=4-4i$$, since the four unshifted roots sum to zero. Their product is the constant term of the monic polynomial $$(z-(1-i))^4-16\operatorname{cis}(2\pi/3)$$:

$$
\prod z_k=(1-i)^4-16\operatorname{cis}\frac{2\pi}{3}
=-4-(-8+8\sqrt3i)=4-8\sqrt3i.
$$

The largest real part is $$1+\sqrt3$$, attained by the real solution $$z=1+\sqrt3$$.
:::
::::

::::problem
16. (Bonus, Brahmagupta's and Bretschneider's formulas)

Let $$ABCD$$ be a cyclic quadrilateral, meaning all four vertices lie on one circle. Let its side lengths be $$a,b,c,d$$, and let its semiperimeter be $$s=\frac12(a+b+c+d)$$.

The goal is to prove the area of a cyclic quadrilateral is:

$$
K=\sqrt{(s-a)(s-b)(s-c)(s-d)},
$$

where $$K$$ is the area of the cyclic quadrilateral. We will also extend the area formula to all cases, not just cyclic ones.

<div style="margin-left: 1.5rem;">

$$(A)$$ Draw diagonal $$AC$$. Let $$\angle ABC=B$$ and $$\angle ADC=D$$. Use triangle area formulas and $$D=180^\circ-B$$ (A property of cyclic quadrilaterals) to rewrite the area as $$K=\frac12(ab+cd)\sin B.$$

$$(B)$$ Apply the Law of Cosines to triangles $$ABC$$ and $$ADC$$ to show that $$2ab\cos B=a^2+b^2-c^2-d^2+2cd\cos D.$$

$$(C)$$ Use $$\cos D=-\cos B$$ to solve for $$\cos B$$, then combine this with $$K=\frac12(ab+cd)\sin B$$ and $$\sin^2B=1-\cos^2B$$ to prove $$K^2=(s-a)(s-b)(s-c)(s-d).$$ This is Brahmagupta's formula.

$$(D)$$ Now suppose $$ABCD$$ is not necessarily cyclic. Keep the same notation, with opposite angles $$B$$ and $$D$$. Show that $$(4K)^2+(a^2+b^2-c^2-d^2)^2=4(a^2b^2+c^2d^2-2abcd\cos(B+D)).$$

$$(E)$$ Now prove **Bretschneider's formula**: $$K^2=(s-a)(s-b)(s-c)(s-d)-abcd\cos^2\left(\frac{B+D}{2}\right).$$

$$(F)$$ Explain why Bretschneider's formula turns into Brahmagupta's formula when $$ABCD$$ is cyclic.

</div>

:::solution
For part (A), draw diagonal $$AC$$. The diagonal splits the quadrilateral into triangles $$ABC$$ and $$ADC$$. Using $$K=\frac12ab\sin C$$ for triangle area, $$[ABC]=\frac12ab\sin B$$ and $$[ADC]=\frac12cd\sin D$$.

Therefore,

$$
K=\frac12ab\sin B+\frac12cd\sin D.
$$

Since $$ABCD$$ is cyclic, opposite angles are supplementary:

$$
B+D=180^\circ.
$$

So $$D=180^\circ-B$$ and $$\sin D=\sin(180^\circ-B)=\sin B$$.

Therefore,

$$
K=\frac12ab\sin B+\frac12cd\sin B
=\frac12(ab+cd)\sin B.
$$

For part (B), apply the Law of Cosines to triangle $$ABC$$:

$$
AC^2=a^2+b^2-2ab\cos B.
$$

Apply the Law of Cosines to triangle $$ADC$$:

$$
AC^2=c^2+d^2-2cd\cos D.
$$

Set these equal:

$$
a^2+b^2-2ab\cos B=c^2+d^2-2cd\cos D.
$$

Rearranging gives

$$
2ab\cos B=a^2+b^2-c^2-d^2+2cd\cos D.
$$

For part (C), since $$D=180^\circ-B$$, $$\cos D=-\cos B$$.

Substitute into the result from part $$(C)$$:

$$
2ab\cos B=a^2+b^2-c^2-d^2-2cd\cos B.
$$

So

$$
2(ab+cd)\cos B=a^2+b^2-c^2-d^2,
$$

and

$$
\cos B=\frac{a^2+b^2-c^2-d^2}{2(ab+cd)}.
$$

From part $$(B)$$,

$$
K=\frac12(ab+cd)\sin B.
$$

Square both sides:

$$
K^2=\frac14(ab+cd)^2\sin^2B.
$$

Use $$\sin^2B=1-\cos^2B$$:

$$
K^2=\frac14(ab+cd)^2\left(1-\left(\frac{a^2+b^2-c^2-d^2}{2(ab+cd)}\right)^2\right).
$$

Simplifying gives

$$
K^2=\frac{4(ab+cd)^2-(a^2+b^2-c^2-d^2)^2}{16}.
$$

This factors as

$$
K^2=\frac{(a+b+c-d)(a+b-c+d)(a-b+c+d)(-a+b+c+d)}{16}.
$$

Since

$$
s=\frac12(a+b+c+d),
$$

the four factors are

$$
2(s-d),\quad 2(s-c),\quad 2(s-b),\quad 2(s-a).
$$

Therefore,

$$
K^2=(s-a)(s-b)(s-c)(s-d),
$$

so

$$
K=\sqrt{(s-a)(s-b)(s-c)(s-d)}.
$$

For part (D), for a general quadrilateral, the area is still

$$
K=\frac12ab\sin B+\frac12cd\sin D,
$$

so

$$
4K=2ab\sin B+2cd\sin D.
$$

Also, using the shared diagonal $$AC$$ again,

$$
a^2+b^2-2ab\cos B=c^2+d^2-2cd\cos D.
$$

Thus,

$$
a^2+b^2-c^2-d^2=2ab\cos B-2cd\cos D.
$$

Now compute

$$
(4K)^2+(a^2+b^2-c^2-d^2)^2.
$$

Substitute the two expressions above:

$$
(2ab\sin B+2cd\sin D)^2+(2ab\cos B-2cd\cos D)^2.
$$

Expand:

$$
4a^2b^2\sin^2B+8abcd\sin B\sin D+4c^2d^2\sin^2D
$$

$$
+4a^2b^2\cos^2B-8abcd\cos B\cos D+4c^2d^2\cos^2D.
$$

Group terms:

$$
4a^2b^2(\sin^2B+\cos^2B)+4c^2d^2(\sin^2D+\cos^2D)
$$

$$
+8abcd(\sin B\sin D-\cos B\cos D).
$$

Since

$$
\sin^2x+\cos^2x=1
$$

and

$$
\cos(B+D)=\cos B\cos D-\sin B\sin D,
$$

this becomes

$$
4a^2b^2+4c^2d^2-8abcd\cos(B+D).
$$

Therefore,

$$
(4K)^2+(a^2+b^2-c^2-d^2)^2=4(a^2b^2+c^2d^2-2abcd\cos(B+D)).
$$

For part (E), rearrange the result from part (D):

$$
16K^2=4(a^2b^2+c^2d^2-2abcd\cos(B+D))-(a^2+b^2-c^2-d^2)^2.
$$

Use $$\cos(B+D)=2\cos^2\left(\frac{B+D}{2}\right)-1$$.

Then

$$
-2abcd\cos(B+D)
=-4abcd\cos^2\left(\frac{B+D}{2}\right)+2abcd.
$$

So

$$
16K^2=4(a^2b^2+c^2d^2+2abcd)-(a^2+b^2-c^2-d^2)^2
$$

$$
-16abcd\cos^2\left(\frac{B+D}{2}\right).
$$

Since $$4(a^2b^2+c^2d^2+2abcd)=4(ab+cd)^2$$, we get

$$
16K^2=4(ab+cd)^2-(a^2+b^2-c^2-d^2)^2
-16abcd\cos^2\left(\frac{B+D}{2}\right).
$$

From part $$(D)$$, the first two terms factor as

$$
16(s-a)(s-b)(s-c)(s-d).
$$

Therefore,

$$
16K^2=16(s-a)(s-b)(s-c)(s-d)
-16abcd\cos^2\left(\frac{B+D}{2}\right).
$$

Divide by $$16$$:

$$
K^2=(s-a)(s-b)(s-c)(s-d)-abcd\cos^2\left(\frac{B+D}{2}\right).
$$

This is Bretschneider's formula.

For part (F), if $$ABCD$$ is cyclic, then opposite angles are supplementary: $$B+D=180^\circ$$.

Thus,

$$
\frac{B+D}{2}=90^\circ,
$$

so

$$
\cos^2\left(\frac{B+D}{2}\right)=\cos^2(90^\circ)=0.
$$

Bretschneider's formula becomes

$$
K^2=(s-a)(s-b)(s-c)(s-d),
$$

which is Brahmagupta's formula.
:::
::::
