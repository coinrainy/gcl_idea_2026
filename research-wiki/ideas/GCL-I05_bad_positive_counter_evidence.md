# GCL-I05: Bad Positive Views as Masked Counter-Evidence

- Stage: Stage 2A
- Status: KILL
- Primary gap: G1 + G3
- Closest works: GCA, G-Censor, GraphMAE2, MaskGAE, CORE/GCMAE
- Reviewer verdict: KILL

## Summary

Low-consistency augmentations become masked latent prediction targets rather than positives.

## Kill Reason

Reviewer judged this too close to module fusion: GCA/G-Censor view failure plus GraphMAE2/MaskGAE masking. The mechanism is not yet necessary or distinct.

## Future Avoidance

Do not regenerate as a main idea. It may appear only as an ablation inside GCL-I01 if failure-driven masks are tested against random and adaptive masks.
