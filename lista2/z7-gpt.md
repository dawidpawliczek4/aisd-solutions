First, observe that for any three vertices $x,y,z$ in a tree $T$, the number of edges in the union of the three pairwise paths

$$
P(x,y)\;\cup\;P(y,z)\;\cup\;P(z,x)
$$

is

$$
\bigl|E\bigl(P(x,y)\cup P(y,z)\cup P(z,x)\bigr)\bigr|
\;=\;\frac{d(x,y)+d(y,z)+d(z,x)}2,
$$

where $d(u,v)$ is the distance (number of edges) between $u$ and $v$.  Indeed, one shows easily that each edge in the minimal subtree spanning $\{x,y,z\}$ is counted exactly twice in the sum $d(x,y)+d(y,z)+d(z,x)$, so the union has half that many edges.

Hence choosing $(a_1,a_2,a_3)$ to maximize the size of

$$
E' \;=\;E\bigl(P(a_1,a_2)\cup P(a_2,a_3)\cup P(a_3,a_1)\bigr)
$$

is equivalent to choosing them to maximize

$$
S \;=\;d(a_1,a_2)\;+\;d(a_2,a_3)\;+\;d(a_3,a_1).
$$

---

### 1. Let $D$ be the diameter length of $T$, with endpoints $u,v$.

By definition, $d(u,v)=D$ and no pair of vertices is farther apart.  We will show that in any triple $(a_1,a_2,a_3)$ maximizing
$\;S=d(a_1,a_2)+d(a_2,a_3)+d(a_3,a_1)$, at least one of the three distances $d(a_i,a_j)$ must already equal $D$; that is, one of the three unordered pairs $\{a_i,a_j\}$ is a diameter.

---

### 2. Pick the “farthest‐apart” pair among the triple.

Without loss of generality, relabel so that

$$
d(a_1,a_2)\;\ge\;d(a_2,a_3)\quad\text{and}\quad d(a_1,a_2)\;\ge\;d(a_3,a_1).
$$

Set

$$
M \;:=\;d(a_1,a_2).
$$

We claim $M=D$.  Suppose, for contradiction, that

$$
M \;<\;D.
$$

Then the path $P(a_1,a_2)$ is strictly shorter than the diameter path $P(u,v)$; in particular, at least one of the diameter‐endpoints, say $u$, lies off $P(a_1,a_2)$ and attaches to it at some positive distance
$\delta>0$.  Concretely, one shows in any tree that

$$
d(a_1,u)+d(a_2,u)
\;=\;d(a_1,a_2)\;+\;2\,d\bigl(u,\;P(a_1,a_2)\bigr)
\;=\;M \;+\;2\delta
\;>\;M.
$$

On the other hand, by choice of $(a_1,a_2)$ as the farthest pair,

$$
d(a_1,a_3)\;\le\;M,
\qquad
d(a_2,a_3)\;\le\;M,
$$

so

$$
d(a_1,a_3)+d(a_2,a_3)\;\le\;M+M\;=\;2M.
$$

Putting these together,

$$
d(a_1,u)+d(a_2,u)
\;=\;M+2\delta
\;>\;M \;+\;(d(a_1,a_3)+d(a_2,a_3))\;-\;M
\;=\;d(a_1,a_3)+d(a_2,a_3),
$$

so that if we replace $a_3$ by $u$ in our triple, the new sum of pairwise distances becomes

$$
S' \;=\;d(a_1,a_2)\;+\;d(a_1,u)\;+\;d(a_2,u)
\;>\;d(a_1,a_2)\;+\;d(a_1,a_3)\;+\;d(a_2,a_3)
\;=\;S,
$$

contradicting maximality of $S$.  Thus our assumption $M<D$ was impossible, and we must have

$$
d(a_1,a_2)\;=\;D.
$$

---

### 3. Conclusion.

We have shown that among the chosen triple $\{a_1,a_2,a_3\}$, the pair $\{a_1,a_2\}$ realizes distance $D$.  But that means $a_1$ and $a_2$ are **endpoints of a diameter** of $T$.  In particular, **at least two** of the vertices $a_1,a_2,a_3$ lie at distance exactly $D$ from each other, i.e.\ are diameter‐endpoints, as was to be proved.
