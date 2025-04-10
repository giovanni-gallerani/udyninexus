import udyninexus

import numpy as np

# NOTE
# if you can't set everything in a certain moment you can put None, but remember to change it later with setters methods
# otherwise you will get an error while trying to write the NeXus file

if __name__ == '__main__':
    output_dir = 'supervisor_directory'
    identifier_experiment = 1234567890 # TODO retrieved from the database.


    # --- SOURCES ---
    source0 = udyninexus.Source(
        name_in_nexus='UV_pump',
        type='UV Laser'
    )

    # another way to do assign the values. NOTE that also this setters have validity check for types and values.
    source1 = udyninexus.Source()
    source1.name_in_nexus = 'LED_probe'
    source1.type='LED'


    # --- BEAMS ---
    beam0 = udyninexus.Beam(
        name_in_nexus='350nm_pump',
        beam_type='pump',
        incident_wavelength=350,
        incident_wavelength_units='nm',
        parameter_reliability='nominal',
        incident_polarization=42,
        beam_polarization_type='linear',
        associated_source=source0
    )


    beam1 = udyninexus.Beam(
        name_in_nexus='500nm_probe',
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
        name_in_nexus='photodiode',
        detector_channel_type='multichannel',
        detector_type='photodiode',
    )


    # --- SAMPLE ---
    sample = udyninexus.Sample(
        name='udyni-sample-709',
        sample_id=709
    )


    # --- NEXUS CONTAINER ---
    nexusObj = udyninexus.NexusContainer(
        title = 'My title', 
        identifier_experiment = identifier_experiment,
        experiment_description = 'My description',
        beams=[beam0, beam1],
        detectors=[detector0],
        sources=[source0, source1],
        sample=sample
    )


    # --- CREATE THE AXES ---
    delay_time = udyninexus.Axis(
        name='delay_tyme',
        data=range(9),
        units='ms'
    )
    wavelength = udyninexus.Axis('wavelength', range(2068), 'ms')


    # --- START MEASUREMENT ---
    nexusObj.set_start_time_now()


    # --- DATA ACQUISITION LOOP (here the data of the signal is just a random matrix) ---
    rng = np.random.default_rng()
    delta_i = rng.uniform(low=0.0, high=100.0, size=(len(delay_time.data), len(wavelength.data)))


    # --- END MEASUREMENT ---
    nexusObj.set_end_time_now()


    # --- DATA ---
    data = udyninexus.Data(
        signal_name='delta_i',
        signal_data=delta_i,
        signal_units='mOD',
        axes=[delay_time, wavelength]
    )
    nexusObj.data = data

    try:
        udyninexus.write_nexus(nexusObj, 'output_example')
    except ValueError as e:
        print('Invalid nexus_container')
        exit(1)