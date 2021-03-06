orgxmldict = dict(
    system_name={''},
    system_binary={''},
    system_planet={''},
    system_star={''},
    system_star_spectraltype={''},
    system_rightascension_str={'ra_str'},
    system_rightascension={'ra'},
    system_declination_str={'dec_str'},
    system_declination={'dec'},
    system_distance={'st_dist', 'star_distance'},
    system_distance_errorplus={'st_disterr1', 'star_distance_error_max'},
    system_distance_errorminus={'st_disterr2', 'star_distance_error_min'},
    system_epoch={''},
    system_videolink={''},
    system_magB={''},
    system_magH={''},
    system_magI={''},
    system_magJ={''},
    system_magK={''},
    system_magR={''},
    system_magU={''},
    system_magV={'st_optmag'},
    system_magV_errorplus_and_errorminus={'st_optmagerr'},

    planet_name={'pl_name', 'name'},
    planet_name_alternate={'alternate_names'},
    planet_list={''},
    planet_semimajoraxis={'pl_orbsmax', 'semi_major_axis'},
    planet_semimajoraxis_errorplus={'pl_orbsmaxerr1', 'semi_major_axis_error_max'},
    planet_semimajoraxis_errorminus={'pl_orbsmaxerr2', 'semi_major_axis_error_min'},
    planet_eccentricity={'pl_orbeccen', 'eccentricity'},
    planet_eccentricity_errorplus={'pl_orbeccenerr1', 'eccentricity_error_max'},
    planet_eccentricity_errorminus={'pl_orbeccenerr2', 'eccentricity_error_min'},
    planet_periastron={'pl_orblper', 'omega'},
    planet_periastron_errorplus={'pl_orblpererr1', 'omega_error_max'},
    planet_periastron_errorminus={'pl_orblpererr2', 'omega_error_min'},
    planet_longitude={''},
    planet_ascending={''},
    planet_inclination={'pl_orbincl', 'inclination'},
    planet_inclination_errorplus={'pl_orbinclerr1', 'inclination_error_max'},
    planet_inclination_errorminus={'pl_orbinclerr2', 'inclination_error_min'},
    planet_impactparameter={'pl_imppar', 'impact_parameter'},
    planet_impactparameter_errorplus={'pl_impparerr1', 'impact_parameter_error_max'},
    planet_impactparameter_errorminus={'pl_impparerr2', 'impact_parameter_error_min'},
    planet_meananomaly={''},
    planet_period={'pl_orbper', 'orbital_period'},
    planet_period_errorplus={'pl_orbpererr1', 'orbital_period_error_max'},
    planet_period_errorminus={'pl_orbpererr2', 'orbital_period_error_min'},
    planet_transittime={'pl_tranmid', 'tzero_tr'},
    planet_transittime_errorplus={'pl_tranmiderr1', 'tzero_tr_error_max'},
    planet_transittime_errorminus={'pl_tranmiderr2', 'tzero_tr_error_min'},
    planet_periastrontime={'pl_orbtper', 'tperi'},
    planet_periastrontime_errorplus={'pl_orbtpererr1', 'tperi_error_max'},
    planet_periastrontime_errorminus={'pl_orbtpererr2', 'tperi_error_min'},
    planet_maximumrvtime={''},
    planet_separation={''},
    planet_mass={'pl_bmassj', 'mass'},
    planet_mass_errorplus={'pl_bmassjerr1', ' mass_error_max'},
    planet_mass_errorminus={'pl_bmassjerr2', 'mass_error_min'},
    planet_radius={'pl_radj', 'radius'},
    planet_radius_errorplus={'pl_radjerr1', 'radius_error_max'},
    planet_radius_errorminus={'pl_radjerr2', 'radius_error_min'},
    planet_temperature={'pl_eqt', 'temp_calculated'},
    planet_temperature_errorplus={'pl_eqterr1', },
    planet_temperature_errorminus={'pl_eqterr2', },
    planet_age={''},
    planet_age_errorplus={''},
    planet_age_errorminus={''},
    planet_discoverymethod={'pl_discmethod', 'detection_type'},
    planet_istransiting={'pl_tranflag', },
    planet_description={''},
    planet_discoveryyear={'pl_disc', 'discovered'},
    planet_lastupdate={'rowupdate', 'updated'},
    planet_image={''},
    planet_imagedescription={''},
    planet_spinorbitalignment={''},
    planet_positionangle={''},
    planet_metallicity={''},
    planet_metallicity_errorplus={''},
    planet_metallicity_errorminus={''},
    planet_spectraltype={''},
    planet_magB={''},
    planet_magB_errorplus={''},
    planet_magB_errorminus={''},
    planet_magH={''},
    planet_magH_errorplus={''},
    planet_magH_errorminus={''},
    planet_magI={''},
    planet_magI_errorplus={''},
    planet_magI_errorminus={''},
    planet_magJ={''},
    planet_magJ_errorplus={''},
    planet_magJ_errorminus={''},
    planet_magK={''},
    planet_magK_errorplus={''},
    planet_magK_errorminus={''},
    planet_magR={''},
    planet_magR_errorplus={''},
    planet_magR_errorminus={''},
    planet_magU={''},
    planet_magU_errorplus={''},
    planet_magU_errorminus={''},
    planet_magV={''},
    planet_magV_errorplus={''},
    planet_magV_errorminus={''},
    star_name={'star_name', 'pl_hostname'},
    star_name_alternate={'star_alternate_names'},
    star_planet={''},
    star_mass={'st_mass', 'star_mass'},
    star_mass_errorplus={'st_masserr1', 'star_mass_error_max'},
    star_mass_errorminus={'st_masserr2', 'star_mass_error_min'},
    star_radius={'st_rad', 'star_radius'},
    star_radius_errorplus={'st_raderr1', 'star_radius_error_max'},
    star_radius_errorminus={'st_raderr2', 'star_radius_error_min'},
    star_temperature={'st_teff', 'star_teff'},
    star_temperature_errorplus={'st_tefferr1', 'star_teff_error_max'},
    star_temperature_errorminus={'st_tefferr2', 'star_teff_error_min'},
    star_age={'st_age', 'star_age'},
    star_age_errorplus={'st_ageerr1', 'star_age_error_max'},
    star_age_errorminus={'st_ageerr2', 'star_age_error_min'},
    star_metallicity={'st_metfe', 'star_metallicity'},
    star_metallicity_errorplus={'st_metfeerr1', 'star_metallicity_error_max'},
    star_metallicity_errorminus={'st_metfeerr2', 'star_metallicity_error_min'},
    star_spectraltype={'st_spstr', 'star_sp_type'},
    star_magB={'st_bj'},
    star_magB_errorplus_and_errorminus={'st_bjerr'},
    star_magH={'st_h', 'mag_h'},
    star_magH_errorplus_and_errorminus={'st_herr'},
    star_magI={'st_ic', 'mag_i'},
    star_magI_errorplus_and_errorminus={'st_icerr'},
    star_magJ={'st_j', 'mag_j'},
    star_magJ_errorplus_and_errorminus={'st_jerr'},
    star_magK={'st_k', 'mag_k'},
    star_magK_errorplus_and_errorminus={'st_kerr'},
    star_magR={'st_rc'},
    star_magR_errorplus_and_errorminus={'st_rcerr'},
    star_magU={'st_uj'},
    star_magU_errorplus_and_errorminus={'st_ujerr'},
    star_magV={'st_vj', 'mag_v'},
    star_magV_errorplus_and_errorminus={'st_vjerr'},
    binary_name={''},
    binary_binary={''},
    binary_star={''},
    binary_planet={''},
    binary_semimajoraxis={''},
    binary_eccentricity={''},
    binary_periastron={''},
    binary_longitude={''},
    binary_meananomaly={''},
    binary_ascendingnode={''},
    binary_inclination={''},
    binary_period={''},
    binary_transittime={''},
    binary_periastrontime={''},
    binary_maximumrvtime={''},
    binary_separation={''},
    binary_positionangle={''},
    binary_magB={''},
    binary_magH={''},
    binary_magI={''},
    binary_magJ={''},
    binary_magK={''},
    binary_magR={''},
    binary_magU={''},
    binary_magV={''},
    planet_letter={'pl_letter'})

orgxmlconvert = dict(
    system_name='<system><name>',
    planet_letter='pl_letter',
    system_binary='<system><binary>',
    system_planet='<system><planet>',
    system_star='<system><star>',
    system_star_spectraltype='<system><star><spectraltype>',
    system_rightascension_str='<system><rightascension>',
    system_rightascension='<system><rightascension>str',
    system_declination_str='<system><declination>',
    system_declination='<system><declination>str',
    system_distance='<system><distance>',
    system_distance_errorplus='<system><distance>errorplus',
    system_distance_errorminus='<system><distance>errorminus',
    system_epoch='<system><epoch>',
    system_videolink='<system><videolink>',
    system_magB='<system><magB>',
    system_magH='<system><magH>',
    system_magI='<system><magI>',
    system_magJ='<system><magJ>',
    system_magK='<system><magK>',
    system_magR='<system><magR>',
    system_magU='<system><magU>',
    system_magV='<system><magV>',
    system_magV_errorplus_and_errorminus='<system><magV>errorplus_and_errorminus',
    planet_name='<planet><name>',
    planet_name_alternate='<planet><name>alternate',
    planet_list='<planet><list>',
    planet_semimajoraxis='<planet><semimajoraxis>',
    planet_semimajoraxis_errorplus='<planet><semimajoraxis>errorplus',
    planet_semimajoraxis_errorminus='<planet><semimajoraxis>errorminus',
    planet_eccentricity='<planet><eccentricity>',
    planet_eccentricity_errorplus='<planet><eccentricity>errorplus',
    planet_eccentricity_errorminus='<planet><eccentricity>errorminus',
    planet_periastron='<planet><periastron>',
    planet_periastron_errorplus='<planet><periastron>errorplus',
    planet_periastron_errorminus='<planet><periastron>errorminus',
    planet_longitude='<planet><longitude>',
    planet_ascending='<planet><ascending>',
    planet_inclination='<planet><inclination>',
    planet_inclination_errorplus='<planet><inclination>errorplus',
    planet_inclination_errorminus='<planet><inclination>errorminus',
    planet_impactparameter='<planet><impactparameter>',
    planet_impactparameter_errorplus='<planet><impactparameter>errorplus',
    planet_impactparameter_errorminus='<planet><impactparameter>errorminus',
    planet_meananomaly='<planet><meananomaly>',
    planet_period='<planet><period>',
    planet_period_errorplus='<planet><period>errorplus',
    planet_period_errorminus='<planet><period>errorminus',
    planet_transittime='<planet><transittime>',
    planet_transittime_errorplus='<planet><transittime>errorplus',
    planet_transittime_errorminus='<planet><transittime>errorminus',
    planet_periastrontime='<planet><periastrontime>',
    planet_periastrontime_errorplus='<planet><periastrontime>errorplus',
    planet_periastrontime_errorminus='<planet><periastrontime>errorminus',
    planet_maximumrvtime='<planet><maximumrvtime>',
    planet_separation='<planet><separation>',
    planet_mass='<planet><mass>',
    planet_mass_errorplus='<planet><mass>errorplus',
    planet_mass_errorminus='<planet><mass>errorminus',
    planet_radius='<planet><radius>',
    planet_radius_errorplus='<planet><radius>errorplus',
    planet_radius_errorminus='<planet><radius>errorminus',
    planet_temperature='<planet><temperature>',
    planet_temperature_errorplus='<planet><temperature>errorplus',
    planet_temperature_errorminus='<planet><temperature>errorminus',
    planet_age='<planet><age>',
    planet_age_errorplus='<planet><age>errorplus',
    planet_age_errorminus='<planet><age>errorminus',
    planet_discoverymethod="<planet><discoverymethod>",
    planet_istransiting='<planet><istransiting>',
    planet_description='<planet><description>',
    planet_discoveryyear='<planet><discoveryyear>',
    planet_lastupdate='<planet><lastupdate>',
    planet_image='<planet><image>',
    planet_imagedescription='<planet><imagedescription>',
    planet_spinorbitalignment='<planet><spinorbitalignment>',
    planet_positionangle='<planet><positionangle>',
    planet_metallicity='<planet><metallicity>',
    planet_metallicity_errorplus='<planet><metallicity>errorplus',
    planet_metallicity_errorminus='<planet><metallicity>errorminus',
    planet_spectraltype='<planet><spectraltype>',
    planet_magB='<planet><magB>',
    planet_magB_errorplus='<planet><magB>errorplus',
    planet_magB_errorerrorminus='<planet><magB>errorerrorminus',
    planet_magH='<planet><magH>',
    planet_magH_errorplus='<planet><magH>errorplus',
    planet_magH_errorerrorminus='<planet><magH>errorerrorminus',
    planet_magI='<planet><magI>',
    planet_magI_errorplus='<planet><magI>errorplus',
    planet_magI_errorerrorminus='<planet><magI>errorerrorminus',
    planet_magJ='<planet><magJ>',
    planet_magJ_errorplus='<planet><magJ>errorplus',
    planet_magJ_errorerrorminus='<planet><magJ>errorerrorminus',
    planet_magK='<planet><magK>',
    planet_magK_errorplus='<planet><magK>errorplus',
    planet_magK_errorerrorminus='<planet><magK>errorerrorminus',
    planet_magR='<planet><magR>',
    planet_magR_errorplus='<planet><magR>errorplus',
    planet_magR_errorerrorminus='<planet><magR>errorerrorminus',
    planet_magU='<planet><magU>',
    planet_magU_errorplus='<planet><magU>errorplus',
    planet_magU_errorerrorminus='<planet><magU>errorerrorminus',
    planet_magV='<planet><magV>',
    planet_magV_errorplus='<planet><magV>errorplus',
    planet_magV_errorerrorminus='<planet><magV>errorerrorminus',
    star_name='<star><name>',
    star_name_alternate='<star><name>alternate',
    star_planet='<star><planet>',
    star_mass='<star><mass>',
    star_mass_errorplus='<star><mass>errorplus',
    star_mass_errorminus='<star><mass>errorminus',
    star_radius='<star><radius>',
    star_radius_errorplus='<star><radius>errorplus',
    star_radius_errorminus='<star><radius>errorminus',
    star_temperature='<star><temperature>',
    star_temperature_errorplus='<star><temperature>errorplus',
    star_temperature_errorminus='<star><temperature>errorminus',
    star_age='<star><age>',
    star_age_errorplus='<star><age>errorplus',
    star_age_errorminus='<star><age>errorminus',
    star_metallicity='<star><metallicity>',
    star_metallicity_errorplus='<star><metallicity>errorplus',
    star_metallicity_errorminus='<star><metallicity>errorminus',
    star_spectraltype='<star><spectraltype>',
    star_magB='<star><magB>',
    star_magB_errorplus_and_errorminus='<star><magB>errorplus_and_errorminus',
    star_magH='<star><magH>',
    star_magH_errorplus_and_errorminus='<star><magH>errorplus_and_errorminus',
    star_magI='<star><magI>',
    star_magI_errorplus_and_errorminus='<star><magI>errorplus_and_errorminus',
    star_magJ='<star><magJ>',
    star_magJ_errorplus_and_errorminus='<star><magJ>errorplus_and_errorminus',
    star_magK='<star><magK>',
    star_magK_errorplus_and_errorminus='<star><magK>errorplus_and_errorminus',
    star_magR='<star><magR>',
    star_magR_errorplus_and_errorminus='<star><magR>errorplus_and_errorminus',
    star_magU='<star><magU>',
    star_magU_errorplus_and_errorminus='<star><magU>errorplus_and_errorminus',
    star_magV='<star><magV>',
    star_magV_errorplus_and_errorminus='<star><magV>errorplus_and_errorminus',
    binary_name='<binary><name>',
    binary_binary='<binary><binary>',
    binary_star='<binary><star>',
    binary_planet='<binary><planet>',
    binary_semimajoraxis='<binary><semimajoraxis>',
    binary_eccentricity='<binary><eccentricity>',
    binary_periastron='<binary><periastron>',
    binary_longitude='<binary><longitude>',
    binary_meananomaly='<binary><meananomaly>',
    binary_ascendingnode='<binary><ascendingnode>',
    binary_inclination='<binary><inclination>',
    binary_period='<binary><period>',
    binary_transittime='<binary><transittime>',
    binary_periastrontime='<binary><periastrontime>',
    binary_maximumrvtime='<binary><maximumrvtime>',
    binary_separation='<binary><separation>',
    binary_positionangle='<binary><positionangle>',
    binary_magB='<binary><magB>',
    binary_magH='<binary><magH>',
    binary_magI='<binary><magI>',
    binary_magJ='<binary><magJ>',
    binary_magK='<binary><magK>',
    binary_magR='<binary><magR>',
    binary_magU='<binary><magU>',
    binary_magV='<binary><magV>'
)
