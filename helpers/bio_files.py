import re


def convert_helper(input_fasta, output_fasta):
    with open(input_fasta, 'r') as inp, open(output_fasta, 'w') as out:
        header = inp.readline()

        while header:
            strs = []
            line = inp.readline()

            while line and not line.startswith('>'):
                strs.append(line.strip())
                line = inp.readline()

            sequence = "".join(strs)
            out.write(header)
            out.write(sequence + "\n")

            header = line


import re


def parse_helper(input_file: str, output_file: str):
    proteins = []

    with open(input_file, "r") as inp, open(output_file, "w") as out:
        take_next_hit = False

        for line in inp:

            if line.strip().startswith("Description"):
                take_next_hit = True
                continue

            if take_next_hit:

                if not line.strip():
                    continue

                description = re.split(r"\s{2,}", line.strip())[0]

                proteins.append(description)

                take_next_hit = False

        proteins.sort()

    
        for protein in proteins:
            out.write(protein + "\n")