import re

# Read original file
with open('preproinsulin-seq.txt', 'r') as file:
    data = file.read()

# Clean the sequence
cleaned_sequence = re.sub(r'ORIGIN|\d+|//|\s+', '', data)

# Save cleaned sequence
with open('preproinsulin-seq-clean.txt', 'w') as file:
    file.write(cleaned_sequence)

# Check cleaned length
assert len(cleaned_sequence) == 110, "Error: Sequence should be exactly 110 characters"

# Extract segments
lsinsulin = cleaned_sequence[:24]
binsulin = cleaned_sequence[24:54]
cinsulin = cleaned_sequence[54:89]
ainsulin = cleaned_sequence[89:]

# Save each part to its own file
with open('lsinsulin-seq-clean.txt', 'w') as file:
    file.write(lsinsulin)

with open('binsulin-seq-clean.txt', 'w') as file:
    file.write(binsulin)

with open('cinsulin-seq-clean.txt', 'w') as file:
    file.write(cinsulin)

with open('ainsulin-seq-clean.txt', 'w') as file:
    file.write(ainsulin)

# Confirm lengths
print(f"lsinsulin: {len(lsinsulin)} characters")
print(f"binsulin: {len(binsulin)} characters")
print(f"cinsulin: {len(cinsulin)} characters")
print(f"ainsulin: {len(ainsulin)} characters")
