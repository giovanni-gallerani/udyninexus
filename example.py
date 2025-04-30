import udyninexus

from pathlib import Path
import numpy as np

# IMPORTANT NOTES
# 1) In order to give maximum flexibily is possible to not assign values to all the fields from the start
# but at nexus time creation all the required fields must have a value assigned to them.
# 2) This demo does not represent an actual experiment, it is a way of showing the capabilities of the udyninexus package.

if __name__ == '__main__':

    udyninexus.set_log_level('INFO')
    udyninexus.set_log_file('app.log', 'INFO')

    # In production environment this ID is retrieved from the experiments database through an API.
    # For more information about the APIs used in the lab see the work at: https://github.com/giovanni-gallerani/UdyniManagement
    identifier_experiment = 1234567890


    # --- SOURCES ---
    source_uv_pump = udyninexus.Source(
        name_in_nexus='UV_pump',
        type='UV Laser'
    )

    # Another way to assign values to objects attributes.
    # NOTE that attributes of the object are not direcly accessed using dot notation, these are setters with validity check for types and values.
    source_led_probe = udyninexus.Source()
    source_led_probe.name_in_nexus = 'LED_probe'
    source_led_probe.type='LED'


    # --- BEAMS ---
    beam_pump = udyninexus.Beam(
        name_in_nexus='350nm_pump',
        beam_type='pump',
        incident_wavelength=350,
        incident_wavelength_units='nm',
        parameter_reliability='nominal',
        incident_polarization=42,
        beam_polarization_type='linear',
        associated_source=source_uv_pump
    )


    beam_probe = udyninexus.Beam(
        name_in_nexus='500nm_probe',
        beam_type='probe',
        incident_wavelength=500,
        incident_wavelength_units='nm',
        parameter_reliability='measured',
        incident_polarization=24,
        beam_polarization_type='circular',
        associated_source=source_led_probe
    )


    # --- DETECTORS ---
    detector_photodiode = udyninexus.Detector(
        name_in_nexus='photodiode',
        detector_channel_type='multichannel',
        detector_type='photodiode',
    )


    # --- SAMPLE ---
    # in production environment the id of the sample is obtained by selecting one of the sample available for the experiment
    # in order to obtain the samples for the experiment a specific API is used, find more at https://github.com/giovanni-gallerani/UdyniManagement
    sample = udyninexus.Sample(
        name='UDynI test sample',
        sample_id=709 
    )


    # --- NEXUS CONTAINER --- # main class that contains all the other ones, serves as a container for all the data that must be inserted in the NeXus file
    nexusObj = udyninexus.NexusContainer(
        title = 'My title', 
        identifier_experiment = identifier_experiment,
        experiment_type='transmission spectroscopy',
        experiment_sub_type='pump-probe',
        experiment_description = 'My description',
        beams=[beam_pump, beam_probe],
        detectors=[detector_photodiode],
        sources=[source_uv_pump, source_led_probe],
        sample=sample
    )


    # --- CREATE THE AXES ---
    delay_time = udyninexus.Axis(
        name='delay_time',
        data=range(9),  # data does not have to be always specified, if not specified is deducted by the shape of signal_data during validation when writing the NeXus file.
        units='ms',  # if units are not specified, they are automatically filled with value 'index' during validation, indicating that the axis has no units.
    )

    # For the second axis the instrument that alters it is specified, so this axis will be saved in the related_instrument group and accessed in data with a NXlink
    wavelength = udyninexus.Axis('wavelength', range(2068), 'nm', related_instrument=beam_pump)

    number_of_measurements = udyninexus.Axis(
        name='number_of_measurements',
        # note that there is no data, it will be calculated automatically from the signal
        # note that there is no units of measurement, it will be put to 'index' during validation when writing the NeXus file.
    )


    # --- START MEASUREMENT ---
    nexusObj.set_start_time_now()  # automatically set start_time


    # --- DATA ACQUISITION LOOP (here the data of the signal is just a random matrix, in the lab data is obtained from the actual experimental station) ---
    rng = np.random.default_rng()
    delta_i = rng.uniform(low=0.0, high=100.0, size=(len(delay_time.data), len(wavelength.data), 10)) # 10 is the number of measurements recorded


    # --- END MEASUREMENT ---
    nexusObj.set_end_time_now()  # automatically set end_time


    # --- DATA ---
    data = udyninexus.Data(
        signal_name='delta_i',
        signal_data=delta_i,
        signal_units='mOD',
        signal_related_instrument=detector_photodiode, # instrument that acquired the data
        axes=[delay_time, wavelength, number_of_measurements] # note that the order of the axis is significant, an arbitrary number of axis can be added
    )
    nexusObj.data = data  # save data in NexusContainer
    

    filename = Path('output_example/UDynI_test_file_generated.nxs').resolve()
    try:
        udyninexus.write_nexus(nexusObj, filename)
    except (udyninexus.NexusValidationError, udyninexus.NexusSaveError) as e:
        print(e)
        exit(1)
    
    print(f"'{filename.name}' saved in '{filename.parent}'")