function [concentration] = concentration(m,n,m_source,n_source)
    diffusion_coeff = 0.360; % mm^2/hr from Fronteirs of oncology paper
    decay = 0.65;            %/hr from Fronteirs of oncology paper
    step_size = .02;         % mm from Fronteirs of oncology paper
    production = 20;         % pg/mm^3 hr Journal of Biological Engineering paper
    radius = (pdist([m n;m_source n_source]))*step_size;
    concentration = (production/(2*(diffusion_coeff*decay)^0.5))*(exp(-((decay/diffusion_coeff)^0.5)*radius)); 
    % concentration in pg/mm3
end

          
    
