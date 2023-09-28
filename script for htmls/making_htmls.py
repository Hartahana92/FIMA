import pandas as pd

met = pd.read_csv("Metabolite_inf.csv", sep=";");
used = set();


HTML = f"""
{{% extends "browse/index.html" %}}
{{% load static %}}
{{% block content %}}

	<div class="container">
		<br>
		<div class = "card">
				<div class="card-header">
						<h3 style="display: inline-block;"> Showing information for HMDB0000001 (&#39;1-methylhistidine&#39;) </h3>
				</div>


			<div class="card-body">




				<table class="table table-border " style="width: 100%;table-layout: fixed;" id="hmdb">
					<thead style="background-color: #E6E6FA;">
						<td colspan="2"><h4 style="float: left;">Metabolite information</h4></td>
					</thead>
					<tbody style="background-color: white;">
						<tr>
							<td style="width: 40%;font-family: monospace;color:black !important;background-color:#FFFAFA;font-size:20px;" >HMDB ID</td>
							<td style="font-family: monospace;color:black !important">HMDB0000001</td>
						</tr>
						<tr>
							<td style="width: 40%; font-family: monospace;color:black !important;background-color: #FFFAFA;font-size:20px;">Synonyms</td>
							<td style="font-family: monospace;color:black !important">
								<div style="overflow-y: auto;height: 150px;">

										<h6>(2S)-2-amino-3-(1-Methyl-1H-imidazol-4-yl)propanoate</h6>

										<h6>(2S)-2-amino-3-(1-Methyl-1H-imidazol-4-yl)propanoic acid</h6>

										<h6>1 Methylhistidine</h6>

										<h6>1-MHis</h6>

										<h6>1-Methyl histidine</h6>

										<h6>1-Methyl-L-histidine</h6>

										<h6>1-Methyl-histidine</h6>

										<h6>1-Methylhistidine</h6>

										<h6>1-Methylhistidine dihydrochloride</h6>

										<h6>1-N-Methyl-L-histidine</h6>

										<h6>L-1-Methylhistidine</h6>

										<h6>N1-Methyl-L-histidine</h6>

										<h6>Pi-methylhistidine</h6>

								</div>
							</td>
						</tr>
						<tr>
							<td style="width: 40%; font-family: monospace;color:black !important;background-color:#FFFAFA;font-size:20px;">Chemical formula</td>
							<td style="font-family: monospace;color:black !important">C7H11N3O2</td>
						</tr>
						<tr>
							<td style="width: 40%; font-family: monospace;color:black !important;background-color: #FFFAFA;font-size:20px;">IUPAC name</td>
							<td style="font-family: monospace;color:black !important"><div style="width: 100%;overflow-x: auto;">(2S)-2-amino-3-(1-methyl-1H-imidazol-4-yl)propanoic acid</div></td>
						</tr>
						<tr>
							<td style="width: 40%; font-family: monospace;color:black !important;background-color: #FFFAFA;font-size:20px;">CAS registry number</td>
							<td style="font-family: monospace;color:black !important">332-80-9</td>
						</tr>
						<tr>
							<td style="width: 40%; font-family: monospace;color:black !important;background-color: #FFFAFA;font-size:20px;">Monoisotopic molecular weight</td>
							<td style="font-family: monospace;color:black !important">169.085126611</td>
						</tr>
						<tr style="background-color: #E6E6FA !important;">
							<td colspan="2"><h4 style="float: left;">Chemical taxonomy</h4></td>
						</tr>
						<tr>
							<td style="width: 40%; font-family: monospace;color:black !important;background-color: #FFFAFA;font-size:20px;">Super class</td>
							<td style="font-family: monospace;color:black !important">Organic acids and derivatives</td>
						</tr>
						<tr>
							<td style="width: 40%; font-family: monospace;color:black !important;background-color: #FFFAFA;font-size:20px;">Class</td>
							<td style="font-family: monospace;color:black !important">Carboxylic acids and derivatives</td>
						</tr>
						<tr>
							<td style="width: 40%; font-family: monospace;color:black !important;background-color: #FFFAFA;font-size:20px;">Sub class</td>
							<td style="font-family: monospace;color:black !important">Amino acids, peptides, and analogues</td>
						</tr>
						<tr style="background-color: #E6E6FA !important;">
							<td colspan="2"><h4 style="float: left;">Biological properties</h4></td>
						</tr>

						<!-- herehereherehereherehereherehereherehere --><!-- herehereherehereherehereherehereherehere -->
						<tr>
								<td style="width: 40%; font-family: monospace;color:black !important;background-color: #FFFAFA;font-size:20px;" colspan="2">Normal concentrations</td>
						</tr>
						<tr>
								<td colspan="2">

										<!-- normal table-->
								</td>
						</tr>
						<tr>
								<td colspan="2" style="width: 40%; font-family: monospace;color:black !important;background-color: #FFFAFA;font-size:20px;">Abnormal concentrations</td>
						</tr>
						<tr>
								<td colspan="2">

									<!-- abnormal table-->
								</td>
						</tr>
						<!-- herehereherehereherehereherehereherehere --><!-- herehereherehereherehereherehereherehere -->

						<tr>

							<td style="width: 40%; font-family: monospace;color:black !important;background-color: #FFFAFA;font-size:20px;"><a href='https://hmdb.ca/metabolites/HMDB0000001#biological_properties' target='_blank'>Pathways (Pathway Details in HMDB)</a></td>
							<td style="font-family: monospace;color:black !important">
								<div style="overflow-y: auto;height: 80px;">

								</div>
							</td>
						</tr>



					</tbody>
				</table>

		</div>
	</div>
	</div>
	<div class="text-center mt-5">
			<p>копирайт © ЛФиМА bebris</p>
	</div>
{{% endblock content %}}
"""
38

views = open("views.txt", "w+")
urls = open("urls.txt", "w+")




for i in range(38, 39):
    print(met.loc[i])
    hmdb_id = '–'
    synonyms = '–'
    chem_form = '–'
    iupac = '–'
    CAS = '–'
    monoi = '–'
    super_cl = '–'
    cl = '–'
    sub_cl = '–'
    norm_con = '–'
    abnorm_con = '–'

views.close()
urls.close()
