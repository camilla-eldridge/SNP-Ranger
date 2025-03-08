# SNP-Ranger

SNP-Ranger is a Python script for functional SNP analysis.

## Overview
Given a GBK annotation file and the output from the SNP exporter tool in Mauve, `snp_ranger.py` identifies whether an SNP falls within the range of annotated features. This method streamlines the process of identifying functionally relevant SNPs while reducing the likelihood of reporting SNPs from contaminants.

## Usage
SNP-Ranger requires two inputs:
- The reference (or first) GBK file used for progressiveMauve alignment.
- The SNP export file generated by Mauve.

### Command:
```bash
snp_ranger.py Exported_SNPS.txt first_gbk_file > snps.txt  
```

## Output
SNP-Ranger generates a plain text output listing SNPs along with their parent nodes, relative positions, and annotations. It excludes SNPs outside the range of annotated tRNA, rRNA, or CDS regions. If an SNP is found in an unannotated region, the script will notify the user for further investigation.

### Example Output:
```
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
```

## Dependencies
The following Python 3 modules are required:
- `sys`
- `regex`
- `typing`

## Additional Notes
- This script was tested using GBK files generated by Prokka v1.7.
- Ensure the alignment is correctly interpreted—SNPs may arise from annotated regions of contaminant species aligning or misannotations between reference and target genomes.

## License
This work is licensed under a [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). You are free to share and adapt this code, provided you credit the original author and indicate any modifications made.

