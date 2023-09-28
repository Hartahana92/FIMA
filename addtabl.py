# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class MetaboliteInf(models.Model):
    metabolite = models.TextField(db_column='Metabolite', blank=True, null=True)  # Field name made lowercase.
    metabolite_name = models.TextField(db_column='metabolite name', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    metabolite_paper_field = models.TextField(db_column='metabolite (paper)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    field_metabolite_name_field = models.TextField(db_column='(metabolite name)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    adduct = models.TextField(blank=True, null=True)
    pubchem_id = models.TextField(db_column='PUBCHEM ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hmdb_id = models.TextField(db_column='HMDB ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    average_molecular_weight = models.TextField(db_column='Average Molecular Weight', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    monisotopic_molecular_weight = models.TextField(db_column='Monisotopic Molecular Weight', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kegg = models.TextField(blank=True, null=True)
    pathway = models.TextField(db_column='Pathway', blank=True, null=True)  # Field name made lowercase.
    sub_pathway = models.TextField(db_column='sub-pathway', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    m_z = models.TextField(db_column='M/Z', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    specimen = models.TextField(db_column='Specimen', blank=True, null=True)  # Field name made lowercase.
    function = models.TextField(blank=True, null=True)
    participantsn_cancer_type_field = models.TextField(db_column='participantsn(cancer type)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    stage = models.TextField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    gender_m_text_f_field = models.TextField(db_column='gender (M TEXT, F)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    age_mean_range_m_f_field = models.TextField(db_column='age mean(range) (M / F)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    smoking_status = models.TextField(db_column='smoking status', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    participantsn_control_field = models.TextField(db_column='participantsn(control)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    number_1 = models.IntegerField(db_column='number.1', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    gender_m_f_field = models.TextField(db_column='gender (M / F)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    age_mean_range_m_f_field_0 = models.TextField(db_column='age mean(range) (M / F).', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because of name conflict.
    smoking_status_1 = models.TextField(db_column='smoking status.1', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    chromatography = models.TextField(db_column='Chromatography', blank=True, null=True)  # Field name made lowercase.
    ion_source = models.TextField(db_column='Ion source', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    positive_negative_mode = models.TextField(db_column='Positive/Negative mode', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mass_analyzer = models.TextField(db_column='Mass analyzer', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    identification_level = models.TextField(db_column='Identification level', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    data_processing_software = models.TextField(db_column='Data processing software', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    database_search = models.TextField(db_column='Database search', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    statistical_software = models.TextField(db_column='statistical software', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    statistical_difference_method = models.TextField(db_column='statistical difference method', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    mean_concentration_case_field = models.TextField(db_column='mean concentration (case)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    mean_concentration_control_field = models.TextField(db_column='mean  concentration (control)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    fold_change_n_case_control_field = models.TextField(db_column='fold change n(case/ control)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    raw_p_value = models.TextField(db_column='RAW p-value', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fdr = models.TextField(blank=True, null=True)
    vip = models.TextField(blank=True, null=True)
    classification_method = models.TextField(db_column='Classification method', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cutoff_value = models.TextField(db_column='Cutoff value', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    auroc_95_ci_field = models.TextField(db_column='AUROC (95%CI)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    sensitivity_field = models.TextField(db_column='Sensitivity (%)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    specificity_field = models.TextField(db_column='Specificity (%)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    accuracy_field = models.TextField(db_column='Accuracy (%)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    survival_analysis_method = models.TextField(db_column='Survival analysis method', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    time_cut_offs_field = models.TextField(db_column='time cut-offs (<=/>)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    hr_95_ci_field = models.TextField(db_column='HR (95%CI)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    p_value = models.TextField(db_column='p-value', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    fdr_1 = models.TextField(db_column='FDR.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase.
    author_emphasized_biomarkers = models.TextField(db_column='author-emphasized biomarkers', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    other_information = models.TextField(db_column='other information', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pubmed_id = models.IntegerField(db_column='Pubmed ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    authors = models.TextField(db_column='Authors', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Metabolite_inf'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BreastCancerPaper(models.Model):
    country = models.TextField(blank=True, null=True)
    pubmed_id = models.IntegerField(db_column='Pubmed ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    authors = models.TextField(blank=True, null=True)
    comparative_study = models.TextField(db_column='Comparative study', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    participants_cancer_control_field = models.TextField(db_column='participants (Cancer/ Control)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    material_source_field = models.TextField(db_column='material (source)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    function = models.TextField(blank=True, null=True)
    participants_n_cancer_type_field = models.TextField(db_column='participants\\n(cancer type)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    stage = models.TextField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    gender_m_f_field = models.TextField(db_column='gender (M / F)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    age_mean_range_m_f_field = models.TextField(db_column='age mean (range) (M / F)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    smoking_status = models.TextField(db_column='smoking status', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    participants_control_field = models.TextField(db_column='participants (control)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    number_1 = models.IntegerField(db_column='number.1', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    gender_m_f_1 = models.TextField(db_column='gender (M / F).1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    age_mean_range_m_f_field_0 = models.TextField(db_column='age mean (range) (M / F).', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because of name conflict.
    smoking_status_1 = models.TextField(db_column='smoking status.1', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    chromatography = models.TextField(blank=True, null=True)
    ion_source = models.TextField(db_column='ion source', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    positive_negative_mode = models.TextField(db_column='positive/ negative mode', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    mass_analyzer = models.TextField(db_column='mass analyzer', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    identification_level = models.TextField(db_column='Identification level', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    data_processing_software = models.TextField(db_column='data processing software', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    database_search = models.TextField(db_column='database search', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    statistical_difference_method = models.TextField(db_column='statistical difference method', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    classification_method = models.TextField(db_column='classification method', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    survival_analysis_method = models.TextField(db_column='survival analysis method', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'breast_cancer_paper'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PaperInf(models.Model):
    country = models.TextField(blank=True, null=True)
    pubmed_id = models.IntegerField(db_column='Pubmed ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    authors = models.TextField(blank=True, null=True)
    comparative_study = models.TextField(db_column='Comparative study', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    participants_cancer_control_field = models.TextField(db_column='participants (Cancer/ Control)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    material_source_field = models.TextField(db_column='material (source)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    function = models.TextField(blank=True, null=True)
    participants_cancer_type_field = models.TextField(db_column='Participants (cancer type)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    stage = models.TextField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    gender_m_f_field = models.TextField(db_column='gender (M / F)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    age_mean_range_m_f_field = models.TextField(db_column='age mean (range) (M / F)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    smoking_status = models.TextField(db_column='smoking status', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    participants_control_field = models.TextField(db_column='Participants (control)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    number_1 = models.TextField(db_column='number.1', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    gender_m_f_1 = models.TextField(db_column='gender (M / F).1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    age_mean_range_m_f_field_0 = models.TextField(db_column='age mean (range) (M / F).', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because of name conflict.
    smoking_status_1 = models.TextField(db_column='smoking status.1', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    chromatography = models.TextField(blank=True, null=True)
    ion_source = models.TextField(db_column='ion source', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    positive_negative_mode = models.TextField(db_column='positive/ negative mode', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    mass_analyzer = models.TextField(db_column='mass analyzer', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    identification_level = models.TextField(db_column='Identification level', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    data_processing_software = models.TextField(db_column='data processing software', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    database_search = models.TextField(db_column='database search', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    statistical_difference_method = models.TextField(db_column='statistical difference method', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    classification_method = models.TextField(db_column='classification method', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    survival_analysis_method = models.TextField(db_column='survival analysis method', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    year = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paper_inf'
