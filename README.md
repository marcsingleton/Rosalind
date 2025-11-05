# Rosalind

## Background
[Rosalind](https://rosalind.info/about/) is a platform for learning bioinformatics by problem solving. Like coding challenge websites, it hosts problems that are graded by an automated checker. The problems themselves contain prompts that give the necessary background or sometimes less necessary (but still interesting!) biological context, a concise statement of the expected inputs and outputs, and a pair of sample inputs and outputs to help with developing a solution. When an input is requested, a correct answer must be provided within a specified time frame (usually a few minutes). The test inputs are typically larger than the sample ones, so the limit ensures the solution implements a computationally efficient method.

There are several distinct problem tracks organized around different themes, for example basic programming, algorithms, and practical bioinformatics. These solutions are for the "Bioinformatics Stronghold" track, which is a broad survey of bioinformatics topics and related algorithms. As of this writing, I've solved most of the problems in this track. Maybe one day I'll complete them all.

## Honor Code
Rosalind is an excellent resource, but it typically offers little direction on how to approach a solution. For many problems, this isn't a major roadblock since the intuitive method is the correct one and implementing it is just a matter of fluency with your chosen coding language. However, some problems use concepts that are only taught in college-level courses on algorithms or bioinformatics, and in these cases Rosalind's reticence can be a barrier to learning. 

These solutions are posted for learning purposes. If you're using Rosalind for a class, you should consult the syllabus for its policy on the topic. If you're self-studying, try to find a solution on your own first. If you're truly stuck, you can look at my solutions as a hint or to study, but please do not copy the code only to get the right answer and move on to the next problem.

## Implementation Notes
My solutions are written in Python. To my knowledge I have only used features and modules that have been supported for many years and will likely continue to be, so I expect they will run on any recent version without issue. I didn't use any biology-focused third-party packages like Biopython or scikit-bio since several of the problems could be trivially solved by functions in those libraries. As a result, I ended up writing a small collection of utility functions, most notably for manipulating trees and parsing Newick files. They are organized as a module in the `utils/` directory, so the project root must be in the `PYTHONPATH` environment variable to allow the scripts to import these functions. Additionally, a few solutions use NumPy arrays for efficiency and clarity.

My solutions focus on the mechanics of the algorithm and do not implement any external interfaces like argument parsing and file IO. To compute a solution, I instead paste the input directly into the script.
