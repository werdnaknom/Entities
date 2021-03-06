import pandas as pd
import numpy as np

dataframe_row = pd.Series({'dut': 'Mentor Harbor', 'pba': 'K31123-001', 'base':
    'K31123', 'dash': 1, 'rework': 0, 'software': None, 'serial_number': ' '
                                                                         'A6081C',
                           'runid': 2, 'comments': 'Configuration #1',
                           'status_json_status': 'Aborted',
                           'status_json_time': '10/4/2019 10:32',
                           'status_json_info': 'Test was aborted by user after 1 Hours 30 Minutes 11 Seconds',
                           'status_json_runtime_total_seconds': 5411,
                           'status_json_runtime_hours': 1,
                           'status_json_runtime_minutes': 30,
                           'status_json_runtime_seconds': 11,
                           'system_info_json_probes_channel_1': 'CH1',
                           'system_info_json_probes_type_1': 'TDP1000',
                           'system_info_json_probes_serial_number_1': 'B017419',
                           'system_info_json_probes_units_1': 'V',
                           'system_info_json_probes_cal_status_1': 'D',
                           'system_info_json_probes_channel_2': 'CH2',
                           'system_info_json_probes_type_2': 'TCP0030A',
                           'system_info_json_probes_serial_number_2': 'C003949',
                           'system_info_json_probes_units_2': 'A',
                           'system_info_json_probes_cal_status_2': 'D',
                           'system_info_json_probes_channel_3': 'CH3',
                           'system_info_json_probes_type_3': 'TDP1000',
                           'system_info_json_probes_serial_number_3': 'B017389',
                           'system_info_json_probes_units_3': 'V',
                           'system_info_json_probes_cal_status_3': 'D',
                           'system_info_json_probes_channel_4': 'CH4',
                           'system_info_json_probes_type_4': 'TDP1000',
                           'system_info_json_probes_serial_number_4': 'B017411',
                           'system_info_json_probes_units_4': 'V',
                           'system_info_json_probes_cal_status_4': 'D',
                           'system_info_json_probes_channel_5': 'CH5',
                           'system_info_json_probes_type_5': 'TDP1000',
                           'system_info_json_probes_serial_number_5': 'B017420',
                           'system_info_json_probes_units_5': 'V',
                           'system_info_json_probes_cal_status_5': 'D',
                           'system_info_json_probes_channel_6': 'CH6',
                           'system_info_json_probes_type_6': 'TDP1000',
                           'system_info_json_probes_serial_number_6': 'B017396',
                           'system_info_json_probes_units_6': 'V',
                           'system_info_json_probes_cal_status_6': 'D',
                           'system_info_json_probes_channel_7': 'CH7',
                           'system_info_json_probes_type_7': 'TDP1000',
                           'system_info_json_probes_serial_number_7': 'B012435',
                           'system_info_json_probes_units_7': 'V',
                           'system_info_json_probes_cal_status_7': 'D',
                           'system_info_json_probes_channel_8': 'CH8',
                           'system_info_json_probes_type_8': 'TDP1000',
                           'system_info_json_probes_serial_number_8': 'B017412',
                           'system_info_json_probes_units_8': 'V',
                           'system_info_json_probes_cal_status_8': 'D',
                           'system_info_json_scope_serial_number': None,
                           'system_info_json_power_supply_serial_number': None,
                           'testrun_json_dut': 'Mentor Harbor',
                           'testrun_json_pba': 'K31123-001',
                           'testrun_json_rework': 0,
                           'testrun_json_serial_number': ' A6081C',
                           'testrun_json_technician': 'Tony Strojan',
                           'testrun_json_test_station': 'lno-test11',
                           'testrun_json_test_points_1': '12V_MAIN',
                           'testrun_json_test_points_2': '12V_MAIN CURRENT',
                           'testrun_json_test_points_3': '3P3V',
                           'testrun_json_test_points_4': '1P8V_VDDH',
                           'testrun_json_test_points_5': 'DVDD',
                           'testrun_json_test_points_6': '0P9V_AVDD_ETH',
                           'testrun_json_test_points_7': '0P9V_AVDD_PCIE',
                           'testrun_json_test_points_8': '1P1V_AVDDH',
                           'testrun_json_board_id': 1955.0,
                           'testrun_json_configuration': 'Config 1',
                           'file_runid_Comments.txt': '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/ A6081C/2/Comments.txt',
                           'file_runid_logfile.txt': '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/ A6081C/2/logfile.txt',
                           'file_runid_power.csv': '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/ A6081C/2/power.csv',
                           'file_runid_power (1).csv':
                               '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/ A6081C/2/power.csv',
                           'file_runid_power.json': '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/ A6081C/2/power.json',
                           'file_runid_settings.xml': '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/ A6081C/2/settings.xml',
                           'file_runid_status.json': '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/ A6081C/2/status.json',
                           'file_runid_steps.xml': '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/ A6081C/2/steps.xml',
                           'file_runid_System Info.json': '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/ A6081C/2/System Info.json',
                           'file_runid_testrun.json': '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/ A6081C/2/testrun.json',
                           'test_category': 'Load Profile', 'capture': 1,
                           'images': "['/npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/ A6081C/2/Tests/Load Profile/1/capture.png']",
                           'meta_json_temperature_setpoint': 25,
                           'meta_json_temperature': 25.051796,
                           'meta_json_power_supply_name_1': '12V_MAIN',
                           'meta_json_power_supply_group_1': 'Main',
                           'meta_json_power_supply_ps_channel_1': 1,
                           'meta_json_power_supply_slew_1': 200,
                           'meta_json_power_supply_voltage_1': 10.80373,
                           'meta_json_power_supply_current_1': 0.709922,
                           'meta_json_power_supply_on_delay_1': 0,
                           'meta_json_power_supply_off_delay_1': 0,
                           'meta_json_power_supply_on_1': True,
                           'meta_json_power_supply_voltage_setpoint_1': 10.8,
                           'meta_json_power_supply_name_2': 'PCIE 3.3V Main',
                           'meta_json_power_supply_group_2': 'Disabled',
                           'meta_json_power_supply_ps_channel_2': 2,
                           'meta_json_power_supply_slew_2': 1000,
                           'meta_json_power_supply_voltage_2': 3.303239,
                           'meta_json_power_supply_current_2': -0.000134086,
                           'meta_json_power_supply_on_delay_2': 0,
                           'meta_json_power_supply_off_delay_2': 0,
                           'meta_json_power_supply_on_2': True,
                           'meta_json_power_supply_voltage_setpoint_2': 3.3,
                           'meta_json_power_supply_name_3': '3.3V_AUX',
                           'meta_json_power_supply_group_3': 'Aux',
                           'meta_json_power_supply_ps_channel_3': 3,
                           'meta_json_power_supply_slew_3': 200,
                           'meta_json_power_supply_voltage_3': 3.300302,
                           'meta_json_power_supply_current_3': 0.00663602,
                           'meta_json_power_supply_on_delay_3': 0,
                           'meta_json_power_supply_off_delay_3': 0,
                           'meta_json_power_supply_on_3': True,
                           'meta_json_power_supply_voltage_setpoint_3': 3.3,
                           'meta_json_power_supply_name_4': None,
                           'meta_json_power_supply_group_4': 'Disabled',
                           'meta_json_power_supply_ps_channel_4': 4.0,
                           'meta_json_power_supply_slew_4': 1000.0,
                           'meta_json_power_supply_voltage_4': 0.002337876,
                           'meta_json_power_supply_current_4': -2.8300000000000003e-05,
                           'meta_json_power_supply_on_delay_4': 0.0,
                           'meta_json_power_supply_off_delay_4': 0.0,
                           'meta_json_power_supply_on_4': False,
                           'meta_json_power_supply_voltage_setpoint_4': 0.02,
                           'capture_json_initial_x': 6.91e-06,
                           'capture_json_x_increment': 8e-05,
                           'capture_json_names_1': '12V_MAIN',
                           'capture_json_names_2': '12V_MAIN CURRENT',
                           'capture_json_names_3': '3P3V',
                           'capture_json_names_4': '1P8V_VDDH',
                           'capture_json_names_5': 'DVDD',
                           'capture_json_names_6': '0P9V_AVDD_ETH',
                           'capture_json_names_7': '0P9V_AVDD_PCIE',
                           'capture_json_names_8': '1P1V_AVDDH',
                           'capture_json_compress': True,
                           'temperature_power_settings_json_chamber_setpoint': 25,
                           'temperature_power_settings_json_dut_on': True,
                           'temperature_power_settings_json_power_supply_channels_channel_name_1': '12V_MAIN',
                           'temperature_power_settings_json_power_supply_channels_channel_on_1': True,
                           'temperature_power_settings_json_power_supply_channels_group_1': 'Main',
                           'temperature_power_settings_json_power_supply_channels_voltage_setpoint_1': 10.8,
                           'temperature_power_settings_json_power_supply_channels_slew_rate_1': 200,
                           'temperature_power_settings_json_power_supply_channels_on_delay_1': 0,
                           'temperature_power_settings_json_power_supply_channels_off_delay_1': 0,
                           'temperature_power_settings_json_power_supply_channels_channel_name_2': 'PCIE 3.3V Main',
                           'temperature_power_settings_json_power_supply_channels_channel_on_2': True,
                           'temperature_power_settings_json_power_supply_channels_group_2': 'Disabled',
                           'temperature_power_settings_json_power_supply_channels_voltage_setpoint_2': 3.3,
                           'temperature_power_settings_json_power_supply_channels_slew_rate_2': 1000,
                           'temperature_power_settings_json_power_supply_channels_on_delay_2': 0,
                           'temperature_power_settings_json_power_supply_channels_off_delay_2': 0,
                           'temperature_power_settings_json_power_supply_channels_channel_name_3': '3.3V_AUX',
                           'temperature_power_settings_json_power_supply_channels_channel_on_3': True,
                           'temperature_power_settings_json_power_supply_channels_group_3': 'Aux',
                           'temperature_power_settings_json_power_supply_channels_voltage_setpoint_3': 3.3,
                           'temperature_power_settings_json_power_supply_channels_slew_rate_3': 200,
                           'temperature_power_settings_json_power_supply_channels_on_delay_3': 0,
                           'temperature_power_settings_json_power_supply_channels_off_delay_3': 0,
                           'temperature_power_settings_json_power_supply_channels_channel_name_4': None,
                           'temperature_power_settings_json_power_supply_channels_channel_on_4': False,
                           'temperature_power_settings_json_power_supply_channels_group_4': 'Disabled',
                           'temperature_power_settings_json_power_supply_channels_voltage_setpoint_4': 0.02,
                           'temperature_power_settings_json_power_supply_channels_slew_rate_4': 1000.0,
                           'temperature_power_settings_json_power_supply_channels_on_delay_4': 0.0,
                           'temperature_power_settings_json_power_supply_channels_off_delay_4': 0.0,
                           'file_capture_capture.json': '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/ A6081C/2/Tests/Load Profile/1/capture.json',
                           'file_capture_capture.png': '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/ A6081C/2/Tests/Load Profile/1/capture.png',
                           'file_capture_CH1.bin': '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/ A6081C/2/Tests/Load Profile/1/CH1.bin',
                           'file_capture_CH2.bin': '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/ A6081C/2/Tests/Load Profile/1/CH2.bin',
                           'file_capture_CH3.bin': '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/ A6081C/2/Tests/Load Profile/1/CH3.bin',
                           'file_capture_CH4.bin': '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/ A6081C/2/Tests/Load Profile/1/CH4.bin',
                           'file_capture_CH5.bin': '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/ A6081C/2/Tests/Load Profile/1/CH5.bin',
                           'file_capture_CH6.bin': '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/ A6081C/2/Tests/Load Profile/1/CH6.bin',
                           'file_capture_CH7.bin': '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/ A6081C/2/Tests/Load Profile/1/CH7.bin',
                           'file_capture_CH8.bin': '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/ A6081C/2/Tests/Load Profile/1/CH8.bin',
                           'file_capture_power.csv':
                               '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/ A6081C/2/power.csv',
                           'file_capture_power (1).csv':
                               '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/ A6081C/2/power.csv',
                           'file_capture_power.json':
                               '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/ A6081C/2/power.json',
                           'file_capture_temperature power settings.json': '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/ A6081C/2/Tests/Load Profile/1/temperature power settings.json',
                           'testpoint': '12V_MAIN', 'scope_channel': 1,
                           'location':
                               '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/ A6081C/2/Tests/Load Profile/1/CH1.bin'})

ethagent_row = pd.Series({
    'dut': 'Mentor Harbor',
    'pba': 'K31123-001',
    'base': 'K31123',
    'dash': 1,
    'rework': 0,
    'software': 'nan',
    'serial_number': 'A60658',
    'runid': 108,
    'comments': 'config 3',
    'status_json_status': 'Complete',
    'status_json_time': '10/8/2019 9:28',
    'status_json_info': 'nan',
    'status_json_runtime_total_seconds': 6110,
    'status_json_runtime_hours': 1,
    'status_json_runtime_minutes': 41,
    'status_json_runtime_seconds': 50,
    'system_info_json_probes_channel_1': 'CH1',
    'system_info_json_probes_type_1': 'TDP1000',
    'system_info_json_probes_serial_number_1': 'B015707',
    'system_info_json_probes_units_1': 'V',
    'system_info_json_probes_cal_status_1': 'D',
    'system_info_json_probes_channel_2': 'CH2',
    'system_info_json_probes_type_2': 'TDP1000',
    'system_info_json_probes_serial_number_2': 'B012394',
    'system_info_json_probes_units_2': 'V',
    'system_info_json_probes_cal_status_2': 'D',
    'system_info_json_probes_channel_3': 'CH3',
    'system_info_json_probes_type_3': 'TDP1000',
    'system_info_json_probes_serial_number_3': 'B012482',
    'system_info_json_probes_units_3': 'V',
    'system_info_json_probes_cal_status_3': 'D',
    'system_info_json_probes_channel_4': 'CH4',
    'system_info_json_probes_type_4': 'TDP1000',
    'system_info_json_probes_serial_number_4': 'B013014',
    'system_info_json_probes_units_4': 'V',
    'system_info_json_probes_cal_status_4': 'D',
    'system_info_json_probes_channel_5': 'CH5',
    'system_info_json_probes_type_5': 'TDP1000',
    'system_info_json_probes_serial_number_5': 'B014712',
    'system_info_json_probes_units_5': 'V',
    'system_info_json_probes_cal_status_5': 'D',
    'system_info_json_probes_channel_6': 'CH6',
    'system_info_json_probes_type_6': 'TDP1000',
    'system_info_json_probes_serial_number_6': 'B015298',
    'system_info_json_probes_units_6': 'V',
    'system_info_json_probes_cal_status_6': 'D',
    'system_info_json_probes_channel_7': 'CH7',
    'system_info_json_probes_type_7': '1X',
    'system_info_json_probes_serial_number_7': 'nan',
    'system_info_json_probes_units_7': 'V',
    'system_info_json_probes_cal_status_7': 'D',
    'system_info_json_probes_channel_8': 'CH8',
    'system_info_json_probes_type_8': '1X',
    'system_info_json_probes_serial_number_8': 'nan',
    'system_info_json_probes_units_8': 'V',
    'system_info_json_probes_cal_status_8': 'D',
    'system_info_json_scope_serial_number': 'nan',
    'system_info_json_power_supply_serial_number': 'nan',
    'system_info_json_ats_version': 'ATS 2.0 Alpha 24_60696',
    'testrun_json_dut': 'Mentor Harbor',
    'testrun_json_pba': 'K31123-001',
    'testrun_json_rework': 0,
    'testrun_json_serial_number': 'A60658',
    'testrun_json_technician': 'Tony Strojan',
    'testrun_json_test_station': 'lno-test5',
    'testrun_json_test_points_1': '3P3V',
    'testrun_json_test_points_2': '3P3V_SFP_TX0',
    'testrun_json_test_points_3': '3P3V_SFP_TX2',
    'testrun_json_test_points_4': '3P3V_SFP_RX0',
    'testrun_json_test_points_5': '3P3V_SFP_RX2',
    'testrun_json_test_points_6': '3P3V_CVL_OSC',
    'testrun_json_test_points_7': 'nan',
    'testrun_json_test_points_8': 'nan',
    'testrun_json_board_id': 1958.0,
    'testrun_json_configuration': 'Config 3',
    'file_runid_Comments.txt': '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/A60658/108/Comments.txt',
    'file_runid_logfile.txt': '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/A60658/108/logfile.txt',
    'file_runid_power.csv': '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/A60658/108/power.csv',
    'file_runid_power.json': '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/A60658/108/power.json',
    'file_runid_settings.xml': '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/A60658/108/settings.xml',
    'file_runid_status.json': '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/A60658/108/status.json',
    'file_runid_steps.xml': '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/A60658/108/steps.xml',
    'file_runid_System Info.json': '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/A60658/108/System Info.json',
    'file_runid_testrun.json': '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/A60658/108/testrun.json',
    'test_category': 'EthAgent',
    'capture': 6,
    'images': '[]',
    'dut_0_json_start_time': 0,
    'dut_0_json_stop_time': 0,
    'dut_0_json_slot_bus_dev_func': '03:00.0',
    'dut_0_json_slot_connection': '192.168.0.52',
    'dut_0_json_slot_crc': 4,
    'dut_0_json_slot_device_id': 1593,
    'dut_0_json_slot_etrack_id': np.NaN,
    'dut_0_json_slot_link': True,
    'dut_0_json_slot_mac_address': '6805CAA60658',
    'dut_0_json_slot_name': 'Intel(R) Ethernet Network Adapter E810-L-2',
    'dut_0_json_slot_packet_size': 1512,
    'dut_0_json_slot_pattern': 'AA Pattern',
    'dut_0_json_slot_remote_mac_address': 0,
    'dut_0_json_slot_revision_id': 1,
    'dut_0_json_slot_rx_bits_per_second': 48973481645,
    'dut_0_json_slot_rx_errors': 0,
    'dut_0_json_slot_rx_packets': 429083663.0,
    'dut_0_json_slot_slot': 2,
    'dut_0_json_slot_speed': 0,
    'dut_0_json_slot_state': 'Sending/Receiving',
    'dut_0_json_slot_subsystem_id': 2,
    'dut_0_json_slot_subsystem_vendor_id': 8086,
    'dut_0_json_slot_tx_bits_per_second': 26076651176,
    'dut_0_json_slot_tx_errors': 0,
    'dut_0_json_slot_tx_packets': 228828579,
    'dut_0_json_slot_vendor_id': 8086,
    'dut_0_json_timestamp': '10/8/2019 8:47',
    'dut_0_json_target_speed': 'AUTO',
    'dut_1_json_start_time': 0,
    'dut_1_json_stop_time': 0,
    'dut_1_json_slot_bus_dev_func': '03:00.1',
    'dut_1_json_slot_connection': '192.168.0.52',
    'dut_1_json_slot_crc': 4,
    'dut_1_json_slot_device_id': 1593,
    'dut_1_json_slot_etrack_id': np.NaN,
    'dut_1_json_slot_link': True,
    'dut_1_json_slot_mac_address': '6805CAA60659',
    'dut_1_json_slot_name': 'Intel(R) Ethernet Network Adapter E810-L-2',
    'dut_1_json_slot_packet_size': 1512,
    'dut_1_json_slot_pattern': 'AA Pattern',
    'dut_1_json_slot_remote_mac_address': 0,
    'dut_1_json_slot_revision_id': 1,
    'dut_1_json_slot_rx_bits_per_second': 48972885527,
    'dut_1_json_slot_rx_errors': 0,
    'dut_1_json_slot_rx_packets': 425793549.0,
    'dut_1_json_slot_slot': 3,
    'dut_1_json_slot_speed': 0,
    'dut_1_json_slot_state': 'Sending/Receiving',
    'dut_1_json_slot_subsystem_id': 2,
    'dut_1_json_slot_subsystem_vendor_id': 8086,
    'dut_1_json_slot_tx_bits_per_second': 26079610866,
    'dut_1_json_slot_tx_errors': 0,
    'dut_1_json_slot_tx_packets': 227077192,
    'dut_1_json_slot_vendor_id': 8086,
    'dut_1_json_timestamp': '10/8/2019 8:47',
    'dut_1_json_target_speed': 'AUTO',
    'link_partner_0_json_start_time': 0,
    'link_partner_0_json_stop_time': 0,
    'link_partner_0_json_slot_bus_dev_func': '02:00.0',
    'link_partner_0_json_slot_connection': '192.168.0.53',
    'link_partner_0_json_slot_crc': 4,
    'link_partner_0_json_slot_device_id': 1593,
    'link_partner_0_json_slot_etrack_id': np.NaN,
    'link_partner_0_json_slot_link': True,
    'link_partner_0_json_slot_mac_address': '6805CAA60848',
    'link_partner_0_json_slot_name': 'Columbiaville',
    'link_partner_0_json_slot_packet_size': 1512,
    'link_partner_0_json_slot_pattern': 'AA Pattern',
    'link_partner_0_json_slot_remote_mac_address': 0,
    'link_partner_0_json_slot_revision_id': 1,
    'link_partner_0_json_slot_rx_bits_per_second': 26076937979,
    'link_partner_0_json_slot_rx_errors': 0,
    'link_partner_0_json_slot_rx_packets': 216563795,
    'link_partner_0_json_slot_slot': 2,
    'link_partner_0_json_slot_speed': 0,
    'link_partner_0_json_slot_state': 'Sending/Receiving',
    'link_partner_0_json_slot_subsystem_id': 2,
    'link_partner_0_json_slot_subsystem_vendor_id': 8086,
    'link_partner_0_json_slot_tx_bits_per_second': 48976406092,
    'link_partner_0_json_slot_tx_errors': 0,
    'link_partner_0_json_slot_tx_packets': 407662057,
    'link_partner_0_json_slot_vendor_id': 8086,
    'link_partner_0_json_timestamp': '10/8/2019 8:47',
    'link_partner_0_json_target_speed': 'AUTO',
    'link_partner_1_json_start_time': 0,
    'link_partner_1_json_stop_time': 0,
    'link_partner_1_json_slot_bus_dev_func': '02:00.1',
    'link_partner_1_json_slot_connection': '192.168.0.53',
    'link_partner_1_json_slot_crc': 4,
    'link_partner_1_json_slot_device_id': 1593,
    'link_partner_1_json_slot_etrack_id': np.NaN,
    'link_partner_1_json_slot_link': True,
    'link_partner_1_json_slot_mac_address': '6805CAA60849',
    'link_partner_1_json_slot_name': 'Columbiaville',
    'link_partner_1_json_slot_packet_size': 1512,
    'link_partner_1_json_slot_pattern': 'AA Pattern',
    'link_partner_1_json_slot_remote_mac_address': 0,
    'link_partner_1_json_slot_revision_id': 1,
    'link_partner_1_json_slot_rx_bits_per_second': 26085132770,
    'link_partner_1_json_slot_rx_errors': 0,
    'link_partner_1_json_slot_rx_packets': 214835642,
    'link_partner_1_json_slot_slot': 3,
    'link_partner_1_json_slot_speed': 0,
    'link_partner_1_json_slot_state': 'Sending/Receiving',
    'link_partner_1_json_slot_subsystem_id': 2,
    'link_partner_1_json_slot_subsystem_vendor_id': 8086,
    'link_partner_1_json_slot_tx_bits_per_second': 48808848651,
    'link_partner_1_json_slot_tx_errors': 0,
    'link_partner_1_json_slot_tx_packets': 404421581,
    'link_partner_1_json_slot_vendor_id': 8086,
    'link_partner_1_json_timestamp': '10/8/2019 8:47',
    'link_partner_1_json_target_speed': 'AUTO',
    'temperature_power_settings_json_chamber_setpoint': 0,
    'temperature_power_settings_json_dut_on': True,
    'temperature_power_settings_json_power_supply_channels_channel_name_1': '12V_MAIN',
    'temperature_power_settings_json_power_supply_channels_channel_on_1': True,
    'temperature_power_settings_json_power_supply_channels_group_1': 'Main',
    'temperature_power_settings_json_power_supply_channels_voltage_setpoint_1': 13.0,
    'temperature_power_settings_json_power_supply_channels_slew_rate_1': 26400,
    'temperature_power_settings_json_power_supply_channels_on_delay_1': 0,
    'temperature_power_settings_json_power_supply_channels_off_delay_1': 0,
    'temperature_power_settings_json_power_supply_channels_channel_name_2':
        np.NaN,
    'temperature_power_settings_json_power_supply_channels_channel_on_2': False,
    'temperature_power_settings_json_power_supply_channels_group_2': 'Disabled',
    'temperature_power_settings_json_power_supply_channels_voltage_setpoint_2': 0.02,
    'temperature_power_settings_json_power_supply_channels_slew_rate_2': 1000,
    'temperature_power_settings_json_power_supply_channels_on_delay_2': 0,
    'temperature_power_settings_json_power_supply_channels_off_delay_2': 0,
    'temperature_power_settings_json_power_supply_channels_channel_name_3': '3.3_AUX',
    'temperature_power_settings_json_power_supply_channels_channel_on_3': True,
    'temperature_power_settings_json_power_supply_channels_group_3': 'Aux',
    'temperature_power_settings_json_power_supply_channels_voltage_setpoint_3': 3.3,
    'temperature_power_settings_json_power_supply_channels_slew_rate_3': 26400,
    'temperature_power_settings_json_power_supply_channels_on_delay_3': 0,
    'temperature_power_settings_json_power_supply_channels_off_delay_3': 0,
    'file_capture_DUT.json': '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/A60658/108/Tests/EthAgent/6/DUT.json',
    'file_capture_Link Partner.json': '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/A60658/108/Tests/EthAgent/6/Link Partner.json',
    'file_capture_power.csv': '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/A60658/108/Tests/EthAgent/6/power.csv',
    'file_capture_power.json': '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/A60658/108/Tests/EthAgent/6/power.json',
    'file_capture_temperature power settings.json': '//npo/coos/LNO_Validation/Validation_Data/_data/ATS 2.0/Mentor Harbor/K31123-001/00/A60658/108/Tests/EthAgent/6/temperature power settings.json'
})
