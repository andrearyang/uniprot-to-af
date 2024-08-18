This is a set of Python scripts to make working with the AlphaFold 3 server easier. It automates the creation of JSON input files from Uniprot IDs, as well as output readings. The outputs are saved to a .csv file and contains the pLDDT, iPTM, and PTM values for each file.

To use,
1. Run main.py in terminal
2. Input Uniprot protein IDs separated by commas
3. Download JSON file protein_search_results.json
4. Upload to AlphaFold server; download output
5. Save output to "output" folder
6. Run data.py in terminal
7. Save .csv outputs (in the "output" folder)

Future work:
1. Take inputs as .csv files

pTM scores above 0.5 means the overall predicted fold for the complex might be similar to the true structure. ipTM values higher than 0.8 present high-quality predictions of the relative positions of subunits within the complex.
