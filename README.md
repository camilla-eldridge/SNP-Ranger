## SNP-Ranger
SNP Ranger is a python script for functional SNP analysis.

Given a gbk annotation file and the output of the SNP exporter tool from Mauve **snp_ranger.py** locates if an SNP is within the range of annotated features. This method speeds up the process of identifying SNP's of functional interest and reduces the chance of reporting SNPs from contaminants.


### Usage
SNP-Ranger takes the reference (or first) gbk input for progressiveMauve alignment and SNP export file as input and outputs a list of SNPs located in annotated regions.


		snp_ranger.py Exported_SNPS.txt  first_gbk_file > snps.txt  


## Output
SNP-Ranger produces plan text output, providing a list of SNPs with their parent NODES, their relative positions and annotation. It will exclude anything outside the range of annotated tRNA, rRNA or CDS positions and notify when an SNP in encountered within a region that is not annotated, to enable further investigation.

	NODE_1: SNP here but no annotations found!
 	-----
	NODE_3:
	Product: hypothetical_protein
	Value: 17
	Range: 13, 210
	-----
	NODE_15:
	Product: Small_toxic_polypeptide_LdrD
	Value: 596
	Range: 596, 723
	-----

## Dependancies:
The following python3 modules are required:
- sys, regex, typing.





### Additional notes:
- This script was tested using gbk files from Prokka v1.7
- Be sure to check the alignment too (SNP's can be from eg. the same contaminants from both samples aligning or misannotations between refeence and target genomes).

