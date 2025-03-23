from hookspecs import hookimpl
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

class PairwiseAlignmentPlugin:
    name = "PairwiseAlignmentPlugin"
    description = "Performs pairwise alignment using Biopython. Usage: 'align <sequence1> <sequence2>'"

    @hookimpl
    def process_input(self, user_input: str) -> str:
        # Check if the command starts with "align "
        if user_input.lower().startswith("align "):
            # Split the command into parts
            parts = user_input.split(maxsplit=2)
            if len(parts) != 3:
                return "Usage: align <sequence1> <sequence2>"
            seq1 = parts[1]
            seq2 = parts[2]
            try:
                # Perform a simple global alignment (using a basic scoring scheme)
                alignments = pairwise2.align.globalxx(seq1, seq2)
                if alignments:
                    # Format and return the first alignment result
                    return format_alignment(*alignments[0])
                else:
                    return "No alignment found."
            except Exception as e:
                return f"Error during alignment: {e}"
        # If the input doesn't start with "align ", this plugin doesn't handle it.
        return ""

    @hookimpl
    def list_abilities(self) -> str:
        return "Pairwise Alignment: type 'align <sequence1> <sequence2>' to perform an alignment."
