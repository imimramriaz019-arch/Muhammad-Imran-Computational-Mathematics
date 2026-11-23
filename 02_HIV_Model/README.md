# Fractional HIV/AIDS Model with Vaccination and Treatment

**Author:** M Imran Riaz
**Affiliation:** BS Mathematics, University of Education Lahore, Vehari Campus, Pakistan
**Email:** imimramriaz019@gmail.com

## About This Work
This is my own extension of the model proposed by Awais et al. (2026) in
*Computational Biology and Chemistry*, 120, 108748.

**Original Model (Awais et al.):** S - I1 - I2 - A

**My Extension (This Work):** S - V - I1 - I2 - A

I added a Vaccinated compartment (V) with vaccination rate `p` and waning immunity rate `w`, to study how vaccination controls HIV/AIDS.

## Compartments
- **S:** Susceptible
- **V:** Vaccinated (My Contribution)
- **I1:** Acute Infected
- **I2:** Asymptomatic Infected
- **A:** AIDS Stage

## My Model Equations
where lam = (beta1*I1 + beta2*I2) / N

## My Parameters
| Parameter | Value | Meaning |
| --- | --- | --- |
| Lambda | 0.31 | Recruitment rate |
| beta1 | 0.0000009 | Transmission S - I1 |
| beta2 | 0.00000027 | Transmission S - I2 |
| mu | 0.1 | Natural death |
| nu | 0.01 | Treatment I2 -> I1 |
| alpha | 0.2 | Progression I1 -> I2 |
| gamma | 0.1 | Progression I2 -> A |
| delta | 0.1 | AIDS death |
| p | 0.15 | Vaccination rate - My Work |
| w | 0.02 | Waning immunity - My Work |
| epsilon | 0.3 | Vaccine efficacy - My Work |

## My Main Results
1. **Positivity and Boundedness:** All solutions remain positive and bounded by Lambda/mu.
2. **Disease-Free Equilibrium:** E0 = (S0, V0, 0, 0, 0)
3. **Basic Reproduction Number R0:** Calculated by Next-Generation Matrix Method.
   - R0 without vaccination > R0 with vaccination
   - Vaccination reduces R0
4. **Local Stability:** DFE is locally asymptotically stable if R0 < 1 (Routh-Hurwitz Criterion).
5. **Global Stability:** Proved by Lyapunov Function.
6. **Sensitivity Analysis:** R0 is most sensitive to p, beta1, beta2.

## My Conclusion
Vaccination is an effective control strategy for HIV/AIDS. Increasing vaccination coverage p decreases R0 below 1, which leads to disease elimination.

## Files in This Folder
- `hiv_vaccination_model.py` - Complete Python Code + Simulation + Graph
- `README.md` - This file

## How to Run
```bash
python hiv_vaccination_model.py
## References

1. Awais, M., Nawaz, T., Ali, A.S., Ahmed, I. (2026). Numerical approximation of fractional order HIV/AIDS model with treatment using Levenberg-Marquardt backpropagation approach. *Computational Biology and Chemistry*, 120, 108748.

2. Van den Driessche, P., & Watmough, J. (2002). Reproduction numbers and sub-threshold endemic equilibria for compartmental models of disease transmission. *Mathematical Biosciences*, 180(1-2), 29-48.

3. Podlubny, I. (1998). *Fractional Differential Equations*. Academic Press.

4. Diekmann, O., Heesterbeek, J. A. P., & Metz, J. A. (1990). On the definition and the computation of the basic reproduction ratio R0 in models for infectious diseases in heterogeneous populations. *Journal of Mathematical Biology*, 28(4), 365-382.
02_HIV_Model/REFERENCES.bib
@article{awais2026hiv,
  title={Numerical approximation of fractional order HIV/AIDS model with treatment using Levenberg-Marquardt backpropagation approach},
  author={Awais, M. and Nawaz, T. and Ali, A.S. and Ahmed, I.},
  journal={Computational Biology and Chemistry},
  volume={120},
  pages={108748},
  year={2026}
}

@article{vandendriessche2002,
  title={Reproduction numbers and sub-threshold endemic equilibria for compartmental models of disease transmission},
  author={Van den Driessche, P. and Watmough, J.},
  journal={Mathematical Biosciences},
  volume={180},
  pages={29--48},
  year={2002}
}

@book{podlubny1998,
  title={Fractional Differential Equations},
  author={Podlubny, I.},
  publisher={Academic Press},
  year={1998}
}
