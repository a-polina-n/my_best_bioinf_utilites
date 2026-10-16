# My BEST bIoInF uTiLiTeS

This is my study project for a Python homework assignment.  
It contains several small bioinformatics utilities for working with  FASTQ, FASTA, and BLAST files.

The tools do not require any packages and use only the Python standard library.  
They were written and tested with Python 3.14.1.

## main

### Function `filter_fastq`

The function takes the following filtering parameters:

- `input_fastq` (`str`): path to the input FASTQ file.
- `output_fastq` (`str`): name or path of the output FASTQ file.
- `gc_bounds` (`int`, `float`, or `tuple`): GC percentage threshold or a tuple containing lower and upper GC percentage boundaries. Default: `(0, 100)`.
- `length_bounds` (`int` or `tuple`): sequence length threshold or a tuple containing lower and upper length boundaries. Default: `(0, 2**32)`.
- `quality_threshold` (`int` or `float`): lower boundary for the mean read quality. Default: `0`.

The function returns nothing.  
Reads that pass all filters are written to a new FASTQ file in the `filtered` directory.


### Function convert_multiline_fasta_to_oneline

Converts a multiline FASTA file into a FASTA file where each sequence is written on a single line.

For example:

```
>sequence_1
ATGC
ATGC
ATGC
```

is converted to:
```
>sequence_1
ATGCATGCATGC
```

The function takes:
- `input_fasta` (`str`): path to the input FASTA file.
- `output_fasta` (`str`, optional): name or path of the output FASTA file.
The function returns nothing and writes the converted sequences to a new FASTA file.

### Function parse_blast_output

Parses BLAST results saved in plain-text format.
For each query, the function finds sequences producing significant alignments: section and extracts the description of the best hit.

The function takes:
- `input_file` (`str`): path to the BLAST output .txt file.
- `output_file` (`str`): path to the output file.

The function returns nothing and the extracted protein descriptions are sorted alphabetically and written to the output file, one description per line.



## Contacts
Hope these tools may help you! :)
Any suggestions or bug reports? Telegram: @a_polina_n
