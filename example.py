import udyninexus

import numpy as np

# NOTE: this library works on the assumption that if something not optional is None everything breaks, but also
# if you can't set everything in a certain moment you can put None, but remember to change it later with setters methods

if __name__ == '__main__':
    output_dir = 'supervisor_directory'
    identifier_experiment = 1234567890 # TODO retrieved from the database


    # --- SOURCES ---
    source0 = udyninexus.Source(type='UV Laser')
    source1 = udyninexus.Source(type='LED')


    # --- BEAMS ---
    beam0 = udyninexus.Beam(
        beam_type='pump',
        incident_wavelength=350,
        incident_wavelength_units='nm',
        parameter_reliability='nominal',
        incident_polarization=42,
        beam_polarization_type='linear',
        associated_source=source0
    )


    beam1 = udyninexus.Beam(
        beam_type='probe',
        incident_wavelength=500,
        incident_wavelength_units='nm',
        parameter_reliability='measured',
        incident_polarization=24,
        beam_polarization_type='circular',
        associated_source=source1
    )


    # --- DETECTORS ---
    detector0 = udyninexus.Detector(
        detector_channel_type='multichannel',
        detector_type='photodiode',
    )


    # --- SAMPLES ---
    sample = udyninexus.Sample(
        name='udyni-sample-000',
        sample_id=000
    )


    # --- NEXUS CONTAINER ---
    nexusObj = udyninexus.NexusDataContainer(
        title = 'My title', 
        identifier_experiment = identifier_experiment,
        experiment_description = 'My description',
        beams=[beam0, beam1],
        detectors=[detector0],
        sources=[source0, source1],
        sample=sample
    )

    # import copy
    # test = copy.deepcopy(nexusObj.beams[0])


    # --- CREATE THE AXES ---
    delay_time = udyninexus.Axis('delay_tyme', range(9), 'ms')
    wavelength = udyninexus.Axis('wavelength', range(2068), 'ms')


    # --- START MEASUREMENT ---
    nexusObj.set_start_time_now()


    # --- DATA ACQUISITION ---
    rng = np.random.default_rng()
    delta_i = rng.uniform(low=0.0, high=100.0, size=(len(delay_time.data), len(wavelength.data)))


    # --- END MEASUREMENT ---
    nexusObj.set_end_time_now()


    # --- DATA ---
    data = udyninexus.Data(
        signal=delta_i,
        axes=[delay_time, wavelength]
    )

    # Every attribute can be accessed like it would be public, in reality it's private. While editing it a setter method is called that ensures
    # that the inserted data is compatible, for example here it checks that data is actually of type udyninexus.Data
    nexusObj.data = data

    udyninexus.validate_nexus_data(nexusObj)
    #udyninexus.write_nexus(nexusObj, )