# Whole Brain Emulation - Tracking and Forecasting
## News

- [1 mouse SNN at $100K in 2015 by University of Manchester's SpiNNaker Project](https://www.youtube.com/watch?v=2e06C-yUwlc)

- [Fluitfly detailed connectome to Electrophysiology level by Google+Jnelia Institute in 2019](https://www.youtube.com/watch?v=PeyHKdmBpqY)

-  Dates in bold are what has already been achieved and other estimates are from [a paper by Future of Humanity Institute](https://www.fhi.ox.ac.uk/brain-emulation-roadmap-report.pdf)

- Mouse WBE [Cost Estimation](https://www.biorxiv.org/content/10.1101/001214v3.full) as of 2013
  - Diamond Knife cost : 20^3/(1 cm^2 × 25 nm) = 168000 sections. 10K sections before replacing knife.
                      : ie 170 Knifes of $2500 each. Total cost = $2500*170 = $425K
                      
- Monkey (rhesus) WBE micron scale in 2021 by [China Brain Project](https://www.freepressjournal.in/science/worlds-first-3d-image-of-monkey-brain-developed)


## Connectome(Scanning+Storage):


| AI       | C. Elegans | FruitFly           | Mouse  | Monkey (rhesus) | Human 
| ------------- |:----------- |:---------------------------:| -----:|  -----:| ------:|
| Neurons(micron scale)|--|--|--| **2021(China)** | -- | 
| Electrophysiology(10 nm scale)|**2008(Janelia,US)**|**2019(Janelia,US)**|--|--| --|
| Metabolome(1 nm scale) |--|--|--|--| --|
| Proteome(1A scale) |--|--|--|--| --|
| States of protein complexes |--|--|--|--| --|
| Distribution of complexes |--|--|--|--| --|
| Stochastic behavior of single molecules |--|--|--|--| --|

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


## Unit Economics with Timeline analysis:



### ORIGINAL MOORES LAW (18 months doubling) WITH IMAGE COMPRESSION(most optimistic case)
|   |2020 |    |2030 |   | 2040 |  | 2050 
| ------------- |:----------- |:--------------:| -----:| ------------- |:----------- |:--------------:| -----:| 
| Scanning(100 Beam SEM x 1M units) |$1T |Scanning(10K Beam SEM x 10K units) |$10B |Scanning(1M Beam SEM x 100 units) |$100M |Scanning(100M Beam SEM) | $1M |
| Storage(1ZB)(raw) |$30B |Storage(1EB) (compressed)|$300K |Storage(1EB) (compressed)|$3K |Storage(1EB) (compressed)|$30 |
| Compute(100 teraflops) |$100M |Compute(100 teraflops) |$1M |Compute(100 teraflops) |$10K |Compute(100 teraflops) |$100 |
| Body with 1M nerve endings |$100M |Body with 1M nerve endings |$10M |Body with 1M nerve endings |$1M |Body with 1M nerve endings |$1M |
| R&D |  |R&D | |R&D |$10M |R&D |$100K |
| Sales & Marketing |  |Sales & Marketing | |Sales & Marketing |0 |Sales & Marketing |$10K |
| Total |$1030.2B |Total |$10.01B |Total |$111.013M |Total |**$2.11M**|

### SLOWED DOWN MOORES LAW (36 months doubling) WITH IMAGE COMPRESSION
|   |2020 |    |2030 |   | 2040 |  | 2050 
| ------------- |:----------- |:--------------:| -----:| ------------- |:----------- |:--------------:| -----:| 
| Scanning(100 Beam SEM x 1M units) |$1T |Scanning(10K Beam SEM x 10K units) |$10B |Scanning(1M Beam SEM x 100 units) |$100M |Scanning(100M Beam SEM) |$1M |
| Storage(1ZB)(raw) |$30B |Storage(1EB) (compressed) |$3M |Storage(1EB) (compressed)| $300K | Storage(1EB) (compressed)|$30K |
| Compute(100 teraflops) |$100M |Compute(100 teraflops) |$10M |Compute(100 teraflops) |$1M |Compute(100 teraflops) |$100K |
| Body with 1M nerve endings |$100M |Body with 1M nerve endings |$10M |Body with 1M nerve endings |$1M |Body with 1M nerve endings |$1M |
| R&D |  |R&D | |R&D |$10M |R&D |$100K |
| Sales & Marketing |  |Sales & Marketing | |Sales & Marketing |0 |Sales & Marketing |$10K |
| Total |$1030.2B |Total |$10.01B |Total |$112.3M |Total |$2.24M |

### ORIGINAL MOORES LAW(18 months doubling)
|   |2020 |    |2030 |   | 2040 |  | 2050 
| ------------- |:----------- |:--------------:| -----:| ------------- |:----------- |:--------------:| -----:| 
| Scanning(100 Beam SEM x 1M units) |$1T |Scanning(10K Beam SEM x 10K units) |$10B |Scanning(1M Beam SEM x 100 units) |$100M |Scanning(100M Beam SEM) |$1M |
| Storage(1ZB)(raw) |$30B |Storage(1ZB) |$300M |Storage(1ZB) |$3M |Storage(1ZB) |$30K |
| Compute(100 teraflops) |$100M |Compute(100 teraflops) |$1M |Compute(100 teraflops) |$10K |Compute(100 teraflops) |$100 |
| Body with 1M nerve endings |$100M |Body with 1M nerve endings |$10M |Body with 1M nerve endings |$1M |Body with 1M nerve endings |$1M |
| R&D |  |R&D | |R&D |$10M |R&D |$100K |
| Sales & Marketing |  |Sales & Marketing | |Sales & Marketing |0 |Sales & Marketing |$10K |
| Total |$1030.2B |Total |$10.31B |Total |$114.3M |Total |$2.14M |

### SLOWED DOWN MOORES LAW(36 months doubling)(most pessimistic case)
|   |2020 |    |2030 |   | 2040 |  | 2050 
| ------------- |:----------- |:--------------:| -----:| ------------- |:----------- |:--------------:| -----:| 
| Scanning(100 Beam SEM x 1M units) |$1T |Scanning(10K Beam SEM x 10K units) |$10B |Scanning(1M Beam SEM x 100 units) |$100M |Scanning(100M Beam SEM) |$1M |
| Storage(1ZB)(raw) |$30B |Storage(1ZB) |$3B |Storage(1ZB) |$300M |Storage(1ZB) |$30M |
| Compute(100 teraflops) |$100M |Compute(100 teraflops) |$10M |Compute(100 teraflops) |$1M |Compute(100 teraflops) |$100K |
| Body with 1M nerve endings |$100M |Body with 1M nerve endings |$10M |Body with 1M nerve endings |$1M |Body with 1M nerve endings |$1M |
| R&D |  |R&D | |R&D |$10M |R&D |$100K |
| Sales & Marketing |  |Sales & Marketing | |Sales & Marketing |0 |Sales & Marketing |$10K |
| Total |$1030.2B |Total |$13.02B |Total |$412M |Total |**$32.21M** |

- Assumptions made here is 10nm resultion scanning is good enough for copying memory.
- From the above table we can see by **2040** the unit cost is estimated to be between **$111.01M and $412M**, and by **2050** the unit cost is estimated to be between **$2.11M and $32.21M**. 
- It is also to be noted that SEM improvements may follow Wrights Law in long term instead of Moores Law. This analysis uses original Moores law for SEM in all the above four cases as in recent past SEM improvements have been moving at par with original moores law if not faster. But beyond 2040 if it slows down the 2050 estimates might get pushed to 2060. 
- As you might have already noticed the dominant cost is the SEM cost. So there are arguments that if some private company takes initiative to accelerate the SEM development then the 2050 projections may even get fast-forwarded to 2040. The reason is  today apart from uses in semiconductor and neuroscience there aren't many uses of multi-beam SEM. In neuroscience since we are currently dealing with fruitfly/mouse there is no initiative to make multi beam SEM scale up faster as in such case storage/compute will fall behind. So multi-beam SEM is progressing in a way such that the three factors remain close to one another. But to move to humans if we have to keep scanning factor of the same order to storage and compute, then it will have to move lot faster than moores/wrights law. 
- The R&D cost is estimated as averaging of the total R&D cost divided by total potential customers who can afford that price range(and also wish to opt for it). The total R&D from government and philanthropic foundations in neuroscience in 2020-2050 period is expected to be of the order of $100B. And as the industry matures private sector is expected to invest capital of the order of $10B. We estimate number of potential customers in 2040-2049 is order of 1k and 2050-2059 is order of 100k. So averaging R&D per customer for 2040s comes as $10M and for 2050s as $100K. 

![plot_estimstes](https://user-images.githubusercontent.com/2527354/143514623-84679f84-6194-416a-8dac-706b29e1a0d7.png)

