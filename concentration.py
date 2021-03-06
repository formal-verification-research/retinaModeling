from scipy import spatial
import math


def concentration(m, n, m_source, n_source):
    diffusion_coeff = 0.360                  # mm ^ 2/hr from Fronteirs of oncology paper
    decay = 0.65                             # /hr from Fronteirs of oncology paper
    step_size = .02                          # mm from Fronteirs of oncology paper
    production = 20 * 0.02                   # pg / mm ^ 2 hr Journal of Biological Engineering paper
    radius = spatial.distance.euclidean((m, n), (m_source, n_source))*step_size
    concentration = (production / (2 * ((diffusion_coeff * decay) ** 0.5))) * \
                    (math.exp(-((decay / diffusion_coeff) ** 0.5) * radius))      # concentration in pg / mm3
    return concentration

