# AF-calculation
CSIR- Institute of Genomics and Integrative Biology, New Delhi

The repository is associated with the manuscripts in process

The folder contains code that was used to calculate allele frequencies (AF) of haplotypes generated from various haplotype caller on population data

The enclosed file contains a python code to calculate AF

The input for the code is a tab seperated file containing three columns: ID, Allele1 and Allele2

The dataset generated from stargazer should be reframed to the above mentioned input form and named as "STARGAZER"; cyrius should be named as "CYRIUS" and the output from xHLA should be named based on the HLA type in capital letter (Eg: HLA-A; HLA-B; HLA-C; HLA-DQB1; HLA-DPB1; HLA-DRB1)

Once the dataset is ready the code can be run using the following command:
python indigen_af_calculator.py
