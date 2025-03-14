# Whole Brain Emulation - Tracking and Forecasting
## News

-  Dates in bold are what has already been achieved and other estimates are from [a paper by Future of Humanity Institute](https://www.fhi.ox.ac.uk/brain-emulation-roadmap-report.pdf)


## Connectome(Scanning+Image Storage):

| AI       | C. Elegans | FruitFly           | Mouse  | Monkey (rhesus) | Human 
| ------------- |:----------- |:---------------------------:| -----:|  -----:| ------:|
| Neurons(micron scale)|--|--|--| **2021(China)** | -- | 
| Electrophysiology(10 nm scale)|**2008(Janelia,US)**|**2019(Janelia,US)**|--|--| --|
| Metabolome(1 nm scale) |--|--|--|--| --|
| Proteome(1A scale) |--|--|--|--| --|
| States of protein complexes |--|--|--|--| --|
| Distribution of complexes |--|--|--|--| --|
| Stochastic behavior of single molecules |--|--|--|--| --|

### News

- Mouse WBE [Cost Estimation](https://www.biorxiv.org/content/10.1101/001214v3.full) as of 2013
  - Diamond Knife cost : 20^3/(1 cm^2 × 25 nm) = 168000 sections. 10K sections before replacing knife.
                      : ie 170 Knifes of $2500 each. Total cost = $2500*170 = $425K
                      

### Scanning Throughput News:

#### 10nm

| Throughput       | Date | Project | Technique | Resolution|
| ----------- |:-------|:------- |:------- |:---------:|
| 234 GB/hour | 2019 | [Janelia Institute + Google (Fluitfly)](https://www.youtube.com/watch?v=PeyHKdmBpqY) | diamond knife + 91 beam SEM|8 nm|
| 1.6 TB/hour | 2020 | [Allen Institute petascale pipeline](https://www.nature.com/articles/s41467-020-18659-3) | diamond knife + TEM|8 nm|



- Desired throughput for mouse is 1EB in 1k hours or **1PB/hour** (ie 1k TB/hr)
- Desired throughput for human is 1ZB in 1k hours or **1EB/hour** (ie 1m TB/hr)
- Zeiss upgraded 91 beam SEM to 331 beam SEM. So I am expecting next upgrade to be [1387 beams and 5419 beams](http://oeis.org/A245489) respectively 
- Potential Candidates:
  - GCIB 10S from Ionoptika mounted on a Zeiss Ultra SEM
  - ANSOM Microscope
  - Hard x-ray scanning microscopy with coherent radiation
  - Magnetic soft X-ray microscopy
  - Expansion microscopy + Light-sheet microscopy + Bessel beam
  - Expansion microscopy + Lightsheet localization microscopy
  - Expansion microscopy + Mid-infrared spectro-microscopy
  - Any of the above low resolution imaging (or their combination to improve resolution slightly) + Deep learning upscaling with models trained on past super resultion EM data

#### 100nm

| Throughput       | Date | Project | Technique | Resolution|
| ----------- |:-------|:------- |:------- |:---------:|
| Many TB/hour | July2020 | [University of Washginton's SEQUIN](https://www.sciencedirect.com/science/article/pii/S0896627320302816)  | ZEISS Airyscan | 144 nm |
| Many TB/hour | Sept2020 | [Harvard](https://www.biorxiv.org/content/10.1101/653188v1.full.pdf)  | X-ray holographic nano-tomography | 100 nm |
| 1 TB/hour | Aug2021 | [Tshinghua University (Mouse)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8497830/pdf/fnana-15-732464.pdf)  | Expansion microscopy + Light-sheet microscopy | 300 nm |
| 1 TB/hour | Sept2021 | [Wuhan National Lab (Mouse)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8515992/pdf/boe-12-9-5614.pdf)  | Expansion microscopy + Light-sheet tomography | 144 nm |
| 8 TB/hour | April2021 | [CMU](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8600979/)  | Expansion microscopy + Light-sheet microscopy | 60 nm |
| 10 TB/hour | Dec2021 | [CMU + Columbia University](https://www.biorxiv.org/content/10.1101/2021.12.22.473713v1.full.pdf)  | Expansion microscopy + Stimulated Raman scattering (SRS) microscopy | 50 nm |


#### 300nm

| Throughput       | Date | Project | Technique | Resolution|
| ----------- |:-------|:------- |:------- |:---------:|
| 20 TB/hour | 2024 | [South East Asia (Human)](https://www.sciencedirect.com/science/article/pii/S0370157322003933) | AXON + MAXWELL microscopy |300 npm|



#### 1μm

| Throughput       | Date | Project | Technique | Resolution|
| ----------- |:-------|:------- |:------- |:---------:|
| 300 GB/hour | July2021 | [Argonne’s Advanced Photon Source (Mouse)](https://www.anl.gov/article/researchers-image-an-entire-mouse-brain-for-the-first-time) |  x-ray microscope(micro CT)|1 micron|
| 5 TB/hour | 2021 | [China CAS (Monkey)](https://english.cas.cn/newsroom/research_news/life/202107/t20210721_276103.shtml) | Flurosence microscopy(VISoR2) |1 micron|
| 6 TB/hour | 2017 | [Taiwan (Mouse)](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-017-0461-8) | synchrotron x-ray tomography |1 micron|




## Simulation(Compute):


| AI       | C. Elegans | FruitFly           | Mouse  | Monkey (rhesus) | Human  | AI(CPU at $1M)
| ------------- |:----------- |:---------------------------:| -----:|  -----:| ------:|------:|
| Spiking neural network(Just neurons)|--|--|**2015(Spinnaker,UK)**| -- | **2021(Tesla Dojo)** | 2023 |
| Electrophysiology(nano scale)|--|--|--|--| --| 2033 |
| Metabolome |--|--|--|--| --| 2044 |
| Proteome |--|--|--|--| --| 2048 |
| States of protein complexes |--|--|--|--| --| 2052 |
| Distribution of complexes |--|--|--|--| --| 2063 |
| Stochastic behavior of single molecules |--|--|--|--| --| 2111 |

### Simulation News

- [1 mouse SNN at $100K in 2015 by University of Manchester's SpiNNaker Project](https://www.youtube.com/watch?v=2e06C-yUwlc)



## Unit Economics with Timeline analysis:



### ORIGINAL MOORES LAW (18 months doubling) WITH IMAGE COMPRESSION(most optimistic case)
|   |2020 |    |2030 |   | 2040 |  | 2050 
| ------------- |:----------- |:--------------:| -----:| ------------- |:----------- |:--------------:| -----:| 
| Scanning(100 Beam SEM x 1M units) |$1T |Scanning(10K Beam SEM x 10K units) |$10B |Scanning(1M Beam SEM x 100 units) |$100M |Scanning(100M Beam SEM) | $1M |
| Compute for Stitching |$1T |Compute for Stitching |$10B |Compute for Stitching |$100M |Compute for Stitching |$1M |
| Image Storage(1ZB)(raw) |$30B |Image Storage(1EB) (compressed)|$300K |Image Storage(1EB) (compressed)|$3K |Image Storage(1EB) (compressed)|$30 |
| Connectome Storage(1PB) |$30K |Connectome Storage(1PB)|$300 |Connectome Storage(1PB)|$0.3 |Connectome Storage(1PB)|$0.003 |
| Compute for Simulation(10 Pflops) |$10M |Compute for Simulation(10 Pflops) |$100K |Compute for Simulation(10 Pflops) |$1K |Compute for Simulation(10 Pflops) |$10 |
| Body with 1M nerve endings |$100M |Body with 1M nerve endings |$10M |Body with 1M nerve endings |$1M |Body with 1M nerve endings |$1M |
| R&D | $110B |R&D | $110B |R&D |$10M |R&D |$100K |
| Sales & Marketing | 0 |Sales & Marketing | 0 |Sales & Marketing |0 |Sales & Marketing |$10K |
| Total |$2140.2B |Total |$130.01B |Total |$211.013M |Total |**$3.11M**|

### SLOWED DOWN MOORES LAW (36 months doubling) WITH IMAGE COMPRESSION
|   |2020 |    |2030 |   | 2040 |  | 2050 
| ------------- |:----------- |:--------------:| -----:| ------------- |:----------- |:--------------:| -----:| 
| Scanning(100 Beam SEM x 1M units) |$1T |Scanning(10K Beam SEM x 10K units) |$10B |Scanning(1M Beam SEM x 100 units) |$100M |Scanning(100M Beam SEM) |$1M |
| Compute for Stitching |$1T |Compute for Stitching |$10B |Compute for Stitching |$100M |Compute for Stitching |$1M |
| Image Storage(1ZB)(raw) |$30B |Image Storage(1EB) (compressed) |$3M |Image Storage(1EB) (compressed)| $300K | Image Storage(1EB) (compressed)|$30K |
| Connectome Storage(1PB) |$30K |Connectome Storage(1PB)|$3k |Connectome Storage(1PB)|$300 |Connectome Storage(1PB)|$30 |
| Compute for Simulation(10 Pflops) |$10M |Compute for Simulation(10 Pflops) |$1M |Compute for Simulation(10 Pflops) |$100K |Compute for Simulation(10 Pflops) |$10K |
| Body with 1M nerve endings |$100M |Body with 1M nerve endings |$10M |Body with 1M nerve endings |$1M |Body with 1M nerve endings |$1M |
| R&D | $110B |R&D | $110B |R&D |$10M |R&D |$100K |
| Sales & Marketing | 0 |Sales & Marketing | 0 |Sales & Marketing |0 |Sales & Marketing |$10K |
| Total |$2140.2B |Total |$130.01B |Total |$212.3M |Total |$3.24M |

### ORIGINAL MOORES LAW(18 months doubling)
|   |2020 |    |2030 |   | 2040 |  | 2050 
| ------------- |:----------- |:--------------:| -----:| ------------- |:----------- |:--------------:| -----:| 
| Scanning(100 Beam SEM x 1M units) |$1T |Scanning(10K Beam SEM x 10K units) |$10B |Scanning(1M Beam SEM x 100 units) |$100M |Scanning(100M Beam SEM) |$1M |
| Compute for Stitching |$1T |Compute for Stitching |$10B |Compute for Stitching |$100M |Compute for Stitching |$1M |
| Image Storage(1ZB)(raw) |$30B |Image Storage(1ZB) |$300M |Image Storage(1ZB) |$3M |Image Storage(1ZB) |$30K |
| Connectome Storage(1PB) |$30K |Connectome Storage(1PB)|$300 |Connectome Storage(1PB)|$0.3 |Connectome Storage(1PB)|$0.003 |
| Compute for Simulation(10 Pflops) |$10M |Compute for Simulation(10 Pflops) |$100K |Compute for Simulation(10 Pflops) |$1K |Compute for Simulation(10 Pflops) |$10 |
| Body with 1M nerve endings |$100M |Body with 1M nerve endings |$10M |Body with 1M nerve endings |$1M |Body with 1M nerve endings |$1M |
| R&D | $110B |R&D | $110B |R&D |$10M |R&D |$100K |
| Sales & Marketing | 0 |Sales & Marketing | 0 |Sales & Marketing |0 |Sales & Marketing |$10K |
| Total |$2140.2B |Total |$130.31B |Total |$214.3M |Total |$3.14M |

### SLOWED DOWN MOORES LAW(36 months doubling)(most pessimistic case)
|   |2020 |    |2030 |   | 2040 |  | 2050 
| ------------- |:----------- |:--------------:| -----:| ------------- |:----------- |:--------------:| -----:| 
| Scanning(100 Beam SEM x 1M units) |$1T |Scanning(10K Beam SEM x 10K units) |$10B |Scanning(1M Beam SEM x 100 units) |$100M |Scanning(100M Beam SEM) |$1M |
| Compute for Stitching |$1T |Compute for Stitching |$10B |Compute for Stitching |$100M |Compute for Stitching |$10M |
| Image Storage(1ZB)(raw) |$30B |Image Storage(1ZB) |$3B |Image Storage(1ZB) |$300M |Image Storage(1ZB) |$30M |
| Connectome Storage(1PB) |$30K |Connectome Storage(1PB)|$3K |Connectome Storage(1PB)|$300 |Connectome Storage(1PB)|$30 |
| Compute for Simulation(10 Pflops) |$10M |Compute for Simulation(10 Pflops) |$1M |Compute for Simulation(10 Pflops) |$100K |Compute for Simulation(10 Pflops) |$10K |
| Body with 1M nerve endings |$100M |Body with 1M nerve endings |$10M |Body with 1M nerve endings |$1M |Body with 1M nerve endings |$1M |
| R&D | $110B |R&D | $110B |R&D |$10M |R&D |$100K |
| Sales & Marketing | 0 |Sales & Marketing | 0 |Sales & Marketing |0 |Sales & Marketing |$10K |
| Total |$2140.2B |Total |$133.02B |Total |$512M |Total |**$42.21M** |

- Assumptions made here is 10nm isotropic resolution scanning is good enough for copying memory.
- From the above table we can see by **2040** the unit cost is estimated to be between **$111.01M and $412M**, and by **2050** the unit cost is estimated to be between **$2.11M and $32.21M**. 
- It is also to be noted that SEM improvements may follow Wrights Law in long term instead of Moores Law. This analysis uses original Moores law for SEM in all the above four cases as in recent past SEM improvements have been moving at par with original moores law if not faster. But beyond 2040 if it slows down the 2050 estimates might get pushed to 2060. 
- As you might have already noticed the dominant cost is the SEM cost. So there are arguments that if some private company takes initiative to accelerate the SEM development then the 2050 projections may happen even sooner. The reason of slow progress in Multibeam SEM is today due to the fact that apart from uses in semiconductor and neuroscience there aren't many uses of multi-beam SEM, and those too are at research level, none at production scale. In neuroscience since we are currently dealing with fruitfly/mouse there is no initiative to make multi beam SEM scale up faster as in such case Image Storage/compute will fall behind. So multi-beam SEM is progressing in a way such that the three factors(Image Storage, compute and scanning) remain close to one another. Secondly as we move higher ion beam milling costs will replace diamond knife slicing costs. But to move to humans if we have to keep scanning cost of the same order as Image Storage or compute, then it will have to move lot faster than moores law. It is very likely that till 10K beams it will grow faster than moores law but beyond 10K beams the development will slow down as we wouln't get much price improvement adding more beams to the same SEM than adding another SEM to the system. However cost will continue to drop if more and more units are manufactured but that cost drop will be incremental more like how solar panel price falls which is called wrights law. 
- The Image Storage and compute estimates as you can see are insignificant compared to SEM costs despite the fact we are quite conservative. Kurzweil says we will have 30PFLOPs of compute for $1K by 2029. We see no chance of Kurzweil's prediction coming anywhere close to reality. We are 300x-3000x conservative(and hence realistic) to that as we expect 100 PFLOPs for $1M(optimistic)-$10M(conservative) .
- The R&D costs are primarily for SEM and simulation algorithm. For Image Storage, compute and body we will piggy-back on semiconductor and robotics industry, and hence very few of the R&D costs will go there. The R&D cost per unit is estimated as averaging of the total R&D cost divided by total potential customers who can afford that price range(and also wish to opt for it). The total R&D from government and philanthropic foundations in neuroscience in 2020-2050 period is expected to be of the order of $100B. And as the industry matures private sector is expected to invest capital of the order of $10B solely for R&D. We estimate those $110B capital would be enough to solve both scanning and simulation problems. We estimate number of potential customers in 2040-2049 is order of 1k and in 2050-2059 is order of 100k. So averaging R&D per customer for 2040s resolves as $10M and for 2050s as $100K. 


![estimate](https://user-images.githubusercontent.com/2527354/145160735-d588e659-37d3-4a41-a9f2-acbe26a60c0b.png)

### Foresight Institute Whole Brain Emulation Workshop 2023 
- https://www.youtube.com/watch?v=52mMtSiIVZ0&list=PLH78wfbGI1x2CI6aV_hiOE1_GOFkZAFph&pp=iAQB

### Computational mechanisms beyond the chemical synapse.
- Glial contributions to neuronal computations
- Neurovascular coupling
- Morphological plasticity of neurons and glia
- NMDA spikes, calcium spikes, other dendritic computations
- Arc-mediated intercellular transport of RNAs
- Gap junctions
- Neuromodulators
- Cotransmission of multiple neurotransmitters from same synaptic terminal
- Ephatic coupling

### 300nm Synchrotron based progress
- [SYNAPSE – Synchrotron for Neuroscience: an Asia-Pacific ... ](https://synapse-sg.org)
