import udyninexus

from pathlib import Path
import numpy as np

# IMPORTANT NOTE
# In order to give maximum flexibily is possible to not assign values to all the field from the start
# but at nexus time creation all the required fields must have a value assigned to them.

if __name__ == '__main__':

    # In production environment this ID is retrieved from the experiments database through an API.
    # For more information about the APIs used in the lab see the work at: https://github.com/giovanni-gallerani/UdyniManagement
    identifier_experiment = 1234567890


    # --- SOURCES ---
    source0 = udyninexus.Source(
        name_in_nexus='UV_pump',
        type='UV Laser'
    )

    # Another way to assign values to objects attributes.
    # NOTE that attributes of the object are not direcly accessed using dot notation, these are setters with validity check for types and values.
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
        name='delay_time',
        data=range(9),
        units='ms'
    )
    wavelength = udyninexus.Axis('wavelength', range(2068), 'ms')


    # --- START MEASUREMENT ---
    nexusObj.set_start_time_now()


    # --- DATA ACQUISITION LOOP (here the data of the signal is just a random matrix, in the lab data is obtained from the experimental station) ---
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
    

    filename = Path('output_example/Udiny_test_file.nxs').resolve()
    try:
        udyninexus.write_nexus(nexusObj, filename)
    except (udyninexus.NexusValidationError, udyninexus.NexusSaveError) as e:
        print(e)
        exit(1)
    
    print(f"'{filename.name}' saved in '{filename.parent}'")