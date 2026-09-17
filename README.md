# Mathematics recovered from nested archives

A second archive sweep opened ZIP files stored inside other ZIP files. This layer contained mathematical material that a top-level file scan could not see.

## Audit

| | count |
|---|---:|
| outer ZIP files | 907 |
| containers holding inner archives | **98** |
| inner archives found | 343 |
| inner archives opened | **253** |
| deduplicated non-excluded archives read in full | 157 |
| archives containing mathematics | **134** |
| text members decompressed | 17,346 |
| claim-shaped statements extracted | 25,612 |

## Recomputed finite results

### Integral four-point configuration

The points

```text
(-12,0), (12,0), (0,5), (0,-9)
```

have pairwise distances

```text
24, 13, 15, 13, 15, 14
```

with no three collinear and no four concyclic.

### Regular polygons

A regular `n`-gon has exactly

\[
\left\lfloor n/2\right\rfloor
\]

distinct distances. This was recomputed for `n=3,...,64`; the general formula is elementary from the chord lengths.

### Powerful-number examples

Within the tested ranges:

```text
n! + 1 powerful, 2<=n<=7     : n = 4,5,7
2^n + 1 powerful, 2<=n<=11   : n = 3
2^n - 1 powerful, 2<=n<=11   : none
```

### Binomial divisibility

Exact checks recover large witnesses such as `n=2480` and `n=3478` for a consecutive-factor divisibility condition. The focused Kummer-based program is published in [`erdos396-binomial-divisibility`](https://github.com/jaredwilder/erdos396-binomial-divisibility).

### Totient equality family

For every odd prime `p`, with `n=p-1`, the least `m` satisfying `n|φ(m)` and the least prime congruent to 1 modulo `n` both equal `p`:

\[
m_{p-1}=p_{p-1}=p.
\]

### Mian–Chowla correction

Recomputation from the greedy definition gives

```text
1,2,3,5,8,13,21,30,39,53,74,95,128,152,...
```

so the thirteenth term is `128`, correcting two conflicting values found in the archived material.

## Major theorem packages recovered

The nested layer also contained substantial work now promoted to focused repositories:

- exact positional-encoding thresholds and sparse encoding — [`positional-encoding-thresholds`](https://github.com/jaredwilder/positional-encoding-thresholds);
- Turán `(3,4)` density identities — [`erdos500-turan34`](https://github.com/jaredwilder/erdos500-turan34);
- Stanley-sequence reflection multiplicity — [`erdos271-stanley-sequences`](https://github.com/jaredwilder/erdos271-stanley-sequences);
- integer quadratic tiling obstruction and other compact theorems — [`erdos-proved-lemmas`](https://github.com/jaredwilder/erdos-proved-lemmas);
- Erdős–Gyárfás structural lemmas — [`erdos-gyarfas-power-of-two-cycles`](https://github.com/jaredwilder/erdos-gyarfas-power-of-two-cycles).

## Verification

```bash
python verify.py
```

The verifier reproduces the finite checks included in this recovery layer.

## Purpose of this repository

This repository is a source-discovery record for mathematics found below the first archive level. The mathematical subjects themselves should be read and cited from their focused repositories when one exists.

Author: Jared Wilder. License: Apache-2.0.
