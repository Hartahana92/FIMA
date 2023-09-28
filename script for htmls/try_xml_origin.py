import pandas as pd
import xml.etree.ElementTree as ET



path = 'D:\Work\LABWORKS\silkroad\\'
used = set()

def iter_metabolites(filename):
    ctx = ET.iterparse(filename)
    for _, metabolite in ctx:
        if metabolite.tag != '{http://www.hmdb.ca}metabolite':
            continue
        yield metabolite
        metabolite.clear()


v = open('views.txt', 'w+')
u = open('urls.txt', 'w+')

# For every metabolite in XML
for metabolite in iter_metabolites(path + 'serum_metabolites.xml'):
    # Reset df for new iteration
    df_metabolite = pd.DataFrame()

    HMDB_id = metabolite.find('{http://www.hmdb.ca}accession').text
    name = metabolite.find('{http://www.hmdb.ca}name').text

    print(HMDB_id + ': ' + name)

    ## Making abnormal table
    df_HMDB = pd.DataFrame()
    for concentration in metabolite.find('{http://www.hmdb.ca}abnormal_concentrations'):
        try:
            conc = concentration.find('{http://www.hmdb.ca}concentration_value').text
        except:
            conc = '-'
        try:
            unit = concentration.find('{http://www.hmdb.ca}concentration_units').text
        except:
            unit = '-'
        try:
            sample = concentration.find('{http://www.hmdb.ca}biospecimen').text
        except:
            sample = '-'
        try:
            age = concentration.find('{http://www.hmdb.ca}patient_age').text
        except:
            age = '-'
        try:
            sex = concentration.find('{http://www.hmdb.ca}patient_sex').text
        except:
            sex = '-'
        try:
            cond = concentration.find('{http://www.hmdb.ca}patient_information').text
        except:
            cond = '-'

        try:
            df_measurement = pd.DataFrame({'Biospecimen': [sample], 'Value': [conc + ' ' + unit], 'Age': [age], 'Sex': [sex], 'Condition': [cond]})
        except:
            df_measurement = pd.DataFrame([])
        '''
        Collect all entries of a metabolite in single df
        '''
        df_metabolite = df_metabolite.append(df_measurement, ignore_index=True)

    # Collect all entries of every metabolite in single df
    df_HMDB = df_HMDB.append(df_metabolite)


    if df_HMDB.empty == False:
        abnormal_table = df_HMDB.to_html(justify='left', border=0, classes='table table-border table-hover', index=False)

    ## Making normal table
    df_HMDB = pd.DataFrame()
    for concentration in metabolite.find('{http://www.hmdb.ca}normal_concentrations'):
        try:
            conc = concentration.find('{http://www.hmdb.ca}concentration_value').text
        except:
            conc = '-'
        try:
            unit = concentration.find('{http://www.hmdb.ca}concentration_units').text
        except:
            unit = '-'
        try:
            sample = concentration.find('{http://www.hmdb.ca}biospecimen').text
        except:
            sample = '-'
        try:
            age = concentration.find('{http://www.hmdb.ca}subject_age').text
        except:
            age = '-'
        try:
            sex = concentration.find('{http://www.hmdb.ca}subject_sex').text
        except:
            sex = '-'
        try:
            cond = concentration.find('{http://www.hmdb.ca}subject_condition').text
        except:
            cond = '-'

        try:
            df_measurement = pd.DataFrame({'Biospecimen': [sample], 'Value': [conc + ' ' + unit], 'Age': [age], 'Sex': [sex], 'Condition': [cond]})
        except:
            df_measurement = pd.DataFrame([])
        '''
        Collect all entries of a metabolite in single df
        '''
        df_metabolite = df_metabolite.append(df_measurement, ignore_index=True)

    # Collect all entries of every metabolite in single df
    df_HMDB = df_HMDB.append(df_metabolite)

    if df_HMDB.empty == False:
        normal_table = df_HMDB.to_html(justify='left', border=0, classes='table table-border table-hover', index=False)


    #Synonyms
    s = []
    for synonym in metabolite.find('{http://www.hmdb.ca}synonyms'):
        s.append(synonym.text)

    synonyms = ''
    for synonym in s:
        synonyms = synonyms + '<h6>' + synonym + '</h6>' + '\n'
    #end of making synonyms

    #chemical formula
    try:
        chem_formula = metabolite.find('{http://www.hmdb.ca}chemical_formula').text
    except:
        chem_formula = '-'
    #endcas_registry_number

    #iupac_name
    try:
        iupac_name = metabolite.find('{http://www.hmdb.ca}iupac_name').text
    except:
        iupac_name = '-'
    #end

    #CAS registry number
    try:
        cas_r_n = metabolite.find('{http://www.hmdb.ca}cas_registry_number').text
    except:
        cas_r_n = '-'
    #end

    #monisotopic_molecular_weight
    try:
        monoistopic = metabolite.find('{http://www.hmdb.ca}monisotopic_molecular_weight').text
    except:
        monoistopic = '-'
    #end

    #classes
    try:
        super_cl = metabolite.find('{http://www.hmdb.ca}taxonomy').find('{http://www.hmdb.ca}super_class').text
        cl = metabolite.find('{http://www.hmdb.ca}taxonomy').find('{http://www.hmdb.ca}class').text
        sub_cl = metabolite.find('{http://www.hmdb.ca}taxonomy').find('{http://www.hmdb.ca}sub_class').text
    except:
        super_cl = '-'
        cl = '-'
        sub_cl = '-'
    #end



    html = f"""
    {{% extends "browse/index.html" %}}
    {{% load static %}}
    {{% block content %}}

    	<div class="container">
    		<br>
    		<div class = "card">
    				<div class="card-header">
    						<h3 style="display: inline-block;"> Showing information for {HMDB_id} (&#39;1-methylhistidine&#39;) </h3>
    				</div>


    			<div class="card-body">




    				<table class="table table-border " style="width: 100%;table-layout: fixed;" id="hmdb">
    					<thead style="background-color: #E6E6FA;">
    						<td colspan="2"><h4 style="float: left;">Metabolite information</h4></td>
    					</thead>
    					<tbody style="background-color: white;">
    						<tr>
    							<td style="width: 40%;font-family: monospace;color:black !important;background-color:#FFFAFA;font-size:20px;" >HMDB ID</td>
    							<td style="font-family: monospace;color:black !important">{HMDB_id}</td>
    						</tr>
    						<tr>
    							<td style="width: 40%; font-family: monospace;color:black !important;background-color: #FFFAFA;font-size:20px;">Synonyms</td>
    							<td style="font-family: monospace;color:black !important">
    								<div style="overflow-y: auto;height: 150px;">

    										{synonyms}

    								</div>
    							</td>
    						</tr>
    						<tr>
    							<td style="width: 40%; font-family: monospace;color:black !important;background-color:#FFFAFA;font-size:20px;">Chemical formula</td>
    							<td style="font-family: monospace;color:black !important">{chem_formula}</td>
    						</tr>
    						<tr>
    							<td style="width: 40%; font-family: monospace;color:black !important;background-color: #FFFAFA;font-size:20px;">IUPAC name</td>
    							<td style="font-family: monospace;color:black !important"><div style="width: 100%;overflow-x: auto;">{iupac_name}</div></td>
    						</tr>
    						<tr>
    							<td style="width: 40%; font-family: monospace;color:black !important;background-color: #FFFAFA;font-size:20px;">CAS registry number</td>
    							<td style="font-family: monospace;color:black !important">{cas_r_n}</td>
    						</tr>
    						<tr>
    							<td style="width: 40%; font-family: monospace;color:black !important;background-color: #FFFAFA;font-size:20px;">Monoisotopic molecular weight</td>
    							<td style="font-family: monospace;color:black !important">{monoistopic}</td>
    						</tr>
    						<tr style="background-color: #E6E6FA !important;">
    							<td colspan="2"><h4 style="float: left;">Chemical taxonomy</h4></td>
    						</tr>
    						<tr>
    							<td style="width: 40%; font-family: monospace;color:black !important;background-color: #FFFAFA;font-size:20px;">Super class</td>
    							<td style="font-family: monospace;color:black !important">{super_cl}</td>
    						</tr>
    						<tr>
    							<td style="width: 40%; font-family: monospace;color:black !important;background-color: #FFFAFA;font-size:20px;">Class</td>
    							<td style="font-family: monospace;color:black !important">{cl}</td>
    						</tr>
    						<tr>
    							<td style="width: 40%; font-family: monospace;color:black !important;background-color: #FFFAFA;font-size:20px;">Sub class</td>
    							<td style="font-family: monospace;color:black !important">{sub_cl}</td>
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
                                            {normal_table}
    										<!-- normal table-->
    								</td>
    						</tr>
    						<tr>
    								<td colspan="2" style="width: 40%; font-family: monospace;color:black !important;background-color: #FFFAFA;font-size:20px;">Abnormal concentrations</td>
    						</tr>
    						<tr>
    								<td colspan="2">
                                        {abnormal_table}
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
    used.add(HMDB_id)
    name = name.lower()
    try:
        h = open(f'_{name}.html', 'w+')
        h.write(html)


        v.write(f"""def {HMDB_id}(request):
        return render(request, 'browse/_{name}')""")
        v.write('\n\n')
        u.write(f"path('browse_metabolites/{name}/', views.{HMDB_id}, name='{HMDB_id}'),")
        u.write('\n')
    except:
        continue



v.close()
u.close()
