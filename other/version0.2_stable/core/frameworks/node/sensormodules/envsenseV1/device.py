from add_sensor_info import *
import time
import serial

class device():

    def __init__(self):
        self.Sensor_Index=["D6T_44L_06_1_T_C","MMA8452_1_A_X_Units","MMA8452_1_A_Y_Units",
                    "MMA8452_1_A_Z_Units","MMA8452_1_A_RMS_Units","SHT15_1_T_C","SHT15_1_H_%","SHT75_1_T_C",
                    "SHT75_1_H_%","MAX4466_1_MaxN_Units","AMBI_1_Units","PhoRes_10K4.7K_1_Units","HIH4030_1_Units",
                    "THERMIS_100K_1_Units","DS18B20_1_T_C","TMP421_1_T_C","RHT03_1_T_C","RHT03_1_H_%",
                    "BMP_180_1_T_C","BMP_180_1_P_PA","TMP102_1_T_F","HIH_6130_1_T_C","HIH_6130_1_H_%",
                    "MLX90614_1_T_F","HTU21D_T_C","HTU21D_H_%","HMC5883_X_uT","HMC5883_Y_uT","HMC5883_Z_uT"]

        self.reading_names = [ ["Temperature",
                        "Temperature","Temperature","Temperature","Temperature",
                        "Temperature","Temperature","Temperature","Temperature",
                        "Temperature","Temperature","Temperature","Temperature",
                        "Temperature","Temperature","Temperature","Temperature"],
                            "Acceleration",
                            "Acceleration",
                            "Acceleration",
                            "Vibration",
                            "Temperature",
                            "Humidity",
                            "Temperature",
                            "Humidity",
                            "Acoustic_Intensity",
                            "Luminous_Intensity",
                            "Luminous_Intensity",
                            "Humidity",
                            "Temperature",
                            "Temperature",
                            "Temperature",
                            "Temperature",
                            "Humidity",
                            "Temperature",
                            "Pressure",
                            "Temperature",
                            "Temperature",
                            "Humidity",
                            "Temperature",
                            "Temperature",
                            "Humidity",
                            "Magnetic_Field",
                            "Magnetic_Field",
                            "Magnetic_Field"]

        self.reading_type = [['f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f'],
                'f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f']

        self.reading_unit = [["C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C"],
                        "g","g","g","g","C","%RH","C","%RH","Units10B0V5","Units10B0V5","Units10B0V5","Units10B0V5",
                        "Units10B0V5","C","C","C","%RH","C","PA","F","C","%RH","F","C","%RH","uT","uT","uT"]

        self.reading_note = [["PTAT",
                        "1x1","1x2","1x3","1x4",
                        "2x1","2x2","2x3","2x4",
                        "3x1","3x2","3x3","3x4",
                        "4x1","4x2","4x3","4x4"],
                            "X",
                            "Y",
                            "Z",
                            "RMS_3Axis",
                            "",
                            "RH",
                            "",
                            "RH",
                            "non-standard",
                            "non-standard",
                            "Voltage_Divider_5V_PDV_Tap_4K7_GND",
                            "RH",
                            "Voltage_Divider_5V_NTC_Tap_68K_GND",
                            "",
                            "",
                            "",
                            "RH",
                            "",
                            "Barometric",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "RH",
                            "X",
                            "Y",
                            "Z"]

        self.sensor_array_index = [2,7,7,7,7,5,5,12,12,15,14,0,13,3,8,9,10,10,6,6,11,4,4,1,16,16,17,17,17]

        self.sensor_names = ["PDV_P8104.API.2006", "MLX90614ESF-DAA.Melexis.008-2013", "D6T-44L-06.Omron.2012", "Thermistor_NTC_PR103J2.US_Sensor.2003",
                "HIH6130.Honeywell.2011", "SHT15.Sensirion.4_3-2010", "BMP180.Bosch.2_5-2013", "MMA8452Q.Freescale.8_1-2013",
                "DS18B20.Maxim.2008", "TMP421.Texas_Instruments.2012", "RHT03.Maxdetect.2011", "TMP102.Texas_Instruments.2008",
                "SHT75.Sensirion.5_2011", "HIH4030.Honeywell.2008", "GA1A1S201WP.Sharp.2007", "MAX4466.Maxim.2001","HTU21D.MeasSpec.2013","HMC5883.Honeywell.2013"]

    def register(self):

        sensor_obj_1 = sensor_info("PDV_P8104_1", "PDV_P8104.API.2006", " ", " ", " ", "Ceramic", "Digi-Key")
        reading_obj_1_1 = reading_info("PDV_P8104.API.2006.Light_intensity", "int", "ohms", " ")
        param_obj_1_1 = param_info(1, "Parameter", "Light_intensity", "string", 0)
        param_obj_1_2 = param_info(1, "Units", "ohms", "string", 0)
        param_obj_1_3 = param_info(1, "Accuracy/Sensitivity", 0.8, "float", 0) # Are sensitivity and accuracy the same thing?
        param_obj_1_4 = param_info(1, "Parameter_min", 400, "int", 0) # These units are nm, not the same as regular units
        param_obj_1_5 = param_info(1, "Parameter_max", 700, "int", 0)
        param_obj_1_6 = param_info(0, "Voltage_min", 0, "int", 0)
        param_obj_1_7 = param_info(0, "Voltage_max", 150, "int", 0)
        param_obj_1_8 = param_info(0, "Voltage_unit", "V", "string", 0)
        param_obj_1_9 = param_info(0, "Current", 0.67, "float", 0)
        param_obj_1_10 = param_info(0, "Max_operating_temp", 75, "int", 0)
        param_obj_1_11 = param_info(0, "Min_operating_temp", -30, "int", 0)
        param_obj_1_12 = param_info(0, "Min_storage_temp", -30, "int", 0)
        param_obj_1_13 = param_info(0, "Max_storage_temp", 75, "int", 0)
        param_obj_1_14 = param_info(0, "Storage_operating_temp_units", "C", "string", 0)
        param_obj_1_15 = param_info(0, "Rise_time", "60ms", "string", 0)
        param_obj_1_16 = param_info(0, "Fall time", "25ms", "string", 0)
        reading_obj_1_1.add_parameter(param_obj_1_1)
        reading_obj_1_1.add_parameter(param_obj_1_2)
        reading_obj_1_1.add_parameter(param_obj_1_3)
        reading_obj_1_1.add_parameter(param_obj_1_4)
        reading_obj_1_1.add_parameter(param_obj_1_5)
        sensor_obj_1.add_parameter(param_obj_1_6)
        sensor_obj_1.add_parameter(param_obj_1_7)
        sensor_obj_1.add_parameter(param_obj_1_8)
        sensor_obj_1.add_parameter(param_obj_1_9)
        sensor_obj_1.add_parameter(param_obj_1_10)
        sensor_obj_1.add_parameter(param_obj_1_11)
        sensor_obj_1.add_parameter(param_obj_1_12)
        sensor_obj_1.add_parameter(param_obj_1_13)
        sensor_obj_1.add_parameter(param_obj_1_14)
        sensor_obj_1.add_parameter(param_obj_1_15)
        sensor_obj_1.add_parameter(param_obj_1_16)
        sensor_obj_1.add_reading(reading_obj_1_1)
        write_to_config_file(sensor_obj_1)


        sensor_obj_2 = sensor_info("MLX90614ESF-DAA_1", "MLX90614ESF-DAA.Melexis.008-2013", 0.001024, 1, 2, "TO-39-4 Modified Metal Can", "Digi-Key")
        reading_obj_2_1 = reading_info("MLX90614ESF-DAA.Melexis.008/2013.Temp", "float", "F", " ")
        param_obj_2_1 = param_info(1, "Parameter", "Temperature", "string", 0)
        param_obj_2_2 = param_info(1, "Units", "F", "string", 0)
        param_obj_2_3 = param_info(1, "Accuracy", 1.8, "float", 0)
        param_obj_2_4 = param_info(1, "Parameter_min", -4, "int", 0)
        param_obj_2_5 = param_info(1, "Parameter_max", 248, "int", 0)
        param_obj_2_6 = param_info(0, "Voltage_min", 2.6, "float", 0)
        param_obj_2_7 = param_info(0, "Voltage_max", 3.6, "float", 0)
        param_obj_2_8 = param_info(0, "Voltage_unit", "V", "string", 0)
        param_obj_2_9 = param_info(0, "Current", 0.0013, "float", 0)
        param_obj_2_10 = param_info(0, "Max_operating_temp", 85, "int", 0)
        param_obj_2_11 = param_info(0, "Min_operating_temp", -40, "int", 0)
        param_obj_2_12 = param_info(0, "Min_storage_temp", -40, "int", 0)
        param_obj_2_13 = param_info(0, "Max_storage_temp", 125, "int", 0)
        param_obj_2_14 = param_info(0, "Storage_operating_temp_units", "C", "string", 0)
        param_obj_2_15 = param_info(0, "PWM_resolution", "10bit", "string", 0)
        reading_obj_2_1.add_parameter(param_obj_2_1)
        reading_obj_2_1.add_parameter(param_obj_2_2)
        reading_obj_2_1.add_parameter(param_obj_2_3)
        reading_obj_2_1.add_parameter(param_obj_2_4)
        reading_obj_2_1.add_parameter(param_obj_2_5)
        sensor_obj_2.add_parameter(param_obj_2_6)
        sensor_obj_2.add_parameter(param_obj_2_7)
        sensor_obj_2.add_parameter(param_obj_2_8)
        sensor_obj_2.add_parameter(param_obj_2_9)
        sensor_obj_2.add_parameter(param_obj_2_10)
        sensor_obj_2.add_parameter(param_obj_2_11)
        sensor_obj_2.add_parameter(param_obj_2_12)
        sensor_obj_2.add_parameter(param_obj_2_13)
        sensor_obj_2.add_parameter(param_obj_2_14)
        sensor_obj_2.add_parameter(param_obj_2_15)
        sensor_obj_2.add_reading(reading_obj_2_1)
        write_to_config_file(sensor_obj_2)

        sensor_obj_3 = sensor_info("D6T-44L-06_1", "D6T-44L-06.Omron.2012", 0.25, 0, 1, "normal", "Digi-Key")
        reading_obj_3_1 = reading_info("D6T-44L-06.Omron.2012.Temp", "int", "C", " ")
        param_obj_3_1 = param_info(1, "Parameter", "Temperature", "string", 0)
        param_obj_3_2 = param_info(1, "Units", "C", "string", 0)
        param_obj_3_3 = param_info(1, "Accuracy", 1.5, "float", 0)
        param_obj_3_4 = param_info(1, "Parameter_min", 5, "int", 0)
        param_obj_3_5 = param_info(1, "Parameter_max", 50, "int", 0)
        param_obj_3_6 = param_info(0, "Voltage_min", 4.5, "float", 0)
        param_obj_3_7 = param_info(0, "Voltage_max", 5.5, "float", 0)
        param_obj_3_8 = param_info(0, "Voltage_unit", "V", "float", 0)
        param_obj_3_9 = param_info(0, "Current", 0.005, "float", 0)
        param_obj_3_10 = param_info(0, "Max_operating_temp", 50, "int", 0)
        param_obj_3_11 = param_info(0, "Min_operating_temp", 0, "int", 0)
        param_obj_3_12 = param_info(0, "Min_storage_temp", -10, "int", 0)
        param_obj_3_13 = param_info(0, "Max_storage_temp", 60, "int", 0)
        param_obj_3_14 = param_info(0, "Storage_operating_temp_units", "C", "string", 0)
        param_obj_3_15 = param_info(0, "View_angle_X", 44.2, "float", 0)
        param_obj_3_16 = param_info(0, "View_angle_Y", 45.7, "float", 0)
        reading_obj_3_1.add_parameter(param_obj_3_1)
        reading_obj_3_1.add_parameter(param_obj_3_2)
        reading_obj_3_1.add_parameter(param_obj_3_3)
        reading_obj_3_1.add_parameter(param_obj_3_4)
        reading_obj_3_1.add_parameter(param_obj_3_5)
        sensor_obj_3.add_parameter(param_obj_3_6)
        sensor_obj_3.add_parameter(param_obj_3_7)
        sensor_obj_3.add_parameter(param_obj_3_8)
        sensor_obj_3.add_parameter(param_obj_3_9)
        sensor_obj_3.add_parameter(param_obj_3_10)
        sensor_obj_3.add_parameter(param_obj_3_11)
        sensor_obj_3.add_parameter(param_obj_3_12)
        sensor_obj_3.add_parameter(param_obj_3_13)
        sensor_obj_3.add_parameter(param_obj_3_14)
        sensor_obj_3.add_parameter(param_obj_3_15)
        sensor_obj_3.add_parameter(param_obj_3_16)
        sensor_obj_3.add_reading(reading_obj_3_1)
        write_to_config_file(sensor_obj_3)




        sensor_obj_4 = sensor_info("Thermistor_NTC_PR103J2_1", "Thermistor_NTC_PR103J2.US_Sensor.2003", " ", " ", " ", "bead", "Digi-Key")
        reading_obj_4_1 = reading_info("Thermistor_NTC_PR103J2.US_Sensor.2003.Temp", "int", "Units10B0V5", " ")
        param_obj_4_1 = param_info(1, "Parameter", "Temperature", "string", 0)
        param_obj_4_2 = param_info(1, "Units", "Units10B0V5", "string", 0)
        param_obj_4_3 = param_info(1, "Accuracy", 0.05, "float", 0)
        param_obj_4_4 = param_info(1, "Parameter_min", " ", " ", " ")
        param_obj_4_5 = param_info(1, "Parameter_max", " ", " ", " ")
        param_obj_4_6 = param_info(0, "Voltage_min", " ", " ", " ")
        param_obj_4_7 = param_info(0, "Voltage_max", " ",  " ", " ")
        param_obj_4_8 = param_info(0, "Voltage_unit", " ",  " ", " ")
        param_obj_4_9 = param_info(0, "Current", " ",  " ", " ")
        param_obj_4_10 = param_info(0, "Max_operating_temp", 80, "int", 0)
        param_obj_4_11 = param_info(0, "Min_operating_temp", -55, "int", 0)
        param_obj_4_12 = param_info(0, "Min_storage_temp", -55, "int", 0)
        param_obj_4_13 = param_info(0, "Max_storage_temp", 50, "int", 0)
        param_obj_4_14 = param_info(0, "Storage_operating_temp_units", "C", "string", 0)
        param_obj_4_15 = param_info(0, "Resistance_25C", 10000, "int", 0)
        param_obj_4_16 = param_info(0, "Temp_coefficient_25C", "-4.4%/C", "string", 0)
        reading_obj_4_1.add_parameter(param_obj_4_1)
        reading_obj_4_1.add_parameter(param_obj_4_2)
        reading_obj_4_1.add_parameter(param_obj_4_3)
        reading_obj_4_1.add_parameter(param_obj_4_4)
        reading_obj_4_1.add_parameter(param_obj_4_5)
        sensor_obj_4.add_parameter(param_obj_4_6)
        sensor_obj_4.add_parameter(param_obj_4_7)
        sensor_obj_4.add_parameter(param_obj_4_8)
        sensor_obj_4.add_parameter(param_obj_4_9)
        sensor_obj_4.add_parameter(param_obj_4_10)
        sensor_obj_4.add_parameter(param_obj_4_11)
        sensor_obj_4.add_parameter(param_obj_4_12)
        sensor_obj_4.add_parameter(param_obj_4_13)
        sensor_obj_4.add_parameter(param_obj_4_14)
        sensor_obj_4.add_parameter(param_obj_4_15)
        sensor_obj_4.add_parameter(param_obj_4_16)
        sensor_obj_4.add_reading(reading_obj_4_1)
        write_to_config_file(sensor_obj_4)



        sensor_obj_5 = sensor_info("HIH6130_1", "HIH6130.Honeywell.2011", 1, 1, 1, "Breakout board", "Sparkfun")
        reading_obj_5_1 = reading_info("HIH6130.Honeywell.2011.Temp", "float", "C", " ")
        reading_obj_5_2 = reading_info("HIH6130.Honeywell.2011.Humidity", "float", "%", " ")
        param_obj_5_1 = param_info(1, "Parameter", "Temperature", "string", 0)
        param_obj_5_2 = param_info(1, "Units", "C", "string", 0)
        param_obj_5_3 = param_info(1, "Accuracy", 1.0, "float", 0)
        param_obj_5_4 = param_info(1, "Parameter_min", 5, "int", 0)
        param_obj_5_5 = param_info(1, "Parameter_max", 50, "int", 0)
        param_obj_5_6 = param_info(1, "Parameter", "Humidity", "string", 0)
        param_obj_5_7 = param_info(1, "Units", "%", "string", 0)
        param_obj_5_8 = param_info(1, "Accuracy", 4, "int", 0)
        param_obj_5_9 = param_info(1, "Parameter_min", 10, "int", 0)
        param_obj_5_10 = param_info(1, "Parameter_max", 90, "int", 0)
        param_obj_5_11 = param_info(0, "Voltage_min", 2.3, "float", 0)
        param_obj_5_12 = param_info(0, "Voltage_max", 5.5, "float", 0)
        param_obj_5_13 = param_info(0, "Voltage_unit", "Vdc", "string", 0)
        param_obj_5_14 = param_info(0, "Current", 0.00065, "float", 0)
        param_obj_5_15 = param_info(0, "Max_operating_temp", 85, "int", 0)
        param_obj_5_16 = param_info(0, "Min_operating_temp", -25, "int", 0)
        param_obj_5_17 = param_info(0, "Min_storage_temp", -40, "int", 0)
        param_obj_5_18 = param_info(0, "Max_storage_temp", 85, "int", 0)
        param_obj_5_19 = param_info(0, "Storage_operating_temp_units", "C", "string", 0)
        reading_obj_5_1.add_parameter(param_obj_5_1)
        reading_obj_5_1.add_parameter(param_obj_5_2)
        reading_obj_5_1.add_parameter(param_obj_5_3)
        reading_obj_5_1.add_parameter(param_obj_5_4)
        reading_obj_5_1.add_parameter(param_obj_5_5)
        reading_obj_5_2.add_parameter(param_obj_5_6)
        reading_obj_5_2.add_parameter(param_obj_5_7)
        reading_obj_5_2.add_parameter(param_obj_5_8)
        reading_obj_5_2.add_parameter(param_obj_5_9)
        reading_obj_5_2.add_parameter(param_obj_5_10)
        sensor_obj_5.add_parameter(param_obj_5_11)
        sensor_obj_5.add_parameter(param_obj_5_12)
        sensor_obj_5.add_parameter(param_obj_5_13)
        sensor_obj_5.add_parameter(param_obj_5_14)
        sensor_obj_5.add_parameter(param_obj_5_15)
        sensor_obj_5.add_parameter(param_obj_5_16)
        sensor_obj_5.add_parameter(param_obj_5_17)
        sensor_obj_5.add_parameter(param_obj_5_18)
        sensor_obj_5.add_parameter(param_obj_5_19)
        sensor_obj_5.add_reading(reading_obj_5_1)
        sensor_obj_5.add_reading(reading_obj_5_2)
        write_to_config_file(sensor_obj_5)



        sensor_obj_6 = sensor_info("SHT15_1", "SHT15.Sensirion.4_3-2010", 1, 1, 1, "Breakout board", "Sparkfun")
        reading_obj_6_1 = reading_info("SHT15.Sensirion.4_3-2010.Temp", "float", "C", " ")
        reading_obj_6_2 = reading_info("SHT15.Sensirion.4_3-2010.Humidity", "float", "%", " ")
        param_obj_6_1 = param_info(1, "Parameter", "Temperature", "string", 0)
        param_obj_6_2 = param_info(1, "Units", "C", "string", 0)
        param_obj_6_3 = param_info(1, "Accuracy", 0.3, "float", 0)
        param_obj_6_4 = param_info(1, "Parameter_min", -40, "int", 0)
        param_obj_6_5 = param_info(1, "Parameter_max", 123.8, "float", 0)
        param_obj_6_6 = param_info(1, "Parameter", "Humidity", "string", 0)
        param_obj_6_7 = param_info(1, "Units", "%", "string", 0)
        param_obj_6_8 = param_info(1, "Accuracy", 2.0, "float", 0)
        param_obj_6_9 = param_info(1, "Parameter_min", 0, "int", 0)
        param_obj_6_10 = param_info(1, "Parameter_max", 100, "int", 0)
        param_obj_6_11 = param_info(0, "Voltage_min", 2.4, "float", 0)
        param_obj_6_12 = param_info(0, "Voltage_max", 5.5, "float", 0)
        param_obj_6_13 = param_info(0, "Voltage_unit", "V", "string", 0)
        param_obj_6_14 = param_info(0, "Current", 0.00055, "float", 0)
        param_obj_6_15 = param_info(0, "Max_operating_temp", 123.8, "float", 0)
        param_obj_6_16 = param_info(0, "Min_operating_temp", -40, "int", 0)
        param_obj_6_17 = param_info(0, "Min_storage_temp", 10, "int", 0)
        param_obj_6_18 = param_info(0, "Max_storage_temp", 50, "int", 0)
        param_obj_6_19 = param_info(0, "Storage_operating_temp_units", "C", "string", 0)
        reading_obj_6_1.add_parameter(param_obj_6_1)
        reading_obj_6_1.add_parameter(param_obj_6_2)
        reading_obj_6_1.add_parameter(param_obj_6_3)
        reading_obj_6_1.add_parameter(param_obj_6_4)
        reading_obj_6_1.add_parameter(param_obj_6_5)
        reading_obj_6_2.add_parameter(param_obj_6_6)
        reading_obj_6_2.add_parameter(param_obj_6_7)
        reading_obj_6_2.add_parameter(param_obj_6_8)
        reading_obj_6_2.add_parameter(param_obj_6_9)
        reading_obj_6_2.add_parameter(param_obj_6_10)
        sensor_obj_6.add_parameter(param_obj_6_11)
        sensor_obj_6.add_parameter(param_obj_6_12)
        sensor_obj_6.add_parameter(param_obj_6_13)
        sensor_obj_6.add_parameter(param_obj_6_14)
        sensor_obj_6.add_parameter(param_obj_6_15)
        sensor_obj_6.add_parameter(param_obj_6_16)
        sensor_obj_6.add_parameter(param_obj_6_17)
        sensor_obj_6.add_parameter(param_obj_6_18)
        sensor_obj_6.add_parameter(param_obj_6_19)
        sensor_obj_6.add_reading(reading_obj_6_1)
        sensor_obj_6.add_reading(reading_obj_6_2)
        write_to_config_file(sensor_obj_6)


        sensor_obj_7 = sensor_info("BMP180_1", "BMP180.Bosch.2_5-2013", 1, 1, 1, "Breakout board", "Adafruit")
        reading_obj_7_1 = reading_info("BMP180.Bosch.2_5-2013.Temp", "float", "C", " ")
        reading_obj_7_2 = reading_info("BMP180.Bosch.2_5-2013.Pressure", "float", "PA", " ")
        param_obj_7_1 = param_info(1, "Parameter", "Temperature", "string", 0)
        param_obj_7_2 = param_info(1, "Units", "C", "string", 0)
        param_obj_7_3 = param_info(1, "Accuracy", 2, "int", 0)
        param_obj_7_4 = param_info(1, "Parameter_min", 0, "int", 0)
        param_obj_7_5 = param_info(1, "Parameter_max", 65, "int", 0)
        param_obj_7_6 = param_info(1, "Parameter", "Pressure", "string", 0)
        param_obj_7_7 = param_info(1, "Units", "PA", "string", 0)
        param_obj_7_8 = param_info(1, "Accuracy", 300, "int", 0)
        param_obj_7_9 = param_info(1, "Parameter_min", 30000, "int", 0)
        param_obj_7_10 = param_info(1, "Parameter_max", 110000, "int", 0)
        param_obj_7_11 = param_info(0, "Voltage_min", 1.8, "float", 0)
        param_obj_7_12 = param_info(0, "Voltage_max", 3.6, "float", 0)
        param_obj_7_13 = param_info(0, "Voltage_unit", "V", "string", 0)
        param_obj_7_14 = param_info(0, "Current", 0.000005, "float", 0)
        param_obj_7_15 = param_info(0, "Max_operating_temp", 85, "int", 0)
        param_obj_7_16 = param_info(0, "Min_operating_temp", -40, "int", 0)
        param_obj_7_17 = param_info(0, "Min_storage_temp", -40, "int", 0)
        param_obj_7_18 = param_info(0, "Max_storage_temp", 85, "int", 0)
        param_obj_7_19 = param_info(0, "Storage_operating_temp_units", "C", "string", 0)
        reading_obj_7_1.add_parameter(param_obj_7_1)
        reading_obj_7_1.add_parameter(param_obj_7_2)
        reading_obj_7_1.add_parameter(param_obj_7_3)
        reading_obj_7_1.add_parameter(param_obj_7_4)
        reading_obj_7_1.add_parameter(param_obj_7_5)
        reading_obj_7_2.add_parameter(param_obj_7_6)
        reading_obj_7_2.add_parameter(param_obj_7_7)
        reading_obj_7_2.add_parameter(param_obj_7_8)
        reading_obj_7_2.add_parameter(param_obj_7_9)
        reading_obj_7_2.add_parameter(param_obj_7_10)
        sensor_obj_7.add_parameter(param_obj_7_11)
        sensor_obj_7.add_parameter(param_obj_7_12)
        sensor_obj_7.add_parameter(param_obj_7_13)
        sensor_obj_7.add_parameter(param_obj_7_14)
        sensor_obj_7.add_parameter(param_obj_7_15)
        sensor_obj_7.add_parameter(param_obj_7_16)
        sensor_obj_7.add_parameter(param_obj_7_17)
        sensor_obj_7.add_parameter(param_obj_7_18)
        sensor_obj_7.add_parameter(param_obj_7_19)
        sensor_obj_7.add_reading(reading_obj_7_1)
        sensor_obj_7.add_reading(reading_obj_7_2)
        write_to_config_file(sensor_obj_7)



        sensor_obj_8 = sensor_info("MMA8452Q_1", "MMA8452Q.Freescale.8_1-2013", 0.04, 1, 1, "Breakout board", "Sparkfun")
        reading_obj_8_1 = reading_info("MMA8452Q.Freescale.8_1-2013.Accel", "float", "g", " ")
        param_obj_8_1 = param_info(1, "Parameter", "Acceleration", "string", 0)
        param_obj_8_2 = param_info(1, "Units", "g", "string", 0)
        param_obj_8_3 = param_info(1, "Accuracy", 0.017, "float", 0)
        param_obj_8_4 = param_info(1, "Parameter_min", -1, "int", 1) # Should this be 2, 4, or 8?
        param_obj_8_5 = param_info(1, "Parameter_max", 1, "int", 1)
        param_obj_8_6 = param_info(0, "Voltage_min", 1.95, "float", 0)
        param_obj_8_7 = param_info(0, "Voltage_max", 3.6, "float", 0)
        param_obj_8_8 = param_info(0, "Voltage_unit", "V", "string", 0)
        param_obj_8_9 = param_info(0, "Current", 0.0000024, "float", 0)
        param_obj_8_10 = param_info(0, "Max_operating_temp", 85, "int", 0)
        param_obj_8_11 = param_info(0, "Min_operating_temp", -40, "int", 0)
        param_obj_8_12 = param_info(0, "Min_storage_temp", -40, "int", 0)
        param_obj_8_13 = param_info(0, "Max_storage_temp", 125, "int", 0)
        param_obj_8_14 = param_info(0, "Storage_operating_temp_units", "C", "string", 0)
        param_obj_8_15 = param_info(0, "Resolution", "8/12bit", "string", 0)
        param_obj_8_16 = param_info(0, "Boot_time", "350ms", "string", 0)
        reading_obj_8_1.add_parameter(param_obj_8_1)
        reading_obj_8_1.add_parameter(param_obj_8_2)
        reading_obj_8_1.add_parameter(param_obj_8_3)
        reading_obj_8_1.add_parameter(param_obj_8_4)
        reading_obj_8_1.add_parameter(param_obj_8_5)
        sensor_obj_8.add_parameter(param_obj_8_6)
        sensor_obj_8.add_parameter(param_obj_8_7)
        sensor_obj_8.add_parameter(param_obj_8_8)
        sensor_obj_8.add_parameter(param_obj_8_9)
        sensor_obj_8.add_parameter(param_obj_8_10)
        sensor_obj_8.add_parameter(param_obj_8_11)
        sensor_obj_8.add_parameter(param_obj_8_12)
        sensor_obj_8.add_parameter(param_obj_8_13)
        sensor_obj_8.add_parameter(param_obj_8_14)
        sensor_obj_8.add_parameter(param_obj_8_15)
        sensor_obj_8.add_parameter(param_obj_8_16)
        sensor_obj_8.add_reading(reading_obj_8_1)
        write_to_config_file(sensor_obj_8)




        sensor_obj_9 = sensor_info("DS18B20_1", "DS18B20.Maxim.2008", 1, 1, 1, "normal", "Sparkfun")
        reading_obj_9_1 = reading_info("DS18B20.Maxim.2008.Temp", "float", "C", " ")
        param_obj_9_1 = param_info(1, "Parameter", "Temperature", "string", 0)
        param_obj_9_2 = param_info(1, "Units", "C", "string", 0)
        param_obj_9_3 = param_info(1, "Accuracy", 2.0, "float", 0)
        param_obj_9_4 = param_info(1, "Parameter_min", -55, "int", 0)
        param_obj_9_5 = param_info(1, "Parameter_max", 125, "int", 0)
        param_obj_9_6 = param_info(0, "Voltage_min", 3.0, "float", 0)
        param_obj_9_7 = param_info(0, "Voltage_max", 5.5, "float", 0)
        param_obj_9_8 = param_info(0, "Voltage_unit", "V", "string", 0)
        param_obj_9_9 = param_info(0, "Current", 0.001, "float", 0)
        param_obj_9_10 = param_info(0, "Max_operating_temp", 125, "int", 0)
        param_obj_9_11 = param_info(0, "Min_operating_temp", -55, "int", 0)
        param_obj_9_12 = param_info(0, "Min_storage_temp", -55, "int", 0)
        param_obj_9_13 = param_info(0, "Max_storage_temp", 125, "int", 0)
        param_obj_9_14 = param_info(0, "Storage_operating_temp_units", "C", "string", 0)
        param_obj_9_15 = param_info(0, "Resolution", "9-12bit", "string", 0)
        reading_obj_9_1.add_parameter(param_obj_9_1)
        reading_obj_9_1.add_parameter(param_obj_9_2)
        reading_obj_9_1.add_parameter(param_obj_9_3)
        reading_obj_9_1.add_parameter(param_obj_9_4)
        reading_obj_9_1.add_parameter(param_obj_9_5)
        sensor_obj_9.add_parameter(param_obj_9_6)
        sensor_obj_9.add_parameter(param_obj_9_7)
        sensor_obj_9.add_parameter(param_obj_9_8)
        sensor_obj_9.add_parameter(param_obj_9_9)
        sensor_obj_9.add_parameter(param_obj_9_10)
        sensor_obj_9.add_parameter(param_obj_9_11)
        sensor_obj_9.add_parameter(param_obj_9_12)
        sensor_obj_9.add_parameter(param_obj_9_13)
        sensor_obj_9.add_parameter(param_obj_9_14)
        sensor_obj_9.add_parameter(param_obj_9_15)
        sensor_obj_9.add_reading(reading_obj_9_1)
        write_to_config_file(sensor_obj_9)



        sensor_obj_10 = sensor_info("TMP421_1", "TMP421.Texas_Instruments.2012", 1, 1, 1, "", "")
        reading_obj_10_1 = reading_info("TMP421.Texas_Instruments.2012.Temp", "float", "C", " ")
        param_obj_10_1 = param_info(1, "Parameter", "Temperature", "string", 0)
        param_obj_10_2 = param_info(1, "Units", "C", "string", 0)
        param_obj_10_3 = param_info(1, "Accuracy", 1.5, "float", 0)
        param_obj_10_4 = param_info(1, "Parameter_min", -40, "int", 0)
        param_obj_10_5 = param_info(1, "Parameter_max", 125, "int", 0)
        param_obj_10_6 = param_info(0, "Voltage_min", 2.7, "float", 0)
        param_obj_10_7 = param_info(0, "Voltage_max", 5.5, "float", 0)
        param_obj_10_8 = param_info(0, "Voltage_unit", "V", "string", 0)
        param_obj_10_9 = param_info(0, "Current", 0.010, "float", 0) # Is this the right current reading? Input current?
        param_obj_10_10 = param_info(0, "Max_operating_temp", 127, "int", 0)
        param_obj_10_11 = param_info(0, "Min_operating_temp", -55, "int", 0)
        param_obj_10_12 = param_info(0, "Min_storage_temp", -60, "int", 0)
        param_obj_10_13 = param_info(0, "Max_storage_temp", 130, "int", 0)
        param_obj_10_14 = param_info(0, "Storage_operating_temp_units", "C", "string", 0)
        param_obj_10_15 = param_info(0, "Resolution", "12bit", "string", 0)
        reading_obj_10_1.add_parameter(param_obj_10_1)
        reading_obj_10_1.add_parameter(param_obj_10_2)
        reading_obj_10_1.add_parameter(param_obj_10_3)
        reading_obj_10_1.add_parameter(param_obj_10_4)
        reading_obj_10_1.add_parameter(param_obj_10_5)
        sensor_obj_10.add_parameter(param_obj_10_6)
        sensor_obj_10.add_parameter(param_obj_10_7)
        sensor_obj_10.add_parameter(param_obj_10_8)
        sensor_obj_10.add_parameter(param_obj_10_9)
        sensor_obj_10.add_parameter(param_obj_10_10)
        sensor_obj_10.add_parameter(param_obj_10_11)
        sensor_obj_10.add_parameter(param_obj_10_12)
        sensor_obj_10.add_parameter(param_obj_10_13)
        sensor_obj_10.add_parameter(param_obj_10_14)
        sensor_obj_10.add_parameter(param_obj_10_15)
        sensor_obj_10.add_reading(reading_obj_10_1)
        write_to_config_file(sensor_obj_10)


        sensor_obj_11 = sensor_info("RHT03_1", "RHT03.Maxdetect.2011", 2, 0, 2, "normal", "Sparkfun")
        reading_obj_11_1 = reading_info("RHT03.Maxdetect.2011.Temp", "float", "C", " ")
        reading_obj_11_2 = reading_info("RHT03.Maxdetect.2011.Humidity", "float", "%", " ")
        param_obj_11_1 = param_info(1, "Parameter", "Temperature", "string", 0)
        param_obj_11_2 = param_info(1, "Units", "C", "string", 0)
        param_obj_11_3 = param_info(1, "Accuracy", 0.5, "float", 0)
        param_obj_11_4 = param_info(1, "Parameter_min", -40, "int", 0)
        param_obj_11_5 = param_info(1, "Parameter_max", 80, "int", 0)
        param_obj_11_6 = param_info(1, "Parameter", "Humidity", "string", 0)
        param_obj_11_7 = param_info(1, "Units", "%", "string", 0)
        param_obj_11_8 = param_info(1, "Accuracy", 2, "int", 0)
        param_obj_11_9 = param_info(1, "Parameter_min", 0, "int", 0)
        param_obj_11_10 = param_info(1, "Parameter_max", 100, "int", 0)
        param_obj_11_11 = param_info(0, "Voltage_min", 3.3, "float", 0)
        param_obj_11_12 = param_info(0, "Voltage_max", 5.5, "float", 0)
        param_obj_11_13 = param_info(0, "Voltage_unit", "V", "string", 0)
        param_obj_11_14 = param_info(0, "Current", 0.0015, "float", 0)
        param_obj_11_15 = param_info(0, "Max_operating_temp", -40, "int", 0)
        param_obj_11_16 = param_info(0, "Min_operating_temp", 80, "int", 0)
        param_obj_11_17 = param_info(0, "Min_storage_temp", -40, "int", 0)
        param_obj_11_18 = param_info(0, "Max_storage_temp", 80, "int", 0)
        param_obj_11_19 = param_info(0, "Storage_operating_temp_units", "C", "string", 0)
        reading_obj_11_1.add_parameter(param_obj_11_1)
        reading_obj_11_1.add_parameter(param_obj_11_2)
        reading_obj_11_1.add_parameter(param_obj_11_3)
        reading_obj_11_1.add_parameter(param_obj_11_4)
        reading_obj_11_1.add_parameter(param_obj_11_5)
        reading_obj_11_2.add_parameter(param_obj_11_6)
        reading_obj_11_2.add_parameter(param_obj_11_7)
        reading_obj_11_2.add_parameter(param_obj_11_8)
        reading_obj_11_2.add_parameter(param_obj_11_9)
        reading_obj_11_2.add_parameter(param_obj_11_10)
        sensor_obj_11.add_parameter(param_obj_11_11)
        sensor_obj_11.add_parameter(param_obj_11_12)
        sensor_obj_11.add_parameter(param_obj_11_13)
        sensor_obj_11.add_parameter(param_obj_11_14)
        sensor_obj_11.add_parameter(param_obj_11_15)
        sensor_obj_11.add_parameter(param_obj_11_16)
        sensor_obj_11.add_parameter(param_obj_11_17)
        sensor_obj_11.add_parameter(param_obj_11_18)
        sensor_obj_11.add_parameter(param_obj_11_19)
        sensor_obj_11.add_reading(reading_obj_11_1)
        sensor_obj_11.add_reading(reading_obj_11_2)
        write_to_config_file(sensor_obj_11)



        sensor_obj_12 = sensor_info("TMP102_1", "TMP102.Texas_Instruments.2008", 0.25, 1, 1, "Breakout board", "Sparkfun")
        reading_obj_12_1 = reading_info("TMP102.Texas_Instruments.2008.Temp", "float", "F", " ")
        param_obj_12_1 = param_info(1, "Parameter", "Temperature", "string", 0)
        param_obj_12_2 = param_info(1, "Units", "F", "string", 0)
        param_obj_12_3 = param_info(1, "Accuracy", 0.5, "float", 0)
        param_obj_12_4 = param_info(1, "Parameter_min", -40, "int", 0)
        param_obj_12_5 = param_info(1, "Parameter_max", 257, "int", 0)
        param_obj_12_6 = param_info(0, "Voltage_min", 1.4, "float", 0)
        param_obj_12_7 = param_info(0, "Voltage_max", 3.6, "float", 0)
        param_obj_12_8 = param_info(0, "Voltage_unit", "V", "string", 0)
        param_obj_12_9 = param_info(0, "Current", 0.000001, "float", 0)
        param_obj_12_10 = param_info(0, "Max_operating_temp", 150, "int", 0)
        param_obj_12_11 = param_info(0, "Min_operating_temp", -55, "int", 0)
        param_obj_12_12 = param_info(0, "Min_storage_temp", -60, "int", 0)
        param_obj_12_13 = param_info(0, "Max_storage_temp", 150, "int", 0)
        param_obj_12_14 = param_info(0, "Storage_operating_temp_units", "C", "string", 0)
        param_obj_12_15 = param_info(0, "Resolution", "12bit", "string", 0)
        reading_obj_12_1.add_parameter(param_obj_12_1)
        reading_obj_12_1.add_parameter(param_obj_12_2)
        reading_obj_12_1.add_parameter(param_obj_12_3)
        reading_obj_12_1.add_parameter(param_obj_12_4)
        reading_obj_12_1.add_parameter(param_obj_12_5)
        sensor_obj_12.add_parameter(param_obj_12_6)
        sensor_obj_12.add_parameter(param_obj_12_7)
        sensor_obj_12.add_parameter(param_obj_12_8)
        sensor_obj_12.add_parameter(param_obj_12_9)
        sensor_obj_12.add_parameter(param_obj_12_10)
        sensor_obj_12.add_parameter(param_obj_12_11)
        sensor_obj_12.add_parameter(param_obj_12_12)
        sensor_obj_12.add_parameter(param_obj_12_13)
        sensor_obj_12.add_parameter(param_obj_12_14)
        sensor_obj_12.add_parameter(param_obj_12_15)
        sensor_obj_12.add_reading(reading_obj_12_1)
        write_to_config_file(sensor_obj_12)



        sensor_obj_13 = sensor_info("SHT75_1", "SHT75.Sensirion.5_2011", 1, 1, 1, "normal", "Newark")
        reading_obj_13_1 = reading_info("SHT75.Sensirion.5_2011.Temp", "float", "C", " ")
        reading_obj_13_2 = reading_info("SHT75.Sensirion.5_2011.Humidity", "float", "%", " ")
        param_obj_13_1 = param_info(1, "Parameter", "Temperature", "string", 0)
        param_obj_13_2 = param_info(1, "Units", "C", "string", 0)
        param_obj_13_3 = param_info(1, "Accuracy", 0.3, "float", 0)
        param_obj_13_4 = param_info(1, "Parameter_min", -40, "int", 0)
        param_obj_13_5 = param_info(1, "Parameter_max", 123.8, "float", 0)
        param_obj_13_6 = param_info(1, "Parameter", "Humidity", "string", 0)
        param_obj_13_7 = param_info(1, "Units", "%", "string", 0)
        param_obj_13_8 = param_info(1, "Accuracy", 1.8, "float", 0)
        param_obj_13_9 = param_info(1, "Parameter_min", 0, "int", 0)
        param_obj_13_10 = param_info(1, "Parameter_max", 100, "int", 0)
        param_obj_13_11 = param_info(0, "Voltage_min", 2.4, "float", 0)
        param_obj_13_12 = param_info(0, "Voltage_max", 5.5, "float", 0)
        param_obj_13_13 = param_info(0, "Voltage_unit", "V", "string", 0)
        param_obj_13_14 = param_info(0, "Current", 0.00055, "float", 0)
        param_obj_13_15 = param_info(0, "Max_operating_temp", 123.8, "float", 0)
        param_obj_13_16 = param_info(0, "Min_operating_temp", -40, "int", 0)
        param_obj_13_17 = param_info(0, "Min_storage_temp", 10, "int", 0)
        param_obj_13_18 = param_info(0, "Max_storage_temp", 50, "int", 0)
        param_obj_13_19 = param_info(0, "Storage_operating_temp_units", "C", "string", 0)
        param_obj_13_20 = param_info(0, "Resolution", "8/12/14bit", "string", 0)
        reading_obj_13_1.add_parameter(param_obj_13_1)
        reading_obj_13_1.add_parameter(param_obj_13_2)
        reading_obj_13_1.add_parameter(param_obj_13_3)
        reading_obj_13_1.add_parameter(param_obj_13_4)
        reading_obj_13_1.add_parameter(param_obj_13_5)
        reading_obj_13_2.add_parameter(param_obj_13_6)
        reading_obj_13_2.add_parameter(param_obj_13_7)
        reading_obj_13_2.add_parameter(param_obj_13_8)
        reading_obj_13_2.add_parameter(param_obj_13_9)
        reading_obj_13_2.add_parameter(param_obj_13_10)
        sensor_obj_13.add_parameter(param_obj_13_11)
        sensor_obj_13.add_parameter(param_obj_13_12)
        sensor_obj_13.add_parameter(param_obj_13_13)
        sensor_obj_13.add_parameter(param_obj_13_14)
        sensor_obj_13.add_parameter(param_obj_13_15)
        sensor_obj_13.add_parameter(param_obj_13_16)
        sensor_obj_13.add_parameter(param_obj_13_17)
        sensor_obj_13.add_parameter(param_obj_13_18)
        sensor_obj_13.add_parameter(param_obj_13_19)
        sensor_obj_13.add_parameter(param_obj_13_20)
        sensor_obj_13.add_reading(reading_obj_13_1)
        sensor_obj_13.add_reading(reading_obj_13_2)
        write_to_config_file(sensor_obj_13)



        sensor_obj_14 = sensor_info("HIH4030_1", "HIH4030.Honeywell.2008", 5, 0, 0, "Breakout board", "Sparkfun")
        reading_obj_14_1 = reading_info("HIH4030.Honeywell.2008.Humidity", "int", "Units10B0V5", " ")
        param_obj_14_1 = param_info(1, "Parameter", "Humidity", "string", 0)
        param_obj_14_2 = param_info(1, "Units", "Units10B0V5", "string", 0)
        param_obj_14_3 = param_info(1, "Accuracy", 3.5, "float", 0) # Technically not same units as output...
        param_obj_14_4 = param_info(1, "Parameter_min", 0, "int", 0)
        param_obj_14_5 = param_info(1, "Parameter_max", 100, "int", 0)
        param_obj_14_6 = param_info(0, "Voltage_min", 4, "int", 0)
        param_obj_14_7 = param_info(0, "Voltage_max", 5.8, "float", 0)
        param_obj_14_8 = param_info(0, "Voltage_unit", "Vdc", "string", 0)
        param_obj_14_9 = param_info(0, "Current", 0.0002, "float", 0)
        param_obj_14_10 = param_info(0, "Max_operating_temp", 85, "int", 0)
        param_obj_14_11 = param_info(0, "Min_operating_temp", -40, "int", 0)
        param_obj_14_12 = param_info(0, "Min_storage_temp", -50, "int", 0)
        param_obj_14_13 = param_info(0, "Max_storage_temp", 125, "int", 0)
        param_obj_14_14 = param_info(0, "Storage_operating_temp_units", "C", "string", 0)
        reading_obj_14_1.add_parameter(param_obj_14_1)
        reading_obj_14_1.add_parameter(param_obj_14_2)
        reading_obj_14_1.add_parameter(param_obj_14_3)
        reading_obj_14_1.add_parameter(param_obj_14_4)
        reading_obj_14_1.add_parameter(param_obj_14_5)
        sensor_obj_14.add_parameter(param_obj_14_6)
        sensor_obj_14.add_parameter(param_obj_14_7)
        sensor_obj_14.add_parameter(param_obj_14_8)
        sensor_obj_14.add_parameter(param_obj_14_9)
        sensor_obj_14.add_parameter(param_obj_14_10)
        sensor_obj_14.add_parameter(param_obj_14_11)
        sensor_obj_14.add_parameter(param_obj_14_12)
        sensor_obj_14.add_parameter(param_obj_14_13)
        sensor_obj_14.add_parameter(param_obj_14_14)
        sensor_obj_14.add_reading(reading_obj_14_1)
        write_to_config_file(sensor_obj_14)


        sensor_obj_15 = sensor_info("GA1A1S201WP_1", "GA1A1S201WP.Sharp.2007", 1, 0, 0, "Breakout board", "Modern_Device")
        reading_obj_15_1 = reading_info("GA1A1S201WP.Sharp.2007.Light_intensity", "int", "Units10B0V5", " ")
        param_obj_15_1 = param_info(1, "Parameter", "Light_intensity", "string", 0)
        param_obj_15_2 = param_info(1, "Units", "Units10B0V5", "string", 0)
        param_obj_15_3 = param_info(1, "Accuracy", " ", " ", " ")
        param_obj_15_4 = param_info(1, "Parameter_min", 3, "int", 0)
        param_obj_15_5 = param_info(1, "Parameter_max", 55000, "int", 0)
        param_obj_15_6 = param_info(0, "Voltage_min", 2.3, "float", 0)
        param_obj_15_7 = param_info(0, "Voltage_max", 3.2, "float", 0)
        param_obj_15_8 = param_info(0, "Voltage_unit", "V", "string", 0)
        param_obj_15_9 = param_info(0, "Current", 0.00007, "float", 0)
        param_obj_15_10 = param_info(0, "Max_operating_temp", 85, "int", 0)
        param_obj_15_11 = param_info(0, "Min_operating_temp", -40, "int", 0)
        param_obj_15_12 = param_info(0, "Min_storage_temp", 5, "int", 0)
        param_obj_15_13 = param_info(0, "Max_storage_temp", 30, "int", 0)
        param_obj_15_14 = param_info(0, "Storage_operating_temp_units", "C", "string", 0)
        param_obj_15_15 = param_info(0, "Peak_sensitivity", "555nm", "string", 0)
        param_obj_15_16 = param_info(0, "Rise_time", "5ms", "string", 0)
        param_obj_15_17 = param_info(0, "Fall_time", "15ms", "string", 0)
        reading_obj_15_1.add_parameter(param_obj_15_1)
        reading_obj_15_1.add_parameter(param_obj_15_2)
        reading_obj_15_1.add_parameter(param_obj_15_3)
        reading_obj_15_1.add_parameter(param_obj_15_4)
        reading_obj_15_1.add_parameter(param_obj_15_5)
        sensor_obj_15.add_parameter(param_obj_15_6)
        sensor_obj_15.add_parameter(param_obj_15_7)
        sensor_obj_15.add_parameter(param_obj_15_8)
        sensor_obj_15.add_parameter(param_obj_15_9)
        sensor_obj_15.add_parameter(param_obj_15_10)
        sensor_obj_15.add_parameter(param_obj_15_11)
        sensor_obj_15.add_parameter(param_obj_15_12)
        sensor_obj_15.add_parameter(param_obj_15_13)
        sensor_obj_15.add_parameter(param_obj_15_14)
        sensor_obj_15.add_parameter(param_obj_15_15)
        sensor_obj_15.add_parameter(param_obj_15_16)
        sensor_obj_15.add_parameter(param_obj_15_17)
        sensor_obj_15.add_reading(reading_obj_15_1)
        write_to_config_file(sensor_obj_15)



        sensor_obj_16 = sensor_info("MAX4466_1", "MAX4466.Maxim.2001", 0.04, 1, 1, "Breakout board", "Adafruit")
        reading_obj_16_1 = reading_info("MAX4466.Maxim.2001.Noise_intensity", "int", "Units10B0V5", " ")
        param_obj_16_1 = param_info(1, "Parameter", "Noise_intensity", "string", 0)
        param_obj_16_2 = param_info(1, "Units", "Units10B0V5", "string", 0)
        param_obj_16_3 = param_info(1, "Accuracy", " ", " ", " ")
        param_obj_16_4 = param_info(1, "Parameter_min", " ", " ", " ")
        param_obj_16_5 = param_info(1, "Parameter_max", " ", " ", " ")
        param_obj_16_6 = param_info(0, "Voltage_min", 2.4, "float", 0)
        param_obj_16_7 = param_info(0, "Voltage_max", 5.5, "float", 0)
        param_obj_16_8 = param_info(0, "Voltage_unit", "V", "string", 0)
        param_obj_16_9 = param_info(0, "Current", 0.000024, "float", 0)
        param_obj_16_10 = param_info(0, "Max_operating_temp", 85, "int", 0)
        param_obj_16_11 = param_info(0, "Min_operating_temp", -40, "int", 0)
        param_obj_16_12 = param_info(0, "Min_storage_temp", -65, "int", 0)
        param_obj_16_13 = param_info(0, "Max_storage_temp", 150, "int", 0)
        param_obj_16_14 = param_info(0, "Storage_operating_temp_units", "C", "string", 0)
        param_obj_16_15 = param_info(0, "Gain_max", "125x", "string", 0)
        param_obj_16_16 = param_info(0, "Gain_min", "25x", "string", 0)
        reading_obj_16_1.add_parameter(param_obj_16_1)
        reading_obj_16_1.add_parameter(param_obj_16_2)
        reading_obj_16_1.add_parameter(param_obj_16_3)
        reading_obj_16_1.add_parameter(param_obj_16_4)
        reading_obj_16_1.add_parameter(param_obj_16_5)
        sensor_obj_16.add_parameter(param_obj_16_6)
        sensor_obj_16.add_parameter(param_obj_16_7)
        sensor_obj_16.add_parameter(param_obj_16_8)
        sensor_obj_16.add_parameter(param_obj_16_9)
        sensor_obj_16.add_parameter(param_obj_16_10)
        sensor_obj_16.add_parameter(param_obj_16_11)
        sensor_obj_16.add_parameter(param_obj_16_12)
        sensor_obj_16.add_parameter(param_obj_16_13)
        sensor_obj_16.add_parameter(param_obj_16_14)
        sensor_obj_16.add_parameter(param_obj_16_15)
        sensor_obj_16.add_parameter(param_obj_16_16)
        sensor_obj_16.add_reading(reading_obj_16_1)
        write_to_config_file(sensor_obj_16)
        
        
        sensor_obj_17 = sensor_info("HTU21D_1", "HTU21D.MeasSpec.2013", 0.04, 1, 1, "Breakout board", "Sparkfun")
        reading_obj_17_1 = reading_info("HTU21D.MeasSpec.2013.Temp", "float", "C", " ")
        reading_obj_17_2 = reading_info("HTU21D.MeasSpec.2013.Humidity", "float", "%", " ")
        param_obj_17_1 = param_info(1, "Parameter", "Temperature", "string", 0)
        param_obj_17_2 = param_info(1, "Units", "C", "string", 0)
        param_obj_17_3 = param_info(1, "Accuracy", 0.3, "float", 0)
        param_obj_17_4 = param_info(1, "Parameter_min", -40, "int", 0)
        param_obj_17_5 = param_info(1, "Parameter_max", 123.8, "float", 0)
        param_obj_17_6 = param_info(1, "Parameter", "Humidity", "string", 0)
        param_obj_17_7 = param_info(1, "Units", "%", "string", 0)
        param_obj_17_8 = param_info(1, "Accuracy", 1.8, "float", 0)
        param_obj_17_9 = param_info(1, "Parameter_min", 0, "int", 0)
        param_obj_17_10 = param_info(1, "Parameter_max", 100, "int", 0)
        param_obj_17_11 = param_info(0, "Voltage_min", 3.0, "float", 0)
        param_obj_17_12 = param_info(0, "Voltage_max", 3.5, "float", 0)
        param_obj_17_13 = param_info(0, "Voltage_unit", "V", "string", 0)
        param_obj_17_14 = param_info(0, "Current", 0.0015, "float", 0)
        param_obj_17_15 = param_info(0, "Max_operating_temp", -40, "int", 0)
        param_obj_17_16 = param_info(0, "Min_operating_temp", 80, "int", 0)
        param_obj_17_17 = param_info(0, "Min_storage_temp", -40, "int", 0)
        param_obj_17_18 = param_info(0, "Max_storage_temp", 80, "int", 0)
        param_obj_17_19 = param_info(0, "Storage_operating_temp_units", "C", "string", 0)
        reading_obj_17_1.add_parameter(param_obj_17_1)
        reading_obj_17_1.add_parameter(param_obj_17_2)
        reading_obj_17_1.add_parameter(param_obj_17_3)
        reading_obj_17_1.add_parameter(param_obj_17_4)
        reading_obj_17_1.add_parameter(param_obj_17_5)
        reading_obj_17_2.add_parameter(param_obj_17_6)
        reading_obj_17_2.add_parameter(param_obj_17_7)
        reading_obj_17_2.add_parameter(param_obj_17_8)
        reading_obj_17_2.add_parameter(param_obj_17_9)
        reading_obj_17_2.add_parameter(param_obj_17_10)
        sensor_obj_17.add_parameter(param_obj_17_11)
        sensor_obj_17.add_parameter(param_obj_17_12)
        sensor_obj_17.add_parameter(param_obj_17_13)
        sensor_obj_17.add_parameter(param_obj_17_14)
        sensor_obj_17.add_parameter(param_obj_17_15)
        sensor_obj_17.add_parameter(param_obj_17_16)
        sensor_obj_17.add_parameter(param_obj_17_17)
        sensor_obj_17.add_parameter(param_obj_17_18)
        sensor_obj_17.add_parameter(param_obj_17_19)
        sensor_obj_17.add_reading(reading_obj_17_1)
        sensor_obj_17.add_reading(reading_obj_17_2)
        write_to_config_file(sensor_obj_17)

        sensor_obj_18 = sensor_info("HMC5883_1", "HMC5883.Honeywell.2013", 0.04, 1, 1, "Breakout board", "Sparkfun")
        reading_obj_18_1 = reading_info("HMC5883.Honeywell.2013.Mag_intensity", "float", "uT", " ")
        param_obj_18_1 = param_info(1, "Parameter", "Magnetic_Field", "string", 0)
        param_obj_18_2 = param_info(1, "Units", "uT", "string", 0)
        param_obj_18_3 = param_info(1, "Accuracy/Sensitivity", 0.02, "float", 0) 
        param_obj_18_4 = param_info(1, "Parameter_min", -180, "int", 0) 
        param_obj_18_5 = param_info(1, "Parameter_max", +180, "int", 0)
        param_obj_18_6 = param_info(0, "Voltage_min", 2.4, "float", 0)
        param_obj_18_7 = param_info(0, "Voltage_max", 3.5, "float", 0)
        param_obj_18_8 = param_info(0, "Voltage_unit", "V", "string", 0)
        param_obj_18_9 = param_info(0, "Current", 0.000024, "float", 0)
        param_obj_18_10 = param_info(0, "Max_operating_temp", 85, "int", 0)
        param_obj_18_11 = param_info(0, "Min_operating_temp", -40, "int", 0)
        param_obj_18_12 = param_info(0, "Min_storage_temp", -65, "int", 0)
        param_obj_18_13 = param_info(0, "Max_storage_temp", 150, "int", 0)
        param_obj_18_14 = param_info(0, "Storage_operating_temp_units", "C", "string", 0)
        reading_obj_18_1.add_parameter(param_obj_18_1)
        reading_obj_18_1.add_parameter(param_obj_18_2)
        reading_obj_18_1.add_parameter(param_obj_18_3)
        reading_obj_18_1.add_parameter(param_obj_18_4)
        reading_obj_18_1.add_parameter(param_obj_18_5)
        sensor_obj_18.add_parameter(param_obj_18_6)
        sensor_obj_18.add_parameter(param_obj_18_7)
        sensor_obj_18.add_parameter(param_obj_18_8)
        sensor_obj_18.add_parameter(param_obj_18_9)
        sensor_obj_18.add_parameter(param_obj_18_10)
        sensor_obj_18.add_parameter(param_obj_18_11)
        sensor_obj_18.add_parameter(param_obj_18_12)
        sensor_obj_18.add_parameter(param_obj_18_13)
        sensor_obj_18.add_parameter(param_obj_18_14)
        sensor_obj_18.add_reading(reading_obj_18_1)
        write_to_config_file(sensor_obj_18)
        pass

    def start(self, input_buffer, output_buffer):

        print ">>>>Loading Sensor Module<<<<<"
        try:
            device_conf_file_handle = open('./device.conf', 'r+')
            DEV_PATH=device_conf_file_handle.readline().split('\n')[0]
            device_conf_file_handle.close()
        except:
            DEV_PATH="/dev/ttyACM0"

        print "Trying to connect to - ",DEV_PATH
        while True:
            wxconnection = False
            while wxconnection == False:
                try:
                    wxsensor = serial.Serial(DEV_PATH,57600,timeout=4)
                    wxconnection = True
                except:
                    print "Waiting for Connection..."
                    time.sleep(10)
                    pass
            try:
                print wxsensor
                wxsensor.flushInput()
                wxsensor.flushOutput()
            except:
                wxsensor.close()
                wxconnection = False
            while wxconnection == True:
                try:
                    readData = ' '
                    readData=wxsensor.readline()
                except:
                    wxsensor.close()
                    wxconnection = False
                if len(readData) > 0 and wxconnection == True:
                    try:
                        sensorsData = readData.split(';')
                        if len(sensorsData) > 2:
                            sensorDataAvail = True
                        else:
                            sensorDataAvail = False
                    except:
                        sensorDataAvail = False

                    if sensorDataAvail == True:
                        if sensorsData[0] == 'WXSensor' and sensorsData[-1]=='WXSensor\r\n':
                            #print "Data Received:", sensorsData[1:-1]
                            sensorReading_bucket = [[[] for col in range(5)] for row in range(18)]
                            for i in range(len(sensorsData)-2):
                                currentSensor = sensorsData[i+1].split(':')
                                if currentSensor[0] <> 'D6T_44L_06_1_T_C':
                                    try:
                                        temp_values = float(currentSensor[1])
                                        which_row = self.sensor_array_index[self.Sensor_Index.index(currentSensor[0])]
                                        sensorReading_bucket[which_row][0].append(self.reading_names[self.Sensor_Index.index(currentSensor[0])])
                                        sensorReading_bucket[which_row][1].append(self.reading_type[self.Sensor_Index.index(currentSensor[0])])
                                        sensorReading_bucket[which_row][2].append(temp_values)
                                        sensorReading_bucket[which_row][3].append(self.reading_unit[self.Sensor_Index.index(currentSensor[0])])
                                        sensorReading_bucket[which_row][4].append(self.reading_note[self.Sensor_Index.index(currentSensor[0])])
                                    except:
                                        print "********", currentSensor
                                        pass
                                else:
                                    pass
                                    try:
                                        temp_values=currentSensor[1].split(',')
                                        for k in range(len(temp_values)):
                                            temp_values[k] = float(temp_values[k])
                                        which_row = self.sensor_array_index[self.Sensor_Index.index(currentSensor[0])]
                                        sensorReading_bucket[which_row][0]=list(self.reading_names[self.Sensor_Index.index(currentSensor[0])])
                                        sensorReading_bucket[which_row][1]=list(self.reading_type[self.Sensor_Index.index(currentSensor[0])])
                                        sensorReading_bucket[which_row][2]=list(temp_values)
                                        sensorReading_bucket[which_row][3]=list(self.reading_unit[self.Sensor_Index.index(currentSensor[0])])
                                        sensorReading_bucket[which_row][4]=list(self.reading_note[self.Sensor_Index.index(currentSensor[0])])
                                    except:
                                        pass
                            for all in range(len(sensorReading_bucket)):
                                if (sensorReading_bucket[all] <> [[],[],[],[],[]]):
                                    sendData=[self.sensor_names[all],int(time.time()),sensorReading_bucket[all][0],sensorReading_bucket[all][1],sensorReading_bucket[all][2],sensorReading_bucket[all][3],sensorReading_bucket[all][4]]
                                    print [self.sensor_names[all],int(time.time()),sensorReading_bucket[all][0],sensorReading_bucket[all][1],sensorReading_bucket[all][2],sensorReading_bucket[all][3],sensorReading_bucket[all][4]]
                                    output_buffer.put([self.sensor_names[all],int(time.time()),sensorReading_bucket[all][0],sensorReading_bucket[all][1],sensorReading_bucket[all][2],sensorReading_bucket[all][3],sensorReading_bucket[all][4]])
