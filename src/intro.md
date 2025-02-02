# MRI acquisition & image reconstruction tutorial

This repository contains code and slides that were initially presented at ISBI'19 in Venice during the tutorial entitled: "Recent advances in acquisition and reconstruction for Compressed Sensing MRI". The code focuses on basics and recent advances in MR acquisition or design of k-space sampling schemes. Then the code has been progressively extended for the 2022 IEEE Biomedical Imaging summer school that held in St Jacut de la Mer in June 2022. Even more recently, in 2024, I started to use MRI-NUFFT to illustrate multiple 2D and 3D non-Cartesian trajectories with density compensated adjoint Non-Unform Fast Fourier transform (NUFFT) reconstruction.   
The aspects related to MRI reconstruction in the ISBI'19 tutorial were taught by [Prof. Jeff Fessler](https://github.com/JeffFessler/MIRT.jl) with code and examples in [Julia](https://julialang.org/) language.




You can find some ipython Notebooks in the [Python](https://github.com/philouc/mri_acq_recon_tutorial/tree/master/python) folder. Note that we illustrate both Cartesian and non-Cartesian sampling, regular~(i.e. periodic or contiguous) and irregular undersampling. Irregular undersampling can be produced using either pseudo-random generation or incoherent optimization-driven sampling like SPARKLING. The code of the latter approach, originally designed by [Carole Lazarus](https://www.linkedin.com/in/carole-lazarus-b44907a6/?originalSubdomain=fr), [Nicolas Chauffert](http://chauffertn.free.fr/) and [Pierre Weiss](https://www.math.univ-toulouse.fr/~weiss/), is actually not disclosed. It can be requested by emailing us. 

Importantly, we also develop our own image reconstruction python package for multiple _Fourier imaging_ modalities, namely [PySAP](https://github.com/CEA-COSMIC/pysap). These developments are done in collaboration with the [CosmoStat](https://cosmostat.org) team ([J. L. Starck](http://jstarck.cosmostat.org/) in the context of the [COSMIC](https://cosmic.cosmostat.org) project. The two core developers of [PySAP](https://github.com/CEA-COSMIC/pysap) are A. Grigis (antoine.grigis@cea.fr) and [S. Farrens](http://www.cosmostat.org/people/sfarrens). The new organization of [PySAP](https://github.com/CEA-COSMIC/pysap) relies on on separate plugin for each imaging modality, for instance for MRI: [pysap-mri](https://github.com/CEA-COSMIC/pysap-mri). The main contributors to this plugin habe been [Chaithya G R](https://github.com/chaithyagr), [Loubna El Gueddari](https://github.com/LElgueddari), [Zaccharie Ramzi](https://github.com/zaccharieramzi), [Guillaume Daval-Frérot](https://github.com/Daval-G) and [Pierre-Antoine Comby](https://github.com/paquiteau)  all former or current PhD candidates under my supervision at [CEA/NeuroSpin](http://joliot.cea.fr/drf/joliot/en/Pages/research_entities/NeuroSpin.aspx).


```{tableofcontents}
```
