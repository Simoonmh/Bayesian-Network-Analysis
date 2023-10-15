# Bayesian-Network-Analysis
This project uses the bnlearn library to build a Bayesian network that models the impact of global events on daily life, with a specific focus on a significant festival. The repository provides both data and code for learning the network structure, defining network parameters, and performing inference queries.

Dataset sample:

![Dataset sample](https://github.com/Simoonmh/Bayesian-Network-Analysis/assets/62888236/9c576d45-e97a-496b-b0d2-c68fdb601d8e)

The dataset is read using Pandas, and then bnlearn is used to plot the network, wich, given a data sample, estimates a directed acyclic graph (DAG) capturing the dependencies between variables.

![1](https://github.com/Simoonmh/Bayesian-Network-Analysis/assets/62888236/5bc2381b-c3f0-4850-90dd-506b8ba489a1)

![2](https://github.com/Simoonmh/Bayesian-Network-Analysis/assets/62888236/e5fc9bcb-5f00-4c2a-983c-c17b77368c5f)

By observing the graph, we can discern the following relationships within the dataset:
- According to the graph, 'guerra_ucrania' and 'inflacion' lead to high prices.
- 'precios_altos' affect 'no_alcohol', 'no_carne' and 'escasez'
- 'guerra_ucrania' affects 'precios_altos' and 'escasez', but is not influenced by other variables.
- 'inflacion' affects 'precios_altos' and 'escasez'
- 'escasez' impacts 'no_confort', 'no_alcohol' and 'no_carne'
- 'no_confort', 'no_alcohol' and 'no_carne' do not affect other variables, but they are affected by them.
